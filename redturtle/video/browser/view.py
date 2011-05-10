# -*- coding: utf-8 -*-

from urlparse import urlparse
from zope.component import getMultiAdapter, ComponentLookupError

from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

from collective.flowplayer.browser.view import File, Link
from plone.memoize.instance import memoize

from redturtle.video.interfaces import IVideoEmbedCode


class Macros(BrowserView):
    template = ViewPageTemplateFile('redturtlevideo_macros.pt')

    def __getitem__(self, key):
        return self.template.macros[key]


class InternalVideo(File):
    """The Internal Video browser view"""

    def __init__(self, context, request):
        File.__init__(self, context, request)

        self.height = self.height or context.getHeight()
        self.width = self.width or context.getWidth()        
        self._scale = "height: %dpx; width: %dpx;" % (self.height, self.width)

    def href(self):
        return self.context.absolute_url()+'/at_download/file'

    def getEmbedCode(self):
        """Return embed code"""
        context = self.context
        portal_url = getToolByName(context, 'portal_url')()
        fpUrl = portal_url+"/%2B%2Bresource%2B%2Bcollective.flowplayer/flowplayer.swf"
        embed = """
        <object width="%(width)d" height="%(height)d" data="%(fpUrl)s" type="application/x-shockwave-flash">
                <param name="movie" value="%(fpUrl)s" />
                <param name="allowfullscreen" value="true" />
                <param name="allowscriptaccess" value="always" />
                <param name="flashvars" value="config=%(here_url)s/config.js" />
        </object>
    """ % {
           "fpUrl"   : fpUrl,
           "baseUrl" : portal_url,
           "here_url": context.absolute_url(),
           "clipUrl" : self.href(),
           "width"   : context.getWidth(),
           "height"   : context.getHeight(),           
           }
        return "".join((x.strip() for x in embed.splitlines()))


class InternalVideoConfiguration(InternalVideo):
    """Return the right configuration js file for this video"""
    
    MODEL = """{'clip':{'scaling':'fit',
                                                       'autoBuffering':false,
                                                       'autoPlay':false,
                                                       'baseUrl':'%(baseUrl)s',
                                                       'url':'%(clipUrl)s'
                                        },
                               'canvas':{'backgroundColor':'#112233'},
                               'plugins':{'controls':{'time':false,
                                                      'volume':false,
                                                      'fullscreen':false},
                                          'content':{'url':'flowplayer.swf',
                                                     'html':'Flash plugins work too'}
                                         }
                                }"""

    def __call__(self):
        portal_url = getToolByName(self.context, 'portal_url')()
        fpUrl = portal_url+"/%2B%2Bresource%2B%2Bcollective.flowplayer/flowplayer.swf"
        self.request.response.setHeader("Content-type", "application/x-javascript")

        return self.MODEL % {
           "fpUrl"   : fpUrl,
           "baseUrl" : portal_url,
           "clipUrl" : self.href()
           }



class RemoteVideo(Link):
    """The External Video link browser view"""

    @memoize
    def getPlayerCode(self):
        """Return code from external service player"""
        video_site = urlparse(self.context.getRemoteUrl())[1].replace('www.','')
        try:
            adapter = getMultiAdapter((self.context, self.request), IVideoEmbedCode, name = video_site)
        except ComponentLookupError:
            adapter = getMultiAdapter((self.context, self.request), IVideoEmbedCode)            
        return adapter()
