import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt

def create_pie(data, title, legend):

    plt.pie(data,autopct = '%1.1f%%')
    plt.title(title)
    plt.legend(legend, loc='lower left')
    plt.show()

def create_hist(df, data, ylabel, xlabel, title=None):

    N = df.shape[0]
    k = round(np.sqrt(N))#Counting bins using a statistical formula

    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.hist(data, bins=k, edgecolor='w')
    plt.show()

def create_bar(names, data, xlabel=None, ylabel=None, title=None):
    
    plt.bar(names, data)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
    