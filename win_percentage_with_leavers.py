import pandas as pd

# Load data from CSV files
radiant_data = pd.read_csv('radiant.csv')
dire_data = pd.read_csv('dire.csv')

# Function to calculate win percentages with and without leavers
def calculate_win_percentages(data):
    total_matches = len(data)
    
    # Calculate win percentages with leavers
    leaver_wins = data[data['leaver_status'] == 1]['radiant_win'].sum()
    leaver_matches = len(data[data['leaver_status'] == 1])
    if leaver_matches > 0:
        leaver_win_percentage = (leaver_wins / leaver_matches) * 100
    else:
        leaver_win_percentage = 0
    
    # Calculate win percentages without leavers
    no_leaver_wins = data[data['leaver_status'] == 0]['radiant_win'].sum()
    no_leaver_matches = len(data[data['leaver_status'] == 0])
    if no_leaver_matches > 0:
        no_leaver_win_percentage = (no_leaver_wins / no_leaver_matches) * 100
    else:
        no_leaver_win_percentage = 0
    
    return leaver_win_percentage, no_leaver_win_percentage

# Calculate win percentages for Radiant team
radiant_leaver_win_percentage, radiant_no_leaver_win_percentage = calculate_win_percentages(radiant_data)
print(f'Radiant team win percentage with leaver: {radiant_leaver_win_percentage:.2f}%')
print(f'Radiant team win percentage without leaver: {radiant_no_leaver_win_percentage:.2f}%')

# Calculate win percentages for Dire team
dire_leaver_win_percentage, dire_no_leaver_win_percentage = calculate_win_percentages(dire_data)
print(f'Dire team win percentage with leaver: {dire_leaver_win_percentage:.2f}%')
print(f'Dire team win percentage without leaver: {dire_no_leaver_win_percentage:.2f}%')
