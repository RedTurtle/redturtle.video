# -*- coding: utf-8 -*-

from Products.ATContentTypes.interface.link import IATLink
from redturtle.video.interfaces import IRTVideo

class IRTRemoteVideo(IATLink, IRTVideo):
    """A link to a video with screenshot"""

