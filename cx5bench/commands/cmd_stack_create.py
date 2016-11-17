from __future__ import print_function

import click

from cx5bench import config
from cx5bench.cli import pass_context


@click.command('stack-create', short_help='stack benchmark')
@click.argument('count')
@click.option('--env', default='1a5', help='which env to create stacks')
@click.option('--docker-compose', '-dp', type=click.File('r'))
@click.option('--rancher-compose', '-rp', type=click.File('r'))
@pass_context
def cli(ctx, count, env, docker_compose, rancher_compose):
    """Benchmark for Stack Create

    ex:

    \b
        #create 10 stacks on Rancher
        cx5bench stack-create 10

    """
    empty = False
    if not (docker_compose and rancher_compose):
        empty = True

    client = config.get_env_client(env)
    if empty:
        for surfix in range(int(count)):
            stack_name=config.STACK_FMT % surfix
            stack = client.create_environment(name=stack_name)
            print('create testing stack data: %s, %s' % (stack.id, stack.name))
    else:
        docker_cp = docker_compose.read()
        rancher_cp = rancher_compose.read()
        for surfix in range(int(count)):
            stack_name=config.STACK_FMT % surfix
            stack = client.create_environment(name=stack_name,
                                              startOnCreate=True,
                                              dockerCompose=docker_cp,
                                              rancherCompose=rancher_cp)
            print('create testing stack data: %s, %s' % (stack.id, stack.name))


__command_name__ = 'stack-create'
