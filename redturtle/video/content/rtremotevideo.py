"""Definition of the RTRemoteVideo content type
"""

from zope.interface import implements, directlyProvides

from AccessControl import ClassSecurityInfo
from Products.CMFCore import permissions
from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.link import ATLink, ATLinkSchema
from Products.ATContentTypes.content.image import ATImageSchema, ATImage
from Products.ATContentTypes.lib.imagetransform import ATCTImageTransform
from Products.validation import V_REQUIRED

from collective.flowplayer.interfaces import IFlowPlayable

from redturtle.video import videoMessageFactory as _
from redturtle.video.interfaces import IRTRemoteVideo
from redturtle.video.config import PROJECTNAME

from redturtle.video.content.video_schema import VIDEO_SCHEMA

RTRemoteVideoSchema = ATLinkSchema + VIDEO_SCHEMA + atapi.Schema((

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

RTRemoteVideoSchema.addField(imageField)
RTRemoteVideoSchema.moveField('image', after = 'remoteUrl')
RTRemoteVideoSchema['remoteUrl'].widget.size = 60

schemata.finalizeATCTSchema(RTRemoteVideoSchema, moveDiscussion = False)


class RTRemoteVideo(ATLink, ATCTImageTransform):
    """A link to a video with screenshot"""
    implements(IRTRemoteVideo, IFlowPlayable)

    meta_type = "RTRemoteVideo"
    schema = RTRemoteVideoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

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

        return ATLink.__bobo_traverse__(self, REQUEST, name)

    def hasSplashScreenImage(self):
        """Boolean value to know if an image is available"""
        if self.getImage():
            return True
        return False

atapi.registerType(RTRemoteVideo, PROJECTNAME)
