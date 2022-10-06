from pickletools import pydict
import pyodbc

conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server}; SERVER=.;DATABASE=QLMonAn;UID=sa;PWD=sa;Encrypt=no')
cursor = conn.cursor()
cursor.execute("SELECT @@version")
conn.close()
db_version = cursor.fetchone()
print("Ban dang dung he quan tri CSDL SQL server phien ban ", db_version)
