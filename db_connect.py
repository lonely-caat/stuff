import MySQLdb

db = MySQLdb.connect('host', 'user',
                     'pswd', 'schema')
try:
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    results = cursor.fetchone()
    # Check if anything at all is returned
    if results:
        print(1)
    else:
        print(0)
except MySQLdb.Error:
    print("Failed to connect to DB")

finally:
    db.close()