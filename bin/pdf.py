#!/usr/bin/env python3

import os
import sys
import subprocess as sp

import setup


def pdf(slides):
    setup.setup()
    cmd = []
    cmd += ['docker', 'run']
    cmd += ['--privileged']
    # We only have the interactive flag here as we are transferring data over
    # STDOUT
    cmd += ['-i']
    cmd += ['--volume', "{}:/slides/".format(slides)]
    cmd += ['aquilia', '/pdf']
    child = sp.Popen(cmd, stdout=sp.PIPE)
    (out, _) = child.communicate()
    if len(out) == 0:
        print("Failed to create PDF")
        return False
    with open(os.path.join(slides, 'index.pdf'), 'wb') as f:
        f.write(out)
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: enter <path to presentation>")
        sys.exit(1)
    success = pdf(os.path.realpath(sys.argv[1]))
    sys.exit(success)
