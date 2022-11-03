FROM gvenzl/oracle-xe:21-slim


COPY ./docker/database/sql/01_create_tablespaces.sql /container-entrypoint-initdb.d/01_create_tablespaces.sql
COPY ./docker/database/sql/02_create_users.sql /container-entrypoint-initdb.d/02_create_users.sql
