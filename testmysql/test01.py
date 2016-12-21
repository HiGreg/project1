#!/usr/bin/env python
import pymysql 
db  = pymysql.connect ("node","root","didong12","hexing")
cursor  = db.cursor()
#cursor.execute("show tables")
#data  = cursor.fetchone()
#print (data)
cursor.execute("drop table if exists good")
sql = ''' create table good (
          id int not null,
		  first_name  char(60),
		  last_name   char(60),
		  age int,
		  sex char(20)
		  )'''
try:

	cursor.execute(sql)

	insert  =  '''  insert into good (id,first_name,last_name,age,sex) values (1,'greg','he',18,'male') '''
	cursor.execute(insert)
	cursor.execute("select * from good")
	print (cursor.fetchall())
	cursor.execute("commit")
except:
	db.rollback()
db.close()

