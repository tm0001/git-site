import openpyxl
import pandas as pd
import glob

export_file_path = '/Users/masatotakeuchi/Desktop/python/51_jupyter notebooks/54_exel/input'
import_folder_path = '/Users/masatotakeuchi/Desktop/python/51_jupyter notebooks/54_exel/output'
path = import_folder_path + '/' + '*.xlsx'
file_path = glob.glob(path)

df_concat=pd.DataFrame()
for i in file_path:
    df_read_excel=pd.read_excel(i)
    df_concat=pd.concat([df_read_excel,df_concat])  

df_drop = df_concat.drop('Unnamed: 0', axis = 1)
df_sort = df_drop.sort_values(by='発注金額', ascending=False)
df_sort.to_excel(export_file_path + '/' + '予実管理表.xlsx')

workbook = openpyxl.load_workbook(export_file_path+'/予実管理表.xlsx')
worksheet = workbook.worksheets[0]
worksheet.delete_cols(1)
workbook.save(export_file_path+'/予実管理表_01.xlsx')
