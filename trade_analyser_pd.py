import pandas as pd

try:
	csv_load = pd.read_csv('trades.csv')
except FileNotFoundError:
	print('File Not Found')
	exit()

csv_load['Outcome'] = csv_load.apply(lambda x: 'Win' if x['Pips'] > 0 else 'Loss', axis=1)

print(csv_load)
wins = csv_load[csv_load['Outcome'] == 'Win']
print(f'\nTotal Wins = {len(wins)}')
losses = csv_load[csv_load['Outcome'] == 'Loss']
print(f'Total Losses = {len(losses)}')

rr = wins['RR']
avg_rr = sum(rr) / len(rr)
print(f'Your average RR across winners: {round(avg_rr, 2)}')

best = csv_load['Pips'].idxmax()
best_trade = csv_load.loc[best]
print('\nThis is your best trade:')
print(best_trade)
