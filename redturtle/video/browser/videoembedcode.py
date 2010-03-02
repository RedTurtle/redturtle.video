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
    >>> print getMultiAdapter((remotevideo, TestRequest()), IVideoEmbedCode)()
    <a href="http://www.site.com/viedo.mpeg">http://www.site.com/viedo.mpeg</a>

    """
    implements(IVideoEmbedCode)
    template = ViewPageTemplateFile('basevideoembedcode_template.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def getVideoLink(self):
        pass

    def __call__(self):
        return self.template()

class YoutubeEmbedCode(object):
    """ YoutubeEmbedCode 
    provides a way to have a html code to embed Youtube video in a web page 

    >>> from zope.interface import implements
    >>> from redturtle.video.interfaces import IRTRemoteVideo
    >>> from redturtle.video.interfaces import IVideoEmbedCode
    >>> from zope.component import getMultiAdapter
    >>> from redturtle.video.tests.base import TestRequest

    >>> class RemoteVideo(object):
    ...     implements(IRTRemoteVideo)
    ...     remoteUrl = 'http://www.youtube.com/watch?v=s43WGi_QZEE&feature=related'
    ...     def getRemoteUrl(self):
    ...         return self.remoteUrl

    >>> remotevideo = RemoteVideo()
    >>> adapter = getMultiAdapter((remotevideo, TestRequest()), 
    ...                                         IVideoEmbedCode, 
    ...                                         name = 'youtube.com')
    >>> adapter.getVideoLink()
    'http://www.youtube.com/v/s43WGi_QZEE'

    >>> print adapter()
    <object width="425" height="344">
      <param name="movie"
             value="http://www.youtube.com/v/s43WGi_QZEE" />
      <param name="allowFullScreen" value="true" />
      <param name="allowscriptaccess" value="always" />
      <embed src="http://www.youtube.com/v/s43WGi_QZEE"
             type="application/x-shockwave-flash"
             allowscriptaccess="always" allowfullscreen="true"
             width="425" height="344"></embed>
    </object>
    <BLANKLINE>

    """
    implements(IVideoEmbedCode)
    template = ViewPageTemplateFile('youtubeembedcode_template.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def getVideoLink(self):
        qs = urlparse(self.context.getRemoteUrl())[4]
        params = qs.split('&')
        for param in params:
            k, v = param.split('=')
            if k == 'v':
                return 'http://www.youtube.com/v/%s' % v

    def __call__(self):
        return self.template()


class VimeoEmbedCode(object):
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
    ...     def getRemoteUrl(self):
    ...         return self.remoteUrl

    >>> remotevideo = RemoteVideo()
    >>> adapter = getMultiAdapter((remotevideo, TestRequest()), 
    ...                                         IVideoEmbedCode, 
    ...                                         name = 'vimeo.com')
    >>> adapter.getVideoLink()
    'http://vimeo.com/moogaloop.swf?clip_id=2075738&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=1&amp;show_portrait=0&amp;color=&amp;fullscreen=1'

    >>> print adapter()
    <object width="425" height="344">
      <param name="movie"
             value="http://vimeo.com/moogaloop.swf?clip_id=2075738&amp;amp;server=vimeo.com&amp;amp;show_title=1&amp;amp;show_byline=1&amp;amp;show_portrait=0&amp;amp;color=&amp;amp;fullscreen=1" />
      <param name="allowFullScreen" value="true" />
      <param name="allowscriptaccess" value="always" />
      <embed src="http://vimeo.com/moogaloop.swf?clip_id=2075738&amp;amp;server=vimeo.com&amp;amp;show_title=1&amp;amp;show_byline=1&amp;amp;show_portrait=0&amp;amp;color=&amp;amp;fullscreen=1"
             type="application/x-shockwave-flash"
             allowscriptaccess="always" allowfullscreen="true"
             width="425" height="344"></embed>
    </object>
    <BLANKLINE>



    """
    implements(IVideoEmbedCode)
    template = ViewPageTemplateFile('youtubeembedcode_template.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def getVideoLink(self):
        video_id = urlparse(self.context.getRemoteUrl())[2][1:]
        return "http://vimeo.com/moogaloop.swf?clip_id=%s&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=1&amp;show_portrait=0&amp;color=&amp;fullscreen=1" % video_id


    def __call__(self):
        return self.template()
