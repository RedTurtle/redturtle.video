# -*- coding: utf-8 -*-

from urlparse import urlparse
from zope.interface import implements
from redturtle.video.interfaces import IVideoEmbedCode
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

class VideoEmbedCode(object):
    """ VideoEmbedCode 
    provides a way to have a html code to embed video in a web page 

    >>> from zope.interface import implements
    >>> from redturtle.video.interfaces import IRTRemoteVideo
    >>> from redturtle.video.interfaces import IVideoEmbedCode
    >>> from zope.component import getMultiAdapter
    >>> from redturtle.video.tests.base import TestRequest

    >>> class RemoteVideo(object):
    ...     implements(IRTRemoteVideo)
    ...     remoteUrl = 'http://www.site.com/viedo.mpeg'
    ...     def getRemoteUrl(self):
    ...         return self.remoteUrl

    >>> remotevideo = RemoteVideo()
    >>> adapter = getMultiAdapter((remotevideo, TestRequest()), IVideoEmbedCode)
    >>> adapter.getVideoLink()
    'http://www.site.com/viedo.mpeg'

    """
    implements(IVideoEmbedCode)
    template = ViewPageTemplateFile('basevideoembedcode_template.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def getVideoLink(self):
        return self.context.getRemoteUrl()

    def getWidth(self):
        return self.context.getWidth()
    
    def getHeight(self):
        return self.context.getHeight()    

    def __call__(self):
        return self.template()


class MetacafeEmbedCode(VideoEmbedCode):
    """ MetacafeEmbedCode 
    provides a way to have a html code to embed Metacafe video in a web page 

    >>> from zope.interface import implements
    >>> from redturtle.video.interfaces import IRTRemoteVideo
    >>> from redturtle.video.interfaces import IVideoEmbedCode
    >>> from zope.component import getMultiAdapter
    >>> from redturtle.video.tests.base import TestRequest

    >>> class RemoteVideo(object):
    ...     implements(IRTRemoteVideo)
    ...     remoteUrl = 'http://www.metacafe.com/watch/4950343/stone_trailer/'
    ...     size = {'width': 440, 'height': 272}
    ...     def getRemoteUrl(self):
    ...         return self.remoteUrl
    ...     def getWidth(self):
    ...         return self.size['width']
    ...     def getHeight(self):
    ...         return self.size['height']

    >>> remotevideo = RemoteVideo()
    >>> adapter = getMultiAdapter((remotevideo, TestRequest()), 
    ...                                         IVideoEmbedCode, 
    ...                                         name = 'metacafe.com')
    >>> adapter.getVideoLink()
    'http://www.metacafe.com/fplayer/4950343/stone_trailer.swf'

    >>> print adapter()
    <embed id="VideoPlayback" width="440" height="272" allowfullscreen="true" allowscriptaccess="always" type="application/x-shockwave-flash" src="http://www.metacafe.com/fplayer/4950343/stone_trailer.swf" />...


    """
    template = ViewPageTemplateFile('metacafeembedcode_template.pt')

    def getVideoLink(self):
        qs = urlparse(self.context.getRemoteUrl())[2]
        p = qs.split('/') [2:4]  
        return 'http://www.metacafe.com/fplayer/%s/%s.swf' %(p[0],p[1])

 