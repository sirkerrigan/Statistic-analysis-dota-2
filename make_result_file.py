import pandas as pd

# File paths
radiant_file = 'radiant.csv'
dire_file = 'dire.csv'
results_file = 'results_file.csv'

# Load the data
radiant_data = pd.read_csv(radiant_file)
dire_data = pd.read_csv(dire_file)

# Ensure both files have the same number of rows
if len(radiant_data) != len(dire_data):
    raise ValueError("The number of rows in radiant.csv and dire.csv must be the same.")

# Prepare a list to store results
results = []

# Iterate through each row in the data
for index in range(len(radiant_data)):
    # Get values from radiant and dire files
    radiant_gpm = radiant_data.loc[index, 'gold_per_min']
    radiant_xpm = radiant_data.loc[index, 'xp_per_min']
    dire_gpm = dire_data.loc[index, 'gold_per_min']
    dire_xpm = dire_data.loc[index, 'xp_per_min']
    leaver_status = dire_data.loc[index, 'leaver_status']
    radiant_win = radiant_data.loc[index, 'radiant_win']
    
    # Determine the winner
    if radiant_gpm > dire_gpm and radiant_xpm > dire_xpm:
        result = 'Radiant'
    elif radiant_gpm < dire_gpm and radiant_xpm < dire_xpm:
        result = 'Dire'
    else:
        result = 'Draw'
    
    # Append results to the list
    results.append({
        'Index': index,
        'Radiant_GPM': radiant_gpm,
        'Dire_GPM': dire_gpm,
        'Radiant_XPM': radiant_xpm,
        'Dire_XPM': dire_xpm,
        'Leaver_status': leaver_status,
        'Result': result,
        'Radiant_Win': radiant_win
    })

# Convert the results to a DataFrame
results_df = pd.DataFrame(results)

# Save the results to a CSV file
results_df.to_csv(results_file, index=False)

print(f"Comparison results saved to {results_file}")
