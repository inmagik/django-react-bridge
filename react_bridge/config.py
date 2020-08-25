import os
from django.conf import settings

DEFAULT_JS_CONFIG = {
    'use_yarn': True,
    'npm_command': 'yarn',
    'output_path': os.path.join(settings.BASE_DIR, 'static/build'),
    'resolve': None,
    'entry': None,
}

JS_CONFIG = {
    **DEFAULT_JS_CONFIG,
    **getattr(settings, 'REACT_BRIDGE_JS_CONFIG', {})
}