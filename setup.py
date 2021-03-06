#!/usr/bin/env python
from setuptools import setup, Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
from sys import version_info

d = { 'language_level' : version_info.major }

setup(
    name='SuchTree',
    version='0.5',
    description='A Python library for doing fast, thread-safe computations on phylogenetic trees.',
    url='http://github.com/ryneches/SuchTree',
    author='Russell Neches',
    author_email='ryneches@ucdavis.edu',
    license='BSD',
    packages=['SuchTree'],
    download_url='https://github.com/ryneches/SuchTree/archive/0.4.tar.gz',
    install_requires=[
        'scipy>=0.18',
        'numpy',
        'dendropy',
        'cython',
        'pandas',
    ],
    zip_safe=False,
    ext_modules = cythonize( [ "SuchTree/SuchTree.pyx" ], compiler_directives = d ),
    #test_suite = 'nose.collector',
    setup_requires = [ 'pytest-runner', ],
    tests_require = [ 'pytest', ],
)
