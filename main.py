#
import pprint

import p4_handler as p4
import stats_handler as sh


P4_TEAM = [
                'danil.konowalow',
                'kilian.fröhler',
                'peter.prinzen',
                'johannes.stiehler',
                'igor.pugliesi'
]


def main():

    std_out_file_list = p4.checkedout_files_depot('//Flintstone/main/...')
    #print(chkd_out[0])
    user_dataset = sh.make_dataset(std_out_file_list, save_csv=False)
    print('There are {} files currently checked out'.format(len(user_dataset.index)))
    users_stats = sh.user_stats(user_dataset['user'])
    pprint.pprint(users_stats)

    full_info = sh.dup_files_owners(user_dataset)
    pprint.pprint(full_info)

    changelists = p4.get_changelists
    changelists_ds = sh.changelist_dataset(changelists)

if __name__ == '__main__':
    main()