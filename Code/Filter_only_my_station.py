import pandas as pd

def filter_station():
    df = pd.read_csv('Datasets/Only_Manhattan.csv')
    df2 = pd.DataFrame(columns=df.columns)
    
    my_station_id = 388
    
    for i in range(df.shape[0]):
        if df.iloc[i]['start station id'] == my_station_id or df.iloc[i]['end station id'] == my_station_id:
            p = pd.Series(list(df.iloc[i]), index=df2.columns)
            df2.loc[df2.shape[0]] = p
    
    df2.to_csv("Datasets/Only_my_Station.csv")

filter_station()