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
        self.connection = pymysql.connect(host='localhost', user='root', passwd='sophie', db='OpenFoodFacts', \
        use_unicode=True, charset="utf8")
        self.connection.autocommit(True)
        self.cursor = self.connection.cursor()
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

    def close_db(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
