import pandas as pd
from sklearn.datasets import load_iris
import math

kw_list = pd.read_excel("KW_list_full.xlsx", usecols='A:B', sheet_name='KW_list') #get kw list here
fin_data = pd.read_excel("KW_list_full.xlsx", usecols='A:AU', sheet_name='Fin_data')
""" eng_data = pd.read_excel("KW_list_full.xlsx", usecols='', sheet_name='Eng_data')
old_data = pd.read_excel("KW_list_full.xlsx", usecols='', sheet_name='Old_data') """
results = pd.read_excel("KW_list_full.xlsx", usecols='A:H', sheet_name='Results', skiprows=3)
""" keywords_columns = [f'Keyword {i}' for i in range(1, 21)]
column_data = results[[f'{i}' for i in range(0,6)]] """

print(kw_list.head())
print(fin_data.columns)
print(results.head())
""" One execution per row of thesis data """
def add_counts(row):
    for value in row:
        selected = kw_list[kw_list['Keywords'] == value]
        if not selected.empty:
            #print(selected)
            results.at[row.name, selected.iloc[0,1]] += 1


fin_data.apply(add_counts, axis=1)

print(results.head())
#kws=pd.DataFrame(add_keywords())
""" def add_keywords(csv_1, kws):
    for index, row in csv_1.loc[:, [keywords_columns]].iterrows():
        kws.append(row[],) """
""" 
def bin_search(kw):
    low = 0
    upper = len(kw_list.index) - 1
    while low <= upper:
        mid = math.floor((lower + upper) / 2)

        comparison = compare(kw, 0, mid)

        if comparison < 0:
            upper = mid - 1
        elif comparison > 0:
            lower = mid + 1
        else:
            return kw_list.iat[mid, len(kw)]

# Utility method
def compare(search_value, search_column_index, df_value_index):      
    if search_column_index >= len(search_value):
        return 0

    if search_value[search_column_index] < kw_list.iat[df_value_index, search_column_index]:
        return -1
    elif search_value[search_column_index] > kw_list.iat[df_value_index, search_column_index]:
        return 1
    else:
        return compare(search_value, search_column_index + 1, df_value_index)
 """
""" # Create a new DataFrame with the selected columns
selected_columns = csv_1[keywords_columns]

# Write the new DataFrame to a new CSV file
selected_columns.to_csv('output.csv', index=False) """