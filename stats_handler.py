# -*- coding: utf-8 -*-

from os import error
import pprint
#import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame

#dataset.to_csv('PANDAS_CSV_LAST.csv', sep='\t', encoding='utf-8', index=False) #save db in csv


#def clean_std_out(std_out):

def make_dataset(std_out_file_list, save_csv= False):
    """[summary]

    Args:
        std_out_file_list ([type]): [description]
        save_csv (bool, optional): [description]. Defaults to False.
    """
    checkedout_files_d = []
    for co_file in std_out_file_list:
        info = {}
        try:
            f_path, user = co_file.split('#')
            user = user.split('by')[1].split('@')[0]
            f_path = f_path.replace('Flintstone/main/', '')
            info['path'] = f_path
            info['user'] = user
        except ValueError:
            pass
        checkedout_files_d.append(info)

        dataset = pd.DataFrame.from_dict(checkedout_files_d)
        # Save data as csv
        if save_csv:
            dataset.to_csv('p4_status.csv', sep='\t', encoding='utf-8', index=False)

    return dataset

def user_stats(data_column):
    """[Get number of checked out files by user]

    Args:
        data_column ([type]): [description]

    Returns:
        [type]: [description]
    """
    user_stats_df = data_column.value_counts().rename_axis('user').reset_index(name='n of files')
    user_stats_df['n of files'] = user_stats_df['n of files'].astype(str).astype(int)
    user_stats_df['Rating'] = user_stats_df['n of files'].apply(lambda x:
                                                            '⭐⭐⭐' if x > 100 else (
                                                            '⭐⭐' if x > 50 else (
                                                            '⭐' if x > 10 else '')))
    #?print('dim of df = ' + str(user_stats_df.shape))
    #?user_stats_df.to_csv('user_stats.csv', sep='\t', encoding='utf-8', index=True)

    return user_stats_df

def dup_files_owners(dataset):

    # Find duplicates
    dataset['duplicate'] = dataset.duplicated(subset='path', keep=False)
    #dataset.to_csv('data_p4.csv', sep='\t', encoding='utf-8', index=True)
    mask = dataset['duplicate'] == True
    duplicates = dataset[mask]
    #pprint.pprint(duplicates)
    unique_files = duplicates['path'].unique().tolist()
    #?pprint.pprint(unique_files)
    full_info = []
    for uniq_f in unique_files:
        info = {}
        info['path'] = uniq_f
        for index, row in duplicates.iterrows():
            if uniq_f == row['path']:
                #info['user'+ str(index)] = row['user']
                info[row['user'].strip()] = '🔥'
        full_info.append(info)

    full_info_df = pd.DataFrame.from_dict(full_info)
    #print(type(full_info_df))

    return full_info_df

def changelist_dataset(std_out_changelist, save_csv= False):

    #pprint.pprint(std_out_changelist)
    changelist = []
    for change in std_out_changelist:
        info = {}
        try:
            change_n = change.split('on', 1)[0].split('Change')[1]
            #print(change)
            date = change.split('on', 1)[1].split('by')[0]
            user = change.split('by')[1].split('@')[0]
            description = '[' + change.split('[')[1].replace('  ', ' ')

            info['change_n'] = change_n
            info['date'] = date
            info['user'] = user
            info['description'] = description

            changelist.append(info)

        except IndexError:
            #print('ERROR')
            continue

    changelist_dt = pd.DataFrame.from_dict(changelist)

    return changelist_dt