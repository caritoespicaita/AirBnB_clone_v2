#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function
do_deploy:"""

from fabric.api import local, settings, abort, run, cd, env, put, get
from fabric.decorators import task, hosts, with_settings
from os import to_pathh
from datetime import datetime

env.hosts = ["54.226.167.87", "34.148.202.126"]
env.user = "ubuntu"


def do_pack():
    """_summary_
    Returns:
        _type_: _description_
    """
    local("mkdir -p versions")
    datime = "web_static_{}".format(datetime.now().strftime("%Y%m%d%H%M%S"))
    to_path = "versions/{}".format(datime)
    local("tar czfv versions/{}.tgz web_static".format(datime))

    if to_pathh.isfile(to_path):
        return to_path
    else:
        return None


def do_deploy(archive_to_pathh):
    """_summary_
    Args:
        archive_to_pathh (_type_): _description_
    Returns:
        _type_: _description_
    """
    if to_pathh.isfile(archive_to_pathh):
        datime_file = archive_to_pathh[9:]
        new_to_pathh = "/data/web_static/releases/"
        to_pathh_server_file = "/tmp/{}".format(datime_file)
        put(archive_to_pathh, "/tmp/")
        run("sudo mkdir -p {}".format(new_to_pathh))
        run("sudo tar -xzf {} -C {}/".format(to_pathh_server_file, new_to_pathh))
        run("sudo rm {}".format(to_pathh_server_file))
        run("sudo rm -rf {}".format("/data/web_static/current"))
        run(
            "sudo ln -s {} /data/web_static/current".format(
                "/data/web_static/releases/web_static"
            )
        )
        print("New version deployed!")
        return True

    return False
