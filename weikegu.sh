#! /bin/sh

export PATH=$PATH:/usr/local/bin
cd /home/jang/weikegu
nohup scrapy crawl weikegu_spider >> weikegu.log 2>&1 &
