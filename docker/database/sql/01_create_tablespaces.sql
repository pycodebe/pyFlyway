alter session set "_ORACLE_SCRIPT"=true;
alter session set container=XEPDB1;

CREATE TABLESPACE tbs_data 
   DATAFILE 'tbs_data.dbf' 
   SIZE 2000m;

CREATE TABLESPACE tbs_index 
   DATAFILE 'tbs_index.dbf' 
   SIZE 1000m;

CREATE TABLESPACE tbs_lob 
   DATAFILE 'tbs_lob.dbf' 
   SIZE 5000m;

exit;