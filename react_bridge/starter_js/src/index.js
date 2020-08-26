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