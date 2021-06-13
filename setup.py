from distutils.core import setup

from setuptools import find_packages

setup(
    name='furry-robot',
    version='0.1.0',
    author="Aditya Misra",
    author_email='amisra14@yahoo.co.uk',
    packages=find_packages(),
    long_description=open('README.md').read(),
    python_requires=">=3.7",
)