from pickletools import pydict
import pyodbc

conn = pyodbc.connect(driver='{SQL Server}',host='WINDOWS-11\SQLEXPRESS', database='QLSinhVien', trusted_connection='yes',encrypt='no')
cursor = conn.cursor()
cursor.execute("SELECT @@version")
conn.close()
db_version = cursor.fetchone()
print("Ban dang dung he quan tri CSDL SQL server phien ban ", db_version)
