# fig-ocf
Export data from OCF Scheduler.

Login to OCF Scheduler server and make a database dump:
'''
ssh lmu
sudo -i

mysqldump -h hotel-db1.it.helsinki.fi -u h132_lmu -p h132_lmu > /tmp/ocf_dump_20150916.sql

scp /tmp/ocf_dump_20150916.sql ...
'''

Start containers:
'''
. make_env.sh
docker-compose up
'''

Initialize database from dump:
'''
docker exec -it ocf_export_mysql bash

ls /dump
env
mysql -u  -p  < /dump/ocf_dump_20150916.sql
'''


'''
docker exec -it ocf_export_dev bash

python /scripts/read_users.py
sh /scripts/cleanup.sh
'''
