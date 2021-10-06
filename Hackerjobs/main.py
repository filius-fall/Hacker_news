import shutil

def move_file_to_config(path):
    destination = '/home/filius-fall/.config/hackerjobs'
    shutil.copy(path,destination)

def env_file_op(api_name,api_version,spread_sheet_id,client_secret_file_name):

    lines = ["SPREAD_SHEET_ID = {0} \n".format(spread_sheet_id),"API_NAME = {0} \n".format(api_name),"API_VERSION = {0} \n".format(api_version),"CLIENT_SECRET_FILE = {0} \n".format(client_secret_file_name)]
    with open('/home/filius-fall/.config/hackerjobs/.env','w+') as file:
        file.writelines(lines)