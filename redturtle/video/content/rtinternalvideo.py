"""Definition of the RTInternalVideo content type
"""

from zope.interface import implements, directlyProvides

from AccessControl import ClassSecurityInfo
from Products.CMFCore import permissions
from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.file import ATFileSchema, ATFile
from Products.ATContentTypes.content.image import ATImageSchema, ATImage
from Products.ATContentTypes.lib.imagetransform import ATCTImageTransform
from Products.validation import V_REQUIRED

from collective.flowplayer.interfaces import IFlowPlayable

from redturtle.video import videoMessageFactory as _
from redturtle.video.interfaces import IRTInternalVideo
from redturtle.video.config import PROJECTNAME

from redturtle.video.content.video_schema import VIDEO_SCHEMA

RTInternalVideoSchema = ATFileSchema.copy() + VIDEO_SCHEMA + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

RTInternalVideoSchema['title'].storage = atapi.AnnotationStorage()
RTInternalVideoSchema['description'].storage = atapi.AnnotationStorage()

imageField = ATImageSchema['image'].copy()
imageField.required = False
imageField.primary = False
imageField.widget.description = _(u'help_video_image',
            default=u'Can be used to provide splash image when needed')
imageField.validators = None

RTInternalVideoSchema.addField(imageField)
RTInternalVideoSchema.moveField('image', after='file')

schemata.finalizeATCTSchema(RTInternalVideoSchema, moveDiscussion=False)


class RTInternalVideo(base.ATCTContent, ATCTImageTransform):
    """A video file with screenshot"""
    implements(IRTInternalVideo, IFlowPlayable)

    meta_type = "RTInternalVideo"
    schema = RTInternalVideoSchema

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

        return base.ATCTContent.__bobo_traverse__(self, REQUEST, name)

    def hasSplashScreenImage(self):
        """Boolean value to know if an image is available"""
        if self.getImage():
            return True
        return False

atapi.registerType(RTInternalVideo, PROJECTNAME)
