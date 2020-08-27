from django.conf import settings

DEFAULT_JS_CONFIG = {
    'use_yarn': True,
    'npm_command': 'yarn',
    'package_json_path': None,
    'output_path': None,
    'output_url': None,
    'resolve': None,
    'entry': None,
}

USE_JS_DEV_SERVER = getattr(settings, 'REACT_BRIDGE_DEV', True)

JS_CONFIG = {
    **DEFAULT_JS_CONFIG,
    **getattr(settings, 'REACT_BRIDGE_JS_CONFIG', {})
}