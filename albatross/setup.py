import os
import warnings

import setuptools

dir_here = os.path.abspath(os.path.dirname(__file__))

# We strive to keep dependencies as flexible as possible, whilst avoiding depdency conflicts in breaking versions.
install_requires = [
    # We pin to exact versions here so we don't pickup breaking changes accidentally
    "Django==4.1.3",
    "black==22.3.0",
    "dataclasses",
    "pre-commit",
]


setuptools.setup(
    name="albatross",
    description="Albatross Planner",
    long_description="Plan your itinerary with Albatross",
    classifiers=[
        "Programming Language :: Python",
    ],
    author="Kevin Nguyen",
    author_email="kevinnguyen.sw@gmail.com",
    packages=setuptools.find_packages(
        exclude="tests",
    ),
    include_package_data=True,
    install_requires=install_requires,
)
