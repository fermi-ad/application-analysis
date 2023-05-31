#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

run = {
    'mcr_closes': False,
    'less_than_14_no_0': True,
    'greater_than_13': True,
    'greater_than_13_less_than_25k': True,
    'console_close_per_app': False,
    'users_per_app': True,
    'unused_apps': True
}

usage = pd.read_pickle('./pickles/usage.pkl')
apps = pd.read_pickle('./pickles/apps.pkl')

merged = pd.merge(usage, apps, on='app_id', how='right')

if run['mcr_closes']:
    plt.figure('mcr_closes')

    merged['console_id'] = merged['console_id'] < 15
    mcr_count = merged.groupby(['app_id', 'console_id']).count()
    mcr_count = mcr_count.drop(columns=['date_time', 'app_instance_y', 'desc']).rename(columns={'app_instance_x': 'count'})
    mcr_count[:26].plot.bar(rot=40)

    plt.savefig('./plots/mcr.png')
    plt.close('mcr_closes')

counts = merged['app_id'].value_counts() - 1

if run['less_than_14_no_0']:
    plt.figure('less_than_14_no_0')

    gt_25k = counts.where(counts >= 1000).dropna()
    gt_25k_df = gt_25k.reset_index().rename(columns={'app_id': 'count', 'index': 'app_id'})
    gt_25k_desc = gt_25k_df.merge(apps, on='app_id')
    gt_25k_desc = gt_25k_desc.drop(columns=['app_instance'])

    gt_0_lt_14_clean = counts.where((counts < 14) & (counts > 0)).dropna()

    plt.xlabel('Number of Closes')
    plt.ylabel('Frequency')
    plt.title('Histogram of Closes\n1-13 closes')
    gt_0_lt_14_clean.hist(bins=14)
    plt.savefig('./plots/less_than_14_no_0.png')

    plt.close('less_than_14_no_0')


if run['greater_than_13']:
    plt.figure('greater_than_13')

    gt_13_clean = counts.where(counts > 13).dropna()

    plt.xlabel('Number of Closes')
    plt.ylabel('Frequency')
    plt.title('Histogram of Closes\n>13 closes')
    gt_13_clean.hist(bins=25)
    plt.yscale('log')
    plt.savefig('./plots/greater_than_13.png')

    plt.close('greater_than_13')


if run['greater_than_13_less_than_25k']:
    plt.figure('greater_than_13_less_than_25k')

    gt_13_lt_25k_clean = counts.where((counts > 13) & (counts < 25000)).dropna()

    plt.xlabel('Number of Closes')
    plt.ylabel('Frequency')
    plt.title('Histogram of Closes\n13-25k closes')
    gt_13_lt_25k_clean.hist(bins=25)
    plt.yscale('log')
    plt.savefig('./plots/greater_than_13_less_than_25k.png')

    plt.close('greater_than_13_less_than_25k')


if run['console_close_per_app']:
    app_con_count = merged.groupby(['app_id', 'console_id']).count()
    app_con_count = app_con_count.drop(columns=['date_time', 'app_instance_y', 'desc']).rename(columns={'app_instance_x': 'count'})
    app_con_count = app_con_count.reset_index()
    application_list = app_con_count['app_id'].unique()

    app_dfs = {}
    for application in application_list:
        app_dfs[application] = app_con_count[app_con_count['app_id'] == application]

    for index, application in enumerate(app_dfs):
        fig = plt.figure('console_closes_' + application)
        app_dfs[application].plot.bar(x='console_id', y='count')
        plt.xlabel('Console ID')
        plt.ylabel('Number of Closes')
        x = app_dfs[application]['console_id']
        plt.title('Closes from Consoles\n' + application)
        plt.tight_layout()
        plt.savefig('./plots/console_closes/' + application + '.png')

        plt.close(fig)


if run['users_per_app']:
    plt.figure('users_per_app')

    # print(merged)
    user_app_count = merged.groupby(['app_id']).nunique()
    print(user_app_count)
    user_app_count.plot.bar(y='user')
    plt.savefig('./plots/users_per_app.png')

    plt.close('users_per_app')

if run['unused_apps']:
    eq_0_clean = counts.where(counts == 0).dropna()

    # print(eq_0_clean.keys())

    np.savetxt('./data/unused_apps.txt', eq_0_clean.keys(), fmt='%s')






    # app_con_count = app_con_count.drop(columns=['date_time', 'app_instance_y', 'desc']).rename(columns={'app_instance_x': 'count'})
    # app_con_count = app_con_count.reset_index()
    # application_list = app_con_count['app_id'].unique()

    # app_dfs = {}
    # for application in application_list:
    #     app_dfs[application] = app_con_count[app_con_count['app_id'] == application]

    # for index, application in enumerate(app_dfs):
    #     fig = plt.figure('console_closes_' + application)
    #     app_dfs[application].plot.bar(x='console_id', y='count')
    #     plt.xlabel('Console ID')
    #     plt.ylabel('Number of Closes')
    #     x = app_dfs[application]['console_id']
    #     plt.title('Closes from Consoles\n' + application)
    #     plt.tight_layout()
    #     plt.savefig('./plots/console_closes/' + application + '.png')

    #     plt.close(fig)
