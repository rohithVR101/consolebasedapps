import mysql.connector
import random

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12348989"
)

mycursor = mydb.cursor()
mycursor.execute("use sudoku")
mycursor.execute("SELECT * FROM puzzles")

x=random.randint(0,4)
results = mycursor.fetchall()

myresult=str(results[x])
myresult=myresult.lstrip("('")
myresult=myresult.rstrip("',)")
myresult=myresult.split(",")

puz=[[],[],[],[],[],[],[],[],[]]
c=0
for i in range(9):
    for j in range(9):
        if(myresult[c].isnumeric()):
            puz[i].append(int(myresult[c]))
        else:
            puz[i].append(myresult[c])
        c+=1
def get_puzzle():
    return puz,x
