# P4 commands handler

import pprint
import subprocess



def run_command(command):
    p = subprocess.Popen(command,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    return p.stdout.read()

def p4_refresh():

    result = run_command('p4 refresh')

    return result

def checkedout_files_user(user_name):

    file_list = run_command('p4 opened -u ' + user_name)

    return file_list

def checkedout_files_depot(depot_name):

    cmd_out = run_command('p4 opened -a ' + depot_name)
    file_list = str(cmd_out, encoding="utf-8", errors='ignore')
    file_list = file_list.split('\r\n')

    return file_list

def get_changelists(n_in_list=20):

    cmd_out = run_command('p4 changes -m ' + str(n_in_list))
    changelists = str(cmd_out, encoding="utf-8", errors='ignore')
    changelists = changelists.split('\r\n')

    return changelists

# a = get_changelists()
# pprint.pprint(a)