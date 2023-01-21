import matplotlib.pyplot as plt
import mysql.connector as msqc

VENTAS=[]
NOMBRES=[]
connect = msqc.connect(user='user', password='password',
                              host='IP',
                              database='database')
cursor = connect.cursor()

query = ("SELECT coumn1,coumn2 FROM table1")
cursor.execute(query);


for i in cursor:
    coumn1.append(i[0])
    coumn2.append(i[1])

plt.bar(coumn1,coumn2)
plt.ylim(0, 100000)
plt.ylabel("label")
plt.xlabel("label")
plt.title("Data")
plt.show()
