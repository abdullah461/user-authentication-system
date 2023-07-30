import mysql.connector
import MySQLdb

'''

 Note: If you're developing on Windows, we recommend using mysql-connector-python instead
  of mysqlclient as it is easier to enable SSL.

db = mysql.connector.connect(
    host = "",
    user = "" ,
    passwd = "",
)

my_cursor = db.cursor()


db = MySQLdb.connect(
    host     = "[HOSTNAME]",
    user     = "[USERNAME]",
    passwd   = "[PASSWORD]",
    db       = "[DATABASE]",
    ssl_mode = "VERIFY_IDENTITY",
    ssl      = {
        "ca": "/etc/ssl/certs/ca-certificates.crt"
    })



import mysql.connector

config = {
    'user': '[USERNAME]',
    'password': '[PASSWORD]',
    'host': '[HOSTNAME]',
    'database': '[DATABASE]',
    'ssl_verify_identity': True,
    'ssl_ca': '/etc/ssl/cert.pem',
}

cnx = mysql.connector.connect(**config)
cnx.close()

print("Successfully connected to PlanetScale!")

'''