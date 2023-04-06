#!/usr/bin/python3
"""
script to upload web static
"""
from fabric.api import env, put, run, sudo
import os

env.hosts = ['18.234.168.198', '35.168.2.70']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        
        archive_filename = os.path.basename(archive_path)
        archive_foldername = archive_filename.split('.')[0]
        run('mkdir -p /data/web_static/releases/{}'.format(archive_foldername))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_filename, archive_foldername))
        
        run('rm /tmp/{}'.format(archive_filename))
        run('sudo rm -f /data/web_static/current')
        
        run('sudo ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(archive_foldername))

        print("New version deployed!")
        return True
    except:
        return False

