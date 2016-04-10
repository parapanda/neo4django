# coding=utf-8
from setuptools import setup

setup(
    name='neo4django',
    version='0.2.0',
    author='Stephen Pandich',
    author_email='pandich@gmail.com',
    description='A Django/Neo4j ORM layer.',
    license='GPL',
    url="https://neo4django.readthedocs.org/en/latest/",
    packages=[
        'neo4django',
        'neo4django.graph_auth',
        'neo4django.db',
        'neo4django.db.models',
        'neo4django.tests',
        'neo4django.gremlin',
        'neo4django.admin',
        'neo4django.admin.templatetags',
        'neo4django.contenttypes',
    ],
    package_dir={
        'neo4django': 'neo4django',
    },
    package_data={
        'neo4django': ['gremlin/*.groovy'],
    },
    long_description=open('README.md').read(),
    platforms=['posix'],
    install_requires=[
        'httplib2 >= 0.9',
        'Django >= 1.9',
        'decorator >= 4',
        'python - dateutil >= 2.5',
        'lucene - querybuilder >= 0.2',
        'neo4jrestclient >= 2',
    ],
    tests_require=[
        'nose >= 1.3.0',
        'nose - regression >= 1.0',
        'requests >= 2.9',
        'lxml >= 3.6',
        'mock >= 2',
        'pretend >= 1.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX',
    ],
)
