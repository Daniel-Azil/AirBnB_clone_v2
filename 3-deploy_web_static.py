#!/usr/bin/python3
"""
    A Fabric script (based on the file 2-do_deploy_web_static.py)
    that creates and distributes an archive to your web servers,
    using the function deploy:
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['54.197.206.197', '18.214.88.47']


def do_pack():
    """
        A function that creates versions of updated static pages
        and gzip of the webstatic directory.
    """
    try:
        current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        zip_filename = "web_static_{}.tgz".format(current_datetime)
        archive_path = "versions/{}".format(zip_filename)
        local("tar -czvf {} web_static".format(archive_path))
        return archive_path

    except:
        return None


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


def deploy():
    """A function that creates and sends the archive to the server"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
