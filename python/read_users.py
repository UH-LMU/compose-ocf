import os
from pprint import pprint
import sys
from sqlalchemy import (create_engine, distinct, MetaData, Table, Column, Integer,
        String, DateTime, Float, ForeignKey, and_)
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.ext.automap import automap_base

db_host = "mysql"
db = os.getenv("MYSQL_DATABASE")
db_user = os.getenv("MYSQL_USER")
db_pass = os.getenv("MYSQL_PASSWORD")

engine = create_engine('mysql://%s:%s@%s/%s') % (db_user,db_pass,db_host,db)


