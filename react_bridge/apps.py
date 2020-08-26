import json
import requests
from react_bridge.config import JS_CONFIG, USE_JS_DEV_SERVER
from django.apps import AppConfig

DEV_SERVER_URL = 'http://localhost:9000'

class ReactBridgeConfig(AppConfig):
    name = 'react_bridge'
    verbose_name = 'React Bridge'
    cached_manifest = None

    def get_manifest(self):
        # On JS DEV always fetch fresh manifest from js dev server
        if USE_JS_DEV_SERVER:
            r = requests.get(DEV_SERVER_URL + '/manifest.json')
            return r.json()

        # When manifest is write (on production build)
        # store last readed manifest in memory
        if self.cached_manifest is not None:
            return self.cached_manifest

        with open(JS_CONFIG['output_path'] + '/manifest.json') as f:
            self.cached_manifest = json.loads(f.read())
        return self.cached_manifest