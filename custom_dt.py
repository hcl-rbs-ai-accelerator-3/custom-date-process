import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

def extract_dt(df):
    df.Date = pd.to_datetime(df.Date)
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Week'] = df['Date'].dt.isocalendar().week
    df['Day'] = df['Date'].dt.day
    df['Dayofweek'] = df['Date'].dt.dayofweek
    df['Dayofyear'] = df['Date'].dt.dayofyear
    return(df)