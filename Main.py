import matplotlib.pyplot as plt
import mysql.connector as msqc

VENTAS=[]
NOMBRES=[]
connect = msqc.connect(user='admin', password='pass',
                              host='10.105.15.152',
                              database='GAME')
cursor = connect.cursor()

query = ("SELECT ID,VENTAS FROM JUEGARDOS")
cursor.execute(query);


for i in cursor:
    VENTAS.append(i[0])
    NOMBRES.append(i[1])

plt.bar(VENTAS,NOMBRES)
plt.ylim(0, 100000)
plt.ylabel("Ventas")
plt.xlabel("Nombre")
plt.title("Datos")
plt.show()
