import pandas as pd
csv_1 = pd.read_csv(r"C:\Users\kkors\OneDrive - Turun ammattikorkeakoulu\24s Capstone\capstone\CSV_old_data.csv", delimiter=",", encoding='utf-8', error_bad_lines=False)
drop_columns = csv_1.columns[0:10] # columns 0-9 dont contain KWs 

""" def add_keywords(csv_1, kws):
    for index, row in csv_1.loc[:, [keywords_columns]].iterrows():
        kws.append(row[],) """

#kws=pd.DataFrame(add_keywords())

# Create a new DataFrame with the selected columns
selected_columns= csv_1.drop(drop_columns, axis='columns')
# Write the new DataFrame to a new CSV file
selected_columns.to_csv('old_KWs_xtracted.csv', index=False)