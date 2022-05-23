#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """create a pack versions"""
    local("mkdir -p versions")
    datime = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(datime)
    local("tar -cvzf {} web_static".format(file))
    if file:
        return(file)
    else:
        return (None)
