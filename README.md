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
    'use_yarn': True,
    'npm_command': 'yarn',
    'output_path': os.path.join(BASE_DIR, 'static/build'),
    'output_url': '/static/build/',

     # Webpack resolve: https://webpack.js.org/configuration/resolve/#resolve
    'resolve': None,

    # Webpack entry: https://webpack.js.org/configuration/entry-context/#entry
    'entry': None,
     # Es:.
    'entry': os.path.join(BASE_DIR, 'js/src/index.js'),
}

# Use js bridge in dev mode
REACT_BRIDGE_DEV = True
```

To use `django-react-bridge` with the default configuration you should
include your top static in your `STATICFILES_DIRS` or your can change
`output_path` according to your staticfile configuration.


```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

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