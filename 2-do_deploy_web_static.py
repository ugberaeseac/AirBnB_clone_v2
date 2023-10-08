#!/usr/bin/python3

"""
Fabric script to deploy archive to web servers
Returns True if successful otherwise returns False
"""


from fabric.api import *
import os
from time import strftime
env.hosts = ['54.242.177.175', '52.91.148.117']


def do_pack():
    """
    generate a .tgz archive
    """
    now = strftime("%Y%M%d%H%M%S")
    local('mkdir -p versions/')
    path = "versions/web_static_{}.tgz".format(now)
    print("Generating archive...")
    result = local('tar -zvcf {} web_static/'.format(path))

    if result.succeeded:
        return path
    else:
        return None

"""
def do_deploy(archive_path):
    '''
    deploy archive to web server
    '''

    if not os.path.exists(archive_path):
        return False

    try:
        fileName = archive_path.split("/")[-1]
        noExtension = fileName.split(".")[0]
        filePath = "/data/web_static/releases/{}/".format(noExtension)
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(filePath))
        run("tar -xzf /tmp/{} -C {}".format(fileName, filePath))
        run("rm /tmp/{}".format(fileName))
        run("mv {}web_static/* {}".format(filePath, filePath))
        run("rm -rf {}web_static".format(filePath))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(filePath))
        print("New version deployed!")
        return True
    except Exception:
        return False
"""

def do_deploy(archive_path):
    """
    Deploy archive to web servers
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        filename = archive_path.split("/")[-1]
        no_ext = filename.split(".")[0]
        path_no_ext = "/data/web_static/releases/{}/".format(no_ext)
        symlink = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}".format(filename, path_no_ext))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(path_no_ext, path_no_ext))
        run("rm -rf {}web_static".format(path_no_ext))
        run("rm -rf {}".format(symlink))
        run("ln -s {} {}".format(path_no_ext, symlink))
        return True
    except:
        return False
