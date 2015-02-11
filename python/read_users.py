import csv, codecs, cStringIO
import os
from pprint import pprint
import string
import sys
from sqlalchemy import (create_engine, distinct, MetaData, Table, Column, Integer,
        String, DateTime, Float, ForeignKey, and_)
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.ext.automap import automap_base


def print_csv(filename, query_result):
    csvfile = open(filename,"w")

    # loop over all rows found
    for r in query_result:
        r = list(r)
        #print r
        # if some field was not found, write "None"
        for i in range(0,len(r)):
            #print r[i], type (r[i])
            if r[i] == None:
                r[i] = "None"
            # the MySQL database used latin1_swedish_ci encoding
            r[i] = r[i].decode('latin1')
        output = string.join(r,",") + "\n"
        output = unicode(output).encode('utf-8')
        csvfile.write(output)
    csvfile.close()


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
webcal_user = Base.classes.webcal_user
webcal_resource = Base.classes.webcal_resource
dept_lookup = Base.classes.dept_lookup

user_resource_x = Base.classes.user_resource_x
user_accounts_x = Base.classes.user_accounts_x

# list instrument access per user
columns = [webcal_user.cal_login, \
        webcal_resource.resource_name]
query = session.query(*columns) \
        .join(user_resource_x,user_resource_x.cal_login==webcal_user.cal_login) \
        .join(webcal_resource,user_resource_x.resource_id==webcal_resource.resource_id)
result = query.all()

print_csv("/output/access.csv", result)


# list user data
columns = [webcal_user.cal_login, \
        webcal_user.cal_passwd, \
        webcal_user.cal_lastname, \
        webcal_user.cal_firstname, \
        webcal_user.cal_email,\
        webcal_user.phone, \
        accounts.account_name,\
        #accounts.account_number,\
        dept_lookup.description]
query = session.query(*columns) \
        .join(accounts, accounts.account_id==webcal_user.default_account_id) \
        .join(dept_lookup, dept_lookup.dept_id==webcal_user.dept_id) \
        .order_by(accounts.account_name,webcal_user.cal_lastname)
result = query.all()
print_csv("/output/users.csv",result)

# list resources
columns = [webcal_resource.resource_name]
query = session.query(*columns)
result = query.all()
print_csv("/output/resources.csv",result)

# list accounts
columns = [accounts.account_number, \
        accounts.account_name, \
        #accounts.account_description\
        ]
query = session.query(*columns)
result = query.all()
print_csv("/output/accounts.csv",result)





