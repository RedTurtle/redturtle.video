import unittest
from redturtle.video.tests import base

from Products.CMFPlone.utils import getToolByName


class TestSetup(base.TestCase):

    def afterSetUp(self):
        self.qi = getToolByName(self.portal, 'portal_quickinstaller')

    def test_skin_installed(self):
        self.failUnless(self.qi.isProductInstalled('collective.flowplayer'))

    def test_catalogindexes(self):
        catalog_indexes = self.portal.portal_catalog.indexes()
        self.failUnless("hasSplashScreenImage" in catalog_indexes)
        self.failUnless("getYear" in catalog_indexes)
        self.failUnless("getDuration" in catalog_indexes)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
