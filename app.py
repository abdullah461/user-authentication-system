from website import create_app
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "lludbA090",
)
my_cursor = mydb.cursor()

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)