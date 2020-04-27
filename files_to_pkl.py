#!/usr/bin/env python3

import pandas as pd

headers = ['date', 'time', 'app_id', 'app_instance', 'console_id', 'user']
test = pd.read_csv('./data/test.csv', names=headers, header=None, parse_dates=[[0,1]])
usage = pd.read_csv('./data/usage.csv', names=headers, header=None, parse_dates=[[0,1]])
pa_colspecs = [(0, 6), (7, 11), (22, 80)]
pas = pd.read_fwf('./data/pas.txt', names=['app_id', 'app_instance', 'desc'], colspecs=pa_colspecs, header=None)
sa_colspecs = [(0, 6), (22, 80)]
sas = pd.read_fwf('./data/sas.txt', names=['app_id', 'desc'], colspecs=sa_colspecs, header=None)

apps = pd.concat([pas, sas])
apps['app_id'] = apps['app_id'].str.upper()

apps.to_pickle('./pickles/apps.pkl')
test.to_pickle('./pickles/test.pkl')
usage.to_pickle('./pickles/usage.pkl')
