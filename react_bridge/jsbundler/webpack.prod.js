const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const { merge } = require('webpack-merge')
const common = require('./webpack.common.js')

module.exports = merge(common, {
  mode: 'production',
  devtool: 'source-map',
  output: {
    filename: '[name].[hash].js',
    path: process.env['REACT_BRIDGE_PRODUCTION_OUTPUT'],
  },
  plugins: [new MiniCssExtractPlugin({
    filename: '[name].[hash].css',
  })],
})
