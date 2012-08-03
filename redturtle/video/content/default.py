# -*- coding: utf-8 -*-

from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import getToolByName

class DefaultVideo(object):
    """Common properties for rt video contents"""

    security = ClassSecurityInfo()

    security.declarePrivate("getDefaultWidth")
    def getDefaultWidth(self):
        p_tool = getToolByName(self, 'portal_properties')
        try:
            return p_tool.redturtle_video_properties.default_videosize_w
        except AttributeError:
            return 251 # old default

    security.declarePrivate("getDefaultHeight")
    def getDefaultHeight(self):
        p_tool = getToolByName(self, 'portal_properties')
        try:
            return p_tool.redturtle_video_properties.default_videosize_h
        except AttributeError:
            return 200 # old default
