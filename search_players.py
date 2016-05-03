import psycopg2
import pprint


def print_player_data(player):
    print("Rank: {} Name: {}".format(player[0], player[1]))
    print("Rushing Stats: ")
    print("Attempts: {} Yards: {} Average Yards: {} Touchdowns: {}".format(
        player[2], player[3], player[4], player[5]))
    print('Receiving Stats: ')
    print("Receptions: {} Yards: {} Average Yards: {} Touchdowns: {}".format(
        player[6], player[7], player[8], player[9]))
    print('Scrimmage Stats: ')
    print('Plays: {} Yards: {} Average Yards: {} Touchdowns: {}'.format(
        player[10], player[11], player[12], player[13]))


conn = psycopg2.connect("dbname=exercise user=gregiskhan host=/tmp/")
cur = conn.cursor()


cur.execute('SELECT player FROM rushing_receiving;')
players = cur.fetchall()
print("Hello! This program accesses a database containing rushing",
      "and receiving information for the 2015 Carolina Tar Heels.")
print("If you wish, enter a name to find that player's information: \n\n")
for player in players:
    print(player[0])
print('\n\n')

name = input("Enter a player name: ")
cur.execute("SELECT * FROM rushing_receiving WHERE player = '{}';".format(name))
player_data = cur.fetchone()
print_player_data(player_data)
cur.close()
conn.close()
