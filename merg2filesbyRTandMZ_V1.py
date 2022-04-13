import numpy as np
import pandas as pd
from itertools import product
import load_data as ld

# path_df1 = r'D:\CD_SandBox\202010317_SandBox_Rat_Serum_HILIC_Pos\Compounds_filter_Background_NormArea_20210419_SandBox_Rat_Serum_HILIC_Pos.xlsx'
# path_df2 = r'D:\CD_SandBox\202010317_SandBox_Rat_Serum_HILIC_Pos\Compounds_filter_Background_NormArea_20210425_SandBox_Rat_Serum_HILIC_Pos.xlsx'


ppm_value = 5
min_value = 0.5
sheet_name = 'Compounds'

# cols = ['Name',	'Formula',	'Calc. MW',	'RT [min]', 'P-value: (EBR-PTSD) / (MBP)']

# df1 = pd.read_excel (path_df1, sheet_name=sheet_name)
# df2 = pd.read_excel (path_df2, sheet_name=sheet_name)

# selecting relvant cols
# common columns

cols = ['Name',	'Formula',	'Calc. MW',	'RT [min]']

#   ratio columns + adj pval cols
ratio_cols=[col for col in ld.df1.columns  if "Ratio" in col ]
adjpvalue_cols=[col for col in ld.df1.columns  if "Adj. P-value" in col ]
df1 = ld.df1[cols+ratio_cols+adjpvalue_cols]

ratio_cols=[col for col in ld.df2.columns  if "Ratio" in col ]
adjpvalue_cols=[col for col in ld.df2.columns  if "Adj. P-value" in col ]
df2 = ld.df2[cols+ratio_cols+adjpvalue_cols]

# df1 = df1[df1['P-value: (EBR-PTSD) / (MBP)']<=0.05]
# df2 = df2[df2['P-value: (EBR-PTSD) / (MBP)']<=0.05]

#  add 4 columns +/- min and +/- ppm to data frame 1 df1
df1.insert(loc=4, column="RT [min] - " + str(min_value), value=df1["RT [min]"]-min_value)
df1.insert(loc=5, column="RT [min] + " + str(min_value), value=df1["RT [min]"]+ min_value)

df1.insert(loc=6, column="Calc. MW - " + str(ppm_value) + " ppm", value=df1["Calc. MW"]*(-ppm_value/10**6 + 1))
df1.insert(loc=7, column="Calc. MW + " + str(ppm_value) + " ppm", value=df1["Calc. MW"]*(+ppm_value/10**6 + 1))

#  add suffix to each data frame so will know where is came form
df1 = df1.add_suffix(' df1')
df2 = df2.add_suffix(' df2')

# df1 = df1.rename(columns={"Name":"Name df1","Formula": "Formula df1" ,"Calc. MW" : "Calc. MW df1 ", "RT [min]" :"RT [min] df1" })
# df2 = df2.rename(columns={"Name":"Name df2","Formula": "Formula df2" ,"Calc. MW" : "Calc. MW df2 ", "RT [min]" :"RT [min] df2" })


def df_iter(df1, df2):
    for row1, row2 in product(df1.values, df2.values):

        # RT [min]-0.2 <=  RT [min] <=  RT [min]+0.2
        if row1[4] <= row2[3] <= row1[5]:

            # Molecular Weight - 5 ppm  <= Molecular Weight <= Molecular Weight + 5 ppm
            if row1[6] <= row2[2] <= row1[7]:
                # print(row2[2])
                yield np.concatenate((row1, row2))


df3_rows = df_iter(df1, df2)

# for row in df3_rows:
#     print(row)
df3 = pd.DataFrame(data = list(df3_rows),
      columns = np.concatenate((df1.columns, df2.columns)))

# df3.to_excel(r'D:\CD_SandBox\202010317_SandBox_Rat_Serum_HILIC_Pos\mergeRatbyRT_Mz_V0.xlsx', sheet_name='My sheet name', index = False)

# df3.to_excel(r'D:\CD_Production\Export Data Analysis\PTSD\20211006_Export_20211004_SandBox_Rat_Serum_Neg\mergeRatPig_by_Rt_MW_Neg_V0.xlsx', sheet_name='My sheet name', index = False)
# df3.to_excel(r'D:\CD_Production\Export Data Analysis\PTSD\20211006_Export_20211004_Analysis_Rat_Serum_HILIC_Pos\mergeRatPig_by_Rt_MW_Pos_V0.xlsx', sheet_name='My sheet name', index = False)


# df3.to_excel(r'D:\CD_Production\Export Data Analysis\PTSD\20211006_Export_20211004_SandBox_Rat_Serum_Neg\mergeRatPig_by_Rt_MW_Neg_V1.xlsx', sheet_name='My sheet name', index = False)
df3.to_excel(r'D:\CD_Production\Export Data Analysis\PTSD\20211006_Export_20211004_Analysis_Rat_Serum_HILIC_Pos\mergeRatPig_by_Rt_MW_Pos_V1.xlsx', sheet_name='My sheet name', index = False)