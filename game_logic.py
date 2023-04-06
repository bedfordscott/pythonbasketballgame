import random

def simulate_game(players):
   game_stats = {}
   for player in players:
       points = random.randint(0, 30)
       rebounds = random.randint(0, 15)
       assists = random.randint(0, 10)
       game_stats[player] = {"Points": points, "Rebounds": rebounds, "Assists": assists}
   return game_stats

def award_points(game_stats, user_teams, players):
   user_points = {}
   for user, team in user_teams.items():
       points = 0
       for player in team:
           if player in players:
               points += game_stats[player]["Points"] + game_stats[player]["Rebounds"] + game_stats[player]["Assists"]
       user_points[user] = points
   return user_points
