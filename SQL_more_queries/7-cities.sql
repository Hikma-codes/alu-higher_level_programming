-- Creates the database hbtn_0d_usa and the table cities within it on your MySQL server
-- Creates the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Selects the database for use
USE hbtn_0d_usa;
-- Creates the table
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
