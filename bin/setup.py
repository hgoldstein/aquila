#!/usr/bin/env python3

import os.path as path
import subprocess as sp

DOCKER_PATH = path.join(path.dirname(path.realpath(__file__)), '..', 'docker')


def setup():
    sp.call(['docker', 'build', '-t', 'aquilia', DOCKER_PATH])

if __name__ == "__main__":
    setup()
