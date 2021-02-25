#
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
    sh.make_dataset(std_out_file_list, save_csv=True)

if __name__ == '__main__':
    main()