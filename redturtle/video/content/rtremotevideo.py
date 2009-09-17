"""Definition of the RTRemoteVideo content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from redturtle.video import videoMessageFactory as _
from redturtle.video.interfaces import IRTRemoteVideo
from redturtle.video.config import PROJECTNAME

RTRemoteVideoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.ImageField(
        'image',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Preview image"),
            description=_(u"Field description"),
        ),
        validators=('isNonEmptyFile'),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

RTRemoteVideoSchema['title'].storage = atapi.AnnotationStorage()
RTRemoteVideoSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(RTRemoteVideoSchema, moveDiscussion=False)

class RTRemoteVideo(base.ATCTContent):
    """A link to a video with screenshot"""
    implements(IRTRemoteVideo)

    meta_type = "RTRemoteVideo"
    schema = RTRemoteVideoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    image = atapi.ATFieldProperty('image')


atapi.registerType(RTRemoteVideo, PROJECTNAME)
