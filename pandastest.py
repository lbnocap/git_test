import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymysql
score1=np.arange(70,100,2)
score=score1.reshape(5,3)
course=['math','lauge','enginsh']
index=[1001,1002,1003,1004,1005]
df1=pd.DataFrame(data=score,columns=course,index=index)
df2=pd.read_csv('nba.csv')
df1['math'][1001]=85
print(df1.query('math>85 and lauge>85')) 
df1.loc[1006]={'math':85,'lauge':85,'enginsh':85}
print(df1.duplicated('math'))
df1.drop_duplicates('math',keep='first',inplace=True)
print(df1)