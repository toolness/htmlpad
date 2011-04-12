#!/usr/bin/env python

import subprocess
import sys
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

def bootstrap():
    vdir = path('.virtualenv')
    if not os.path.exists(vdir):
        subprocess.check_call([sys.executable, path('dev', 'virtualenv.py'),
                               vdir])
    requirements = path('requirements.txt')
    req_contents = open(requirements, 'r').read()
    last_requirements = path(vdir, 'requirements.txt')
    last_req_contents = ''
    if os.path.exists(last_requirements):
        last_req_contents = open(last_requirements, 'r').read()
    if req_contents != last_req_contents:
        pip = path(vdir, 'bin', 'pip')
        subprocess.check_call([pip, 'install', '-r', requirements])
        open(last_requirements, 'w').write(req_contents)
    activate_this = path(vdir, 'bin', 'activate_this.py')
    execfile(activate_this, dict(__file__=activate_this))

bootstrap()

from django.core.management import execute_manager
import dev.settings

if __name__ == "__main__":
    execute_manager(dev.settings)
