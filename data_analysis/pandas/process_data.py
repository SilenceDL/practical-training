import pandas as pd
import pymysql


class processData():
    host = '127.0.0.1'
    user = 'root'
    pwd = '123456'
    db = 'spider'
    c = 'utf8'
    port = 3306

    def connect_db(self):
        db=pymysql.connect(host=self.host,port=3306,user=self.user,passwd=self.pwd,db=self.db,charset=self.c)
        sql = "SELECT * FROM a51job"  # SQL query
        df = pd.read_sql(sql=sql, con=db)  # read data to DataFrame 'df'
        return df

    def process_data(self, df):
        pass

if __name__ == '__main__':
    p = processData()
    out = pd.ExcelWriter('51job.xls')
    p.connect_db().to_excel(out)
    out.save()

