# -*- coding: utf-8 -*-
import os
import unit.nayuki_core as nayuki_core

#========== String Here ==========#
kill_all_screen: str = '''screen -wipe
screen -ls | grep Detached | cut -d. -f1 | awk '{print $1}' | xargs kill
sleep 1
'''
#========== String Done ==========#


# in file [restart].
def restart_server():
    # kill all exist screen.
    nayuki_core.send_command(kill_all_screen)
    # start all minecraft server.
    nayuki_core.run_command_from_yaml('create', nayuki_core.minecraft_server_yaml_path, 'start.sh')
    nayuki_core.run_command_from_yaml('create', nayuki_core.MCDR_server_list_yaml_path, 'python3 -m mcdreforged')


# in file [stopAllServer].
def stoped_server():
    # stop all minecraft server.
    nayuki_core.run_command_from_yaml('execute', nayuki_core.MCDR_server_list_yaml_path, 'stop')
    nayuki_core.run_command_from_yaml('execute', nayuki_core.minecraft_server_yaml_path, 'stop')


# in File [reloadMCDR]
def reload_mcdr():
    nayuki_core.run_command_from_yaml('execute', nayuki_core.MCDR_server_list_yaml_path, '!!MCDR r $1')


# in File [cbr]
def reload_chatbridge():
    nayuki_core.run_command_from_yaml('execute', nayuki_core.MCDR_server_list_yaml_path, '!!ChatBridge $1')