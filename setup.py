from setuptools import find_packages, setup

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='IFCDataLib',
    package_dir={"": "src"},
    packages=find_packages(),
    version='0.0.1',
    description='Librería IFC que te ayuda a procesar datos IFC',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Ángel Torada',
    license='MIT',
    include_package_data=True,
)