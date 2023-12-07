#!/usr/bin/python3
""" based on task 2-creates and ditributes arhive to web servers with func """

from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """ creates and distributes an archive to your web servers """
    try:
        local("mkdir -p versions")
        timestr = datetime.now().strftime("%Y%m%d%H%M%S")
        path = "versions/web_static_{}.tgz".format(timestr)
        local("tar -cvzf {} web_static".format(path))
        return path
    except Exception as e:
        return None


def do_deploy(archive_path):
    """ distributes archive """
    if not os.path.exists(archive_path):
        return False

    try:
        filename = archive_path.split("/")[-1]
        path_no_ext = "/data/web_static/releases/{}".format(
            filename.replace(".tgz", ""))
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}".format(filename, path_no_ext))
        run("rm /tmp/{}".format(filename))
        run("mv {}/web_static/* {}".format(path_no_ext, path_no_ext))
        run("rm -rf {}/web_static".format(path_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path_no_ext))
        return True
    except Exception as e:
        return False


def deploy():
    """ full deployment """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)


if __name__ == "__main__":
    deploy()
