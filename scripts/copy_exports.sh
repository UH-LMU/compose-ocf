CONTAINER=figocf_dev_1
OUTPUT=/output
DEST=/home/hajaalin/tmp/ocf_export

mkdir -p $DEST

docker cp $CONTAINER:$OUTPUT/users.csv $DEST
docker cp $CONTAINER:$OUTPUT/resources.csv $DEST
docker cp $CONTAINER:$OUTPUT/reservations.csv $DEST
docker cp $CONTAINER:$OUTPUT/accounts.csv $DEST
docker cp $CONTAINER:$OUTPUT/access.csv $DEST

ls -l $DEST
