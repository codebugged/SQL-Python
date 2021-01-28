# SQL-Python
Ever thought of sending data on SQL using python. LOL that's here

Install SQL on local system using 
python -m pip install mysql-connector-python

Install SQL on cloud server using

sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation

Launch SQL using command
mysql -u root -p

From there, create a new user and give it a strong password:
CREATE USER 'sammy'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'user_name'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;



 
