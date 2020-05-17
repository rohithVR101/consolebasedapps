#Use the package Faker 4.1.0
from faker import Faker

def createplayers(n):
    fake = Faker()
    #Make a new text file
    file = open('players.txt', 'w')
    file.close()
    #Generate Player Names in players.txt
    file = open('players.txt', 'a')
    for i in range(n):
        file.write(fake.name()+"\n")
    file.close()
