from __future__ import print_function

import click

from cx5bench.cli import pass_context
from sh import ab


@click.command('server-stress', short_help='Rancher Server stress tests')
@click.argument('url', default='http://192.168.1.101:8080/v1/environments')
@click.option('--requests', '-n', default='100',
              help='Number of requests to perform')
@click.option('--concurrency', '-c', default='10',
              help='Number of multiple requests to make at a time')
@pass_context
def cli(ctx, url, requests, concurrency):
    """Benchmark for Rancher Server

    ex:

    \b
        cx5bench server-stress 10
    """
    print(ab('-n', requests, '-c', concurrency, url))


__command_name__ = 'server-stress'
