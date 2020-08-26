import shutil
import os
import json
from django.core.management.base import BaseCommand
from react_bridge.utils import run_npm_command
from react_bridge.config import JS_CONFIG

BUNDLER_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../jsbundler'))

class Command(BaseCommand):
    help = 'Build your js'

    def handle(self, *args, **options):
        # Remove old build dir
        shutil.rmtree(JS_CONFIG['output_path'], ignore_errors=True)

        conf = json.dumps(JS_CONFIG)
        current_env = os.environ.copy()
        current_env['REACT_BRIDGE_JS_CONFIG'] = conf
        run_npm_command(['install'], cwd=BUNDLER_DIR)
        run_npm_command(['build'], env=current_env, cwd=BUNDLER_DIR)