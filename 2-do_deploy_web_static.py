#!/usr/bin/python3
"""
a  script to deploy web_static to
my servers
"""

from fabric.api import run, env, put
import os.path

env.hosts = ['18.234.168.198', '35.168.2.70']
env.key_filename = '~/.ssh/school'
env.user = 'ubuntu'


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
