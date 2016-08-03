try:
    from setuptools import setup, find_packages
    from codecs import open
    from os import path
except importError:
    from distutils.core import setup


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='WindowsDNS server log parser',

    version='1.0',

    description='Windows server DNS log converter to Database',
    long_description=long_description,

    url='https://github.com/Abdullahaltuhami/Windows-server-dnslogParser',

    author='Abdullah AL-Tuhami & Faisal Q',

    license='MIT',

    classifiers=[
        # Project maturity
        'Development status :: 3 - alpha',

        'Intended Audience :: Developers & sysadmins',
        'Topic :: Cyber security :: Analysis Tools'
    ],

    install_requires=['MySQL-python', 'ez-setup']

)
