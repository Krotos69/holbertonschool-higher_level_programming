-- Command to Create a database hbtn_0d_2 if it doesn't already exits
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create the user if it doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant SELECT priviege on the database to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
