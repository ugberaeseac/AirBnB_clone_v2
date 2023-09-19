-- Create a test database
-- This script prepares a DBMS for the airbnb project clone
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED WITH authentication_plugin BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON 'hbnb_test_db'.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON 'performance_schema'.* TO 'hbnb_test'@'localhost';
