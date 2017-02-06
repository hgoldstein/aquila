#! /usr/bin/env python3

import os
import sys
import subprocess as sp

import scripts.setup as setup


def run(slides, local):
    setup.run(local)
    cmd = []
    cmd += ['docker', 'run']
    cmd += ['--env', 'SLIDES={}'.format(slides)]
    cmd += ['--privileged']
    cmd += ['-p', '8000:8000']
    cmd += ['-p', '35729:35729']
    cmd += ['-it']
    cmd += ['--volume', "{}:/slides/".format(slides)]
    cmd += [image_name(), '/run']
    sp.call(cmd)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: serve <path to presentation>")
        sys.exit(1)
    run(os.path.realpath(sys.argv[1]))
