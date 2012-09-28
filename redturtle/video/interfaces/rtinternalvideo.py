# -*- coding: utf-8 -*-

from Products.ATContentTypes.interface import IFileContent
from redturtle.video.interfaces import IRTVideo

class IRTInternalVideo(IRTVideo, IFileContent):
    """A video file with screensplash"""

