# A wrapper for Flyway in Docker written in Python 

![GitHub issues](https://img.shields.io/github/issues/pycodebe/flyway-wrapper?&labelColor=black&color=eb3b5a&label=Issues&logo=issues&logoColor=black&style=for-the-badge) &nbsp;
![GitHub Contributions](https://img.shields.io/github/contributors/pycodebe/flyway-wrapper?&labelColor=black&color=8854d0&style=for-the-badge) &nbsp;
![repo size](https://img.shields.io/github/repo-size/pycodebe/flyway-wrapper?label=Repo%20Size&style=for-the-badge&labelColor=black&color=20bf6b) &nbsp;
![GitHub forks](https://img.shields.io/github/forks/pycodebe/flyway-wrapper?&labelColor=black&color=0fb9b1&style=for-the-badge) &nbsp;
![GitHub stars](https://img.shields.io/github/stars/pycodebe/flyway-wrapper?&labelColor=black&color=f7b731&style=for-the-badge) &nbsp;
![GitHub LastCommit](https://img.shields.io/github/last-commit/pycodebe/flyway-wrapper?logo=github&labelColor=black&color=d1d8e0&style=for-the-badge) &nbsp;

## Overview

Flyway-wrapper is a python wrapper for the Flyway open-source database-migration tool. <br />
In this project, you will need 2 things:
* Flyway as a Docker container
* Your Flyway and database configuration in a YAML file

<br />

## Requirements

    Python mackages:
    ----------------
    python(>=3.7.x)
    pyyaml(>=6.0)

    Containers:
    -----------
    Flyway

<br />

## Project Organization

    flyway-wrapper
    ├── docker                                          <- containers builder 
    │    └── database                                   <- Oracle DB
    │        ├── sql                                    
    │        │    ├── 01_create_tablespaces.sql
    │        │    └── 02_create_users.sql
    │        └── Dockerfile                             
    ├── wrapper                                         <- Flyway package
    │    ├── __init__.py                                
    │    └── wrapper.py                          
    ├── .gitignore                                      
    ├── conf.yml                                        <- YAML config template
    ├── docker-compose.yml                              <- compose for flyway & oracle DB
    ├── LICENSE                                         
    ├── pyproject.toml                                  <- config & dependencies for the  package builder
    ├── README.md                                       
    ├── setup.py                                        <- config & dependencies for the  package builder
    └── test.py                                         <- basic script to demonstrate

<br />

## Configuration

<br />

### YAML configuration file

```
environment:            <The name of your environment>
versionTable:           <The name of Flyway’s schema history table>
versionPrefix:          <The file name prefix for versioned SQL migrations>
clean:                  <Whether to disable clean command>
baselineDescription:    <Description to tag an existing schema with when executing baseline>
baselineVersion":       <The version to tag an existing schema with when executing baseline>
installedBy:            <The username that will be recorded in the schema history table as having applied the migration>
databaseURL:            <The jdbc url to use to connect to the database>
schemas: 
  docker_user:          <Name of the schema>
    user:               <User to connect to the schema>
    password:           <Password to connect to the schema>
container:
  platform:             <Container platform>
  image:                <Image/Container>
  network:              <Network used to communicate between containers if Flyway container has to connect with a DB in a container as well>
```

Sample
```
environment: development
versionTable: flyway_migrations
versionPrefix: v
clean: False,
baselineDescription: Baseline
baselineVersion": 0.0
installedBy: docker_user
databaseURL: jdbc:oracle:thin:@//database:1521/XEPDB1
schemas: 
  docker_user:
    user: docker_user
    password: docker_user
container:
  platform: docker
  image: flyway/flyway
  network: docker-services_dbnet
```

<br />


## Usage

```
from wrapper import Flyway

client = Flyway(verbose=False, conf_path='conf.yml')
client.help()
client.info()
client.migrate()
...
```

<br />

## Contributing

1. Fork it (<https://github.com/pycodebe/flyway-wrapper.git>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
