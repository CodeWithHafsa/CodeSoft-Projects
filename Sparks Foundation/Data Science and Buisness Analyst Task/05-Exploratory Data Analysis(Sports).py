# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the IPL dataset
url = "https://bit.ly/34SRn3b"
ipl_df = pd.read_csv(url)

# Explore the dataset
print(ipl_df.head())  # Display the first few rows

# Calculate top run-scorer
top_scorer = ipl_df.groupby("batsman")["batsman_runs"].sum().idxmax()
print(f"Top Run-Scorer: {top_scorer}")

# Calculate top wicket-taker
top_wicket_taker = ipl_df.groupby("bowler")["player_dismissed"].count().idxmax()
print(f"Top Wicket-Taker: {top_wicket_taker}")

# Analyze team performance
team_wins = ipl_df.groupby("winner")["match_id"].nunique()
team_wins.plot(kind="bar", color="skyblue")
plt.title("IPL Team Performance")
plt.xlabel("Team")
plt.ylabel("Number of Wins")
plt.show()

# Explore factors influencing wins and losses
# You can add more analysis here based on your requirements!

# Endorsement recommendations
print("\nEndorsement Recommendations:")
print(f"Consider endorsing {top_scorer} and {top_wicket_taker} for your products.")
print("Successful teams like Mumbai Indians, Chennai Super Kings, and Kolkata Knight Riders are also good choices.")
