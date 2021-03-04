
import pprint

import pandas as pd
from pandas.core.frame import DataFrame

import p4_handler as p4
import stats_handler as sh


P4_TEAM = [
                'danil.konowalow',
                'kilian.fröhler',
                'peter.prinzen',
                'johannes.stiehler',
                'igor.pugliesi'
]


def logic_handler():

    std_out_file_list = p4.checkedout_files_depot('//Flintstone/main/...')

    user_dataset = sh.make_dataset(std_out_file_list, save_csv=False)
    chkdout_stats = ('There are {} files currently checked out'.format(len(user_dataset.index)))
    users_stats_df = sh.user_stats(user_dataset['user'])


    full_info = sh.dup_files_owners(user_dataset)
    pprint.pprint(full_info)

    # changelists = p4.get_changelists
    # changelists_ds = sh.changelist_dataset(changelists)

    return users_stats_df, chkdout_stats

# if __name__ == '__main__':
#     logic_handler()

logic_handler()