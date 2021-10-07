import shutil
import os

def move_file_to_config(path):
    """ This function moves file from given location to application config folder we created in .config folder """
    destination = str(os.path.expanduser('~')) +'/.config/hackerjobs/'
    shutil.copy(path,destination)

def env_file_op(api_name,api_version,spread_sheet_id,client_secret_file_name):
    """ This function creates an .env file if not already present in the .config/hackerjobs folder and fill it with environment variables """

    lines = ["SPREAD_SHEET_ID = {0} \n".format(spread_sheet_id),"API_NAME = {0} \n".format(api_name),"API_VERSION = {0} \n".format(api_version),"CLIENT_SECRET_FILE = {0} \n".format(client_secret_file_name)]
    
    path = str(os.path.expanduser('~')) +'/.config/hackerjobs/.env'
    with open(path,'w+') as file:
        file.writelines(lines)


