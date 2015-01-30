import os
from pprint import pprint
import sys
from sqlalchemy import (create_engine, distinct, MetaData, Table, Column, Integer,
        String, DateTime, Float, ForeignKey, and_)
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.ext.automap import automap_base

db_host = "mysql"
db_name = os.getenv("MYSQL_DATABASE")
db_user = os.getenv("MYSQL_USER")
db_pass = os.getenv("MYSQL_PASSWORD")

conn_str = 'mysql+pymysql://%s:%s@%s/%s' % (db_user,db_pass,db_host,db_name)
#print conn_str
engine = create_engine(conn_str)

Base = automap_base()
Base.prepare(engine, reflect=True)
session = Session(engine)

account = Base.classes.accounts
user = Base.classes.webcal_user
resource = Base.classes.webcal_resource
department = Base.classes.dept_lookup

user_resource_x = Base.classes.user_resource_x
user_accounts_x = Base.classes.user_accounts_x

columns = [user.cal_login, \
        resource.resource_name]
queryAccess = session.query(*columns) \
        .join(user_resource_x,user_resource_x.cal_login==user.cal_login) \
        .join(resource,user_resource_x.resource_id==resource.resource_id)

result = queryAccess.all()
for r in result:
    print r


