import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv('results_file.csv')

# Create a binary variable for match results
data['Radiant_Win'] = data['Radiant_Win'].apply(lambda x: 1 if x == 1 else 0)

# Create scatter plots for GPM and XPM vs. win/loss
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Scatter Plot for GPM
sns.scatterplot(x='Radiant_GPM', y='Radiant_Win', data=data, ax=axes[0])
axes[0].set_title('Radiant GPM vs. Win/Loss')
axes[0].set_xlabel('Radiant Gold Per Minute (GPM)')
axes[0].set_ylabel('Radiant Win (1) / Loss (0)')

# Scatter Plot for XPM
sns.scatterplot(x='Radiant_XPM', y='Radiant_Win', data=data, ax=axes[1])
axes[1].set_title('Radiant XPM vs. Win/Loss')
axes[1].set_xlabel('Radiant Experience Per Minute (XPM)')
axes[1].set_ylabel('Radiant Win (1) / Loss (0)')

plt.tight_layout()
plt.show()

# Create histograms for GPM and XPM distributions
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Histogram for GPM
sns.histplot(data[data['Radiant_Win'] == 1]['Radiant_GPM'], bins=30, color='green', label='Win', ax=axes[0], kde=True)
sns.histplot(data[data['Radiant_Win'] == 0]['Radiant_GPM'], bins=30, color='red', label='Loss', ax=axes[0], kde=True)
axes[0].set_title('Distribution of Radiant GPM')
axes[0].set_xlabel('Radiant Gold Per Minute (GPM)')
axes[0].set_ylabel('Frequency')
axes[0].legend()

# Histogram for XPM
sns.histplot(data[data['Radiant_Win'] == 1]['Radiant_XPM'], bins=30, color='green', label='Win', ax=axes[1], kde=True)
sns.histplot(data[data['Radiant_Win'] == 0]['Radiant_XPM'], bins=30, color='red', label='Loss', ax=axes[1], kde=True)
axes[1].set_title('Distribution of Radiant XPM')
axes[1].set_xlabel('Radiant Experience Per Minute (XPM)')
axes[1].set_ylabel('Frequency')
axes[1].legend()

plt.tight_layout()
plt.show()

# Create box plots for GPM and XPM
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Box Plot for GPM
sns.boxplot(x='Radiant_Win', y='Radiant_GPM', data=data, ax=axes[0])
axes[0].set_title('Box Plot of Radiant GPM by Win/Loss')
axes[0].set_xlabel('Radiant Win (1) / Loss (0)')
axes[0].set_ylabel('Radiant Gold Per Minute (GPM)')

# Box Plot for XPM
sns.boxplot(x='Radiant_Win', y='Radiant_XPM', data=data, ax=axes[1])
axes[1].set_title('Box Plot of Radiant XPM by Win/Loss')
axes[1].set_xlabel('Radiant Win (1) / Loss (0)')
axes[1].set_ylabel('Radiant Experience Per Minute (XPM)')

plt.tight_layout()
plt.show()
