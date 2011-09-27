# -*- coding: utf-8 -*-

from collective.flowplayer.interfaces import IVideo
from collective.flowplayer.interfaces import IMediaInfo

def migrateRTInternalVideo(context):
    from plone.app.blob.migrations import migrate
    return migrate(context, 'RTInternalVideo')


# helper to build custom blob migrators for the given type
# some code stolen from the migration of plone.app.blob
def makeMigrator(context):
    """ generate a migrator for the given at-based portal type """
    from Products.contentmigration.archetypes import InplaceATItemMigrator
    
    class FlowplayerMigrator(InplaceATItemMigrator):
        src_portal_type = 'File'
        src_meta_type = 'ATFile'
        dst_meta_type = 'RTInternalVideo'
        dst_portal_type = 'RTInternalVideo'

        def last_migrate_mediaData(self):
            media = IMediaInfo(self.old)
            self.new.getField('width').set(self.new, media.width)
            self.new.getField('height').set(self.new, media.height)

    return FlowplayerMigrator

def migrateFlowplayerToRedTurtleVideo(context):
    from Products.contentmigration.walker import CustomQueryWalker
    migrator = makeMigrator(context)
    walker = CustomQueryWalker(context, migrator, use_savepoint=True, query={'object_provides': IVideo.__identifier__})
    walker.go()
    return walker.getOutput()

