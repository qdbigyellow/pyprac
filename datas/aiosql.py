# https://github.com/nackjicholson/aiosql
# read query from sql file,  and apply it to a database connection
# avoid writing all complex sql in the code. 
# easy to test the sql script 

# -- name: get-all-users
# -- Get all user records
# select userid,
#        username,
#        firstname,
#        lastname
#   from users;


# -- name: get-user-by-username^
# -- Get user with the given username field.
# select userid,
#        username,
#        firstname,
#        lastname
#   from users
#  where username = :username;


import aiosql
import sqlite3

conn = sqlite3.connect("myapp.db")
# read query from .sql file
queries = aiosql.from_path("users.sql", "sqlite3")

# run query "get_all_users" on connection "conn",  "get_all_user" is the name property of sql query
users = queries.get_all_users(conn)

# run query "get_user_by_username" on connection "conn",  "get_user_by_username" is the name property of sql query
users = queries.get_user_by_username(conn, username="nackjicholson")