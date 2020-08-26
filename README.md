# Django React Bridge
> Think Create React App but for Django


## Installation
```sh
pip install django-react-bridge
```

## Configuration

Add `react_bridge` to the installed apps:

```py
INSTALLED_APPS = (
    # ...
    'react_brdige',
)
```

Add the react component context processor:

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
    'output_path': os.path.join(settings.BASE_DIR, 'static/build'),
    'output_url': '/static/build/',

     # Webpack resolve: https://webpack.js.org/configuration/resolve/#resolve
    'resolve': None,

    # Webpack entry: https://webpack.js.org/configuration/entry-context/#entry
    'entry': None,
     # Es:.
    'entry': os.path.join(settings.BASE_DIR, 'js/src/index.js'),
}
```