from zope import interface
from zope import component

from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

from collective.flowplayer.browser.view import File, Link

from plone.memoize.instance import memoize

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    BeautifulSoup = None

import urllib

class InternalVideo(File):
    """The Internal Video browser view"""

    def href(self):
        return self.context.absolute_url()+'/at_download/file'
    
    def getEmbedCode(self):
        """Return embed code"""
        base_url = self.context.absolute_url()
        url = self.href()
        embed_code = '<object width="251" height="200" data="http://flowplayer.org/swf/flowplayer-3.1.5.swf" type="application/x-shockwave-flash"><param name="movie" value="http://flowplayer.org/swf/flowplayer-3.1.5.swf" /><param name="allowfullscreen" value="true" /><param name="allowscriptaccess" value="always" /><param name="flashvars" value='
        config="'config={"
        clip='"clip":{"scaling":"fit","autoBuffering":false,"autoPlay":false,"baseUrl":"' + base_url + '","url":"' + url + '"},"playlist":[{"scaling":"fit","autoBuffering":false,"autoPlay":false,"baseUrl":"' + base_url + '","url":"' + url + '"}],"canvas":{"backgroundColor":"#112233"},"plugins":{"controls":{"time":false,"volume":false,"fullscreen":false},"content":{"url":"flowplayer.content-3.1.0.swf","html":"Flash plugins work too"}}}'
        object="' /></object>"
        return embed_code + config + clip + object

class RemoteVideo(Link):
    """The External Video link browser view"""

    def fromYouTube(self):
        """Check if the current player must be taken from youtube"""
        return self.context.getRemoteUrl().startswith("http://www.youtube.com/")
    
    def getYoutubePlayerCode(self):
        """Return code from youtube player"""
        embed_code = None
        if BeautifulSoup:
            data = urllib.urlopen(self.context.getRemoteUrl())
            html = data.read()
            html = html.split("\n")
            for line in html:
                if line.find('id="embed_code"')>-1:
                    soup = BeautifulSoup(line)
                    embed_code = soup.fetch('input')[0].get('value')
        return embed_code