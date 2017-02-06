#!/usr/bin/env python3

import os.path as path
import subprocess as sp

from scripts.config import image_name

DOCKER_PATH = path.join(path.dirname(path.realpath(__file__)), '..', 'docker')


def run(local=True):
    if local:
        sp.call(['docker', 'build', '-t', image_name(), DOCKER_PATH])
    else:
        sp.call(['docker', 'pull', 'huntergoldstein/aquila'])

if __name__ == "__main__":
    run()
