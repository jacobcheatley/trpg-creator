from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    readme = f.read()

with open(path.join(here, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

setup(
    name='trpgcreator',
    version='0.1.0',
    description='GUI creator for generating custom campaigns for TRPG.',
    long_description=readme,
    url='https://github.com/jacobcheatley/trpg-creator',
    author='Jacob Cheatley',
    author_email='jacobcheatley@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Gamers and Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5'
    ],
    keywords='text roleplaying game engine',
    packages=find_packages(exclude=['ui_files']),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'trpgcreator=trpgcreator.__main__:main'
        ]
    }
)