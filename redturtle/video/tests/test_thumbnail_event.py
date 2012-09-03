# -*- coding: utf-8 -*-

from zope.event import notify
from redturtle.video.tests.base import TestCase
from Products.Archetypes.event import ObjectInitializedEvent
import urllib2
import md5


class TestInitializedEvent(TestCase):

    def afterSetUp(self):
        self.setRoles(('Contributor', ))
        self.original_urlopen = urllib2.urlopen
        urllib2.urlopen = self.custom_urlopen
        self.image1, self.image2 = self.get_images()

    def tearDown(self):
        urllib2.urlopen = self.original_urlopen

    def test_no_image_provided(self):
        """
        what's if no image is provided by user?
        """
        self.portal.invokeFactory(type_name="RTRemoteVideo",
                                  id="remote-video-file")
        f = getattr(self.portal, 'remote-video-file')
        f.edit(title="A remote file",
               remoteUrl="http://foo.com/foo")
        notify(ObjectInitializedEvent(f))
        plone_italia_png = md5.new(self.image1.read()).digest()
        img_from_video = md5.new(f.getImage().data).digest()
        self.assertEqual(plone_italia_png, img_from_video)

    def test_image_provided(self):
        self.portal.invokeFactory(type_name="RTRemoteVideo",
                                  id="other-remote-video-file")
        f = getattr(self.portal, 'other-remote-video-file')
        f.edit(title="Another remote file",
               remoteUrl="http://foo.com/foo",
               image=self.image2.read(),
              )

        self.image2.seek(0)
        notify(ObjectInitializedEvent(f))
        plone_italia_png = md5.new(self.image1.read()).digest()
        plone_logo_png = md5.new(self.image2.read()).digest()
        img_from_video = md5.new(f.getImage().data).digest()
        self.assertNotEqual(plone_italia_png, img_from_video)
        self.assertEqual(plone_logo_png, img_from_video)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestInitializedEvent))
    return suite
