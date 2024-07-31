import pandas as pd

# Load data from CSV files
radiant_data = pd.read_csv('radiant.csv')
dire_data = pd.read_csv('dire.csv')

# Check if the number of rows in both dataframes is the same
if len(radiant_data) != len(dire_data):
    raise ValueError("The number of rows in radiant_data and dire_data do not match.")

# Combine data based on their index
# Concatenate dataframes along columns with hierarchical indexing to distinguish between the two
combined_data = pd.concat([radiant_data, dire_data], axis=1, keys=['radiant', 'dire'])

# Filter matches where there is a leaver on both teams
matches_with_leaver_in_both = combined_data[
    (combined_data[('radiant', 'leaver_status')] == 1) &
    (combined_data[('dire', 'leaver_status')] == 1)
]

# Calculate the win percentage for Radiant in matches with leavers on both teams
radiant_wins_with_leaver_in_both = matches_with_leaver_in_both[('radiant', 'radiant_win')].sum()
total_matches_with_leaver_in_both = len(matches_with_leaver_in_both)

# Calculate the win percentage for Radiant
radiant_win_percentage_with_leaver_in_both = (radiant_wins_with_leaver_in_both / total_matches_with_leaver_in_both) * 100 if total_matches_with_leaver_in_both > 0 else 0

# Calculate the win percentage for Dire
# If Radiant wins are not counted, Dire wins can be inferred as the remaining matches
dire_wins_with_leaver_in_both = (total_matches_with_leaver_in_both - radiant_wins_with_leaver_in_both)
dire_win_percentage_with_leaver_in_both = (dire_wins_with_leaver_in_both / total_matches_with_leaver_in_both) * 100 if total_matches_with_leaver_in_both > 0 else 0

# Print the results
print(f'Radiant team win percentage with leaver in both teams: {radiant_win_percentage_with_leaver_in_both:.2f}%')
print(f'Dire team win percentage with leaver in both teams: {dire_win_percentage_with_leaver_in_both:.2f}%')
