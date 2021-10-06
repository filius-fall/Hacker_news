import click
from ..load_values_to_sheets import execute_sheets

from ..main import move_file_to_config,env_file_op

@click.group()
@click.option('--count', default=1, help='number of greetings')
def cli(count):
    click.echo(count)

@cli.command()
def who_wants_to_be_hired():
    # is_same_thread
    click.echo('Hired')

@cli.command()
@click.option('--api-name',default=" ",help="insert API-name")
@click.option('--api-version',default=" ",help="Takes API-version")
@click.option('--spread-sheet-id',default=" ",help="Your Account SpreadSheetId")
@click.option('--client-secret-file-name',default=" ",help="Your .json file created during OAth process")
@click.option('--secret-file',help='moves secret file to config')
def config(api_name,api_version,spread_sheet_id,client_secret_file_name,secret_file):
    env_file_op(api_name,api_version,spread_sheet_id,client_secret_file_name)
    move_file_to_config(secret_file)

    click.echo("ENV FILE CREATED")

@cli.command()
def who():
    click.echo('Yo')
    execute_sheets()