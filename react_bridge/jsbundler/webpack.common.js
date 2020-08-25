const ManifestPlugin = require('webpack-manifest-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const path = require('path')
const fs = require('fs')

const djangoBridgeConfig = JSON.parse(process.env['REACT_BRIDGE_JS_CONFIG'])

console.log('Django Bridge Config:\n', djangoBridgeConfig)

module.exports = {
  entry: djangoBridgeConfig.entry,
  output: {
    filename: '[name].js',
  },
  optimization: {
    splitChunks: {
      chunks: 'all',
    },
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /(node_modules)/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react'],
          },
        },
      },
      {
        test: /\.css$/i,
        use: [
          process.env.NODE_ENV === 'production'
            ? MiniCssExtractPlugin.loader
            : 'style-loader',
          'css-loader',
        ],
      },
    ],
  },
  plugins: [new ManifestPlugin()],
  resolve: {
    ...djangoBridgeConfig.resolve,
    alias: {
      'react-django-bridge': path.resolve('./bridge.js'),
      ...((djangoBridgeConfig.resolve || {}).alias || {}),
    },
  },
}
