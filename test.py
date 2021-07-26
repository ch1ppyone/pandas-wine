import pandas as pd

excel_data_df = pd.read_excel('wine2.xlsx',  header=None)
print(excel_data_df[0])