alter session set "_ORACLE_SCRIPT"=true;
alter session set container=XEPDB1;

create user docker_admin identified by docker_admin quota unlimited on tbs_data;
alter user docker_admin default tablespace tbs_data;
grant dba to docker_admin;

create user docker_user identified by docker_user quota unlimited on tbs_data;
alter user docker_user default tablespace tbs_data;
grant connect, resource to docker_user;

exit;