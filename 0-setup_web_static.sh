#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
# Installs Nginx if it not already installed
# Creates folder /data/web_static/shared/ if it doesn’t already exist
# Creates f older /data/web_static/releases/test/ if it doesn’t already exist
# Creates  HTML file /data/web_static/releases/test/index.html 
#	with simple content to test your Nginx configuration
# Creates symbolic link /data/web_static/current linked to the /data/web_static/releases/test/
# 	If link already exists, deletes and recreates whenever script is ran.
# Gives ownership of /data/ to ubuntu user && group and should be recursive
# Ngins should serve the content of /data/web_static/current/ to hbnb_static
#	(example: https://mydomainname.tech/hbnb_static).
# Restart Nginx after updating the configuration

sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web/static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo "# x03. AirBnB clone - Deploy static" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current/
sudo chown -hR ubuntu:ubuntu /data/
content_1="\\\tlocation /hbnb_static {\n\t\t alias /data/web_static/current;\n\t}\n\n"
sudo sed -i "49i $content_1" /etc/nginx/sites-available/default
sudo service nginx restart
