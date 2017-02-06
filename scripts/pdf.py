#!/usr/bin/env python3

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
    # We only have the interactive flag here as we are transferring data over
    # STDOUT
    cmd += ['-i']
    cmd += ['--volume', "{}:/slides/".format(slides)]
    cmd += [image_name(), '/pdf']
    child = sp.Popen(cmd, stdout=sp.PIPE)
    (out, _) = child.communicate()
    if len(out) == 0:
        return False
    with open(os.path.join(slides, 'index.pdf'), 'wb') as f:
        f.write(out)
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: enter <path to presentation>")
        sys.exit(1)
    success = run(os.path.realpath(sys.argv[1]), True)
    sys.exit(success)
