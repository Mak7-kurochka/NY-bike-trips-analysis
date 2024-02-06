import pandas as pd
import numpy as np
import Funcs_for_graphs as ffg

df = pd.read_csv('Datasets/Only_my_bike.csv')

df['tripduration'] = list(x/3600 for x in df['tripduration'])

print(sum(df['tripduration']))