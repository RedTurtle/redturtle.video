from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from redturtle.video import videoMessageFactory as _

class IRTInternalVideo(Interface):
    """A video file with screenshot"""
    
    # -*- schema definition goes here -*-
    image = schema.TextLine(
        title=_(u"Preview image"), 
        required=False,
        description=_(u"Field description"),
    )

