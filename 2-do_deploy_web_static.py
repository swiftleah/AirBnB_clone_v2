#!/usr/bin/python3
""" distributes arhive to web servers using func do_deploy """


from fabric.api import env, put, run, local
from os.path import exists
from datetime import datetime
from fabric.context_managers import cd


def do_deploy(archive_path):
    """ func """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        filename = archive_path.split('/')[-1]
        foldername = filename.split('.')[0]
        full_path = '/data/web_static/releases/{}'.format(foldername)
        run('mkdir -p {}'.format(full_path))
        with cd(full_path):
            run('tar -xzf /tmp/{} --strip-components=1'.format(filename))

        run('rm /tmp/{}'.format(filename))
        current_link = '/data/web_static/current'
        run('rm -rf {}'.format(current_link))
        run('ln -s {} {}'.format(full_path, current_link))

        print('New version deployed!')
        return True

    except Exception as e:
        return False


if __name__ == "__main__":
    archive_path = local("fab -f 1-pack_web_static.py do_pack", capture=True)
    archive_path = archive_path.split()[-1]

    result = do_deploy(archive_path)
    if result:
        print("Deployment successful!")
    else:
        print("Deployment failed.")
