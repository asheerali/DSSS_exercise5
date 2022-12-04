from distutils.core import setup
from setuptools import find_packages

setup(
    name = "snowflake",
    version="1.0",
    author="asheerali",
    author_email="asheerali1997@gmail.com",
    packages=find_packages(),
    install_requires=["numpy", "turtles"]
)