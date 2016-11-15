from __future__ import print_function

import os
import gdapi
import json

from urlparse import urljoin


ENV_FREFIX = 'benchmark'
ENV_FMT = ENV_FREFIX + '_%s'

STACK_FREFIX = 'benchmark'
STACK_FMT = STACK_FREFIX + '-%s'

SERVICE_FREFIX = 'benchmark'
SERVICE_FMT = SERVICE_FREFIX + '-%s'

CONF_FILE_PATH = os.environ['HOME']+'/.cx5bench.conf'
CONF_ENV_FILE_PATH = os.environ['HOME']+ '/.cx5bench.%s.conf'


class CattleClient(object):

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(CattleClient, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
            return cls._instance

    def __init__(self):
        with open(CONF_FILE_PATH, 'r') as conf_file:
            conf = json.loads(conf_file.read())
            self.url = conf['url']
            self.access_key = conf['access_key']
            self.secret_key = conf['secret_key']

    def global_client(self):
        return gdapi.Client(url=self.url,
                            access_key=self.access_key,
                            secret_key=self.secret_key)

    def env_client(self, env):
        if not self.url.endswith('/'):
            self.url = self.url + '/'
        env_url = urljoin(self.url, 'projects/%s' % env)

        env_conf_file = CONF_ENV_FILE_PATH % env
        if os.path.exists(env_conf_file):
            with open(env_conf_file, 'r') as conf_file:
                conf = json.loads(conf_file.read())
                return gdapi.Client(url=env_url,
                                    access_key=conf['access_key'],
                                    secret_key=conf['secret_key'])
        else:
            global_client = self.global_client()
            api_key = global_client.create_apiKey(accountId=env, name='cli')
            access_key = api_key.publicValue
            secret_key = api_key.secretValue
            with open(env_conf_file, 'w') as conf_file:
                conf = {'url':env_url, 'access_key':access_key,
                        'secret_key':secret_key}
                conf_file.writelines(json.dumps(conf))

            return gdapi.Client(url=env_url,
                                access_key=access_key,
                                secret_key=secret_key)


def get_global_client():
    return CattleClient().global_client()

def get_env_client(env):
    return CattleClient().env_client(env)


