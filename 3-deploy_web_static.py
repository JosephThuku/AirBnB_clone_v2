#!/usr/bin/python3
"""
script to pack and deploy archive
"""
import os
from fabric.api import env, put, run
from datetime import datetime

env.hosts = ['18.234.168.198', '35.168.2.70']
env.user = 'ubuntu'
env.file_name = '~/.ssh/school'


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


def do_deploy(archive_path):
    """
    upload and decompress the archive_file
    """

    if not os.path.isfile(archive_path):
        return False
    compressed_file = archive_path.split("/")[-1]
    remove_extension = compressed_file.split(".")[0]

    try:
        uncompress_to = "/data/web_static/releases/{}/".format(
                remove_extension)
        sym_link = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(uncompress_to))
        run("sudo tar -xvzf /tmp/{} -C {}".format(compressed_file,
            uncompresss_to))
        run("sudo rm /tmp/{}".format(compressed_file))
        run("sudo mv {}/web_static/* {}".format(uncompress_to, uncompress_to))
        run("sudo rm -rf {}/web_static".format(uncompress_to))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {} {}".format(uncompress_to, sym_link))
        return True
    except Exception as e:
        return False


def deploy():
    """
    Create and distribute the archive to the web servers
    """
    path = do_pack()
    if not path:
        return False
    return do_deploy(path)
