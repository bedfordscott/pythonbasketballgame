import web_scraping
import data_cleaning
import user_interface
import game_logic
import data_storage

# Step 1: Web Scraping
player_data = web_scraping.scrape_players_data()
df = web_scraping.create_players_dataframe(player_data)

# Step 2: Data Cleaning
df_clean = data_cleaning.clean_players_data(df)

# Step 3: User Interface
root = user_interface.create_user_interface(df_clean)
players = df_clean["Name"].tolist()
user_teams = user_interface.get_user_teams(root, players)

# Step 4: Game Logic
game_stats = game_logic.simulate_game(players)
user_points = game_logic.award_points(game_stats, user_teams, players)

# Step 5: Data Storage
data_storage.store_game_results(user_points)

# Print the final results to the console
print(user_points)
