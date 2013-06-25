#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='reddit_modcard',
      description='Moderator info cards for reddit',
      version='0.1',
      author='Andre D',
      author_email='andre@andred.ca',
      packages=find_packages(),
      install_requires=['r2'],
      entry_points={
          'r2.plugin':
          'modcard = reddit_modcard:Modcard'
      },
      include_package_data=True,
      zip_safe=False,
)
