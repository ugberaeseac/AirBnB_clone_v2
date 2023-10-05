#!/usr/bin/env bash
# This script sets up a new webserver

sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo "Ifebusola's website" > sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current 
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '0,/=404;/s//=404;\n\t}\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;/' /etc/nginx/sites-available/default
sudo ln -sf /etc/nginx/sites-enabled/
sudo service nginx restart
