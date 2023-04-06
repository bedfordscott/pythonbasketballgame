import sqlite3

def store_game_results(user_points):
   # Connect to the database
   conn = sqlite3.connect("fantasy_basketball.db")

   # Create a table to store the game results
   conn.execute("""CREATE TABLE IF NOT EXISTS game_results (
                   user TEXT,
                   points INT
                   );""")

   # Insert the game results into the table
   for user, points in user_points.items():
       conn.execute("INSERT INTO game_results (user, points) VALUES (?, ?)", (user, points))

   # Commit the changes and close the connection
   conn.commit()
   conn.close()
