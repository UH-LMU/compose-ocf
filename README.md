# compose-ocf
Export data from OCF Scheduler.

Login to OCF Scheduler server and make a database dump:
```
ansible-playbook --become --ask-become-pass -i inventory ocf.yml --vault-password-file=~/.ansible_vault_passes/compose-ocf
./scripts/download.sh

```

Start containers:
```
. make_env.sh
docker-compose up
```

Initialize database from dump:
```
docker exec -it ocf_export_mysql /dump/dump.sh

ls /dump
env
mysql -u ${MYSQL_USER} -p${MYSQL_PASSWORD} ${MYSQL_DATABASE} < /dump/ocf_dump_20150916.sql
```


```
docker exec -it ocf_export_dev /scripts/extract.sh

python /scripts/read_users.py
sh /scripts/cleanup.sh
```
