# pylint: disable=missing-docstring

import subprocess
import sys
from pathlib import Path
from typing import Union

import yaml  # pylint: disable=import-error

from .errors import CleanForbiddenError, NoSchemaFoundError


class Flyway:  # pylint: disable=too-many-instance-attributes
    """Flyway client class."""

    @classmethod
    def __init__(cls, verbose: str, conf_path: Path) -> None:
        cls.verbose = verbose

        with open((f"{conf_path}"), "rb") as stream:
            data_loaded = yaml.safe_load(stream)
            cls.version_table = data_loaded["versionTable"]
            cls.version_prefix = data_loaded["versionPrefix"]
            cls.clean_allowed = data_loaded["clean"]
            cls.installer = data_loaded["installedBy"]
            cls.database_url = data_loaded["databaseURL"]
            cls.schemas = data_loaded["schemas"]

            if data_loaded["container"]:
                cls.container_platform = data_loaded["container"]["platform"]
                cls.container_image = data_loaded["container"]["image"]
                cls.container_network = data_loaded["container"]["network"]

    @classmethod
    def _execute_command(cls, cmd: Union[str, None]) -> str:
        def run_command(cmd: list) -> str:
            subprocess.run(cmd, check=True)

        def _command(
            self,
            cmd: Union[str, None],
            user: Union[str, None],
            pwd: Union[str, None],
        ) -> list:
            try:
                command_line = [self.container_platform, "run", "--rm"]
                if self.container_network:
                    command_line.append(f"--network={self.container_network}")
                command_line.append(self.container_image)

                if cmd:
                    config = [
                        f"-table={self.version_table}",
                        f"-sqlMigrationPrefix={self.version_prefix}",
                        f"-installedBy={self.installer}",
                        f"-user={user}",
                        f"-password={pwd}",
                        f"-url={self.database_url}",
                    ]
                    command_line = command_line + config
                    command_line.append(cmd)

                if self.verbose:
                    print(command_line)

                return command_line

            except (Exception,) as err:  # pylint: disable=broad-except
                print(f"An error occurs with {_command.__name__} : {err}")
                sys.exit(1)

        if len(cls.schemas) > 0:
            for schema in cls.schemas:
                user = cls.schemas[schema]["user"]
                pwd = cls.schemas[schema]["password"]
                print(f"Schema: {schema}")
                run_command(cmd=_command(cls, cmd=cmd, user=user, pwd=pwd))
        else:
            raise NoSchemaFoundError

    @classmethod
    def version(cls) -> None:
        """Return Flyway version and edition"""
        cls._execute_command(cmd=cls.version.__name__)

    @classmethod
    def help(cls) -> None:
        """Return Flyway help"""
        cls._execute_command(cmd=None)

    @classmethod
    def clean(cls) -> None:
        """Drops all objects in the configured schemas"""
        command_name = cls.clean.__name__
        if cls.clean_allowed():
            raise CleanForbiddenError
        cls._execute_command(cmd=command_name)

    @classmethod
    def info(cls) -> None:
        """Return informations about migrations"""
        cls._execute_command(cmd=cls.info.__name__)

    @classmethod
    def migrate(cls) -> None:
        """Migrates the database"""
        cls._execute_command(cmd=cls.migrate.__name__)

    @classmethod
    def repair(cls) -> None:
        """Repairs the schema history table"""
        cls._execute_command(cmd=cls.repair.__name__)

    @classmethod
    def baseline(cls) -> None:
        """Baselines an existing database at the baselineVersion"""
        cls._execute_command(cmd=cls.baseline.__name__)
