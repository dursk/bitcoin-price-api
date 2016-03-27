# Copyright (C) 2015 Bitquant Research Laboratories (Asia) Limited
# Released under the Simplified BSD License

from setuptools import (
    setup,
    find_packages,
)

setup(
    name='bitcoin-price-api',
    version = '0.0.4',
    author='Matthew Madurski',
    author_email='madurskimr@gmail.com',
    url='https://github.com/dursk/bitcoin-price-api',
    description="API's for bitcoin exchanges",
    long_description='''Price API's for bitcoin exchanges''',
    license='MIT',
    packages=['exchanges'],
    install_requires = ['requests', 'python-dateutil'],
    use_2to3 = True
)
