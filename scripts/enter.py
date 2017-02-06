#! /usr/bin/env python3

import os
import sys
import subprocess as sp
import scripts.setup as setup
from scripts.config import image_name

def run(slides, local):
    setup.run(local)
    cmd = []
    cmd += ['docker', 'run']
    cmd += ['--privileged']
    cmd += ['-p', '8000:8000']
    cmd += ['-p', '35729']
    cmd += ['-it']
    cmd += ['--volume', "{}:/slides/".format(slides)]
    cmd += [image_name(), '/enter']
    sp.call(cmd)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: enter <path to presentation>")
        sys.exit(1)
    run(os.path.realpath(sys.argv[1]))
