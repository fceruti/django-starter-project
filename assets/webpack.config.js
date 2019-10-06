const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const path = require("path");
const webpack = require("webpack");
const BundleTracker = require("webpack-bundle-tracker");

const resolve = path.resolve.bind(path, __dirname);

module.exports = (env, argv) => {
  let output;
  let bundleTrackerPlugin;
  let extractCssPlugin;
  let fileLoaderPath;

  switch (argv.mode) {
    case "production":
      output = {
        path: resolve("bundles/"),
        filename: "[chunkhash]/[name].js",
        chunkFilename: "[chunkhash]/[name].[id].js",
        publicPath: "https://example.com/static/bundles/"
      };
      bundleTrackerPlugin = new BundleTracker({
        filename: "bundles/webpack-bundle.prod.json"
      });
      extractCssPlugin = new MiniCssExtractPlugin({
        filename: "[chunkhash]/[name].css",
        chunkFilename: "[chunkhash]/[name].[id].css"
      });
      fileLoaderPath = "file-loader?name=[name].[hash].[ext]";
      break;

    case "development":
      output = {
        path: resolve("bundles/"),
        filename: "dev/[name].js",
        chunkFilename: "dev/[name].js",
        publicPath: "http://127.0.0.1:8000/static/bundles/"
      };
      bundleTrackerPlugin = new BundleTracker({
        filename: "bundles/webpack-bundle.dev.json"
      });
      extractCssPlugin = new MiniCssExtractPlugin({
        filename: "dev/[name].css",
        chunkFilename: "dev/[name].[id].css"
      });
      fileLoaderPath = "file-loader?name=[name].[ext]";
      break;
    default:
      break;
  }

  return {
    mode: argv.mode,
    entry: "./index.js",
    output,
    module: {
      rules: [
        // Scripts
        {
          test: /\.js$/,
          exclude: /node_modules/,
          loader: "babel-loader"
        },
        // Styles
        {
          test: /\.(sa|sc|c)ss$/,
          use: [
            MiniCssExtractPlugin.loader,
            {
              loader: "css-loader",
              options: {
                sourceMap: true
              }
            },
            {
              loader: "sass-loader",
              options: {
                sourceMap: true
              }
            }
          ]
        },
        // Fonts
        {
          test: /\.(eot|otf|ttf|woff|woff2)(\?v=[0-9.]+)?$/,
          loader: "file-loader",
          options: {
            outputPath: "fonts"
          }
        },
        // Images
        {
          test: /\.(png|svg|jpg)(\?v=[0-9.]+)?$/,
          loader: "file-loader",
          options: {
            outputPath: "images"
          }
        }
      ]
    },
    plugins: [bundleTrackerPlugin, extractCssPlugin],
    devtool: "source-map"
  };
};
