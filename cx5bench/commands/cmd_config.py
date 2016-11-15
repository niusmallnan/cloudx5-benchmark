from __future__ import print_function

import click
import json

from cx5bench import config
from cx5bench.cli import pass_context


@click.command('config', short_help='config tool')
@pass_context
def cli(ctx):
    cattle_url = click.prompt('Cattle URL',
                              default='http://192.168.99.100:8080/v1')
    access_key = click.prompt('Access Key',
                              default='xxxxxxxxxxxxx')
    secret_key = click.prompt('Secret Key',
                              default='xxxxxxxxxxxxxxxxxx')
    conf = {'url':cattle_url, 'access_key':access_key, 'secret_key':secret_key}
    with open(config.CONF_FILE_PATH, 'w') as conf_file:
        conf_file.writelines(json.dumps(conf))
    print('config init......')

