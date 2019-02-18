import cx_Oracle

connect = cx_Oracle.connect('travis/travis@localhost:1521/XE')
print(connect.version)