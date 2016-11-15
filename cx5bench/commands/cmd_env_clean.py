from __future__ import print_function

import click

from cx5bench import config
from cx5bench.cli import pass_context


@click.command('env-clean', short_help='clean env test data')
@pass_context
def cli(ctx):
    """Clean test data"""
    client = config.get_global_client()
    for env in client.list_project():
        if env.name.startswith(config.ENV_FREFIX):
            print('remove testing env data: %s, %s' % (env.id, env.name))
            if env.state == 'active':
                client.action(env, 'deactivate')
            client.delete(env)


__command_name__ = 'env-clean'
