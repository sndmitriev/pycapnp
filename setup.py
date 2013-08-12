#!/usr/bin/env python
try:
    from Cython.Build import cythonize
    import Cython
except ImportError:
    raise RuntimeError('No cython installed. Please run `pip install cython`')

if Cython.__version__ < '0.19.1':
    raise RuntimeError('Old cython installed. Please run `pip install -U cython`')

from distutils.core import setup
import os

MAJOR = 0
MINOR = 2
MICRO = 0
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

def write_version_py(filename=None):
    cnt = """\
version = '%s'
short_version = '%s'
"""
    if not filename:
        filename = os.path.join(
            os.path.dirname(__file__), 'capnp', 'version.py')

    a = open(filename, 'w')
    try:
        a.write(cnt % (VERSION, VERSION))
    finally:
        a.close()

write_version_py()

setup(
    name="capnp",
    packages=["capnp"],
    version=VERSION,
    package_data={'capnp': ['*.pxd']},
    ext_modules=cythonize('capnp/*.pyx'),
    # PyPi info
    description="A cython wrapping of the C++ capnproto library",
    author="Jason Paryani",
    author_email="pypi-contact@jparyani.com",
    url = 'https://github.com/jparyani/capnpc-python-cpp',
    download_url = 'https://github.com/jparyani/capnpc-python-cpp/archive/v{}.zip'.format(VERSION),
    keywords = ['testing', 'logging', 'example'], # arbitrary keywords
    classifiers = [],
)