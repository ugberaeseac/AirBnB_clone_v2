#!/usr/bin/python3
"""
Fabric script to deploy archive to web servers
Returns True if successful otherwise returns False
"""


from fabric.api import *
import os
env.hosts = ['54.242.177.175', '52.91.148.117']


def do_deploy(archive_path):
    """
    deploy archive to web server
    """

    if not os.path.exists(archive_path):
        return False

    try:
        fileName = archive_path.split("/")[-1]
        noExtension = fileName.split(".")[0]
        filePath = "/data/web_static/releases/{}/".format(noExtension)
        print("Deploying archive to webservers...")
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(filePath))
        run("tar -xzf /tmp/{} -C {}".format(fileName, filePath))
        run("rm /tmp/{}".format(fileName))
        symLink = "/data/web_static/current"
        run("rm -rf {}".format(symLink))
        run("mv {}web_static/* {}".format(filePath, filePath))
        run("rm -rf {}web_static".format(filePath))
        run("ln -sf {} {}".format(filePath, symLink))
        return True
    except Exception:
        return False
