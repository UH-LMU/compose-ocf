TMP="tmp.sql"
echo $MYSQL_PASSWORD >> $TMP
cat /dump/*.sql >> $TMP

mysql -u $MYSQL_USER -p $MYSQL_DATABASE < $TMP

rm $TMP
