# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

version = '0.5.2'

tests_require=['zope.testing']

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
      install_requires=['setuptools',
                        'Plone',
                        'hachoir_core',
                        'hachoir_metadata',
                        'hachoir_parser',
                        'collective.flowplayer',
                        'plone.app.imaging>=1.0b9',
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'redturtle.video.tests.test_doctest.test_suite',
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
