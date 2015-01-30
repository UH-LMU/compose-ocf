
cat /dump/*.sql |mysql -u h132_lmu -p $MYSQL_DATABASE <<-EOF
$MYSQL_PASSWORD 
EOF
