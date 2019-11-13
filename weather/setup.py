from setuptools import setup, find_packages

__version__ = '0.1a'

setup(
    name='ltf-limon',
    version=__version__,
    packages=find_packages(),
    install_requires=['selenium', 'pytest', 'configparser'],
    namespace_packages=['ltf'],
)
