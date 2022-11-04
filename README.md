![GitHub issues](https://img.shields.io/github/issues/pycodebe/pyFlyway?&labelColor=black&color=eb3b5a&label=Issues&logo=issues&logoColor=black&style=for-the-badge) &nbsp;
![GitHub Contributions](https://img.shields.io/github/contributors/pycodebe/pyFlyway?&labelColor=black&color=8854d0&style=for-the-badge) &nbsp;
![repo size](https://img.shields.io/github/repo-size/pycodebe/pyFlyway?label=Repo%20Size&style=for-the-badge&labelColor=black&color=20bf6b) &nbsp;
![GitHub forks](https://img.shields.io/github/forks/pycodebe/pyFlyway?&labelColor=black&color=0fb9b1&style=for-the-badge) &nbsp;
![GitHub stars](https://img.shields.io/github/stars/pycodebe/pyFlyway?&labelColor=black&color=f7b731&style=for-the-badge) &nbsp;
![GitHub LastCommit](https://img.shields.io/github/last-commit/pycodebe/pyFlyway?logo=github&labelColor=black&color=d1d8e0&style=for-the-badge) &nbsp;


Overview
========

pyFlyway is a basic [Flyway](https://flywaydb.org/) client written in Python. <br />
This current version is especially made to work with a containarized version of Flyway

<br />

Status
======

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pycodebe/pyFlyway/master.svg)](https://results.pre-commit.ci/latest/github/pycodebe/pyFlyway/master)

<br />

Requirements
============
* python (>=3.6.x)
* Flyway in a docker container


<br />

Project Organization
====================

    flyway-wrapper
    ├── .github
    │     └── dependabot.yml                            <- Automated dependency updates built into GitHub
    ├── docker                                          <- Containers builder
    │    └── database                                   <- Oracle DB
    │        ├── sql
    │        │    ├── 01_create_tablespaces.sql
    │        │    └── 02_create_users.sql
    │        └── Dockerfile
    ├── wrapper                                         <- Flyway module
    │    ├── __init__.py
    │    └── wrapper.py
    ├── .gitignore
    ├── conf.yml                                        <- Template for your YAML config
    ├── docker-compose.yml                              <- Compose for flyway & oracle DB
    ├── LICENSE
    ├── README.md
    ├── requirements.txt                                <- Modules dependencies

<br />

Configuration
=============

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
  network:              <Network used to communicate between containers>
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

Usage
=====

```python
from wrapper import Flyway

client = Flyway(verbose=False, conf_path='conf.yml')
client.info()
client.migrate()
```

<br />

Contributing
============

1. Fork it (<https://github.com/pycodebe/pyflyway.git>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
6. Your Pull Request will go through pre-commit hooks
