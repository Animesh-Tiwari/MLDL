
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',

'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})



df1 = pd.DataFrame(df['RecentDelays'].tolist(),columns=['delay_1','delay_2','delay_3'])
df2 = pd.concat([df,df1],axis=1)
df2.drop('RecentDelays',axis=1,inplace=True)
df2
