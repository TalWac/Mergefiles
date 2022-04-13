
import load_data as ld
# ratio_cols=[col for col in ld.df1.columns  if "Ratio" in col ]

#  columns to filter by and athores
ratio_cols=[col for col in ld.df1.columns if "Ratio: (EBR)" in col ]

cols = ['Name',	'Formula',	'Calc. MW',	'RT [min]']+ratio_cols
df1 = ld.df1[cols]
df2 = ld.df2[cols]

df1_filter = ld.df1.loc[((ld.df1[ratio_cols[0]]>1) &
                         (ld.df1[ratio_cols[1]]>1) &
                         (ld.df1[ratio_cols[2]]>1))|
                        ((ld.df1[ratio_cols[0]] < 1) &
                         (ld.df1[ratio_cols[1]] < 1) &
                         (ld.df1[ratio_cols[2]] < 1))
                        ]


df2_filter = ld.df2.loc[((ld.df2[ratio_cols[0]]>1) &
                         (ld.df2[ratio_cols[1]]>1) &
                         (ld.df2[ratio_cols[2]]>1))|
                        ((ld.df2[ratio_cols[0]] < 1) &
                         (ld.df2[ratio_cols[1]] < 1) &
                         (ld.df2[ratio_cols[2]] < 1))
                        ]


ld.df1[ratio_cols[:3]]>1
ld.df1[ratio_cols[0]]>1

ld.df2[ratio_cols[:3]]>1


df2 = df.loc[((df['a'] > 1) & (df['b'] > 0)) | ((df['a'] < 1) & (df['c'] == 100))]
