import tkinter as tk

def create_user_interface(df):
   # Create the user interface
   root = tk.Tk()
   player_listbox = tk.Listbox(root)
   player_listbox.pack(side=tk.LEFT)
   for player in df["Name"].tolist():
       player_listbox.insert(tk.END, player)
   draft_button = tk.Button(root, text="Draft Player", command=root.quit)
   draft_button.pack(side=tk.LEFT)
   return root

def get_user_teams(root, players):
   user_teams = {}
   while len(user_teams) < 2:
       root.mainloop()
       selected_player = player_listbox.get(player_listbox.curselection())
       if selected_player in players:
           player_listbox.delete(player_listbox.curselection())
           user = f"User {len(user_teams) + 1}"
           if user not in user_teams:
               user_teams[user] = []
           user_teams[user].append(selected_player)
   return user_teams
