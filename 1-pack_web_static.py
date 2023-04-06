#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the
# contents of the web_static folder
# return the path if the .tgz is created
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generate a .tgz archive from contents of web_static folder
    """
    current_time = datetime.now().strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        tgz_path = "versions/web_static_{}.tgz".format(current_time)
        local("tar -cvzf {} web_static/".format(tgz_path))
        return tgz_path
    except Exception:
        return None
