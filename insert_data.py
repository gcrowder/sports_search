import psycopg2
import pandas as pd


def create_table():
    cur.execute(
        """CREATE TABLE rushing_receiving (
           Rank INTEGER,
           Player varchar,
           Rushing_Attempts numeric,
           Rushing_Yds numeric,
           Rushing_Avg numeric,
           Rushing_TD numeric,
           Receiving_Rec numeric,
           Receiving_Yds numeric,
           Receiving_Avg numeric,
           Receiving_TD numeric,
           Scrimmage_Plays numeric,
           Scrimmage_Yds numeric,
           Scrimmage_Avg numeric,
           Scrimmage_TD numeric
         );""")


def insert_data():
    rushing_receiving = pd.read_csv('2015_Carolina_Rushing_Receiving.csv')
    rushing_receiving.fillna(0, inplace=True)
    for row in rushing_receiving.itertuples():
        cur.execute(
            """INSERT INTO rushing_receiving VALUES (
            {}, '{}', {}, {}, {}, {}, {},
            {}, {}, {}, {}, {}, {}, {}
            );""".format(row[1], row[2], row[3], row[4], row[5], row[6],
                         row[7], row[8], row[9], row[10], row[11], row[12],
                         row[13], row[14]))

conn = psycopg2.connect("dbname=exercise user=gregiskhan host=/tmp/")
cur = conn.cursor()

cur.execute("select exists(select * from information_schema.tables where table_name=%s)", ('2015_carolina_football',))
if cur.fetchone()[0]:
    insert_data()
else:
    create_table()
    insert_data()

conn.commit()
cur.close()
conn.close()
