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


class VimeoEmbedCode(VideoEmbedCode):
    """ VimeoEmbedCode 
    provides a way to have a html code to embed Vimeo video in a web page 

    >>> from zope.interface import implements
    >>> from redturtle.video.interfaces import IRTRemoteVideo
    >>> from redturtle.video.interfaces import IVideoEmbedCode
    >>> from zope.component import getMultiAdapter
    >>> from redturtle.video.tests.base import TestRequest

    >>> class RemoteVideo(object):
    ...     implements(IRTRemoteVideo)
    ...     remoteUrl = 'http://vimeo.com/2075738'
    ...     size = {'width': 400, 'height': 225}
    ...     def getRemoteUrl(self):
    ...         return self.remoteUrl
    ...     def getWidth(self):
    ...         return self.size['width']
    ...     def getHeight(self):
    ...         return self.size['height']

    >>> remotevideo = RemoteVideo()
    >>> adapter = getMultiAdapter((remotevideo, TestRequest()), 
    ...                                         IVideoEmbedCode, 
    ...                                         name = 'vimeo.com')
    >>> adapter.getVideoLink()
    'http://vimeo.com/moogaloop.swf?clip_id=2075738&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=1&amp;show_portrait=0&amp;color=&amp;fullscreen=1'

    >>> print adapter()
    <object width="400" height="225">
       <param name="allowfullscreen" value="true" />
       <param name="allowscriptaccess" value="always" />
       <param name="movie" value="http://vimeo.com/moogaloop.swf?clip_id=2075738&amp;amp;server=vimeo.com&amp;amp;show_title=1&amp;amp;show_byline=1&amp;amp;show_portrait=0&amp;amp;color=&amp;amp;fullscreen=1" />
       <embed type="application/x-shockwave-flash" allowfullscreen="true" allowscriptaccess="always" width="400" height="225" src="http://vimeo.com/moogaloop.swf?clip_id=2075738&amp;amp;server=vimeo.com&amp;amp;show_title=1&amp;amp;show_byline=1&amp;amp;show_portrait=0&amp;amp;color=&amp;amp;fullscreen=1"></embed>
    </object>
    <BLANKLINE>

    """
    template = ViewPageTemplateFile('vimeoembedcode_template.pt')

    def getVideoLink(self):
        video_id = urlparse(self.context.getRemoteUrl())[2][1:]
        return "http://vimeo.com/moogaloop.swf?clip_id=%s&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=1&amp;show_portrait=0&amp;color=&amp;fullscreen=1" % video_id


class MetacafeEmbedCode(VimeoEmbedCode):
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

 