import unittest
from zope.testing import doctest
import redturtle.video.browser.videoembedcode

import zope.component
import redturtle.video.interfaces


def setUp(test):
    zope.component.provideAdapter(
            redturtle.video.browser.videoembedcode.VideoEmbedCode,
            (redturtle.video.interfaces.IRTRemoteVideo,
             zope.publisher.interfaces.browser.IHTTPRequest),
            provides=redturtle.video.interfaces.IVideoEmbedCode
        )

    zope.component.provideAdapter(
            redturtle.video.browser.videoembedcode.YoutubeEmbedCode,
            (redturtle.video.interfaces.IRTRemoteVideo,
             zope.publisher.interfaces.browser.IHTTPRequest),
            provides=redturtle.video.interfaces.IVideoEmbedCode,
            name='youtube.com'
        )

    zope.component.provideAdapter(
            redturtle.video.browser.videoembedcode.VimeoEmbedCode,
            (redturtle.video.interfaces.IRTRemoteVideo,
             zope.publisher.interfaces.browser.IHTTPRequest),
            provides=redturtle.video.interfaces.IVideoEmbedCode,
            name='vimeo.com'
        )


def test_suite():
    return unittest.TestSuite((
        doctest.DocTestSuite(redturtle.video.browser.videoembedcode,
                     setUp=setUp,
                     optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS,),
        ))
