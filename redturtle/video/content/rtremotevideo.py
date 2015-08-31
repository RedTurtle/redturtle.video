"""Definition of the RTRemoteVideo content type
"""

import urlparse
from AccessControl import ClassSecurityInfo
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.content.image import ATImageSchema
from Products.ATContentTypes.content.link import ATLink, ATLinkSchema
from Products.ATContentTypes.lib.imagetransform import ATCTImageTransform
from Products.Archetypes import atapi
from Products.CMFCore import permissions
from redturtle.video import videoMessageFactory as _
from redturtle.video.config import PROJECTNAME
from redturtle.video.content.default import DefaultVideo
from redturtle.video.content.video_schema import VIDEO_SCHEMA
from redturtle.video.interfaces import IRTRemoteVideo
from urllib import quote
from zope.interface import implements

RTRemoteVideoSchema = ATLinkSchema.copy() + VIDEO_SCHEMA.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

RTRemoteVideoSchema['title'].storage = atapi.AnnotationStorage()
RTRemoteVideoSchema['description'].storage = atapi.AnnotationStorage()

imageField = ATImageSchema['image'].copy()
imageField.required = False
imageField.primary = False
imageField.widget.description = _(u'help_video_image',
                                  default = u'Can be used to provide splash image when needed')
imageField.validators = None
imageField.sizes = None

RTRemoteVideoSchema.addField(imageField)
RTRemoteVideoSchema.moveField('image', after = 'remoteUrl')
RTRemoteVideoSchema['remoteUrl'].widget.size = 60
RTRemoteVideoSchema['remoteUrl'].accessor = 'getRemoteVideoURL'

schemata.finalizeATCTSchema(RTRemoteVideoSchema, moveDiscussion = False)


class RTRemoteVideo(ATCTContent, ATCTImageTransform, DefaultVideo):
    """A link to a video with screenshot"""
    implements(IRTRemoteVideo)

    meta_type = "RTRemoteVideo"
    schema = RTRemoteVideoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    security = ClassSecurityInfo()

    security.declareProtected(permissions.View, 'tag')
    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        return self.getField('image').tag(self, **kwargs)

    def __bobo_traverse__(self, REQUEST, name):
        """Transparent access to image scales
        """
        if name.startswith('image'):
            field = self.getField('image')
            image = None
            if name == 'image':
                image = field.getScale(self)
            else:
                scalename = name[len('image_'):]
                scalename.replace(".jpg", "")
                if scalename in field.getAvailableSizes(self):
                    image = field.getScale(self, scale=scalename)
            if image is not None and not isinstance(image, basestring):
                # image might be None or '' for empty images
                return image

        return ATCTContent.__bobo_traverse__(self, REQUEST, name)

    security.declareProtected(permissions.ModifyPortalContent, 'setRemoteUrl')
    def setRemoteUrl(self, value, **kwargs):
        """remute url mutator

        Use urlparse to sanify the url
        Also see http://dev.plone.org/plone/ticket/3296
        """
        if value:
            value = urlparse.urlunparse(urlparse.urlparse(value))
        self.getField('remoteUrl').set(self, value, **kwargs)

    security.declareProtected(permissions.View, 'getRemoteVideoURL')
    def getRemoteVideoURL(self):
        """Sanitize output
        """
        value = self.Schema()['remoteUrl'].get(self)
        if not value: value = ''  # ensure we have a string
        return quote(value, safe='?$#@/:=+;$,&%')

atapi.registerType(RTRemoteVideo, PROJECTNAME)
