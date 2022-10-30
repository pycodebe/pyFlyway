from subprocess import PIPE, Popen
from typing import Union
from sys import exit
import json

def run_command(command: list) -> str:
    with Popen(command, stdout=PIPE, stderr=None, shell=True) as process:
        return process.communicate()[0].decode("utf-8")
        

class Flyway:

    def __init__(self, platform: str, image: str, clean_allowed: bool, environ: str) -> None:
        self.platform = platform 
        self.image = image
        self.clean_allowed = clean_allowed
        self.environ = environ
        
        with open(f'{self.environ}.json') as f:
            data = json.load(f)
            self.history_table = data['history_table']
            self.prefix = data['prefix']
            self.installer = data['installedBy']
            self.url = data['url']
            
    def _command(self, command: Union[str, None]) -> list:
        try:
            command_line = [self.platform, "run", "--rm", "--network=docker-services_dbnet", self.image]
            if command:    
                config = [
                    f'-table={self.history_table}',
                    f'-sqlMigrationPrefix={self.prefix}',
                    f'-installedBy={self.installer}',
                    f'-user=xxxx', 
                    '-password=xxxx', 
                    f'-url={self.url}'] 
                command_line = command_line + config
                command_line.append(command)
                
            return command_line
        except Exception as e:
            print(f"An error occurs with {self._command.__name__} : {e}")
            exit(1)

    def version(self, verbose: bool=False) -> None:
        """Print the Flyway version and edition"""
        if verbose:
            print(self._command(self.version.__name__))
        print(run_command(self._command(self.version.__name__)))

    def help(self) -> None:
        print(run_command(self._command(None)))

    def clean(self, verbose:bool=False) -> None:
        """Drops all objects in the configured schemas"""
        if not self.clean_allowed:
            print(f"The command {self.clean.__name__} has been disable")
        else:
            if verbose:
                print(self._command(self.clean.__name__))
            print(run_command(self._command(self.clean.__name__)))

    def info(self, verbose: bool=False) -> None:
        """Prints the information about applied, current and pending migrations"""
        command = self._command(self.info.__name__)
        if verbose:
            print(command)
        print(run_command(command))
    
    def migrate(self, verbose: bool=False) -> None:
        """Migrates the database"""
        if verbose:
            print(self._command(self.migrate.__name__))
        print(run_command(self._command(self.migrate.__name__)))
    
    def repair(self, verbose: bool=False) -> None:
        """Repairs the schema history table"""
        if verbose:
            print(self._command(self.repair.__name__))
        print(run_command(self._command(self.repair.__name__)))
    
    def baseline(self, verbose: bool=False) -> None:
        """Baselines an existing database at the baselineVersion"""
        if verbose:
            print(self._command(self.baseline.__name__))
        run_command(self._command(self.baseline.__name__))
        print(run_command(self._command(self.baseline.__name__)))




flyway = Flyway(platform="docker", image="flyway/flyway", clean_allowed=False, environ="development")
flyway.info(verbose=True)
