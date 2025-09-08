import pymysql
conn = pymysql.connect(host='localhost', user='kth', password='q1w2e3', db='shopping_db1')
cur = conn.cursor()
cur.execute('select avg(age) from Customer where address="경기"')
result = cur.fetchone()
print(int(result[0]))
cur.close()
conn.close()

