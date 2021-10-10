import os
import re
from .sheets_instance import create_service
from decouple import config

from dotenv import load_dotenv
from pathlib import Path 

from .get_news import new_thread_id,make_lists,get_list_of_comments

dotenv_path = str(os.path.expanduser('~')) +'/.config/hackerjobs/.env'
load_dotenv(dotenv_path=dotenv_path)



client_file = str(os.path.expanduser('~')) +'/.config/hackerjobs/'+str(os.getenv("CLIENT_SECRET_FILE"))
api_name = os.getenv("API_NAME")
api_version = os.getenv("API_VERSION")
scopes = ['https://www.googleapis.com/auth/spreadsheets']

service =  create_service(client_file, api_name, api_version, scopes)


# def service_initiation():

#     client_file = str(os.path.expanduser('~')) +'/.config/hackerjobs/'+str(os.getenv("CLIENT_SECRET_FILE"))
#     api_name = os.getenv("API_NAME")
#     api_version = os.getenv("API_VERSION")
#     scopes = ['https://www.googleapis.com/auth/spreadsheets']

#     return create_service(client_file, api_name, api_version, scopes)


spreadsheet_id = config("SPREAD_SHEET_ID")







def add_data_to_sheets(data,range_name,spreadsheet_id):
    """
        This function will add the given list of lists to sheets at given range of the given sheet of spreadsheet_id

        Examples:

            data = [[1,2,3],[4,5,6]]
            range = "A1:D1"

            The first two rows of sheets are filled with first row being 1 2 3 and
            second row being 4 5 6 respectively 

        Input:
            data: 
                Type : List of Lists
            range_name:
                Type : String
                structure: "<alphabit><number>:<alphabit><numer>"
                example: "A1:D5"
            spreadsheet_id:
                Type: String
     """
    body = {
    'values': data,
    'majorDimension': 'ROWS',
    }
    # service = service_initiation()

    # The below will update the existing data in the rows with List of lists of data
    # valueInputOption is required for updating sheets

    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=range_name,valueInputOption='USER_ENTERED',
        body=body).execute()




def add_heading_to_sheets(list_of_comments):
    """
        Descryption:
            This function will add heading to the sheets i.e, it will add only first row of sheets.
            This function will take list of comment objects as input
    """

    heading_list = [list(make_lists(list_of_comments)['list_of_dicts'][0].keys())]
    add_data_to_sheets(heading_list,"A1:Z1",spreadsheet_id)


def add_to_sheets(list_of_comments):
    body = {
    'values': make_lists(list_of_comments)['list_of_lists'],
    'majorDimension': 'ROWS',
    }
    # service = service_initiation()

    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range="A2:J2",valueInputOption='USER_ENTERED',insertDataOption="INSERT_ROWS",
        body=body).execute()
    return result






def get_values_from_sheets():
    """
        Descryption:
            This function will get values from the sheet and return thread_id value of last row
    """
    # service = service_initiation()


    # lookup the data on the last row
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A:Z'
    ).execute()

    # Result is a dict which contains its parameters as keys like range,majorDimension,values
    try:
        val = result['values']              # This will give values key value of result dictionary
        last_thread = val[-1]               # This will give last comment list
        thread_id_value = last_thread[-2]   # This will get penultimate value which is thread_id so [-2]
        thread_value = int(thread_id_value)
        return thread_value
    except ValueError:
        return 0

def is_same_thread():
    """
        Descryption:
            This function will check if the previous added data post_id is same to the current fetched post_id
            If they are same it wont add the data to the sheets else it adds data to sheet
    """

    last_value = int(get_values_from_sheets())


    if last_value == int(new_thread_id()):
        return None
    else:
        add_to_sheets(get_list_of_comments())


def execute_sheets():
    add_heading_to_sheets(get_list_of_comments())
    is_same_thread()

