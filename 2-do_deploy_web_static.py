#!/usr/bin/python3
"""Python Script(Fabric script) (based on the file 1-pack_web_static.py),
   Distributes an archive to the web servers, using the function do_deploy
Fabric deployment script for web_static
"""

import os
from datetime import datetime
from fabric.api import local, runs_once, env, put, run, task
from fabric.contrib import files
from os.path import exists, basename, splitext

# Enable SSH configuration and specify the hosts to connect to
env.use_ssh_config = True
env.hosts = ["52.201.220.59", "54.146.61.93"]

@runs_once
def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    d_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        d_time.year,
        d_time.month,
        d_time.day,
        d_time.hour,
        d_time.minute,
        d_time.second
    )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, size))
    except Exception:
        output = None
    return output

def do_deploy(archive_path):
    """
    Deploys the web_static archive to remote servers.
    Args:
        archive_path (str): Path of the archive file to deploy.
    Returns:
        bool: True if deployment succeeds, False otherwise.
    """
    try:
        # Check if the archive file exists
        if not exists(archive_path):
            return False

        # Extract the base name and extension of the archive file
        ext = basename(archive_path)
        no_ext, ext = splitext(ext)

        # Define the remote directory for web_static
        web_static_dir = "/data/web_static/releases/"

        # Upload the archive file to the remote /tmp directory
        put(archive_path, "/tmp/")

        # Define the list of commands to execute remotely
        commands = [
            "rm -rf {}{}/".format(web_static_dir, no_ext),
            "mkdir -p {}{}/".format(web_static_dir, no_ext),
            "tar -xzf /tmp/{} -C {}{}/".format(ext, web_static_dir, no_ext),
            "rm /tmp/{}".format(ext),
            "mv {0}{1}/web_static/* {0}{1}/".format(web_static_dir, no_ext),
            "rm -rf {}{}/web_static".format(web_static_dir, no_ext),
            "rm -rf /data/web_static/current",
            "ln -s {}{}/ /data/web_static/current".format(web_static_dir, no_ext),
        ]

        # Run the commands remotely
        for command in commands:
            run(command)

        print("New version deployed!")
        return True
    except Exception:
        return False
