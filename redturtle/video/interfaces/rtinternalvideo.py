from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers
from redturtle.video.interfaces import IRTVideo

from redturtle.video import videoMessageFactory as _

class IRTInternalVideo(IRTVideo):
    """A video file with screenshot"""
    
    # -*- schema definition goes here -*-


