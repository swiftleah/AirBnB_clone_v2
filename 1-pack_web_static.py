#!/usr/bin/python3
""" function generates a .tgz archive from web_static folder """


from datetime import datetime
from fabric.api import *


def do_pack():
    """ generates .tgz archive """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    if result.succeeded:
        return filename
    else:
        return None
