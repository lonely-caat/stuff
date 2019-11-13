from setuptools import setup, find_packages

__version__ = '0.1a'

setup(
    version=__version__,
    packages=find_packages(),
    install_requires=['requests', 'selenium', 'pytest', 'configparser'],
)
