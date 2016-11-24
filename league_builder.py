import csv
import sys
import os
import random
import time

if __name__ == "__main__":
    # create variables
    Sharks = []
    Dragons = []
    Raptors = []
    players_list = []
    xp = []
    no_xp = []
    teams = {'Sharks': [], 'Dragons': [], 'Raptors': []}

    # function that takes in a list of players
    # and divides them into equal teams
    def get_teams(players):
        # check if number of experienced players is even
        if len(players) % 2 > 0:
            # check if number of experienced players
            # is divisible by number of teams
            if len(players) % 3 == 0:
                while len(players) > 0:
                    random.shuffle(players)
                    teams['Sharks'].append(players[0])
                    players.remove(players[0])
                    teams['Dragons'].append(players[0])
                    players.remove(players[0])
                    teams['Raptors'].append(players[0])
                    players.remove(players[0])
            else:
                print("""Uneven number of players.
                         One team will be advantaged/disadvantaged!!!""")

    # read csv file with the list of players
    with open('soccer_players.csv', newline='') as f:
        players = csv.reader(f)
        players_list = list(players)

        # remove the header
        players_list.remove(players_list[0])

        # separate all the  experienced players first from the rest
        for player in players_list:
            # use 2 since its the index for soccer experience
            if player[2].lower() == 'yes':
                xp.append(player)
            else:
                no_xp.append(player)

    # programming logic to divide 18 players into 3 teams of 6 players
    # team names are Sharks, Dragons, and Raptors and should have
    # equal number of players and experienced players should be even.
    get_teams(xp)
    get_teams(no_xp)

    # function that creates team.txt that includes:
    # name of team
    # player_name, EXPERIENCED, guardian(s)_name
    def write_team(file, team_name, players):
        f = open(file, 'a')
        f.write(team_name + '\n')
        for player in players:
            f.write("{}, {}, {}\n".format(player[0], player[2], player[3]))
        f.write('\n')
        f.close()

    # Function that checks if a file exists
    def exist(file):
        if os.path.exists(file):
            # if the file exists open it and clear everything inside
            f = open(file, 'w')
            f.close()

    exist('team.txt')
    # write teams to file
    for name, players in teams.items():
        write_team('team.txt', name, players)

    # create 18 player_name.txt files(a .txt file for each player)
    # which are welcome letters to players' guardians
    # each player_name.txt file begins with the text "Dear 'guardian(s)_name' "
    # and should include
    # player_name, team_name, and time & date of first practise
    def write_letter(file, team_name, layers):
        for player in players:
            # check if a directory letters exsists then make it if it doesn't
            if not os.path.exists(file):
                os.makedirs(file)
            exist(file + '_'.join(player[0].split(' ')) + '.txt')
            f = open(file + '_'.join(player[0].split(' ')) + '.txt', 'a')
            f.write('Dear {},\n'.format(player[3]))
            f.write("{} of team {} is required for practice on {} at 1700hrs."
                    .format(player[0], team_name, time.strftime("%d/%m/%Y")))
            f.close()
    f = os.getcwd() + '/Letters/'
    # write letters for every team member for all teams
    for name, players in teams.items():
        write_letter(f, name, players)
