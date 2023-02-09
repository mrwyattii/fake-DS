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

def public_func():
    for i in range(3):
        print("doing work...")

def public_func_2():
    pass
