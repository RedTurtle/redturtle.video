# -*- coding: utf-8 -*-

import os, sys
from setuptools import setup, find_packages

version = '0.7.0'

tests_require=['zope.testing']

install_requires = ['setuptools',
                    'hachoir_core',
                    'hachoir_metadata',
                    'hachoir_parser',
                    'collective.flowplayer',
                    'plone.app.imaging>=1.0b9',
                    ]

# what I read there seems not working propery for Plone 3.3
# http://plone.org/documentation/manual/upgrade-guide/version/upgrading-plone-4.0-to-4.1/referencemanual-all-pages
if sys.version_info < (2, 6):
    install_requires.append('Plone')
else:
    install_requires.append('Products.CMFPlone')

setup(name='redturtle.video',
      version=version,
      description="Basic video contents (site's internal and remote) for Plone; "
                  "use collective.flowplayer but also pluggable with external services",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Multimedia :: Video',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='plone video flowplayer plonegov',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.net',
      url='http://plone.org/products/redturtle.video',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['redturtle', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'redturtle.video.tests.test_doctest.test_suite',
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
