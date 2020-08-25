function bindComponentRender(React, ReactDOM, component) {
  const render = (element, props) => {
    ReactDOM.render(React.createElement(component, props), element)
  }
  return {
    render,
  }
}

export function registerComponents({
  React,
  ReactDOM,
  components,
}) {
  const bindComponents = Object.keys(components).reduce((binded, name) => {
    binded[name] = bindComponentRender(React, ReactDOM, components[name])
    return binded
  }, {})

  window.DjangoComponents = {
    ...window.DjangoComponents || {},
    ...bindComponents,
  }
}