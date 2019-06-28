#!/usr/bin/env python3
# coding: utf-8

from setuptools import setup, find_packages

install_requires = [
    # IPython,
    'selenium',
    'beautifulsoup4',
    'scrapy',
    'Flask==1.0.2',
    'Flask-WTF',
    'pytest',
    'flask-login',
    'Flask-SQLAlchemy',
    'flask-bcrypt',
    'flask-mail',
    'PyPDF2',
    'Pillow',
    'pdf2image',
    'pyvirtualdisplay'

]

setup(
    name='sultan',
    version='0.0.1',
    python_requires='>=3.6',
    packages=find_packages(),
    author='AlexandreGazagnes',
    author_email='a_syoez@yahoo.fr',
    description='job search ultimate automated solution',
    long_description='See [here](https://github.com/XXXXXXX) for complete user guide.',
    url='https://github.com/XXXXXXX',
    install_requires=install_requires,
    license='XXXXXX',
)
