#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static.
if ! command -v nginx &> /dev/null
then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create the folder /data/ if it doesn’t already exist
sudo mkdir -p /data

# Create the folder /data/web_static/ if it doesn’t already exist
sudo mkdir -p /data/web_static

# Create the folder /data/web_static/releases/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases

# Create the folder /data/web_static/shared/ if it doesn’t already exist
sudo mkdir -p /data/web_static/shared

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test

# Create a fake HTML file /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
if [ -L /data/web_static/current ]
then
    sudo unlink /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i 's|root /var/www/html;|root /data/web_static/current;|g' /etc/nginx/sites-available/default
sudo sed -i 's|server_name _;|server_name mydomainname.tech;|g' /etc/nginx/sites-available/default
sudo sed -i '$ i \
    location /hbnb_static { \
        alias /data/web_static/current; \
    }' /etc/nginx/sites-available/default

# Restart Nginx after updating the configuration
sudo systemctl restart nginx
