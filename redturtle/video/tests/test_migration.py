# -*- coding: utf-8 -*-

from zope.event import notify
from redturtle.video.tests.base import TestCase
from Products.Archetypes.event import ObjectInitializedEvent

from redturtle.video.migrator import migrateFlowplayerToRedTurtleVideo

class TestView(TestCase):

    def afterSetUp(self):
        self.setRoles(('Contributor', ))
        portal = self.portal
        portal.invokeFactory(type_name="File", id="one-atfile")
        portal.invokeFactory(type_name="Folder", id="folder")
        portal.folder.invokeFactory(type_name="File", id="another-atfile")
        f = getattr(portal, 'one-atfile')
        f.edit(title="A simple ATFile", file=self.getVideoFile())
        f.setFilename('1-2-3.mp4')
        notify(ObjectInitializedEvent(self.portal['one-atfile']))
        f = getattr(portal.folder, 'another-atfile')
        f.edit(title="Another simple ATFile", file=self.getVideoFile())
        f.setFilename('1-2-3.mp4')
        notify(ObjectInitializedEvent(self.portal.folder['another-atfile']))


    def test_siteMigration(self):
        output = migrateFlowplayerToRedTurtleVideo(self.portal)
        self.assertEqual(output,
                         ['Migrating /plone/one-atfile (File -> RTInternalVideo)',
                          'Migrating /plone/folder/another-atfile (File -> RTInternalVideo)'])


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestView))
    return suite
