# -*- coding: utf-8 -*-

#from zope.component import getMultiAdapter
from redturtle.video.tests.base import TestCase

class TestView(TestCase):

    def afterSetUp(self):
        self.setRoles(('Contributor', ))
        portal = self.portal
        portal.invokeFactory(type_name="File", id="atfile")
        f = getattr(portal, 'atfile')
        f.edit(title="Simple ATFile", file=self.getVideoFile())


    def test_getEmbedCode_accessible(self):
        # BBB: FAKE TESTS right now
        # seems that during tests the allowed_interface limitation are not taken
        self.portal.invokeFactory(type_name='RTInternalVideo', id='internal-video')
        video = getattr(self.portal, 'internal-video')
        video.edit(title='Internal Video', file=self.getVideoFile())
        #view = getMultiAdapter((video, self.portal.REQUEST), name='flowplayer')
        view = self.portal['internal-video'].restrictedTraverse('@@flowplayer')
        self.assertTrue(view.getEmbedCode())



def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestView))
    return suite
