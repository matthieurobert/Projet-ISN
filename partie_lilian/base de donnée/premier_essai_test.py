import sqlite3

connection = sqlite3.connect("partie_lilian\base de donnée\base.db")
cusor = connection.cursor()

print(type(connection))
print(type(cusor))



 
connection.close()