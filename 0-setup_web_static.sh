#!/usr/bin/env bash
# This script sets up a new webserver

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo '<h1>Hello World</h1>' > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown ubuntu:ubuntu /data/

sed -i '0,/=404;/s//=404;\n\t}\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;/' /etc/nginx/sites-available/default
sudo ln -sf /etc/nginx/sites-enabled/
sudo service nginx restart
