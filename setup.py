from setuptools import setup, find_packages
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

import os
import uuid

# parse_requirements() returns generator of pip.req.InstallRequirement objects
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
reqs_file = os.path.join(BASE_DIR, 'requirements.txt')
install_reqs = parse_requirements(reqs_file, session=uuid.uuid1())

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(
    # Application name:
    name="datatools",

    # Version number (initial):
    version="0.2.0",

    # Application author details:
    author="Xu Cheng",
    author_email="bd66_6@hotmail.com",

    # Packages
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),

    # Include additional files into the package
    include_package_data=True,

    # Details
    # url="http://pypi.abc.com/pypi/datatools_v010",

    #
    # license="LICENSE.txt",
    description="Simple ETL Data Tools",

    long_description=open("README.md").read(),

    # Dependent packages (distributions)
    install_requires=reqs,
)
