# Copyright 2010-2012 RethinkDB, all rights reserved.
from setuptools import setup

setup(name="rethinkdbold"
     ,version="1.5.0-0"
     ,description="This package provides the Python driver library for the RethinkDB database server."
     ,url="http://rethinkdb.com"
     ,maintainer="RethinkDB Inc."
     ,maintainer_email="bugs@rethinkdb.com"
     ,packages=['rethinkdbold']
     ,install_requires=['protobuf']
)
