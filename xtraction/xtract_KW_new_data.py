import pandas as pd
csv_1 = pd.read_csv(r"C:\Users\kkors\Downloads\cleaned_finnish_v3.csv", delimiter=";", encoding='utf-8')
keywords_columns = [f'Keyword {i}' for i in range(1, 21)]

""" def add_keywords(csv_1, kws):
    for index, row in csv_1.loc[:, [keywords_columns]].iterrows():
        kws.append(row[],) """

#kws=pd.DataFrame(add_keywords())

# Create a new DataFrame with the selected columns
selected_columns = csv_1[keywords_columns]

# Write the new DataFrame to a new CSV file
selected_columns.to_csv('output.csv', index=False)