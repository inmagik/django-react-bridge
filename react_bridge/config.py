import os
from django.conf import settings

DEFAULT_JS_CONFIG = {
    'use_yarn': True,
    'npm_command': 'yarn',
    'output_path': os.path.join(settings.BASE_DIR, 'static/build'),
    'output_url': '/static/build/',
    'resolve': None,
    'entry': None,
}

USE_JS_DEV_SERVER = getattr(settings, 'REACT_BRIDGE_DEV', True)

JS_CONFIG = {
    **DEFAULT_JS_CONFIG,
    **getattr(settings, 'REACT_BRIDGE_JS_CONFIG', {})
}