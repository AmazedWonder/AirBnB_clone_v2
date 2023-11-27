#!/usr/bin/python3
"""Python script(Fabric script) that defines a
   function called do_pack which is used to
   generate a .tgz archive of static files.
"""

from datetime import datetime
from fabric.api import *
from os.path import isdir
import os


def do_pack():
    """generates a tgz archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    if isdir("versions") is False:
        local("sudo mkdir -p versions")
    file_name = "versions/web_static_{}.tgz".format(date)
    try:
        #date = datetime.now().strftime("%Y%m%d%H%M%S")
        #if isdir("versions") is False:
            #local("sudo mkdir -p versions")
        #file_name = "versions/web_static_{}.tgz".format(date)
        print("Packing web_static to {}".format(file_name))
        local("sudo tar -cvzf {} web_static".format(file_name))
        size = os.stat(file_name).st_size
        print("web_static packed: {} -> {} Bytes".format(file_name, size))
        return file_name
    except:
        return None
