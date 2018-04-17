from setuptools import setup


setup(
    name='make-talk',
    version='0.0.1',
    description='Creates a skelton for and manges a LaTeX Beamer presentation',
    install_requires=['jinja2'],
    entry_points={
        'console_scripts': [
            'make-talk = make_talk.shell:main'
        ]
    }
)
