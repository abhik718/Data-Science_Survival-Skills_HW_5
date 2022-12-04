from distutils.core import setup
from setuptools import find_packages

setup(
    name="snowflake",
    version="5.0",
    author="Abhik",
    author_email="abhik.sarkar@fau.de",
    packages=find_packages(),
    install_requires=["numpy","turtles"],
)