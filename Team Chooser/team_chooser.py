from random import choice
import data_generator

def split_teams(n,t):
    #create a list of players from a file
    players = []
    data_generator.createplayers(n)
    file = open('players.txt', 'r')
    players = file.read().splitlines()

    #create a list of team names from a file
    teamNames = []
    file = open('teamNames.txt', 'r')
    teamNames = file.read().splitlines()[0:t]

    #create empty team lists with random names
    teams={x: [] for x in teamNames}

    #loop until there are no players left
    while len(players) > 0:
        for team in teamNames:
            player = choice(players)
            teams[team].append(player)
            players.remove(player)
            if players == []:
                break
    #print the teams
    print('Here are your teams:\n')
    for x in teams:
        print(x)
        for y in teams[x]:
            print('\t'+y)


if __name__=="__main__":
    #Get user data to provide boundaries
    n=int(input("Enter the total number of players: "))
    t=int(input("Enter the total number of teams: (less than 10)"))
    split_teams(n,t)
