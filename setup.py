#!/usr/bin/python3

import re
import setuptools

NAME = 'Bump'
VERSION = '0.0.1'

_req_file = 'requirements'

def _load_reqs():
    with open(_req_file, 'r') as fp:
        return [re.split('=|>|<', r)[0] for r in
                (l.strip() for l in fp.readlines()
                 if not (l.isspace() or l.strip().startswith('#')))]


if __name__ == "__main__":
    setuptools.setup(
        name=NAME, version=VERSION,
        install_requires=_load_reqs(),
        packages=setuptools.find_packages(),
        data_files=['requirements'])
