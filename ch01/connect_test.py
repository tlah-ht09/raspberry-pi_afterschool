import pymysql

#1. 연결
conn = pymysql.connect(host="localhost",user="jht", password="q1w2e3",db="shopping_db2")

#2. 커서
cur = conn.cursor()

#3. 쿼리 작성
cur.execute("select avg(age) from Customer where address='경기'")

#4. 결과 조회
result = cur.fetchall()
print(int(result[0][0]))

#5. 종료(연결 해제)
cur.close()
conn.close()
