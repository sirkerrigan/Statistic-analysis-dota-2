import pandas as pd
from scipy import stats

# Load data from CSV file
data = pd.read_csv('results_file.csv')

# Create a binary variable for match results
# Assume Radiant_Win == 1 means Radiant won, and 0 means Radiant lost
data['Radiant_Win'] = data['Radiant_Win'].apply(lambda x: 1 if x == 1 else 0)

# Extract GPM values for winning and losing matches
gpm_win = data[data['Radiant_Win'] == 1]['Radiant_GPM']
gpm_loss = data[data['Radiant_Win'] == 0]['Radiant_GPM']

# Perform t-test for independent samples
t_stat, p_value = stats.ttest_ind(gpm_win, gpm_loss, equal_var=False)  # Use equal_var=False if variances are assumed to be different

# Print results
print(f"t-statistic: {t_stat:.2f}")
print(f"p-value: {p_value:.4f}")

# Interpretation of results
alpha = 0.05  # Significance level
if p_value < alpha:
    print("Reject the null hypothesis: Higher GPM significantly affects the win rate of a team.")
else:
    print("Fail to reject the null hypothesis: Higher GPM does not significantly affect the win rate of a team.")
