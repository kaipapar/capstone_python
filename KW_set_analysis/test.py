import pandas as pd

# Sample DataFrames
data_a = {'A': ['apple', 'banana', 'orange'],
          'B': ['cat', 'dog', 'fish']}
data_b = {'C': ['apple', 'elephant', 'fish'],
          'D': ['dog', 'gorilla', 'zebra']}
df_a = pd.DataFrame(data_a)
df_b = pd.DataFrame(data_b)

# Check if any cell in a row of DataFrameA contains any cells of DataFrameB
for index, row in df_a.iterrows():
    if row.isin(df_b.values.flatten()).any():
        print(f"At least one cell in row {index} of DataFrameA contains a cell from DataFrameB.")
        
    else:
        print(f"No cell in row {index} of DataFrameA contains a cell from DataFrameB.")
