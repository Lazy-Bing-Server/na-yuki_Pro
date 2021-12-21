import os
import time
from ruamel.yaml import YAML as yaml

# ========================================================================================= #
MCDR_server_list_yaml_path = os.path.join(os.path.abspath('..'), 'config', 'mcdrServerList.yaml')
minecraft_server_yaml_path = os.path.join(os.path.abspath('..'), 'config', 'minecraftServer.yaml')
log_path = os.path.join(os.path.abspath('..'), 'log', f'na_yuki_log')
log_prefix = format(time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime()))
DEBUG_FLAG = True
# ========================================================================================= #


def send_command(command: str):
    os.system(command)


def logger(log_text: str):
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    with open('{0}_{1}'.format(log_path, time.strftime('%Y-%m-%d', time.localtime())), 'a+') as f:
        f.write('{0}  {1}'.format(log_prefix, log_text))


def execute_screen_command(operate_type: str, screen_name:str, server_path: str, run_command:str):
    # create new screen.
    if operate_type == 'create':
        command = ('screen -RU {0} -p 0 -X stuff "cd {1}\n{2}\n"'.format(screen_name, server_path, run_command))
        return command
    # run command in screen.
    elif operate_type == 'execute':
        command = ('screen -xU {0} -p 0 -X stuff "{1}\n"'.format(screen_name, run_command))
        return command


def run_command_from_yaml(operate_type: str, yaml_path: str, command: str):
    # open .yaml file to get server info.
    with open(yaml_path, encoding='utf-8') as file:
        server_dict = yaml().load(file)
    try:
        for server_path, server in server_dict.items():
            for server_name in server:
                server_full_path = os.path.join(server_path, server_name)
                if DEBUG_FLAG:
                    print(execute_screen_command(operate_type, server_name, server_full_path, command))
                else:
                    send_command(execute_screen_command(operate_type, server_name, server_full_path, command))
                    logger(execute_screen_command(operate_type, server_name, server_full_path, command))
                    print('{} starting now.'.format(server_name))
                time.sleep(1)
    except AttributeError:
        print('no server in {}\n'.format(yaml_path))