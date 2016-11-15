from __future__ import print_function

import click
import subprocess

from cx5bench.cli import pass_context


@click.command('server-stress', short_help='Rancher Server stress tests')
@click.argument('shell_file', type=click.Path(exists=True))
@click.option('--concurrency', '-c', default='10',
              help='Number of multiple requests to make at a time')
@pass_context
def cli(ctx, shell_file, concurrency):
    """Benchmark for jenkins.system

    ex:

    \b
        cx5bench jenkins-download -c 10
    """
    for i in range(int(concurrency)):
        cmd = '%s %s' % (shell_file, i)
        print(cmd)
        subprocess.Popen(cmd, shell=True)


__command_name__ = 'jenkins-download'
