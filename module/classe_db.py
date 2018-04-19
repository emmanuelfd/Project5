# coding: utf-8

import pymysql
import pymysql.cursors


class DataBaseConnection:



    def __init__(self):
        connection = pymysql.connect(host='localhost',user='root',passwd='sophie',db='OPenFoodFacts',use_unicode=True,\
        charset="utf8")
        connection.autocommit(True)
        self.cursor = connection.cursor()
        #self.commit = connection.commit()

    def fetchalll(self,sql):
        self.cursor.execute(sql)
        #self.commit
        return self.cursor.fetchall()

    def query_insert(self,sql):
        self.cursor.execute(sql)
        #self.commit
        return print('insert## ' + sql + ' ##OK')
