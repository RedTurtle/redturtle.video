# -*- coding: utf-8 -*-
from urlparse import urlparse
from zope import interface
from zope.component import getMultiAdapter

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

    def href(self):
        return self.context.absolute_url()+'/at_download/file'

    def getEmbedCode(self):
        """Return embed code"""
        baseUrl = self.context.absolute_url()
        fpUrl = baseUrl+"/%2B%2Bresource%2B%2Bcollective.flowplayer/flowplayer.swf"
        #fpUrl = 'http://releases.flowplayer.org/swf/flowplayer-3.1.5.swf'
        embed = """
        <object width="251" height="200" data="%(fpUrl)s" type="application/x-shockwave-flash">
                <param name="movie" value="%(fpUrl)s" />
                <param name="allowfullscreen" value="true" />
                <param name="allowscriptaccess" value="always" />
                <param name="flashvars" value='config={"clip":{"scaling":"fit",
                                                       "autoBuffering":false,
                                                       "autoPlay":false,
                                                       "baseUrl":"%(baseUrl)s",
                                                       "url":"%(clipUrl)s"
                                        },
                               "playlist": [{"scaling":"fit",
                                             "autoBuffering":false,
                                             "autoPlay":false,"baseUrl":"%(baseUrl)s",
                                             "url":"%(clipUrl)s"}],
                               "canvas":{"backgroundColor":"#112233"},
                               "plugins":{"controls":{"time":false,
                                                      "volume":false,
                                                      "fullscreen":false},
                                          "content":{"url":"flowplayer.swf",
                                                     "html":"Flash plugins work too"}
                                         }
                                }' />
        </object>
    """ % {
           "fpUrl"   : fpUrl,
           "baseUrl" : self.context.absolute_url(),
           "clipUrl" : self.href()
           }
        return "".join((x.strip() for x in embed.splitlines()))

class RemoteVideo(Link):
    """The External Video link browser view"""

    @memoize
    def getPlayerCode(self):
        """Return code from youtube player"""
        video_site = urlparse(self.context.getRemoteUrl())[1].replace('www.','')
        try:
            adapter = getMultiAdapter((self.context, self.request), IVideoEmbedCode, name = video_site)
        except:
            adapter = getMultiAdapter((self.context, self.request), IVideoEmbedCode)            
        return adapter()
