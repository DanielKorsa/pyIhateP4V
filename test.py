#
import pprint
import subprocess

from collections import Counter


#! Files opened by user
# p4 opened -u  kilian.fröhler
#p4 opened -u  danil.konowalow

#! Files opened by folder-------------------

#! p4 opened -a //Flintstone/main/...
#! -----------------------------------------

p4_nanion_team = [
                'danil.konowalow',
                'kilian.fröhler',
                # 'peter.prinzen',
                # 'johannes.stiehler',
                # 'igor.pugliesi'
]


def run_command(command):
    p = subprocess.Popen(command,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    return p.stdout.read()


def checkedout_files_user(user_name):

    file_list = run_command('p4 opened -u ' + user_name)

    return file_list

def checkedout_files_depot(depot_name):

    cmd_out = run_command('p4 opened -a ' + depot_name)
    #file_list = str(cmd_out)
    file_list = str(cmd_out, encoding="utf-8", errors='ignore')
    #print(type(cmd_out))
    #file_list.splitlines()
    file_list = file_list.split('\r\n')

    return file_list


# reply = run_command('p4 sync')
# print(reply)

# for user in p4_nanion_team:
#     file_list = str(checkedout_files_user(user))
#     #print(type(file_list))
#     pprint.pprint(file_list)

chekedout_files_info = checkedout_files_depot('//Flintstone/main/...')

checkedout_files_d = []
user_list = []
files_list = []

for co_file in chekedout_files_info:

    info = {}
    try:
        f_path, user = co_file.split('#')
        user = user.split('by')[1].split('@')[0]
        info['path'] = f_path
        info['user'] = user
        user_list.append(user)
        files_list.append(f_path)
    except ValueError:
        pass

    checkedout_files_d.append(info)

print('There are {} currently checked out'.format(len(files_list)))

#! Checked out data stats by user
checkedout_stats = Counter(user_list)
pprint.pprint(checkedout_stats)

#duplicates = list(set(files_list))

#! Cross checked out files
duplicates = set([x for x in files_list if files_list.count(x) > 1])
pprint.pprint(duplicates)
print(len(duplicates))
#print(potential_issue)
#print(type(potential_issue))


'//Flintstone/main/WP_based/Panels/AnalyserPanel2Y/Private/GraphicObjects/IC50-Control/AnaPnl_PX_GraphicObject_Handler(IC50-Control).vi#49 - edit default change (binary) by peter.prinzen@peter.prinzen_Arco2_305\r\n'