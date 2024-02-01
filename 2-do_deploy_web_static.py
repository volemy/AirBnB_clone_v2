#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
import os.path
from fabric.api import env, run, put

env.hosts = ['54.237.12.204', '3.86.13.209']


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    Args:
        archive_path: path of the archive to distribute
    Returns:
        True if all operations have been done correctly
        False otherwise
    """
    if not os.path.exists(archive_path):
        return False
    filename = archive_path.split("/")[-1]
    name = filename.split(".")[0]

    if put(archive_path, "/tmp/{}".format(filename)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(filename, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(filename)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True
