import pandas as pd
pd.show_versions()
# =============================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# =============================================================================
titanic = pd.read_csv('titanic.csv')


titanic.info()
titanic[['Age','Sex']]
titanic[titanic['Age']>35].shape

titanic[titanic['Age'].notna()]#非空行

titanic[titanic['Age']>35]['Name']
titanic.loc[titanic['Age']>35,'Name']


titanic.iloc[9:25,1:5] = 0#可读可写


air_quality = pd.read_csv('air_quality_no2.csv')
air_quality = pd.read_csv('air_quality_no2.csv', index_col=0, parse_dates=True)
air_quality.info()
air_quality.head()

air_quality.plot()
air_quality['station_paris'].plot()

air_quality.plot.scatter(x='station_london',y='station_paris')
air_quality.plot.bar()
air_quality.plot.area(subplots=True)

titanic[['Age','Fare']].describe()

#指定列的信息
titanic.agg({'Age':['min','max','mean'],
             'Fare':['min','std','mean']
})

#男女平均年龄
titanic.groupby('Sex').mean()['Age']

titanic.groupby('Sex')['Age'].mean()

titanic[['Age','Sex']].groupby('Sex').mean()
