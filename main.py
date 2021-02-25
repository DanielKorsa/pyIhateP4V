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
    dataset = sh.make_dataset(std_out_file_list, save_csv=False)
    print('There are {} files currently checked out'.format(len(dataset.index)))
    users_stats = sh.user_stats(dataset['user'])
    pprint.pprint(users_stats)

    # Find duplicates
    dataset['duplicate'] = dataset.duplicated(subset='path', keep=False)
    #dataset.to_csv('data_p4.csv', sep='\t', encoding='utf-8', index=True)
    mask = dataset['duplicate'] == True
    duplicates = dataset[mask]
    #pprint.pprint(duplicates)
    unique_files = duplicates['path'].unique().tolist()
    pprint.pprint(unique_files)
    # for index, row in duplicates.iterrows():
    #     duplicate_tree = {}
    #     print(row['user'])
    full_info = []
    for uniq_f in unique_files:
        info = {}
        info['path'] = uniq_f
        for index, row in duplicates.iterrows():
            if uniq_f == row['path']:
                info['user'+ str(index)] = row['user']
        full_info.append(info)

    pprint.pprint(full_info)

if __name__ == '__main__':
    main()