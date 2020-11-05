#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path
import sys

here = path.abspath(path.dirname(__file__))

long_description = """"
# Pipeline for extracellular electrophysiology using Neuropixels probe and kilosort clustering method

Build a full ephys pipeline using the canonical pipeline modules
+ [lab-management](https://github.com/vathes/canonical-lab-management)
+ [colony-management](https://github.com/vathes/canonical-colony-management)
+ [ephys](https://github.com/vathes/canonical-ephys)
"""

with open(path.join(here, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

setup(
    name='canonical-full-ephys-pipeline',
    version='0.0.1',
    description="Extracellular electrophysiology pipeline using the DataJoint canonical pipeline modules",
    long_description=long_description,
    author='DataJoint NEURO',
    author_email='info@vathes.com',
    license='MIT',
    url='https://github.com/vathes/canonical-full-ephys-pipeline',
    keywords='neuroscience datajoint ephys',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=requirements,
)
