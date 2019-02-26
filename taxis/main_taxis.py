import matplotlib.pyplot as plt
import numpy as np
import os, sys
import pandas as pd
import re
import seaborn as sns


def calc_distance(deg1, deg2):
    '''Returns the distance in km of two points in NYC based on angular separation'''
    radius = 6369.4
    rad_diff = np.absolute(deg1 - deg2)*np.pi/180
    return round(rad_diff*radius, 4)
    

def read_data(filename, lines):
    folder = os.path.join(os.getcwd(), 'data')
    readfile = os.path.join(folder, filename)
    reader = pd.read_csv(readfile, iterator=True)
    return reader.get_chunk(lines)


def clean_data(df):
    df['pickup_datetime'] = df['pickup_datetime'].apply(pd.to_datetime, format='%Y-%m-%d %H:%M:%S %Z')
    coords = ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']
    df[coords] = df[coords].astype('float32')


def plot_distance(df):
    #df['distance'] = df.[['dropoff_longitude', 'pickup_longitude']].apply()
    df['distance'] = df['dropoff_longitude']
    
    #.abs() + (df['dropoff_latitude'] - df['pickup_latitude']).abs()
    print(df.head())
    sns.lmplot(x='distance', y='fare_amount', data=df, fit_reg=False)
    plt.show()


def main():
    df = read_data('train.csv', lines=1000)
    print(df.describe())
    print(calc_distance(0, 90))
    exit()

    clean_data(df)
    #print(df.info())
    #print(type(df.iloc[1]['pickup_longitude']))
    #print(df.iloc[1]['pickup_longitude'])
    plot_distance(df)

if __name__ == '__main__':
    main()
