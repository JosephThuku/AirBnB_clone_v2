#!/usr/bin/env bash

# Install nginx if not already installed
if ! [ -x "$(command -v nginx)" ]; then
  sudo apt-get update
  sudo apt-get -y install nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/{releases,test,shared}

# Create fake HTML file for testing Nginx configuration
echo "Test HTML file" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link to current release
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Configure Nginx to serve content of /data/web_static/current to hbnb_static
sudo sed -i '/listen 80 default_server;/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart

