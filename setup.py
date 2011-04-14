# -*- coding: utf-8 -*-
"""
This module contains the tool of redturtle.video
"""
import os
from setuptools import setup, find_packages

version = '0.4.0'

tests_require=['zope.testing']

setup(name='redturtle.video',
      version=version,
      description="Basic video contents for Plone, with collective.flowplayer integration",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Development Status :: 4 - Beta',
        'Topic :: Multimedia :: Video',
        'Topic :: Software Development :: Libraries :: Python Modules',
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
      install_requires=['Plone',
                        'setuptools',
                        'hachoir_core',
                        'hachoir_metadata',
                        'hachoir_parser',
                        'collective.flowplayer',
                        'plone.app.imaging',
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
