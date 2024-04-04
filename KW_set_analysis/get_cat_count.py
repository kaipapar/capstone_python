import pandas as pd
from sklearn.datasets import load_iris
import numpy as np

class Category_counter():
    
    def __init__(self, data, file_in, file_out):
        self.data = data
        self.file_in = file_in
        self.file_out = file_out
        self.kw_list = pd.read_excel(file_in, usecols='A:B', sheet_name='KW_list') #get kw list here
        self.results = pd.DataFrame()

    def read(self):
        print(self.kw_list.head())
        print(self.data.head())
        self.results = pd.DataFrame(0, index=range(len(self.data)), columns=range(8))
        self.results[0] = self.data.iloc[:, 0].values

        print(self.data.head())
        print(self.results.head())
        """ One execution per row of thesis data """

        self.data.apply(self.add_counts, axis=1)
        print(self.results.head())

    def add_counts(self, row):
        for value in row:
            selected = self.kw_list[self.kw_list['Keywords'] == value]
            if not selected.empty:
                self.results.at[row.name, selected.iloc[0,1]] += 1

    def write_xcel(self):
        # creating an ExcelWriter object
        with pd.ExcelWriter(self.file_out) as writer:
            # writing to the 'Employee' sheet
            self.results.to_excel(writer, index=False)
        #print('DataFrames are written to Excel File successfully.')

if __name__ == "__main__":
    file = "KW_list_full.xlsx"
    file_out = "KW_occurence_count.xlsx"
    #data = pd.read_excel(file, usecols='A:AU', sheet_name='Fin_data') 
    data = pd.read_excel(file, usecols='', sheet_name='Eng_data')
    #data = pd.read_excel(file, usecols='', sheet_name='Old_data')
    print(data.head())
    cls_instance = Category_counter(data, file, file_out)
    cls_instance.read()
    cls_instance.write_xcel()

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