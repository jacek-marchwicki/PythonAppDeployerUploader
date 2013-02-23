#! /usr/bin/env python
# -*- coding: utf-8 -*-
#   Copyright 2013 Jacek Marchwicki <jacek.marchwicki@gmail.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from setuptools import setup, find_packages
setup(
  name = "app_deployer_uploader",
  version = "0.0.1",
  author = "Jacek Marchwicki",
  author_email = "jacek.marchwicki@gmail.com",
  packages = ["app_deployer_uploader"],
  license = "Apache 2.0",
  entry_points = {
    "console_scripts": [
      'app-deployer-uploader = app_deployer_uploader.upload:main',
    ]
  },
  long_description=open('README.txt').read(),
  install_requires=[
    "requests >= 1.1.0",
  ],
  classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Environment :: Console",
    "Programming Language :: Python",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: Apache Software License",
  ],
)
