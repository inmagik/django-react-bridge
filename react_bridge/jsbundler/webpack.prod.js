const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const { merge } = require('webpack-merge')
const common = require('./webpack.common.js')

const djangoBridgeConfig = JSON.parse(process.env['REACT_BRIDGE_JS_CONFIG'])

module.exports = merge(common, {
  mode: 'production',
  devtool: 'source-map',
  output: {
    filename: '[name].[hash].js',
    path: djangoBridgeConfig['output_path'],
    publicPath: djangoBridgeConfig['output_url'],
  },
  plugins: [new MiniCssExtractPlugin({
    filename: '[name].[hash].css',
  })],
})
