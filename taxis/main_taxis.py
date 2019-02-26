import matplotlib.pyplot as plt
import numpy as np
import os, sys
import pandas as pd
import re
import seaborn as sns
import math


def read_data(filename, lines):
    folder = os.path.join(os.getcwd(), 'data')
    readfile = os.path.join(folder, filename)
    reader = pd.read_csv(readfile, iterator=True)
    return reader.get_chunk(lines)


def clean_data(df):
    df = df[(df['pickup_longitude'] < -73.5) & (df['pickup_longitude'] > -74.2)]
    df = df[(df['pickup_latitude'] < 40.9) & (df['pickup_latitude'] > 40.4)]
    coords = ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']
    df[coords] = df[coords].astype('float32')
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], format='%Y-%m-%d %H:%M:%S %Z')

    dlong = (df['pickup_longitude'] - df['dropoff_longitude']) * 111
    dlat = (df['pickup_latitude'] - df['dropoff_latitude']) * 85
    distance = np.sqrt(dlong ** 2 + dlat ** 2)
    #df['fare_amount'] = pd.qcut(df['fare_amount'], 3, labels = [0,1,2])

    df['dayofweek'] = [x.weekday() for x in df['pickup_datetime']]
    df['hourofday'] = [x.hour for x in df['pickup_datetime']]


def mooieplot(df, alpha=0.01, size=6):
    sns.lmplot(x = 'pickup_longitude', y = 'pickup_latitude',data = df, fit_reg = False, height = 20, scatter_kws = {'alpha': alpha, 's': size})
    plt.show()


def main():
    df = read_data('train.csv', lines=1000)
    clean_data(df)
    mooieplot(df, alpha=0.2, size=6)


if __name__ == '__main__':
    main()
