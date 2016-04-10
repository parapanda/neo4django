# coding=utf-8
from setuptools import setup

setup(
    name='neo4django2',
    version='1.0.0b1',
    description='A Django/Neo4j ORM layer.',
    long_description=open('README.rst').read(),
    url="https://github.com/parapanda/neo4django2",

    author='Stephen Pandich',
    author_email='pandich@gmail.com',

    license='GPLv3',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='django neo4j',

    packages=[
        'neo4django2',
        'neo4django2.graph_auth',
        'neo4django2.db',
        'neo4django2.db.models',
        'neo4django2.tests',
        'neo4django2.gremlin',
        'neo4django2.admin',
        'neo4django2.admin.templatetags',
        'neo4django2.contenttypes',
    ],

    install_requires=[
        'httplib2>=0.9',
        'Django>=1.9',
        'decorator>=4',
        'python-dateutil>=2.5',
        'lucene-querybuilder>=0.2',
        'neo4jrestclient>=2',
    ],

    package_data={
        'neo4django2': ['gremlin/*.groovy'],
    },

)


def bdist_wheel():
    pass
