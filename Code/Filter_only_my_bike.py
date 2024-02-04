import pandas as pd

def filter_bike_func():
    df = pd.read_csv('Datasets/Only_Manhattan.csv')
    df2 = pd.DataFrame(columns=df.columns)
    
    my_bike_id = 16027
    
    for i in range(df.shape[0]):
        if df.iloc[i]['bikeid'] == my_bike_id:
            p = pd.Series(list(df.iloc[i]), index=df2.columns)
            df2.loc[df2.shape[0]] = p
    
    df2.to_csv('Datasets/Only_my_bike.csv')

filter_bike_func()