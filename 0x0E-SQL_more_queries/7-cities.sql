-- Creates DB and table in same DB
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE auto_generated NOT NULL primary key,
	state_id INT NOT NULL,
	foreign key(state_id) references states(id),
	name VARCHAR(256) NOT NULL,
	);
