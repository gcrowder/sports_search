# sports_search
This repository documents a small exercise in learning SQL and the psycopg2 module.


If you wish to run this exercise locally, you must create a postgresql database and change the dbname and user variables to your own settings in the database connection command.
## insert_data.py
This script checks to see if a certain table has been created in the database. If the table has been exists, the script inserts 19 rows of player data into the table. If the table doesn't exist, it creates the table and then inserts the data.

## search_players.py
This script can retrieve and insert data into the table from user input.

## 2015_Carolina_Rushing_Receiving.txt
This csv file was collected from: [Sports-Reference.com](http://www.sports-reference.com/cfb/schools/north-carolina/2015.html).
