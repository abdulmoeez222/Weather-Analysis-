import pandas as pd
data = pd.read_csv("Weather_Dataset.csv")

##COMMANDS

# print(data.head())
# print(data.shape)
# print(data.index)
# print(data.columns)
# print(data.dtype)
# print(data["weather"].unique())
# print(data.nunique())
# print(data.count())
# print(data["Weather"].value_counts())
# print(data.info())

##

data["Wind_Speed_km/h"].nunique()
data["Wind_Speed_km/h"].unique()


data.Weather.value_counts()
# data[data.Weather == "Clear"]
data.groupby("Weather").get_group('Clear')


# data[data["Wind_Speed_km/h"]==4]


data.isnull().sum()


data.rename(columns={'Weather : Weather Condition '})


data.visibilty_km.mean()


data.Press_kPa.std()

data['Rel_HUm_%'].var()


data['Weather Condition'].value_counts()
# data[data['Weather Condition'] == 'Snow']
data['Weather Condition'].str.contains('Snow')

#
# data[(data['Wind Speed_km/h > 24'] & data['visibilty_km']==25)]


data.groupby('Weather Condition').mean()
data.groupby('Weather Condition').min()
data.groupby('Weather Condition').max()

data[data['Weather Condition']=='Fog']




