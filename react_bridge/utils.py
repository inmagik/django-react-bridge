import os
import subprocess
from react_bridge.config import JS_CONFIG

def run_npm_command(command, **kwargs):
    return subprocess.run([JS_CONFIG['npm_command'], *command], **kwargs)

def run_node_add_packages(packages, dev=False, **kwargs):
    if JS_CONFIG['use_yarn']:
        command = ['add'] + packages
        if dev:
            command.append('--dev')
        return run_npm_command(command, **kwargs)
    else:
        command = ['install'] + packages
        if dev:
            command.append('--save-dev')
        return run_npm_command(command, **kwargs)