from __future__ import print_function

import click

from cx5bench import config
from cx5bench.cli import pass_context


@click.command('env-create', short_help='env benchmark')
@click.argument('count')
@pass_context
def cli(ctx, count):
    """Benchmark for Env Create

    ex:

    \b
        #create 10 envs on Rancher
        cx5bench env-create 10

    """
    client = config.get_global_client()
    bench_env_list = []
    for surfix in range(int(count)):
        env_name=config.ENV_FMT % surfix
        client.create_project(name=env_name, description=config.ENV_FREFIX)
        bench_env_list.append(env_name)

    print('\n'.join(bench_env_list))


__command_name__ = 'env-create'
