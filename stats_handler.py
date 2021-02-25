#

import pprint
#import numpy as np
import pandas as pd

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

    return data_column.value_counts().to_dict()