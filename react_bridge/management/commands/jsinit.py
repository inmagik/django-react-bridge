import os
import shutil
from django.conf import settings
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

        self.stdout.write(self.style.HTTP_NOT_MODIFIED('Install build tools and a linter'))
        bundler_packages =[
            # Build
            "@babel/core",
            "@babel/preset-env",
            "@babel/preset-react",
            "babel-loader",
            "css-loader",
            "mini-css-extract-plugin",
            "style-loader",
            "webpack",
            "webpack-cli",
            "webpack-dev-server",
            "webpack-manifest-plugin",
            "webpack-merge",
            # Linter
            'eslint-config-react-app',
            'babel-eslint@10.x',
            'eslint-plugin-flowtype@4.x',
            'eslint@6.x',
            'eslint-plugin-import@2.x',
            'eslint-plugin-jsx-a11y@6.x',
            'eslint-plugin-react@7.x',
            'eslint-plugin-react-hooks@2.x',
        ]
        run_node_add_packages(bundler_packages, cwd=output_path, dev=True)

        rel_pkg_path_hint = os.path.relpath(output_path, settings.BASE_DIR)
        output_path_hint = os.path.join(rel_pkg_path_hint, 'static/build')
        output_url_hint = '/static/build/'
        entry_hint = os.path.join(rel_pkg_path_hint, 'src/index.js')

        self.stdout.write('\n')
        self.stdout.write(self.style.HTTP_NOT_MODIFIED('Some configuration to help get started:'))

        conf_str = "REACT_BRIDGE_JS_CONFIG = {\n"
        conf_str += f"    'package_json_path': os.path.join(BASE_DIR, '{rel_pkg_path_hint}'),\n"
        conf_str += f"    'output_path': os.path.join(BASE_DIR, '{output_path_hint}'),\n"
        conf_str += f"    'output_url': '{output_url_hint}',\n"
        conf_str += f"    'entry': os.path.join(BASE_DIR, '{entry_hint}'),\n"
        conf_str += "}"
        self.stdout.write('\n')
        self.stdout.write(conf_str)
        self.stdout.write('\n')

        staticfiles_hint = os.path.join(rel_pkg_path_hint, 'static')

        dj_extra_conf = "STATICFILES_DIRS = [\n"
        dj_extra_conf += f"    os.path.join(BASE_DIR, '{staticfiles_hint}'),\n"
        dj_extra_conf += "]"
        self.stdout.write(dj_extra_conf)