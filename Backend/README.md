## set up Mysql database
1. Install Mysql
2. cd into the directory where set_up_mysql.sql is located
3. run the command
```bash
cd Backend
```
2. run the command
```bash
mysql -u root -p
```
to test if Mysql is installed correctly
3. run the script
```bash
mysql -u root -p < set_up_mysql.sql
```


## To start the API
1. cd into the directory where app.py is located
2. install the required packages
```bash
pip install -r requirements.txt
```
2. run the command
```bash
python3 apis.py
```