#!/usr/bin/python3

"""
    A Fabric script (based on the file 1-pack_web_static.py) that
    distributes an archive to your web servers, using the function do_deploy.
"""


from fabric.api import put, run, env
from os.path import exists
env.hosts = ['142.44.167.228', '144.217.246.195']


def do_deploy(archive_path):
    """sends given archive to specified servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path_to_upload = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path_to_upload, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path_to_upload, no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path_to_upload, no_ext))
        run('rm -rf {}{}/web_static'.format(path_to_upload, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path_to_upload, no_ext))
        return True
    except:
        return False
