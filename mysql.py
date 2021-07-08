# 导入pymysql
import pymysql

# 打开数据库连接
db = pymysql.connect(host="39.106.209.136", user="root", password="Zhaoxw2019@", db="test_db", port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()

# 1.查询操作
# 编写sql 查询语句  user 对应我的表名
sql = "select * from t_user"
try:
    # 执行sql语句
    cur.execute(sql)

    # 获取查询的所有记录
    results = cur.fetchall()
    print("id", "name", "age", "address")
    # 遍历结果
    for row in results:
        userId = row[0]
        name = row[1]
        age = row[2]
        address = row[3]
        print(userId, name, age, address)
except Exception as e:
    raise e
finally:
    # 关闭连接
    db.close()
