import os
from setuptools import setup

ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

setup(
    name='htmlpad',
    version='0.1dev',
    packages=['htmlpad'],
    author="Atul Varma",
    author_email="atul@mozilla.com",
    install_requires=open(path('requirements.txt')).read(),
)