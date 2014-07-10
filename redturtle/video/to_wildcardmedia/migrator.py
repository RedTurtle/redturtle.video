# -*- coding: utf-8 -*-

'''
This stuff has been stolen from plone.app.contentypes migrations
'''

import logging
from Products.CMFPlone.utils import safe_unicode
from Products.contentmigration.basemigrator.migrator import CMFItemMigrator
from Products.contentmigration.basemigrator.walker import CatalogWalker
from plone.app.textfield.value import RichTextValue
from plone.namedfile.file import NamedBlobFile
from plone.namedfile.file import NamedBlobImage
from zope.component import adapter
from zope.component import getAdapters
from zope.interface import Interface
from zope.interface import implementer
from wildcard.media.async import queueJob
#from z3c.relationfield import RelationValue

logger = logging.getLogger(__name__)


def migrate(portal, migrator):
    """return a CatalogWalker instance in order
    to have its output after migration"""
    walker = CatalogWalker(portal, migrator)()
    return walker



class ICustomMigrator(Interface):
    """Adapter implementer interface for custom migrators.
    Please note that you have to register named adapters in order to be able to
    register multiple adapters to the same adaptee.
    """
    def migrate(old, new):
        """Start the custom migraton.
        :param old: The old content object.
        :param new: The new content object.
        """


@implementer(ICustomMigrator)
@adapter(Interface)
class BaseCustomMigator(object):
    """Base custom migration class. Does nothing.

    You can use this as base class for your custom migrator adapters.
    You might register it to some specific orginal content interface.
    """
    def __init__(self, context):
        self.context = context

    def migrate(self, old, new):
        return


class ATCTContentMigrator(CMFItemMigrator):
    """Base for contentish ATCT
    """

    def __init__(self, *args, **kwargs):
        super(ATCTContentMigrator, self).__init__(*args, **kwargs)
        logger.info(
            "Migrating object %s" %
            '/'.join(self.old.getPhysicalPath())
        )

    def migrate_atctmetadata(self):
        field = self.old.getField('excludeFromNav')
        self.new.exclude_from_nav = field.get(self.old)

    def migrate_custom(self):
        """Get all ICustomMigrator registered migrators and run the migration.
        """
        for _, migrator in getAdapters((self.old, ), ICustomMigrator):
            migrator.migrate(self.old, self.new)


class RTInternalVideoMigrator(ATCTContentMigrator):

    src_portal_type = 'RTInternalVideo'
    src_meta_type = 'RTInternalVideo'
    dst_portal_type = 'WildcardVideo'
    dst_meta_type = None  # not used

    def migrate_schema_fields(self):
        # text/transcript
        field = self.old.getField('text')
        mime_type = field.getContentType(self.old)
        raw_text = safe_unicode(field.getRaw(self.old))
        if raw_text.strip() != '':
            richtext = RichTextValue(raw=raw_text, mimeType=mime_type,
                                     outputMimeType='text/x-html-safe')
            self.new.transcript = richtext
        # video source
        old_file = self.old.getField('file').get(self.old)
        filename = safe_unicode(old_file.filename)
        namedblobfile = NamedBlobFile(contentType=old_file.content_type,
                                      data=old_file.data,
                                      filename=filename)
        self.new.video_file = namedblobfile
        # image/splashscreen
        old_image = self.old.getField('image').get(self.old)
        if old_image != '':
            filename = safe_unicode(old_image.filename)
            # BBB: plone.app.contenttypes migrator use old_image.data,
            # but I get ComponentLookupError
            namedblobimage = NamedBlobImage(data=old_image.data.data,
                                            filename=filename)
            self.new.image = namedblobimage
        # size
        width = self.old.getField('width').get(self.old)
        self.new.width = width
        height = self.old.getField('height').get(self.old)
        self.new.height = height
        # running video conversion
        queueJob(self.new)



def migrate_internalvideo(portal):
    return migrate(portal, RTInternalVideoMigrator)



class RTRemoteVideoMigrator(ATCTContentMigrator):

    src_portal_type = 'RTRemoteVideo'
    src_meta_type = 'RTRemoteVideo'
    dst_portal_type = 'WildcardVideo'
    dst_meta_type = None  # not used

    def migrate_schema_fields(self):
        # text/transcript
        field = self.old.getField('text')
        mime_type = field.getContentType(self.old)
        raw_text = safe_unicode(field.getRaw(self.old))
        if raw_text.strip() != '':
            richtext = RichTextValue(raw=raw_text, mimeType=mime_type,
                                     outputMimeType='text/x-html-safe')
            self.new.transcript = richtext
        # image/splashscreen
        old_image = self.old.getField('image').get(self.old)
        if old_image != '':
            filename = safe_unicode(old_image.filename)
            # BBB: plone.app.contenttypes migrator use old_image.data,
            # but I get ComponentLookupError
            namedblobimage = NamedBlobImage(data=old_image.data.data,
                                            filename=filename)
            self.new.image = namedblobimage
        # video link
        remote_url = self.old.getField('remoteUrl').get(self.old)
        self.new.youtube_url = remote_url
        # size
        width = self.old.getField('width').get(self.old)
        self.new.width = width
        height = self.old.getField('height').get(self.old)
        self.new.height = height  


def migrate_videolink(portal):
    return migrate(portal, RTRemoteVideoMigrator)
