#!/usr/bin/python3

"""
    A python module that utilizes fabric to create gzip
    of specified directory.
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


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
        print("An error occurred while creating the archive.")
        return None
