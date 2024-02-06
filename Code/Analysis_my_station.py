import pandas as pd
from matplotlib import pyplot as plt
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
genders = ['Male', 'Unrecognized', 'Female']
genders_c = list(df.value_counts(df['gender']))
ffg.create_pie(genders_c, 'Gender of customers', genders)



#Customers type pie plot
usertype = ['Subcriber', 'Customer']
usertype_c = list(df.value_counts(df['usertype']))
ffg.create_pie(usertype_c, 'User Type', usertype)



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



#Check trip duration distribution
mean_td = df['tripduration'].mean()
std_td = df['tripduration'].std()
variance_td = df['tripduration'].var()

ffg.create_hist(df, df['tripduration'], 'Number of people','Trip duration(in hours)',  'Trip duration[1 = 60 minutes]')


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

ffg.create_bar(['Weekdays', 'Weekend'], [count_weekdays, count_weekend],\
                'Part of the week', 'Number of trips', 'Number of trips by part of the week')

ffg.create_bar(['Weekdays', 'Weekend'], [avg_weekdays, avg_weekends],\
                'Part of the week', 'Duration', 'Average trip duration by part of the week')



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

ffg.create_bar(['Night', 'Morning', 'Midday', 'Evening'], avg_tripduration(df)[1],\
                'Part of day', 'Number', 'Number of trips by part of the day')

ffg.create_bar(['Night', 'Morning', 'Midday', 'Evening'], avg_tripduration(df)[0],\
                'Part of day', 'Time', 'Average trip time by part of the day')



#Let's create a 'Number of trips by different days of the week' graph
ffg.create_bar(['Friday', 'Saturday', 'Sunday'], [df_friday.shape[0]*1.5, df_saturday.shape[0], df_sunday.shape[0]*1.715],'Day of the week','Number','Number of trips by different days of the week')

#Let's create a 'Average trip duration by different days of the week' graph
ffg.create_bar(['Friday', 'Saturday', 'Sunday'], [df_friday['tripduration'].mean(),df_saturday['tripduration'].mean(),df_sunday['tripduration'].mean()],\
               'Day of the week', 'Time', 'Average trip duration by different days of the week')


#Let's create a 'Average trip duration by part of the day' graph for each of days we have

#Friday#
ffg.create_bar(['Night', 'Morning', 'Midday', 'Evening'], avg_tripduration(df_friday)[0],\
               'Part of day','Time[h]','Average trip duration by part of the day on Friday')

#Saturday#
ffg.create_bar(['Night', 'Morning', 'Midday', 'Evening'], avg_tripduration(df_saturday)[0],\
               'Part of day','Time[h]','Average trip duration by part of day on Saturday')

#Sunday#
ffg.create_bar(['Night', 'Morning', 'Midday', 'Evening'], avg_tripduration(df_sunday)[0],\
               'Part of day','Time[h]','Average trip duration by part of day on Sunday')



#I defined this function to describe a specific inference about bike usage by customer gender
def tripduration_by_gender(llst):
    men = []
    women = []
    for i in range(llst.shape[0]):
        if llst['gender'][i] == 'Male':
            men.append(llst.iloc[i]['tripduration'])
        elif llst['gender'][i] == 'Female':
            women.append(llst.iloc[i]['tripduration'])
    
    avg_men = np.average(men)
    avg_women = np.average(women)

    return [avg_men, avg_women]

ffg.create_bar(['Male', 'Female'], tripduration_by_gender(df),title="Average trip duration by gender")


#Last part of my analysis was a calculatinf numbers of cases when the station was the starting and ending station
#So, to calculate this was wrotten the following lines:
#Determining  necessary variables
friday_end = 0
friday_start = 0
saturday_end = 0
saturday_start = 0
sunday_end = 0
sunday_start = 0

#Starts for lopp that counts the number I need
for i in range(df.shape[0]):
    if df['start date'][i] == friday:
        if df['end station id'][i] == 388:
            friday_end += 1
        else:
            friday_start += 1
    elif df['start date'][i] == saturday:
        if df['end station id'][i] == 388:
            saturday_end += 1
        else:
            saturday_start += 1
    else:
        if df['end station id'][i] == 388:
            sunday_end += 1
        else:
            sunday_start += 1


X = ['Friday', 'Saturday', 'Sunday']
X_axis = np.arange(len(X))

plt.bar(X_axis - 0.2, [friday_start, saturday_start, sunday_start], 0.4, label='Starting')
plt.bar(X_axis + 0.2, [friday_end, saturday_end, sunday_end], 0.4, label='Ending')
plt.plot([friday_start+friday_end, saturday_start+saturday_end, sunday_start+sunday_end],label='Sum')

plt.title('Number of cases when the station was the starting and ending station')
plt.xticks(X_axis, X)
plt.xlabel('Day')
plt.ylabel('Number')
plt.legend()
plt.show()


def helper(func):
    def wrapper(avg,std,var):
        print('\n********')
        func(avg,std,var)
        print('********')
    return wrapper

@helper
def print_func(avg,std,var):
    print(f'Average:{avg}\nStandart deviation:{std}\nVariance:{var}')


print('The data that was collected during the project\n\nFor age of users:')
print_func(mean_age,std_age,variance_age)
print('For trip duration:')
print_func(mean_td,std_td,variance_td)
