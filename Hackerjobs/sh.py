import os
import re
from .sheets_instance import create_service
from decouple import config

from dotenv import load_dotenv
from pathlib import Path 

from .get_news import list_of_dicts,list_of_lists,new_thread_id

dotenv_path = str(os.path.expanduser('~')) +'/.config/hackerjobs/.env'
load_dotenv(dotenv_path=dotenv_path)

# test = os.getenv('TEST')
# print(test)
# print(os.getcwd())

# k = str(os.path.expanduser('~')) +'/.config/hackerjobs/'+str(os.getenv("CLIENT_SECRET_FILE"))
# print(k)



client_file = str(os.path.expanduser('~')) +'/.config/hackerjobs/'+str(os.getenv("CLIENT_SECRET_FILE"))
api_name = os.getenv("API_NAME")
api_version = os.getenv("API_VERSION")
scopes = ['https://www.googleapis.com/auth/spreadsheets']


def service_initiation():

    return create_service(client_file, api_name, api_version, scopes)

range_name = 'A1'

spreadsheet_id = config("SPREAD_SHEET_ID")




def add_data_to_sheets(data,range_name,spreadsheet_id):
    body = {
    'values': data,
    'majorDimension': 'ROWS',
    }
    service = service_initiation()
    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=range_name,valueInputOption='USER_ENTERED',
        body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))




def add_heading_to_sheets():


    heading_list = [list(list_of_dicts[0].keys())]
    add_data_to_sheets(heading_list,"A1:Z1",spreadsheet_id)


def add_to_sheets():
    body = {
    'values': list_of_lists,
    'majorDimension': 'ROWS',
    }
    service = service_initiation()

    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range="A2:J2",valueInputOption='USER_ENTERED',insertDataOption="INSERT_ROWS",
        body=body).execute()


# add_to_sheets()




def get_values_from_sheets():
    service = service_initiation()

    result1 = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id, range="A2").execute()


    # lookup the data on the last row
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A:Z'
    ).execute()
    try:
        return result['values'][-1][-2]
    except KeyError:
        return 0

def is_same_thread():
    try:
        last_value = int(get_values_from_sheets())
    except ValueError:
        last_value = 0
    print(last_value,new_thread_id)
    if last_value == int(new_thread_id):
        return None
    else:
        print("ADDDDING TO SHEEEEEETSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
        add_to_sheets()


def execute_sheets():
    add_heading_to_sheets()
    is_same_thread()

