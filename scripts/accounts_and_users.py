import csv, codecs, cStringIO
import os
from pprint import pprint
import string
import sys
from sqlalchemy import (create_engine, distinct, MetaData, Table, Column, Integer,
        String, DateTime, Float, ForeignKey, and_, asc)
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.ext.automap import automap_base

from read_users import print_csv



db_host = "mysql"
db_name = os.getenv("MYSQL_DATABASE")
db_user = os.getenv("MYSQL_USER")
db_pass = os.getenv("MYSQL_PASSWORD")

conn_str = 'mysql+pymysql://%s:%s@%s/%s' % (db_user,db_pass,db_host,db_name)
#print conn_str
engine = create_engine(conn_str)
#, encoding='latin1-swedish-ci', convert_unicode=True)

Base = automap_base()
Base.prepare(engine, reflect=True)
session = Session(engine)

accounts = Base.classes.accounts
webcal_entry = Base.classes.webcal_entry
webcal_user = Base.classes.webcal_user
webcal_resource = Base.classes.webcal_resource
dept_lookup = Base.classes.dept_lookup

resource_services = Base.classes.resource_services

user_resource_x = Base.classes.user_resource_x
user_accounts_x = Base.classes.user_accounts_x

# select user_accounts_x.cal_login,account_id from user_accounts_x inner join (select cal_login from user_accounts_x group by cal_login having count(*)>1) dup on user_accounts_x.cal_login=dup.cal_login;

columns = [user_accounts_x.cal_login, \
user_accounts_x.account_id]

login = user_accounts_x.cal_login
account = user_accounts_x.account_id
account_name = accounts.account_name
account_id = accounts.account_id
account_number = accounts.account_number

#.group_by(user_accounts_x.cal_login) \
#query = session.query(*columns) \
query = session.query(account_name, account_number, login) \
.join(user_accounts_x, user_accounts_x.account_id==accounts.account_id) \
.order_by(asc(account_name))
#.having(func.count(account)>1)
result = query.all()
print_csv("/output/accounts_and_users.csv", result)
