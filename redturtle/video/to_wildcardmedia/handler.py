# -*- coding: utf-8 -*-

try:
    import wildcard.media
    WM_FOUND = True
except ImportError:
    WM_FOUND = False
try:
    import Products.contentmigration
    CONTENTMIGRATION_FOUND = True
except ImportError:
    CONTENTMIGRATION_FOUND = False

from redturtle.video import logger
from redturtle.video.to_wildcardmedia.migrator import migrate_internalvideo
from redturtle.video.to_wildcardmedia.migrator import migrate_videolink


def toWildcardMedia(context):
    if context.readDataFile('redturtle.video_to_wmedia_migration.txt') is None:
        return

    site = context.getSite()
    if not WM_FOUND:
        logger.error("wildcard.media not found. Can't migrate anything")
    if not CONTENTMIGRATION_FOUND:
        logger.error("Products.contentmigration not found. Can't migrate anything")
    logger.info("Migrate internal videos")
    migrate_internalvideo(site)
    logger.info("Internal video migration done")
    logger.info("Migrate video links")
    migrate_videolink(site)
    logger.info("Video links migration done")
    logger.info("Migration completed")
