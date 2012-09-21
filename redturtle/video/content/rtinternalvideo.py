"""Definition of the RTInternalVideo content type
"""

from zope.interface import implements

from AccessControl import ClassSecurityInfo
from Products.CMFCore import permissions
from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.file import ATFileSchema
from Products.ATContentTypes.content.image import ATImageSchema
from Products.ATContentTypes.lib.imagetransform import ATCTImageTransform

from collective.flowplayer.interfaces import IFlowPlayable

from redturtle.video import videoMessageFactory as _
from redturtle.video.interfaces import IRTInternalVideo
from redturtle.video.config import PROJECTNAME
from redturtle.video.content.default import DefaultVideo
from redturtle.video.content.video_schema import VIDEO_SCHEMA

RTInternalVideoSchema = ATFileSchema.copy() + VIDEO_SCHEMA.copy()

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

RTInternalVideoSchema['title'].storage = atapi.AnnotationStorage()
RTInternalVideoSchema['title'].required = True
RTInternalVideoSchema['description'].storage = atapi.AnnotationStorage()
RTInternalVideoSchema['file'].searchable = False
#RTInternalVideoSchema['file'].index_method = '_at_accessor'

imageField = ATImageSchema['image'].copy()
imageField.required = False
imageField.primary = False
imageField.widget.description = _(u'help_video_image',
                                  default=u'Can be used to provide splash image when needed')
imageField.validators = None
imageField.sizes = None

RTInternalVideoSchema.addField(imageField)
RTInternalVideoSchema.moveField('image', after='file')

fileField = RTInternalVideoSchema['file']
fileField.widget.label = _(u'label_video_file',
                          default=u'Video file')
fileField.widget.description = _(u'help_video_file',
                                default=u'Put there the video file in a compatible format')

schemata.finalizeATCTSchema(RTInternalVideoSchema, moveDiscussion=False)


class RTInternalVideo(base.ATCTContent, ATCTImageTransform, DefaultVideo):
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

    security.declareProtected(permissions.View, 'size')
    def size(self):
        """Get size video size
        """
        return self.get_size()

    security.declareProtected(permissions.View, 'get_size')
    def get_size(self):
        """ZMI / Plone get size method
        """
        f = self.getPrimaryField()
        if f is None:
            return 0
        return f.get_size(self) or 0

    def hasSplashScreenImage(self):
        """Boolean value to know if an image is available"""
        if self.getImage():
            return True
        return False

    security.declarePrivate('getIndexValue')
    def getIndexValue(self, mimetype='text/plain'):
        # Need to overridide because plone.app.blob use and force this to exists
        return ''

atapi.registerType(RTInternalVideo, PROJECTNAME)
