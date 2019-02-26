import numpy as np
import os, sys
import pandas as pd
import re
import seaborn as sns
import math


def loaddata():
    df = pd.read_csv('train.csv', chunksize = 100000)
    for i in df:
        df = pd.DataFrame(i)
        break

def datamanipulatie():
    df = df[(df['pickup_longitude'] < -73.5) & (df['pickup_longitude'] > -74.2)]
    df = df[(df['pickup_latitude'] < 40.9) & (df['pickup_latitude'] > 40.4)]
    #df['fare_amount'] = pd.qcut(df['fare_amount'], 3, labels = [0,1,2])
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    dlong = (df['pickup_longitude'] - df['dropoff_longitude']) * 111
    dlat = (df['pickup_latitude'] - df['dropoff_latitude']) * 85

    distance = np.sqrt(dlong ** 2 + dlat ** 2)

    df['dayofweek'] = [x.weekday() for x in df['pickup_datetime']]
    df['hourofday'] = [x.hour for x in df['pickup_datetime']]

def mooieplot():
    sns.lmplot(x = 'pickup_longitude', y = 'pickup_latitude',data = df, fit_reg = False, height = 20, scatter_kws = {'alpha' : 0.01, 's':6})

def main():
    print('main')
    pass


if __name__ == '__main__':
    main()
