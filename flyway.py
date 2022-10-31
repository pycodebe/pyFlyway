from subprocess import PIPE, Popen
from typing import Union
import sys
import yaml


class Flyway:

    def __init__(self, platform: str, image: str, clean_allowed: bool, environ: str, verbose: str) -> None:
        self.platform = platform 
        self.image = image
        self.clean_allowed = clean_allowed
        self.environ = environ
        self.verbose = verbose
        
        with open(f'{self.environ}.yml', 'r') as stream:
            data_loaded = yaml.safe_load(stream)
            self.version_table = data_loaded['versionTable']
            self.version_prefix = data_loaded['versionPrefix']
            self.installer = data_loaded['installedBy']
            self.database_url = data_loaded['databaseURL']
            self.schemas = data_loaded['schemas']

    def _execute_command(self, command: Union[str, None]) -> None:

        def run_command(command: list) -> str:
            with Popen(command, stdout=PIPE, stderr=None, shell=True) as process:
                return process.communicate()[0].decode("utf-8")

        def _command(self, command: Union[str, None], user: Union[str, None], password: Union[str, None]) -> list:
            try:
                command_line = [self.platform, "run", "--rm", "--network=docker-services_dbnet", self.image]         
                if command:  
                    config = [
                        f'-table={self.version_table}',
                        f'-sqlMigrationPrefix={self.version_prefix}',
                        f'-installedBy={self.installer}',
                        f'-user={user}', 
                        f'-password={password}', 
                        f'-url={self.database_url}'] 
                    command_line = command_line + config
                    command_line.append(command)

                if self.verbose:
                    print(command_line)

                return command_line
                
            except Exception as e:
                print(f"An error occurs with {self._command.__name__} : {e}")
                exit(1)

        if len(self.schemas) > 0:
            for schema in self.schemas:
                user = self.schemas[schema]['user']
                password = self.schemas[schema]['password']
                print(run_command(command=_command(self, command=command, user=user, password=password)))
        else:
            print("There is no schema defined in the YAML file")
            sys.exit(1)

    def version(self) -> None:
        """Print the Flyway version and edition"""
        print(self._execute_command(self.version.__name__))

    def help(self) -> None:
        print(self._execute_command(command=None))

    def clean(self) -> None:
        """Drops all objects in the configured schemas"""
        command_name = self.clean.__name__
        if not self.clean_allowed:
            print(f"The command {command_name} has been disable")
        else:
            print(self._execute_command(command=command_name))
                
    def info(self) -> None:
        """Prints the information about applied, current and pending migrations"""
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


flyway = Flyway(platform="docker", image="flyway/flyway", clean_allowed=False, environ="development", verbose=True)
flyway.info()
