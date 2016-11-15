from __future__ import print_function

import click

from cx5bench import config
from cx5bench.cli import pass_context


@click.command('stack-clean', short_help='clean stack test data')
@click.option('--env', default='1a5', help='which env to clean stacks')
@pass_context
def cli(ctx, env):
    """Clean test data"""
    client = config.get_env_client(env)
    for stack in client.list_environment():
        if stack.name.startswith(config.STACK_FREFIX):
            print('remove testing stack data: %s, %s' % (stack.id, stack.name))
            client.delete(stack)


__command_name__ = 'stack-clean'
