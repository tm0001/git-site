import openpyxl
import pandas as pd
import glob

import_file_path = '/Users/masatotakeuchi/Desktop/python/51_jupyter notebooks/54_exel/sample.xlsx'
excel_sheet_name = '発注管理表'
export_file_path = '/Users/masatotakeuchi/Desktop/python/51_jupyter notebooks/54_exel/output'

'Desktop/python/51_jupyter notebooks/54_exel/sample.xlsx'

df_order = pd.read_excel(import_file_path, sheet_name = excel_sheet_name)

company_name = df_order['会社名'].unique()

for i in company_name:
    df_order_company = df_order[df_order['会社名'] == i]
    df_order_company.to_excel(export_file_path+'/'+i+'.xlsx')
