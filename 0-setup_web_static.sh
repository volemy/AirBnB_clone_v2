#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static.

# Install Nginx
apt-get -y update
apt-get -y install nginx

# Create directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create fake HTML
echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>" > /data/web_static/releases/test/index.html

# Create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership
chown -hR ubuntu:ubuntu /data/

# Configure Nginx
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart
