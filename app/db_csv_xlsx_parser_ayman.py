import sqlite3
from io import BytesIO

import pandas as pd

def csv_to_xlsx_pd(file_name):
    df = pd.read_csv(file_name, on_bad_lines='skip')
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='data', index=False)
    output.seek(0)
    return pd.ExcelFile(output)


def loadXlsx(file_name):
    xl = pd.ExcelFile(file_name)
    return xl


def getXlxsFromDB(file_name):
    conn = sqlite3.connect(file_name)

    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Loop through each table and export data to separate Excel sheets
    for table in tables:
        table_name = table[0]
        output = BytesIO()
        # Export data to an Excel sheet in memory sheets
        df = pd.read_sql_query(f"SELECT * FROM {table_name};", conn)
        # print(table_name)
        if table_name != 'sqlite_sequence':
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='data', index=False)
            output.seek(0)
            conn.close()
            return pd.ExcelFile(output)
        else:
            print(table_name)


def parse(instance, type='xlsx'):
    sheet_list = instance.sheet_names
    concatenated_df = pd.DataFrame()

    for sheet_name in sheet_list:
        # Read each sheet into a DataFrame
        df = pd.read_excel(instance, sheet_name=sheet_name, engine='openpyxl')

        # Stack the DataFrame one below the other
        concatenated_df = pd.concat([concatenated_df, df], ignore_index=True)
        if type == 'db':
            concatenated_df.dropna(inplace=True)

    csv_data = concatenated_df.to_csv(header=False, index=False)

    return csv_data

#usage
# file_name = "/Users/test/Downloads/sample_set_labeld/db/true_names/while-hundred-list.db"
# if file_name.endswith('.db'):
#     instance = getXlxsFromDB(file_name)
# elif file_name.endswith('.xlsx'):
#     instance = loadXlsx(file_name)
# elif file_name.endswith('.csv'):
#     instance = csv_to_xlsx_pd(file_name)
# csv_data = parse(instance)