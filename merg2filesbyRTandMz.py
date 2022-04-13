import pandas as pd
import load_data as ld
#
# /*************************************************************
# Working solution Example
# linke: https://stackoverflow.com/questions/65464300/how-to-join-two-dataframes-for-which-2-columns-values-are-within-a-certain-2-ran
# df2
df2 = pd.read_excel ('D:\CD_SandBox\Compounds Rat_Serum_Neg.xlsx', sheet_name='Sheet2')
# df1  is data with the added confident interval i.e RT [min]-+0.2 and Molecular Weight - + 0.2

df1 = pd.read_excel (r'D:\CD_SandBox\Compounds Pig_saliva_Neg.xlsx', sheet_name='Sheet2')
df1 = df1.drop(['RT [min]',  'Molecular Weight'], axis=1)

import numpy as np
from itertools import product


def df_iter(df1, df2):
    for row1, row2 in product(df1.values, df2.values):

        # RT [min]-0.2 <=  RT [min] <=  RT [min]+0.2
        if row1[2] <= row2[2] <= row1[1]:

            # Molecular Weight - 0.2 <= Molecular Weight <= Molecular Weight + 0.2
            if row1[4] <= row2[1] <= row1[3]:
                yield np.concatenate((row1, row2))


df3_rows = df_iter(df1, df2)

for row in df3_rows:
    print(row)
df3 = pd.DataFrame(data = list(df3_rows),
      columns = np.concatenate((df1.columns, df2.columns)))


# /*************************************************************
# df1  is data with the added confident interval i.e RT [min]-+0.2 and Calc. MW+0.2
df1 = pd.read_excel (r'D:/CD_Production/Export Data Analysis/PTSD/20210112_Export_20210107_Analysis_Rat_Serum_HILIC_Pos/Compounds_adjuspval_lessthen_005.xlsx', sheet_name='Sheet2')
df1 = df1.rename(columns={"Name":"Name df1","Formula": "Formula df1" ,"Calc. MW" : "Calc. MW df1 ", "RT [min]" :"RT [min] df1" })

df1 = pd.read_excel (r'D:\CD_Production\Export Data Analysis\PTSD\2020124_Export_20201019_Analysis_Rat_Serum_HILIC_Neg\Compounds_adjuspval_lessthen_005.xlsx', sheet_name='Sheet1')

# df1 = df1.drop(['RT [min]',  'Molecular Weight'], axis=1)
# df2
df2 = pd.read_excel (r'D:\CD_Production\Export Data Analysis\PTSD\20200106_Export_20201231_Re-inject_Analysis_Pig_Saliva_HILIC_Pos/Compounds_adjuspval_lessthen_005.xlsx', sheet_name='Sheet2')
# df2.rename(columns={"Name":"Name df2"})
df2 = df2.rename(columns={"Name":"Name df2","Formula": "Formula df2" ,"Calc. MW" : "Calc. MW df2 ", "RT [min]" :"RT [min] df2" })

df2 = pd.read_excel (r'D:\CD_Production\Export Data Analysis\PTSD\20210124_Export_20201022_Pig_Saliva_HILIC_Neg\Compounds_adjuspval_lessthen_005.xlsx', sheet_name='Sheet1')

import numpy as np
from itertools import product
import  openpyxl

def df_iter(df1, df2):
    for row1, row2 in product(df1.values, df2.values):

        # RT [min]-0.2 <=  RT [min] <=  RT [min]+0.2
        if row1[4] <= row2[3] <= row1[5]:
            # yield np.concatenate((row1, row2))

            # Molecular Weight - 5 ppm  <= Molecular Weight <= Molecular Weight + 5 ppm
            if row1[6] <= row2[2] <= row1[7]:
                yield np.concatenate((row1, row2))



def df_iter(df1, df2):
    for row1, row2 in product(df1.values, df2.values):

        # # RT [min]-0.2 <=  RT [min] <=  RT [min]+0.2
        # if row1[4] <= row2[3] <= row1[5]:
        #     # yield np.concatenate((row1, row2)) only the last yield to use!!!!!

        # Molecular Weight - 0.2 <= Molecular Weight <= Molecular Weight + 0.2
        if row1[6] <= row2[2] <= row1[7]:
            yield np.concatenate((row1, row2))



df3_rows = df_iter(df1, df2)

for row in df3_rows:
    print(row)
df3 = pd.DataFrame(data = list(df3_rows),
      columns = np.concatenate((df1.columns, df2.columns)))

pd.set_option('display.max_columns', None)

df3.to_excel(r'D:\CD_Production\Export Data Analysis\PTSD\202010117_Results\mergePigRatbyRT_Mz_V1.xlsx', sheet_name='My sheet name', index = False)
df3.to_excel(r'D:\CD_Production\Export Data Analysis\PTSD\202010117_Results\mergePigRatbyRT_Mz_V2.xlsx', sheet_name='My sheet name', index = False)