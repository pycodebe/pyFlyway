import sys
from pathlib import Path
from subprocess import PIPE, Popen
from typing import Union

import yaml

class Flyway:

    def __init__(self, verbose: str, conf_path: Path) -> None:
        self.verbose = verbose

        with open((f"{conf_path}"), "r", encoding="utf-8") as stream:
            data_loaded = yaml.safe_load(stream)
            self.version_table = data_loaded["versionTable"]
            self.version_prefix = data_loaded["versionPrefix"]
            self.clean_allowed = data_loaded["clean"]
            self.installer = data_loaded["installedBy"]
            self.database_url = data_loaded["databaseURL"]
            self.schemas = data_loaded["schemas"]

            if data_loaded["container"]:
                self.container_platform = data_loaded["container"]["platform"]
                self.container_image = data_loaded["container"]["image"]
                self.container_network = data_loaded["container"]["network"]

    def is_clean_allowed(self):
        return self.clean_allowed

    def _execute_command(self, command: Union[str, None]) -> None:
        def run_command(command: list) -> str:
            with Popen(command, stdout=PIPE, stderr=None, shell=True) as p:
                return p.communicate()[0].decode("utf-8")

        def _command(
            self,
            command: Union[str, None],
            user: Union[str, None],
            password: Union[str, None],
        ) -> list:
            try:
                command_line = [self.container_platform, "run", "--rm"]
                if self.container_network:
                    command_line.append(f"--network={self.container_network}")
                command_line.append(self.container_image)

                if command:
                    config = [
                        f"-table={self.version_table}",
                        f"-sqlMigrationPrefix={self.version_prefix}",
                        f"-installedBy={self.installer}",
                        f"-user={user}",
                        f"-password={password}",
                        f"-url={self.database_url}",
                    ]
                    command_line = command_line + config
                    command_line.append(command)

                if self.verbose:
                    print(command_line)

                return command_line

            except Exception as e:
                print(f"An error occurs with {_command.__name__} : {e}")
                sys.exit(1)

        if len(self.schemas) > 0:
            for schema in self.schemas:
                user = self.schemas[schema]["user"]
                password = self.schemas[schema]["password"]
                print(
                    run_command(
                        command=_command(
                            self, command=command, user=user, password=password
                        )
                    )
                )
        else:
            print("There is no schema defined in the YAML file")
            sys.exit(1)

    def version(self) -> None:
        """Print the Flyway version and edition"""
        print(self._execute_command(self.version.__name__))

    def help(self) -> None:
        """Print Flyway help"""
        print(self._execute_command(command=None))

    def clean(self) -> None:
        """Drops all objects in the configured schemas"""
        command_name = self.clean.__name__
        if self.is_clean_allowed():
            print(f"The command {command_name} has been disable")
        else:
            print(self._execute_command(command=command_name))

    def info(self) -> None:
        """Prints the information about migrations"""
        print(self._execute_command(command=self.info.__name__))

    def migrate(self) -> None:
        """Migrates the database"""
        print(self._execute_command(command=self.migrate.__name__))

    def repair(self) -> None:
        """Repairs the schema history table"""
        print(self._execute_command(command=self.repair.__name__))

    def baseline(self) -> None:
        """Baselines an existing database at the baselineVersion"""
        print(self._execute_command(command=self.baseline.__name__))
