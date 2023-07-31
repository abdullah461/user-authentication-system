from website import create_app
import mysql.connector
from dotenv import load_dotenv
import os 
import MySQLdb
from sqlalchemy import create_engine, text
load_dotenv()


''''
cnx = MySQLdb.connect(
    user = os.getenv('USERNAME'),
    password = os.getenv('PASSWORD'),
    host = os.getenv('HOST'),
    database = os.getenv('DATABASE'),
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY",
    ssl      = {
    'ca': "/etc/ssl/cert.pem",
    'capath': "/path/to/certs",
  }
)

print("Successfully connected to PlanetScale!")


connection = mysql.connector.connect(
  host= os.getenv("HOST"),
  user=os.getenv("USERNAME"),
  passwd= os.getenv("PASSWORD"),
  db= os.getenv("DATABASE"),
  autocommit = True,
  ssl_mode = "VERIFY_IDENTITY",
)
my_cursor = connection.cursor()
'''
connect = os.getenv('SQLALCHEMY_DATABASE_URI')
engine = create_engine(connect)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)