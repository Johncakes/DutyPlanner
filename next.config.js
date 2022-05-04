/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
}

const WindiCSSWebpackPlugin = require('windicss-webpack-plugin')

module.exports = {
  // ...
  nextConfig,
  webpack(config) {
    config.plugins.push(new WindiCSSWebpackPlugin())
    return config
  },
}
