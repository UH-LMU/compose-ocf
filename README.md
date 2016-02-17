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


```
# initialize database from dump
docker exec -it ocf_export_mysql /dump/import.sh

# extract data
docker exec -it ocf_export_dev /scripts/extract.sh

```
