import pandas as pd
from matplotlib import pyplot as plt
import math
import numpy as np
from datetime import datetime
import Funcs_for_graphs as ffg
plt.style.use('seaborn-v0_8-pastel')

df = pd.read_csv('Datasets/Only_my_station.csv')

#In my dataset, the date and time were in the same column and because of this,
#I couldn't analyze them, so I decided to unsplit them into different columns using built-in "DateTime" module
#Additionaly i converte them from String type to the DateTime
df['start date'] = list(datetime.strptime(df['starttime'][x][0:10], '%d/%m/%Y') for x in range(df.shape[0]))
df['start hour'] = list(datetime.strptime(df['starttime'][x][11:], "%H:%M") for x in range(df.shape[0]))

df['stop date'] = list(datetime.strptime(df['stoptime'][x][0:10], '%d/%m/%Y') for x in range(df.shape[0]))
df["stop hour"] = list(datetime.strptime(df['stoptime'][x][11:], "%H:%M")for x in range(df.shape[0]))

df.drop(columns=['Unnamed: 0', 'starttime', "stoptime"], inplace=True)#Dropped the old columns that are useless
df = df[['tripduration', 'start date', 'start hour', 'stop date', 'stop hour','start station id', 'start station name',
       'start station latitude', 'start station longitude', 'end station id',
       'end station name', 'end station latitude', 'end station longitude',
       'bikeid', 'usertype', 'birth year', 'gender']]
#Changed the column order
df['tripduration'] = list(x/3600 for x in df['tripduration'])


#Let's build the gender pie plot using Matplotlib module
df['gender'] = df['gender'].replace({1, 2, 0}, {'Male', 'Female', "Unrecognised"})
genders = ['Unrecognised', 'Female', 'Male']
genders_c = list(df.value_counts(df['gender']))
ffg.create_pie(genders_c, 'Gender of customers', genders)



#Customers type pie plot
usertype = ['Subcriber', 'Customer']
usertype_c = list(df.value_counts(df['usertype']))
ffg.create_pie(usertype_c, 'User Type', usertype)



#Check trip duration distribution
mean_td = df['tripduration'].mean()
std_td = df['tripduration'].std()
variance_td = df['tripduration'].var()

ffg.create_hist(df, df['tripduration'], 'Number of people','Trip duration(in hours)',  'Trip duration[1 = 60 minutes]')



#Converte 'bithyear datatype to numeric, becauese I need this for analysis
df['birth year'] = pd.to_numeric(df['birth year'], errors='coerce')
_ = []
#We have 'birth year' in data, but we needed age for the analysis, so the following lines do that
for i in range(df.shape[0]):
    if df.iloc[i]['birth year'] == np.nan:
        pass
    else:
        _.append(2013 - df['birth year'][i])

ages = np.array(_)
ages = ages[~np.isnan(ages)]

mean_age = np.mean(ages)
std_age = np.std(ages)
variance_age = np.var(ages)

ffg.create_hist(df, ages, 'Number of people', 'Age of customer')



#To sort data by day, I need to convert data to the datetime type
friday = datetime.strptime('19/07/2013', '%d/%m/%Y')
saturday = datetime.strptime('20/07/2013', '%d/%m/%Y')
sunday = datetime.strptime('21/07/2013', '%d/%m/%Y')

#We need to define a fuction which sorts our date by days of the week
def sort_dw(day, llst):
    for i in range(df.shape[0]):
        if df['start date'][i] == day:
            p = pd.Series(list(df.iloc[i]), index=llst.columns)
            llst.loc[llst.shape[0]] = p
    return llst.astype(df.dtypes)

#Creatin data frames
df_friday = sort_dw(friday, pd.DataFrame(columns=df.columns))
df_saturday = sort_dw(saturday, pd.DataFrame(columns=df.columns))
df_sunday = sort_dw(sunday, pd.DataFrame(columns=df.columns))

weekends = list(df_saturday['tripduration']) + list(df_sunday['tripduration'])
avg_weekdays = df_friday['tripduration'].mean()
avg_weekends = np.mean(weekends)
count_weekdays = df_friday.shape[0]
count_weekend = len(weekends)

ffg.create_bar(['Weekdays', 'Weekend'], [count_weekdays, count_weekend], 'Part of the week', 'Number of trips', 'Number of trips by part of the week')

ffg.create_bar(['Weekdays', 'Weekend'], [avg_weekdays, avg_weekends], 'Part of the week', 'Duration', 'Average trip duration by part of the week')



#This function calculates average trip duration and thei number in defferent parts of the day
def avg_tripduration(llst):
    #Defining some variables for function
    first_h = datetime.strptime('12:00', '%H:%M')
    second_h = datetime.strptime('18:00', '%H:%M')
    third_h = datetime.strptime('23:59', '%H:%M')
    forth_h = datetime.strptime('00:00', '%H:%M')
    fifth_h = datetime.strptime('6:00', '%H:%M')

    morning = []
    midday = []
    evening = []
    night = []

    #Runs a for loop that sorts data by parts of the input day
    for i in range(llst.shape[0]):
        if llst['start hour'][i] >= first_h and llst['start hour'][i] <= second_h:
            midday.append(llst.iloc[i]['tripduration'])
        elif llst['start hour'][i] > second_h and llst['start hour'][i] <= third_h:
            evening.append(llst.iloc[i]['tripduration'])
        elif llst['start hour'][i] >= forth_h and llst['start hour'][i] <= fifth_h:
            night.append(llst.iloc[i]['tripduration'])
        else:
            morning.append(llst.iloc[i]['tripduration'])

    avg_morning = np.mean(morning)
    avg_midday = np.mean(midday)
    avg_evening = np.mean(evening)
    avg_night = np.mean(night)

    return [[avg_night, avg_morning, avg_midday, avg_evening], [len(night), len(morning), len(midday), len(evening)]]

ffg.create_bar(['Night', 'Morning', 'Midday', 'Evening'], avg_tripduration(df)[1], 'Part of day', 'Number', 'Number of trips by part of the day')

ffg.create_bar(['Night', 'Morning', 'Midday', 'Evening'], avg_tripduration(df)[0], 'Part of day', 'Time', 'Average trip time by part of the day')