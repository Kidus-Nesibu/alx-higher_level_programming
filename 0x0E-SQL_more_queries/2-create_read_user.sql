-- script that creates a database and user
CREATE DATABASE IF NOT EXSISTS hbtn_0d2;
CREATE USER IF NOT EXSISTS 'user_0d_2'@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON 'hbtn_0d_2'.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
