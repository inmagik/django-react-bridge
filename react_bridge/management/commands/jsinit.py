import os
import shutil
from django.core.management.base import BaseCommand
from react_bridge.utils import run_node_add_packages

STARTER_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../starter_js'))

class Command(BaseCommand):
    help = 'Bootstrap a js project'

    def add_arguments(self, parser):
        parser.add_argument('output', type=str)

    def handle(self, *args, **options):
        output_path = os.path.join(os.getcwd(), options['output'])

        shutil.copytree(STARTER_DIR, output_path, ignore=shutil.ignore_patterns('*node_modules'))
        self.stdout.write(self.style.HTTP_INFO('New js project created at: %s' % output_path))

        self.stdout.write(self.style.HTTP_NOT_MODIFIED('Install React'))
        run_node_add_packages(['react', 'react-dom'], cwd=output_path)

        self.stdout.write(self.style.HTTP_NOT_MODIFIED('Install a linter'))
        linter_packages =[
            'eslint',
            'eslint-config-react-app',
            'babel-eslint@10.x',
            'eslint-plugin-flowtype@4.x',
            'eslint@6.x',
            'eslint-plugin-import@2.x',
            'eslint-plugin-jsx-a11y@6.x',
            'eslint-plugin-react@7.x',
            'eslint-plugin-react-hooks@2.x',
        ]
        run_node_add_packages(linter_packages, cwd=output_path, dev=True)