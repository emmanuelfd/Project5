# coding: utf-8

import pymysql
import pymysql.cursors


class DataBaseConnection:
    """ to be used when working on accessing MySql DB
    """

    def __init__(self):
        """ connect to the DB with autocommit
        cursor active
        """
        connection = pymysql.connect(host='localhost', user='root', passwd='sophie', db='OPenFoodFacts', \
        use_unicode=True, charset="utf8")
        connection.autocommit(True)
        self.cursor = connection.cursor()
        #self.commit = connection.commit()

    def fetchalll(self, sql):
        """ to return data loaded, execute cursor and return all
        """
        self.cursor.execute(sql)
        #self.commit
        return self.cursor.fetchall()

    def query_insert(self, sql):
        """ to execute cursor. for insertion in db, return a validation
        """
        self.cursor.execute(sql)
        #self.commit
        return print('insert## ' + sql + ' ##OK')
