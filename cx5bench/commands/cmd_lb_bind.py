from __future__ import print_function

import click

from cx5bench import config
from cx5bench.cli import pass_context


@click.command('lb-bind', short_help='test rancher-lb bind services')
@click.argument('lb-service-id')
@click.argument('count')
@click.option('--env', default='1a5', help='which env to operate')
@pass_context
def cli(ctx, lb_service_id, count, env):
    """Test Rancher-lb bind services

    ex:

    \b
        #bind 10 services to lb 1s12
        cx5bench lb-bind 1s12 10
    """
    client = config.get_env_client(env)
    all_bind_service_list = []
    for service in client.list_service():
        if service.name.startswith(config.SERVICE_FREFIX) and service.state == 'active':
            all_bind_service_list.append({'serviceId': service.id,
                                          'ports': []})

    to_bind_service_list = all_bind_service_list[:int(count)]
    lb = client.by_id_loadBalancerService(lb_service_id)
    client.action(lb, 'setservicelinks', serviceLinks=to_bind_service_list)

    print('\n'.join([s['serviceId']+' linked' for s in to_bind_service_list]))


__command_name__ = 'lb-bind'
