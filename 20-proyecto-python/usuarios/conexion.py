import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host = "localhost",
        user = "user",
        passwd = "XhS8eSDaQtVh7stW",
        database = "master_python",
        port = 3306
        )

    cursor = database.cursor(buffered=True)
    return [database, cursor]
