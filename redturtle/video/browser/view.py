from zope import interface
from zope import component

from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from collective.flowplayer.utils import properties_to_javascript

from collective.flowplayer.interfaces import IFlowPlayable
from collective.flowplayer.interfaces import IMediaInfo, IFlowPlayerView
from collective.flowplayer.browser.view import File

from plone.memoize.instance import memoize

class InternalVideo(File):
    """The RedTurtle Internal Video browser view"""

    def href(self):
        return self.context.absolute_url()+'/at_download/file'

