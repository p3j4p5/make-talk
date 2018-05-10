import os
from setuptools import setup

PACKAGE_NAME = 'make_talk'

DATA_SOURCE = 'share'

DATA_FILES = [
    (os.path.join(PACKAGE_NAME, top), [os.path.join(top, f) for f in files])
    for top, dirs, files in os.walk(DATA_SOURCE)
]

setup(
    name=PACKAGE_NAME,
    version='0.0.1',
    description='Creates a skelton for and manges a LaTeX Beamer presentation',
    ntry_points={
        'console_scripts': [
            'make-talk = %s.shell:main' % PACKAGE_NAME
        ]
    },
    data_files=DATA_FILES,
)
