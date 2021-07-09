import pymysql

db = pymysql.connect(host="39.106.209.136", user="root", password="Zhaoxw2019@", db="test_db", port=3306)
cur = db.cursor()
sql = "select * from t_user"
try:
    cur.execute(sql)
    results = cur.fetchall()
    print("id", "name", "age", "address")
    for row in results:
        userId = row[0]
        name = row[1]
        age = row[2]
        address = row[3]
        print(userId, name, age, address)
except Exception as e:
    raise e
finally:
    db.close()
