# Django React Bridge
> Think at Create React App but for Django


## Installation
```sh
pip install django-react-bridge
```

## Configuration

Add `react_bridge` to the installed apps:

```py
INSTALLED_APPS = (
    # ...
    'react_bridge',
)
```

Add the react components context processor:

```py
TEMPLATES = [
    {
        # ...
        'OPTIONS': {
            'context_processors': [
                # ...
                'react_bridge.context_processors.react_components',
            ],
        },
    },
]
```

Configure react bridge:

```python
REACT_BRIDGE_JS_CONFIG = {
    # Should use yarn or npm? default: True
    'use_yarn': True,

    # Path of your npm_command or yarn command according to use_yarn default: yarn
    'npm_command': '/bin/path/to/my/yarn/or/npm',

    # Path of package json where js is installed default: None your should configure your own
    'package_json_path': os.path.join(BASE_DIR, 'js'),

    # Path of bundler output default: None your should configure your own
    'output_path': os.path.join(BASE_DIR, 'static/build'),

    # Url where the bundler output is server default: None your should configure your own
    'output_url': '/static/build/',

    # Webpack entry: https://webpack.js.org/configuration/entry-context/#entry
    # default: None
    'entry': os.path.join(BASE_DIR, 'js/src/index.js'),

    # Webpack resolve: https://webpack.js.org/configuration/resolve/#resolve
    # default: None
    'resolve': {
      'alias': {
        '@components': os.path.join(BASE_DIR, 'shared/components'),
      }
    },

}

# Use js bridge in dev mode
REACT_BRIDGE_DEV = True
```

To use `django-react-bridge` in non standard paths you should
include your top static in your `STATICFILES_DIRS` or your can change
`output_path` according to your staticfile configuration.


```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

To install al required node packages needs to run `django-react-bridge` run:

```sh
python manage.py jsinit path/to/my/js/project
```

This commands install all for you and when finished print on console a base
`REACT_BRIDGE_JS_CONFIG` with adjusted path related to initial given project path.


## Usage

Inside your entry javascript file:

```js
import React from 'react'
import ReactDOM from 'react-dom'
import { registerComponents } from 'django-react-bridge'
import MyComponent from './MyComponent'

registerComponents({
  React,
  ReactDOM,
  components: {
    // Register here yuor components
    MyComponent,
  }
})
```

Inside your Django template:

```html
{% load react_bridge %}
<html>
  <head>
    {% react_head_tags %}
  </head>
  <body>

    {% render_component "MyComponent" in_tag='div' myPropA='a' myPropB='b' %}

    {% react_body_tags %}
  </body>
</html>
```

Multi bundle set up:

If you need to split your app in multiple bundles:


```python
REACT_BRIDGE_JS_CONFIG = {
    'entry': {
      'frontend': os.path.join(BASE_DIR, 'front/src/index.js'),
      'admin': os.path.join(BASE_DIR, 'admin/src/index.js'),
    }
}
```

Then in your template you need to pass the bundle name when render related tags:

```html
{% load react_bridge %}
<html>
  <head>
    {% react_head_tags 'admin' %}
  </head>
  <body>
    {% react_body_tags 'admin %}
  </body>
</html>
```

## Commands

**NOTE:**

Before run these commands you should run `jsinit` to install al relative
packages needed to run js build tools.

### jsdevserver

Start dev server on port 9000.

You should have `REACT_BRIDGE_DEV = True`.


```sh
python manage.py jsdevserver
```

### jsbuild

Build your js and realted assets according to your `REACT_BRIDGE_JS_CONFIG`.

```sh
python manage.py jsbuild
```

### jsinit

Init a js project at given path.

```sh
python manage.py jsinit path/to/my/js/project
```