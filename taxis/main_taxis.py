import matplotlib.pyplot as plt
import numpy as np
import os, sys
import pandas as pd
import re
import seaborn as sns
import math


def calc_distance(df):
    '''Returns a Series of distance in km of two points in NYC based on angular separation'''
    radius = 6369.4
    long_diff = ((df['pickup_longitude'] - df['dropoff_longitude'])*(np.pi/180)*radius)
    lat_diff = ((df['pickup_latitude'] - df['dropoff_latitude'])*(np.pi/180)*radius)
    return np.sqrt(long_diff**2 + lat_diff**2).round(decimals=3)
    

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

    df['distance'] = calc_distance(df)
    df = df[(df['distance'] > 0.2) & (df['distance'] < 60)]

    df['dayofweek'] = [x.weekday() for x in df['pickup_datetime']]
    df['hourofday'] = [x.hour for x in df['pickup_datetime']]
    return df


def plot_distance(df, alpha=0.2, size=6):
    print(df['fare_amount'].unique())
    exit()
    sns.lmplot(x='distance', y='fare_amount', data=df, fit_reg=False, scatter_kws={'alpha': alpha, 's': size})
    plt.show()


def mooieplot(df, alpha=0.01, size=6):
    sns.lmplot(x = 'pickup_longitude', y = 'pickup_latitude',data = df, fit_reg = False, height = 20, scatter_kws = {'alpha': alpha, 's': size})
    plt.show()


def main():
    df = read_data('train.csv', lines=10000)
    #df = read_data('train.csv', lines=1000000)
    df = clean_data(df)
    #mooieplot(df, alpha=0.02, size=6)
    plot_distance(df)


if __name__ == '__main__':
    main()
