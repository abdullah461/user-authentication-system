import mysql.connector

db = mysql.connector.connect(
    host = "gcp.connect.psdb.cloud",
    user = "pgdaxrj9kn5ooadbodu0" ,
    passwd = "pscale_pw_MhtAbC6zEJCYsfkujE4IPaw1CGpsC05vGD74bwGHgzt",
)

my_cursor = db.cursor()
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)