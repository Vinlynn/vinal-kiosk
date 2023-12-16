from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# credentials of db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Vinal_Kiosk'

#create an object
mysql = MySQL(app)

from appfolder import routes
