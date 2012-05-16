# -*- coding: utf-8 -*-

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

