# Analysing data on trips on rented bicycles in Manhattan

In this project we are going to analyse the trips made on rented bicycles in Manhattan. We have 3 days(19/07/2013 – 21/07/2013) of data about bike trips in New York City. Unfortunately, the dataset lacks information about the first 16 hour of Friday and the last 10 hours of Sunday(in total it’s 26 hours, so we missed more than a day). This data was obtained from the university as part of one of the projects and I have to analyse it, so I decided to do it with Python. It contains information about trip duration, start time, stop time, start station id, start station name, start station latitude, start station longitude, end station id, end station name, end station latitude, end station longitude, bike id, user type, birth year, gender. We will not use all of this data for our analysis, but only some of it(trip duration, start time, stop time, user type, birth year, gender). At the end of this project, we will be able to profile the average bike share user thanks to the data we have collected from people.



## Used technology

🐍 [Python](https://www.python.org/)
🐼 [Pandas](https://pandas.pydata.org/)
📊 [MatPlotLib](https://matplotlib.org/)
0️⃣ [NumPy](https://numpy.org/)
🕧 [DateTime](https://docs.python.org/3/library/datetime.html)


## Data Manipulations

The analysis started by filtering the data for Manhattan only(filtering was done using another input file that contains all Manhattan stations IDs). You can find the code used for this in“Filter_station_only_Manhattan.py”. The raw dataset contained 50 000 of trips but after using a function 42 777 were obtained. The next step was to filter data for my station and my bike only. Station ID is 388, bike ID is 16027. The dataset that contains only my station ID has information about 360 trips. The dataset that contains only my bike ID has information about 16 trips.
## Analysis
The analysis started after some preliminary data manipulations. In the first stage, we will analyse the dataset that contains only my station, and in the second stage, we will analyse some specific data about bicycle. All code that was used for this analysis can be checked in “Anslysis_my_station.py” file.
I would like to start analysis by acquaintances with users. We have a few data about it, so let’s start from gender. As we can see in the graph below, men predominated among those who used this station (52.8%). 28.1% of users didn’t identify their sex and 19.2% were women. It means that men more than twice time as likely to use bike sharing services as women

![Graph ;)](https://github.com/Mak7-kurochka/NY-bike-trips-analysis/blob/master/Graphs/Gender_of_customers.png?raw=true)

Having data on the gender of users, we can analyse the average trip duration of women and men. As we can see, it is almost 10 minutes longer for women. So, the number of trips is higher for men, and the average duration for women

![Graph ;)](https://github.com/Mak7-kurochka/NY-bike-trips-analysis/blob/master/Graphs/Average_trip_duration_by_gender.png?raw=true)

The next data that we can conclude it is type of users. There are 2 type: Subscriber(the user that has subscribed for services) and Customer( the user that has not subscribed for services). In our data, we have 71.9% subscribers and 28.1% customers. It can mean that people use bikes very often, which means that bike sharing is popular, well organized and developed. The confirmation of these words can be seen in the graph below:

![Graph ;)](https://github.com/Mak7-kurochka/NY-bike-trips-analysis/blob/master/Graphs/User_Type.png?raw=true)

The last information about the users was the year of birth, and we can easily convert it to age at the moment of trip(2013 – year of birth). But first, let’s talk about concrete numbers. The majority of customers are between the ages of 20 and 50(89% excluding unrecognised users). Only 1 of users was 10-20 years old. 4 users were 60-70 and 1 was 70-80 years old. 101 users didn’t identify their date of birth. As a tentative conclusion, we can say that bicycle rental is used more elderly people, for traveling to/from work, to/from shops etc. This data you can see at table below:
| Interval             | Number                                                                |
| ----------------- | ------------------------------------------------------------------ |
| 10-20 | 1 |
| 20-30 | 67 |
| 30-40 | 95 |
| 40-50 | 69 |
| 50-60 | 22 |
| 60-70 | 4 |
| 70-80 | 1 |
| Unrecognised | 101 |

So, we got their age and can build a histogram showing their distribution. As we can see, the majority of customers between 30 and 60 years old, with an average age of 37 years, a standard deviation of 9.98(which is quite a lot, ¼ of the average, it mean that bicycles are in demand among people of all ages) and a variance of 99.6. Looking at the histogram, we can say that it has positive skew and peak falls on people aged <40 years.

![Graph ;)](https://github.com/Mak7-kurochka/NY-bike-trips-analysis/blob/master/Graphs/Age_of_customers_distribution.png?raw=true)

After getting to know your users we can begin to analyzing travel data. Firstly, let’s check the number of trips by their duration in specific intervals and build a histogram based on this data. As we can see at graph below, the majority of trips(92.5%) lasted <30 minutes(1 = 1 hour = 60 minutes, so 0.5 = 30 minutes). However, were users who rented a bike for 90, 100, 170, and even 200 minutes(but the number of trips with this duration is small). Most likely, these people used them for recreational cycling. and for most of the trips, they were probably for specific purposes, like getting home from work or going to the store, because Manhattan is a very big area. Average trip duration is 20 minutes, with a standard deviation of 20 minutes and a variance of 5 minutes. This means that customers don't use bicycles for long distance trip, as the average speed of a beginner cyclist is 15-20 kmph, so people use them for trips of 4.5-6 km. It confirms my previous theories.

![Graph ;)](https://github.com/Mak7-kurochka/NY-bike-trips-analysis/blob/master/Graphs/Trip_duration.png?raw=true)

Further, we are going to analyse and compare data for weekends and weekdays, parts of days and different days. Let’s begin with parts of the week. We have weekdays and weekends. In the dataset, only Friday is a weekday, and Saturday and Sunday are weekends. It means that comparing  parts of the week it is a bad idea, because the result won’t be representative, but I will do it. Firstly, let’s juxtapose number of trips on weekdays and weekends. Remind, that we have only the second half of Friday and the first half of Sunday. As we can see at the graph below, the number of trips on Friday is slightly over 100, and on weekends is approximately 250

![Graph ;)](https://github.com/Mak7-kurochka/NY-bike-trips-analysis/blob/master/Graphs/Number_of_trips_by_part_of_the_week.png?raw=true)

This is not representative data, but we can try to calculate number of trips on weekdays thanks to the data on Friday. We only have the last 16 hours of Friday, which means that to get the full data, we have to multiply it by 1.5. As a result, we get 170 trips. There are 5 weekdays in a week, so we ought to multiply the result by 5. Thus, we get 850 trips(this result can be representative only if the trend of bike rental remains the same throughout the week). In the same way, we will supplement the date for the weekend. We have the first 14 hour of Sunday, so we must multiply the sum by 1.715. As a result, we get 100 trips in Sunday. On Saturday, 189 trips were made, and the total is 289.Now we can calculate the average for weekdays and weekends. It is 170 on weekdays and 145 on weekends. So, bike sharing is most in demand on weekends. This result confirms my previous theories.
Further, let’s check and compare average trip duration on weekdays(we only can accept data for Friday as for all days) and weekends. In the graph below we can see, that the average trip duration on weekends is slightly longer than on weekdays. It is only by 1.2 minutes, so we can round it and conclude that the duration of trips is the same.

![Graph ;)](https://github.com/Mak7-kurochka/NY-bike-trips-analysis/blob/master/Graphs/Average_trip_duration_by_part_of_the_week.png?raw=true)

And now let's move on to analysing trips in parts of the day. Let’s start with a week. The first indicator is the number of trips daypart. As we can see, most trips were made in the midday(159), followed by evening(125), morning(66) and night(10).

![Graph ;)](https://github.com/Mak7-kurochka/NY-bike-trips-analysis/blob/master/Graphs/Number_of_trips_by_part_of_the_day.png?raw=true)

The second indicator is the average trip duration. If we look at the graph, we can see that the difference between dayparts is not that big. The peak occurs at midday(19.2 minutes), followed by morning(18 minutes),evening(14.5 minutes) and night(12 minutes).

![Graph ;)](https://github.com/Mak7-kurochka/NY-bike-trips-analysis/blob/master/Graphs/Average_trip_time_by_part_of_the_day.png?raw=true)

Onwards, let’s compare number of trips on different days of the week. We only have data for 3 days(Friday and Sunday are not full). Therefore, we can build a useless graph and analyse it. But on the other hand, we can remember that we calculated this number for the whole day. So, there were 170 trips on Friday and 100 on Sunday. The most trips were made on Sunday. This means that bicycles are most needed on weekends, which does not work in favour of my theory that people use them to commute to work (but you can't draw conclusions from only 3 partial days of data)

![Graph ;)](https://github.com/Mak7-kurochka/NY-bike-trips-analysis/blob/master/Graphs/Number_of_trips_by_different_days_of_the_week.png?raw=true)

But if we check average duration of the trips, we will see different information. The average trip duration weas longer on Sunday(20 minutes), followed by Saturday(17 minutes) and Friday(16.5 minutes). But this difference is not that big. It means we can say that that the duration of trips is the same.

![Graph ;)](https://github.com/Mak7-kurochka/NY-bike-trips-analysis/blob/master/Graphs/Average_trip_duration_by_different_days_of_the_week.png?raw=true)

As a preliminary part of our analysis, we will look at the average journey time depending on the part of the day separately for Friday, Saturday and Sunday, and compare their results. Let’s begin with Friday. Unfortunately, we can analyse only midday and evening. And as we can see, duration of the trips in midday is about 30% longer

![Graph ;)](https://github.com/Mak7-kurochka/NY-bike-trips-analysis/blob/master/Graphs/Average_trip_duration_by_part_of_the_day_on_Friday.png?raw=true)

Next, let's look at the same data for Saturday. Here, the trend continues and the average duration of trips is longer in the middle of the day (but a few minutes shorter than on Friday), followed by morning, then evening (just like on Friday, the difference between evening and middle of the day is about 20-30%) and the shortest at night

![Graph ;)](https://github.com/Mak7-kurochka/NY-bike-trips-analysis/blob/master/Graphs/Average_trip_duration_by_par_of_day_on_Saturday.png?raw=true)

So, it remains to analyse the data for Sunday only. Unfortunately, we have no data available after 14:00, so it is not possible to analyse the average trip duration in the evening, and therefore we will not know whether the trend of a drop in activity in the evening persists. As we can see from the graph, the longest trips on Sunday were not the same as on other days, which is surprising. Morning is the first in terms of duration, followed by night and only then the middle of the day (but we should make a note that we have data for only 3 hours of this part of the day)

![Graph ;)](https://github.com/Mak7-kurochka/NY-bike-trips-analysis/blob/master/Graphs/Average_trip_duration_by_part_of_day_on_Sunday.png?raw=true)

We can conclude that on Friday and Saturday, the data is roughly the same, both in terms of duration and parts of the day. But on Sunday, the data is radically different, and this is very surprising. We can make a theory that on Sunday people, tired from the working week, rest and start their morning with a bike, which is very commendable, because it is sport that can be called a real rest for our brain
The last analysis for station, is number of cases when the station was the starting and ending station. As we can observe in the graph below, station more people started their bike rent from the station than ended them. The difference between them was 30 trips, which is almost 10% of the total number of trips (let me remind you that there were 360 trips connected to this station)

![Graph ;)](https://github.com/Mak7-kurochka/NY-bike-trips-analysis/blob/master/Graphs/Number_of_cases_when_the_station_was_the_starting_and_ending_station.png?raw=true)

We complete the station analysis and we can start analysing the bike.
The only thing we couldn't analyse in the station and possibly in the bike was the downtime. That is, the time that the bike stood at different stations without moving. To calculate it, we use the following formula:
```bash
  t_d=t_s-t_w
```
Where:
t_d – downtime

t_s – total time we have(46.4 hours)

t_w – total time of work(3.11 hours)

After calculating we can say that downtime of the bike was 43 hours and 32 minutes. That can means three things:
	
 1 - all the stations where the bike stopped were very unpopular with users
	
 2 - the bike has been broken for a long time
	
 3 - there are so many bicycles at the stations that one of them can stand idle for 43 and a half hours
 
If we look at these three options, the first one seems to me the least likely, the third the most likely, and the second something in between


# Conclusion

In this project, we analysed bike sharing in the Manhattan area. For the analysis, data was available for less than three days (46 hours), including Friday, Saturday and Sunday. Therefore, the analysis cannot be called representative, but I will try to summarise some results. We analysed two things, the station and the bike (only the idle time was analysed, because all the other data is already available in the station). So, to summarise everything that has been said in this paper, bike sharing is very popular in New York, because during those 46 hours, 50,000 bikes were rented. This shows that people like to do sports and be outdoors and, on the other hand, do not like to stand in traffic jams, which are very common in New York. Bicycles are most in demand on weekdays (we calculated this based on Friday data). If we look at parts of the day, the most popular periods for bicycles are between 12 and 18 hours. If we look at the data on trips, we can see that the average duration of trips is not very long, 20 minutes, and taking into account the average speed of the bike, it will be 4.5-6 km per trip. Of course, there were also people who used the bike for an hour, two or three, but they were very few. This suggests that bike sharing is more popular for short trips. Regarding the gender of users, in 52% of cases they are men and only in 19 cases they are women. The average age is 37 years old, and most users are in the 30-50 age range. There were also younger people (10-20) and older people (70-80). At the beginning of the analysis, I made a theory about the users, and further analysis reinforced my belief in it. Therefore, as a result of this work, I would like to make a portrait of the average bike share user. In 50% of cases, it is a man aged 30 to 50 (on average 37) who uses a bicycle to get from point A to point B. This person is most likely to commute to work if they rent a bike in the morning or return from work if they rent a bike in the evening. Or if they rent it on weekends (this is not a mandatory criterion, people may go to a shop that is up to 5 km away from their home). Because people prefer to use a bicycle, they are more athletic and less likely to get sick
