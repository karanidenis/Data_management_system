-- this script prepares a MySQL server for the project
-- create project developement database with the name : management_db
CREATE DATABASE IF NOT EXISTS management_db;
-- creating new user named : admin_mgt with all privileges on the db management_db
-- with the password : Pwd.mgt if it dosen't exist
CREATE USER IF NOT EXISTS 'admin_mgt'@'localhost' IDENTIFIED BY 'Pwd1.mgt';
-- granting all privileges to the new user
GRANT ALL PRIVILEGES ON management_db.* TO 'admin_mgt'@'localhost';
FLUSH PRIVILEGES;
-- granting the SELECT privilege for the user hbnb_dev in the db performance_schema
GRANT SELECT ON performance_schema.* TO 'admin_mgt'@'localhost';
FLUSH PRIVILEGES;