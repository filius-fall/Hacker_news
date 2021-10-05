import os
import re
from Google import Create_Service
from decouple import config


from get_news import list_of_dicts,list_of_lists,new_thread_id



client_file = config("CLIENT_SECRET_FILE")
api_name = config("API_NAME")
api_version = config("API_VERSION")
scopes = ['https://www.googleapis.com/auth/spreadsheets']


service = Create_Service(client_file, api_name, api_version, scopes)
range_name = 'A1'

spreadsheet_id = config("SPREAD_SHEET_ID")




def add_data_to_sheets(data,range_name,spreadsheet_id):
    body = {
    'values': data,
    'majorDimension': 'ROWS',
    }
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
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range="A2:J2",valueInputOption='USER_ENTERED',insertDataOption="INSERT_ROWS",
        body=body).execute()


# add_to_sheets()

add_heading_to_sheets()


def get_values_from_sheets():

    result1 = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id, range="A2").execute()


    # lookup the data on the last row
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A:Z'
    ).execute()

    return result['values'][-1][-2]


def is_same_thread():
    try:
        last_value = int(get_values_from_sheets())
    except ValueError:
        last_value = 0
    print(last_value,new_thread_id)
    if last_value == int(new_thread_id):
        return "ss"
    else:
        print("ADDDDING TO SHEEEEEETSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
        add_to_sheets()


is_same_thread()