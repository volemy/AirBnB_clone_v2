#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
import os.path
from fabric.api import env, run, put

env.hosts = ['54.236.45.68', '100.25.102.49']


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
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}{}/web_static/* {}'.format(path, no_ext, path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
