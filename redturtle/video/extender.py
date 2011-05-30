# -*- coding: utf-8 -*-

from zope.component import adapts
from zope.interface import implements

from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField
from plone.app.blob.field import BlobField

from Products.Archetypes import atapi

from redturtle.video.interfaces import IRTInternalVideo
from redturtle.video.content.rtinternalvideo import RTInternalVideoSchema

class ExtensionBlobField(ExtensionField, BlobField):
    """ derivative of blobfield for extending schemas """


class RemoteVideoATTypeExtender(object):
    adapts(IRTInternalVideo)
    implements(ISchemaExtender)

    fields = [
        ExtensionBlobField('file',
            widget=atapi.FileWidget(
                label=RTInternalVideoSchema['file'].widget.label,
                description=RTInternalVideoSchema['file'].widget.description,
            ),
            required=True,
            primary=True,
            validators=('isNonEmptyFile'),
        ),

    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
