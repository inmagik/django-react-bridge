import json
import requests
from django import template
from django.utils.safestring import mark_safe
from react_bridge.config import JS_CONFIG, USE_JS_DEV_SERVER

DEV_SERVER_URL = 'http://localhost:9000'

register = template.Library()

@register.simple_tag(takes_context=True)
def render_component(context, component_name, in_tag='div', **props):
    if component_name not in context['BRIDGED_REACT_COMPONENTS']:
        context['BRIDGED_REACT_COMPONENTS'][component_name] = []

    tag_id = 'dj_components__' + component_name + '__' + str(len(context['BRIDGED_REACT_COMPONENTS'][component_name]))
    context['BRIDGED_REACT_COMPONENTS'][component_name].append({
        'tag_id': tag_id,
        'props': props,
    })

    return mark_safe(f'<{in_tag} id="{tag_id}"></{in_tag}>')


def js_render_component(component_name, tag_id, props):
    js_props = json.dumps(props)
    js_dom_element = 'document.getElementById("' + tag_id + '")'
    js_dj_component = 'window.DjangoComponents["' + component_name + '"]'

    return js_dj_component + '.render(' + js_dom_element + ',' + js_props + ');'

def make_script(filename):
    return '<script type="text/javascript" src="' + filename +'"></script>'

def make_style(filename):
    return '<link rel="stylesheet" href="' + filename +'"></script>'

def get_body_files_from_manifest(manifest, entry):
    names = list(manifest.keys())

    def check_name(name):
        if name == entry + '.js':
            return True
        if name.startswith('vendors') and ('~' + entry) in name and name.endswith('.js'):
            return True

        return False

    entry_names = [name for name in names if check_name(name)]
    return [manifest[name] for name in entry_names]

def get_head_files_from_manifest(manifest, entry):
    names = list(manifest.keys())

    def check_name(name):
        if name == entry + '.css':
            return True
        if name.startswith('vendors') and ('~' + entry) in name and name.endswith('.css'):
            return True

        return False

    entry_names = [name for name in names if check_name(name)]
    return [manifest[name] for name in entry_names]

@register.simple_tag(takes_context=True)
def react_body_tags(context, entry='main'):
    # Generate the correct files my entry point
    if USE_JS_DEV_SERVER:
        r = requests.get(DEV_SERVER_URL + '/manifest.json')
        manifest = r.json()
    else:
        with open(JS_CONFIG['output_path'] + '/manifest.json') as f:
            manifest = json.loads(f.read())

    files = get_body_files_from_manifest(manifest, entry)

    out = ''
    for entry_file in files:
        out += make_script(entry_file)

    # Call render con components
    out += '<script type="text/javascript">'
    out += '(function(){'

    for component_name, component_instances in context['BRIDGED_REACT_COMPONENTS'].items():
        for component_istance in component_instances:
            out += js_render_component(component_name, component_istance['tag_id'], component_istance['props'])

    out += '})();'
    out += '</script>'

    return mark_safe(out)

@register.simple_tag(takes_context=True)
def react_head_tags(context, entry='main'):
    # Generate the correct files my entry point
    if USE_JS_DEV_SERVER:
        # Loaded by webpack using JS
        return ''
    else:
        with open(JS_CONFIG['output_path'] + '/manifest.json') as f:
            manifest = json.loads(f.read())

    files = get_head_files_from_manifest(manifest, entry)

    out = ''
    for entry_file in files:
        out += make_style(entry_file)

    return mark_safe(out)