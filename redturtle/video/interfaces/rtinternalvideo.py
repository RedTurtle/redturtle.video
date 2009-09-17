from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers
from Products.ATContentTypes.interface.file import IATFile

from redturtle.video import videoMessageFactory as _

class IRTInternalVideo(IATFile):
    """A video file with screenshot"""
    
    # -*- schema definition goes here -*-


