# 12 云计算: Google App Engine

## App Engine

App Engine系统主要由4部分组成:

1. 语言运行时: 当前支持Python, HVM, PHP, Go等

2. 硬件基础设置 Bigtable: App Engine 用于存储数据的非关系型数据库

3. 基于Web的管理和系统状态

4. 软件开发包SDK

## 沙盒和App Engine SDK

安全策略限制, 一些功能使用受限; 不过提供了一些API以补全这些功能.

webapp2, Flask, Django 这些web框架都可以使用.

tipfy

1. 下载SDK: `https://cloud.google.com/sdk/docs/#deb`


2. 几个命令: gcloud, dev_appserver.py

dev运行: `dev_appserver.py app.yaml`

部署: `gcloud app deploy`

之后访问类似的URL: `https://glrh11glrh11.appspot.com/`

删除应用: 在这里删除app `https://console.cloud.google.com/cloud-resource-manager?_ga=2.141838388.-764531817.1505729338`

## 

