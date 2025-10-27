import pymysql

class MySQL:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='q1w2e3', db='study_db')
        self.cur = self.db.cursor()
        print("connect ok")

    def add(self, temp, hum):
      
        sql = "insert into record_dht(temperature, humidity) values({0}, {1})".format(temp, hum)

        self.cur.execute(sql)
        
        self.db.commit()

        return [temp, hum]

    def selectAll(self):
        sql = "select * from record_dht"
        all_list = self.cur.execute(sql)
        all_list = self.cur.fetchall()
        return all_list
    
