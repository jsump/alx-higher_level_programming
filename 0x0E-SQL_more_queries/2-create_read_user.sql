-- Create the DB hbtn_0d_2 and user user_0d_2 with SELECT privilege on the DB
-- Password set to user_0d_2_pwd
CREATE IF NOT EXISTS DATABASE hbtn_0d_2;
CREATE IF NOT EXISTS USER user_0d_2 IDENTIFIED BY user_0d_2_pwd;
GRANT SELECT TO 'user_0d_2'@'hbtn_0d_2';
FLUSH PRIVILEGES;
