SELECT users.name, users.uid, users.mail, from_unixtime(created)
FROM users
INNER JOIN (
  SELECT mail
  FROM users
  GROUP BY mail
  HAVING count(mail) > 1
) dupes ON users.mail = dupes.mail
ORDER BY users.mail;


SELECT user_accounts_x.cal_login,accounts.account_name
FROM user_accounts_x
INNER JOIN (
  SELECT cal_login
  FROM user_accounts_x
  GROUP BY cal_login
  HAVING count(account_id) > 1
) dupes ON user_accounts_x.cal_login = dupes.cal_login
INNER JOIN accounts ON accounts.account_id = user_accounts_x.account_id
ORDER BY user_accounts_x.cal_login;

SELECT user_accounts_x.cal_login,accounts.account_name
FROM user_accounts_x
INNER JOIN (
  SELECT cal_login
  FROM user_accounts_x
  GROUP BY cal_login
  HAVING count(account_id) > 1
) dupes ON user_accounts_x.cal_login = dupes.cal_login
INNER JOIN accounts ON accounts.account_id = user_accounts_x.account_id
WHERE user_accounts_x.cal_login NOT IN ('crivaro','hajaalin','mmolin','tanhuanp')
ORDER BY user_accounts_x.cal_login;

# find active users that
# - have made reservations in 2015
# - have more than 1 account
SELECT user_accounts_x.cal_login,accounts.account_name
FROM user_accounts_x
INNER JOIN (
  SELECT cal_login
  FROM user_accounts_x
  GROUP BY cal_login
  HAVING count(account_id) > 1
) dupes ON user_accounts_x.cal_login = dupes.cal_login
INNER JOIN accounts ON accounts.account_id = user_accounts_x.account_id
INNER JOIN (
  SELECT DISTINCT cal_create_by
  FROM webcal_entry
  WHERE webcal_entry.cal_date > '20150101'
) actives ON user_accounts_x.cal_login = actives.cal_create_by
WHERE user_accounts_x.cal_login NOT IN ('crivaro','hajaalin','mmolin','tanhuanp')
ORDER BY user_accounts_x.cal_login;

# list user+account id that have reservations in 2015
SELECT DISTINCT cal_create_by,account_id
FROM webcal_entry
WHERE webcal_entry.cal_date > '20150101'
AND cal_create_by NOT IN ('crivaro','hajaalin','mmolin','tanhuanp')
ORDER BY cal_create_by;

# select users that have reservations in multiple accounts in 2015
SELECT DISTINCT cal_create_by
FROM webcal_entry
INNER JOIN (
  SELECT cal_login
  FROM user_accounts_x
  GROUP BY cal_login
  HAVING count(account_id) > 1
) dupes ON webcal_entry.cal_create_by = dupes.cal_login
WHERE webcal_entry.cal_date > '20150101'
AND cal_create_by NOT IN ('crivaro','hajaalin','mmolin','tanhuanp')
GROUP BY cal_create_by;

# select users that have reservations in multiple accounts
SELECT DISTINCT cal_create_by
FROM webcal_entry
INNER JOIN (
  SELECT cal_login
  FROM user_accounts_x
  GROUP BY cal_login
  HAVING count(account_id) > 1
) dupes ON webcal_entry.cal_create_by = dupes.cal_login
WHERE cal_create_by NOT IN ('crivaro','hajaalin','mmolin','tanhuanp')
GROUP BY cal_create_by;
