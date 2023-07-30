from website import create_app
import mysql.connector
from dotenv import load_dotenv
import os 

load_dotenv()

config = {
    'user': os.getenv('USERNAME'),
    'password': os.getenv('PASSWORD'),
    'host': os.getenv('HOST'),
    'database': os.getenv('DATABASE'),
    'ssl_verify_identity': True,
    'ssl_ca': '/etc/ssl/cert.pem',
}

cnx = mysql.connector.connect(**config)
cnx.close()

print("Successfully connected to PlanetScale!")

''''
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "lludbA090",
)
my_cursor = mydb.cursor()
'''


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)