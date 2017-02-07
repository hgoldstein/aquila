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
    cmd += [image_name(), '/zip']
    child = sp.Popen(cmd, stdout=sp.PIPE)
    (out, _) = child.communicate()
    if len(out) == 0:
        return False
    with open(os.path.join(slides, 'pres.zip'), 'wb') as f:
        f.write(out)
    return True
