import numpy as np
import pandas as pd

sheet_name = 'Compounds'
#  Neg mode rats + pigs
# path_df1= r'D:\CD_Production\Export Data Analysis\PTSD\20211006_Export_20211004_SandBox_Rat_Serum_Neg\Compounds_filter_Background_QCls30_per-ratio_adjpval005_ratio_ls05ORgt2_NEG.xlsx'
# path_df2 =r'D:\CD_Production\Export Data Analysis\PTSD\20210701_Export_20210628_SandBox_Pig_Saliva_HILIC_Neg\Compounds_filter_Background_adpvals0005_QCls30_ratiols05gr2_neg.xlsx'


# path_df1 = r'D:\CD_Production\Export Data Analysis\PTSD\20211006_Export_20211004_SandBox_Rat_Serum_Neg\Compounds_filter_Background_QCls30_Neg.xlsx'
# path_df2 = r'D:\CD_Production\Export Data Analysis\PTSD\20210701_Export_20210628_SandBox_Pig_Saliva_HILIC_Neg\Compounds_filter_Background_QCls30_neg.xlsx'


#  Pos mode rats + pigs
# path_df1 =r'D:\CD_Production\Export Data Analysis\PTSD\20211006_Export_20211004_Analysis_Rat_Serum_HILIC_Pos\Compounds_filter_Background_QCls30_per-ratio_adjpval005_ratio_ls05ORgt2_POS.xlsx'
# path_df2 =r'D:\CD_Production\Export Data Analysis\PTSD\20210701_Export_20210628_SandBox_Re-inject_Pig_Saliva_HILIC_Pos\Compounds_filter_Background_adpvals0005_QCls30_ratiols05gr2_pos.xlsx'

path_df1 = r'D:\CD_Production\Export Data Analysis\PTSD\20211006_Export_20211004_Analysis_Rat_Serum_HILIC_Pos\Compounds_filter_Background_QCls30_Pos.xlsx'
path_df2 = r'D:\CD_Production\Export Data Analysis\PTSD\20210701_Export_20210628_SandBox_Re-inject_Pig_Saliva_HILIC_Pos\Compounds_filter_Background_QCls30_pos.xlsx'

df1 = pd.read_excel (path_df1, sheet_name=sheet_name)
df2 = pd.read_excel (path_df2, sheet_name=sheet_name)