import click
from ..load_values_to_sheets import execute_sheets

from ..main import move_file_to_config,env_file_op

@click.group()
def cli():
    """
    This function is the entry point for 'the hackerjobs' command
    """
    pass

# the variable in this brackets are the name of the command and is used along with 'hackerjobs' main command
@cli.command('config') 
@click.option('--api-name',required=True,help="Insert API-name.")    
@click.option('--api-version',required=True,help="Takes API-version")
@click.option('--spread-sheet-id',required=True,help="Your Account SpreadSheetId")
@click.option('--client-secret-file-name',required=True,help="Your .json file created during OAth process")
@click.option('--secret-file',required=True,help='moves secret file to config')
def create_config(api_name,api_version,spread_sheet_id,client_secret_file_name,secret_file):
    """Config DocString
        
        This function takes the values from the options written above and stores them into config file

        Examples:
            All the options mentioned above are required. Missing values for any option will result in an error

            $ hackerjobs config --api-name 'sheets'
            $ hackerjobs config --secret-file 'home/$USER/tokens/token.json'
            $ hackerjobs config --spread-sheet-id <google-sheet-id-of-your-sheet>

    """
    env_file_op(api_name,api_version,spread_sheet_id,client_secret_file_name)
    move_file_to_config(secret_file)

    click.echo("ENV FILE CREATED")


@cli.command("who-wants-to-be-hired")
def adding_data_to_sheets():
    """ This function adds data to the Google Sheet of your mentioned Sheet-Id """
   
    execute_sheets()
    click.echo("Data added to sheets")



if __name__ == "__main__":
    cli()