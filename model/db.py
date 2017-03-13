#coding:utf-8
import sqlite3
class db(object):
	def __init__(self, table):
		#db connect
		self.conn = sqlite3.connect("cache.db")
		self.conn.execute('''
            create table if  not exists  project(
		    id             int       primary key    not null,
		    name           char(80)  not null,
	        taskid         int       not null,
	        respath        char(50)  not null,
	        status         int);
	    ''')
		self.table = table

	def sqlexec(self,sql):
		return self.conn.execute(sql)

	def insert(self,context):
		if type(context) != dict:
			return False
		for key in context:
			sql_columns  = key + ","
			sql_vlaue  =  context[key] + ","
			sql = "insert into " + self.table +"(%s) values(%s);" %(sql_columns[:len(sql_columns)-1],sql_vlaue[:sql_vlaue]-1)
		return self.sqlexec(sql)

	def select(self,where = "1=1" ,limit="0,5"):
	    sql = "select * from " + self.table + " where %s limit %s" %(where,limit)
	    return self.sqlexec(sql)

db = db("project")



