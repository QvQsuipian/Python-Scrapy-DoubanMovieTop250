from pymysql import connect

# 连接数据库
db = connect(
    host="localhost",
    user="root",
    password="12345678",
    database="douban"
)

# 查询所有电影信息
cursor = db.cursor()
cursor.execute("SELECT * FROM movies")
result = cursor.fetchall()

# 打印结果
for row in result:
    print(row)

# 关闭连接
db.close()
