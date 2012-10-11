# -*- coding: utf-8 -*-

import unittest
from redturtle.video.tests import base

from Products.CMFPlone.utils import getToolByName


class TestSetup(base.TestCase):

    def afterSetUp(self):
        self.qi = getToolByName(self.portal, 'portal_quickinstaller')

    def test_skin_installed(self):
        self.failUnless(self.qi.isProductInstalled('collective.flowplayer'))


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
