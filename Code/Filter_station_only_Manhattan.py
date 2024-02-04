import pandas as pd

def filter_func():   
    df = pd.read_csv('Datasets/2013-07_Citi_Bike_trip_dane_podstawowe_part_2.csv')

    filt = list(pd.read_csv("Datasets/Manhattan_stations (2023ukr).csv")['station id'])

    df2 = pd.DataFrame(columns=df.columns)

    for i in range(df.shape[0]):
        if df.iloc[i]['start station id'] in filt and df.iloc[i]['end station id'] in filt:
            p = pd.Series(list(df.iloc[i]), index=df2.columns)
            df2.loc[df2.shape[0]] = p

    df2.to_csv('Datasets/Only_Manhattan')

filter_func()