-- Create DB and table with unique, auto-generated attrubute that can't ne null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT PRIMARY KEY UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL
	);
