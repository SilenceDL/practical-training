# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
# from job_spyder.job_spyder import settings
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# MYSQL_HOST = '127.0.0.1'
# MYSQL_DBNAME = 'spider'
# MYSQL_USER = 'root'
# MYSQL_PASSWD = '123456'
# CHARSET = 'utf8'

# MYSQL_PORT = 3306

class JobSpyderPipeline:
    def process_item(self,item, spider):
        host = '127.0.0.1'
        user = 'root'
        pwd = '123456'
        db = 'spider'
        c = 'utf8'
        port = 3306

        # 数据库连接
        con = pymysql.connect(host=host, user=user, passwd=pwd, db=db, charset=c, port=port)
        # 数据库游标
        cue = con.cursor()
        print("Mysql connect succes!")
        sqls = "insert into a51job(Title,Company,Salary,Location,date,DataSource,Experience,Education) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        paras = (item['title'], item['company'], item['salary'], item['location'], item['date'], item['datasource'], item['experience'], item['education'])
        # paras = ('title', 'company', 'salary', 'location', 'date', 'datasource')

        try:
            cue.execute(sqls, paras)
            print("insert success")
        except Exception as e:
            print("Insert error: ", e)
            con.rollback()
        else:
            con.commit()
        con.close()

        return item

