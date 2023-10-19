-- Creates DB and table in same DB
CREATE DATABASE IF EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF EXISTS cities (
	id INT UNIQUE auto_generated NOT NULL primary key,
	state_id INT NOT NULL,
	foreign key(states_id) references states(id),
	name VARCHAR(256)
	);
