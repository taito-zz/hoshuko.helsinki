from setuptools import find_packages
from setuptools import setup


setup(
    name='hoshuko.helsinki',
    version='0.2',
    description="Helsinki Hoshuko Policy",
    long_description='',
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@abita.fi',
    url='http://helsinki.hoshuko.info/',
    license='Non-free',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['hoshuko'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Products.Maps',
        'hexagonit.testing',
        'plonetheme.terrafirma',
        'setuptools',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
