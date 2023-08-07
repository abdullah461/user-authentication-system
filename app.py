from website import create_app
import mysql.connector
from dotenv import load_dotenv
import os 
import MySQLdb
from sqlalchemy import create_engine, text
load_dotenv()

connect = os.getenv('SQLALCHEMY_DATABASE_URI')
engine = create_engine(connect)

app = create_app()

if __name__ == '__main__':
  app.run(debug=True)