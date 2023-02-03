'''
Copyright 2022 The Microsoft DeepSpeed Team
'''

from setuptools import setup, find_packages

install_requires = ["fake_mii", "pytest"]

setup(name="fake_ds",
      version="1.0",
      description='fake DS',
      install_requires=install_requires,
      packages=find_packages(),
      )

fake_val = 1e20
new_val = 100
