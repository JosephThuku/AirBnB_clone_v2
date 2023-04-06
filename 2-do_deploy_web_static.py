#!/usr/bin/python3

from fabric.api import env, put, run, sudo
import os

#script to deploy webstatic on two servers
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
        sudo('mkdir -p /data/web_static/releases/{}'.format(archive_foldername))
        sudo('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_filename, archive_foldername))
        
        sudo('sudo rm -f /tmp/{}'.format(archive_filename))
        
        sudo('sudo rm -f /data/web_static/current')
        
        sudo('sudo ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(archive_foldername))

        print("New version deployed!")
        return True
    except:
        return False

