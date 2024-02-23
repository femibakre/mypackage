from setuptools import setup, find_packages

setup(
    name= "mypackage",
    packages= find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Example Python Package',
    long_description=open('README.md').read(),
    install_requires= ['numpy'],
    url='https://github.com/femibakre/mypackage',
    author='Guy 1',
    author_email='guy1@yahoo.com'
)