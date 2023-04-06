def clean_players_data(df):
   # Remove any whitespace from the stats column
   df["Stats"] = df["Stats"].str.strip()

   # Split the stats column into separate columns for points, rebounds, and assists
   df[["Points", "Rebounds", "Assists"]] = df["Stats"].str.split(",", expand=True)

   # Remove the original stats column
   df = df.drop("Stats", axis=1)

   # Convert the points, rebounds, and assists columns to integers
   df[["Points", "Rebounds", "Assists"]] = df[["Points", "Rebounds", "Assists"]].astype(int)

   return df
