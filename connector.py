from mysql.connector import connect,Error
try:
    db = connect(
        host="localhost",
        user="root",
        password="45874556",
        use_pure=True,
        port=3306
    ) 
    db.autocommit = True
    c = db.cursor()
    c.execute("USE dota")
except Error as e:
    print(e)