"""Definition of the RTInternalVideo content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from redturtle.video import videoMessageFactory as _
from redturtle.video.interfaces import IRTInternalVideo
from redturtle.video.config import PROJECTNAME

RTInternalVideoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'image',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Preview image"),
            description=_(u"Field description"),
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

RTInternalVideoSchema['title'].storage = atapi.AnnotationStorage()
RTInternalVideoSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(RTInternalVideoSchema, moveDiscussion=False)

class RTInternalVideo(base.ATCTContent):
    """A video file with screenshot"""
    implements(IRTInternalVideo)

    meta_type = "RTInternalVideo"
    schema = RTInternalVideoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    image = atapi.ATFieldProperty('image')


atapi.registerType(RTInternalVideo, PROJECTNAME)
