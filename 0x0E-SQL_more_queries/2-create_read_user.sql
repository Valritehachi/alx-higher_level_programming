-- Creates the MySQL database 'hbtn_0d_2'.
-- Creates the MySQL user 'user_0d_2' with a password.
-- Grants the SELECT privilege on all tables. 
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
