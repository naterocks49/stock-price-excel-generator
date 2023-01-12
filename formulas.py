import pandas as pd
import json
import openpyxl

def JSON_to_EXCEL(json_data):

    df = pd.DataFrame(json_data)
    

    df.reset_index(inplace=True)
    df.rename(columns={'index':'date'}, inplace=True)

    print(df)
    return df.to_excel('data.xlsx', engine='openpyxl', index=False)

