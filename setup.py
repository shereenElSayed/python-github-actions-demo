import os
from setuptools import find_packages, setup

# read in README
this_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_dir, 'README.md'), 'rb') as f:
    long_description = f.read().decode().strip()

# requirements
install_requires = ["click", "flake8"]

setup(
    name = 'Hello-CS148',
    description = 'Demo application for github actions',
    author = 'Shereen Elsayed',
    author_email = 's_elsayed@ucsb.edu',

    packages = find_packages(),

    entry_points = {
        'console_scripts': [
            'CS148 = main:main',
        ],
    },

    python_requires = '>=3.6.*',
    install_requires = install_requires,
    setup_requires = ['setuptools_scm'],
    zip_safe=False,
    use_scm_version = {
        'write_to': '_version.py'
    },

    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX',
        'Operating System :: Unix',
    ],

)