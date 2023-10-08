#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
files in the directory web_static added to create .tgz file
archives must be stored in the directory versions
name of archive: web_static_<year><month><day><hour><minute><second>.tgz
return the archive path if success else return None
"""


from fabric.api import *
from time import strftime


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
