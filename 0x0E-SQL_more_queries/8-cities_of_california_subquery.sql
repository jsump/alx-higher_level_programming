-- List all ccities of California
SELECT id, name FROM cities WHERE state_id = (SELECTid FROM states WHERE name = 'California') ORDER BY id ASC;
