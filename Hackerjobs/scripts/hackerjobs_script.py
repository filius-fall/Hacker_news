import click

from ..main import move_file_to_config,env_file_op

@click.group()
@click.option('--count', default=1, help='number of greetings')
def cli(count):
    click.echo(count)

@cli.command()
@click.argument('filename')
def who_wants_to_be_hired(filename):
    click.echo('Moved')
    move_file_to_config(filename)

@cli.command()
@click.option('--api-name',default="",help="insert API-name")
@click.option('--api-version',default="",help="Takes API-version")
@click.option('--spread-sheet-id',default="",help="Your Account SpreadSheetId")
@click.option('--client-secret-file-name',default="",help="Your .json file created during OAth process")
def config(api_name,api_version,spread_sheet_id,client_secret_file_name):
    env_file_op(api_name,api_version,spread_sheet_id,client_secret_file_name)
    click.echo("ENV FILE CREATED")