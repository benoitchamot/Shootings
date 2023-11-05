# Dependencies
import pandas as pd
from pathlib import Path

# Local modules
from Local_Modules.data_exploration import find_keyword_in_list

# Import all datasets
cases_df = pd.read_csv(Path('clean_data/clean_cases.csv'))
firearms_df = pd.read_csv(Path('clean_data/clean_firearms.csv'))
shooters_df = pd.read_csv(Path('clean_data/clean_shooters.csv'))

dataset_choice = {
    '1': cases_df,
    '2': firearms_df,
    '3': shooters_df
}

print('Select a dataset:')
print('1: cases_df')
print('2: firearms_df')
print('3: shooters_df')

dataset = input('Your selection: ')
search = input('Enter your search term: ')

print('----')
print('Results:')


results = find_keyword_in_list(search,dataset_choice[dataset].columns)

for r in results:
    print(f"* {r}")

print('----')