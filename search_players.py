import psycopg2


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


def insert_player(player_dict):
    cur.execute(
        """INSERT INTO rushing_receiving VALUES (
        {}, '{}', {}, {}, {}, {}, {},
        {}, {}, {}, {}, {}, {}, {}
        );""".format(player_dict['Rank'], player_dict['Name'], player_dict['Rushing Attempts'],
                     player_dict['Rushing Yards'], player_dict['Rushing Average'], player_dict['Rushing Touchdowns'],
                     player_dict['Receptions'], player_dict['Receiving Yards'], player_dict['Receiving Average'],
                     player_dict['Receiving Touchdowns'], player_dict['Scrimmage Plays'], player_dict['Scrimmage Yards'],
                     player_dict['Scrimmage Average'], player_dict['Scrimmage Touchdowns']))

conn = psycopg2.connect("dbname=exercise user=gregiskhan host=/tmp/")
cur = conn.cursor()

while True:
    cur.execute('SELECT player FROM rushing_receiving;')
    players = cur.fetchall()
    print("Hello! This program accesses a database containing rushing",
          "and receiving information for the 2015 Carolina Tar Heels.")
    user_choice = input("Do you [1] seek player information or [2] wish to enter new information? ")
    if user_choice == '1':
        print("Enter a name to find that player's information: \n\n")
        for player in players:
            print(player[0])
        print('\n\n')

        name = input("Enter a player name: ")
        cur.execute("SELECT * FROM rushing_receiving WHERE player = '{}';".format(name))
        player_data = cur.fetchone()
        print_player_data(player_data)
    elif user_choice == '2':
        player_dict = {}
        player_dict['Rank'] = input("What is the player's rank? ")
        player_dict['Name'] = input("What is the player's name? ")
        player_dict['Rushing Attempts'] = input("How many rushing attempts did the player make? ")
        player_dict['Rushing Yards'] = input("For how many yards did the player rush? ")
        player_dict['Rushing Average'] = input("How many rushing yards did the player average? ")
        player_dict['Rushing Touchdowns'] = input("How many rushing touchdowns did the player score? ")
        player_dict['Receptions'] = input("How many receptions did the player make? ")
        player_dict['Receiving Yards'] = input("How many receiving yards did the player get? ")
        player_dict['Receiving Average'] = input("How many receiving yards did the player average? ")
        player_dict['Receiving Touchdowns'] = input("How many touchdowns did the player catch? ")
        player_dict['Scrimmage Plays'] = input("How many plays from scrimmage did the player participate in? ")
        player_dict['Scrimmage Yards'] = input("How many yards from scrimmage did the player make? ")
        player_dict['Scrimmage Average'] = input("How many yards from scrimmage did the player average? ")
        player_dict['Scrimmage Touchdowns'] = input("How many touchdowns did the player score from scrimmage plays? ")
        insert_player(player_dict)
        conn.commit()
    elif user_choice == '':
        break
    else:
        continue
cur.close()
conn.close()
