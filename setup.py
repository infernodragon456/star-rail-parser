
from setuptools import setup, find_packages


from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="star-rail-parser",
    version="0.1.0",
    description="Python library to parse Honkai: Star Rail user data with the mihomo API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="Vighnesh Mandavkar",
    author_email="vighnesh_mandavkar@outlook.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["star_rail_parser"],
    include_package_data=True,
    install_requires=["requests"]
)