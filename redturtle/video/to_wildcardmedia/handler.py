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


def toWildcardMedia(context):
    site = context.getSite()
    if not WM_FOUND:
        logger.error("wildcard.media not found. Can't migrate anything")
    if not CONTENTMIGRATION_FOUND:
        logger.error("Products.contentmigration not found. Can't migrate anything")
    migrate_internalvideo(site)
    logger.info("Migration completed")