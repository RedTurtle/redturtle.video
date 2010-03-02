# -*- coding: utf-8 -*-

from zope import component
from Products.CMFCore.utils import getToolByName

INDEXES_TO_ADD = (
                  #('hasSplashScreenImage', 'FieldIndex',
                  # {'indexed_attrs': 'hasSplashScreenImage', }, ),
                  )


# form : http://maurits.vanrees.org/weblog/archive/2009/12/catalog
def addKeyToCatalog(portal, logger=None):
    '''Takes portal_catalog and adds a key to it
    @param portal: context providing portal_catalog
    '''
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger('redturtle.video')

    catalog = getToolByName(portal, 'portal_catalog')
    indexes = catalog.indexes()
    # Specify the indexes you want, with ('index_name', 'index_type')
    wanted = (('hasSplashScreenImage', 'FieldIndex'),
              ('getYear', 'KeywordIndex'),
              ('getDuration', 'KeywordIndex')
              )

    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info("Added %s for field %s.", meta_type, name)
    if len(indexables) > 0:
        logger.info("Indexing new indexes %s.", ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)


def setupVarious(context):
    if context.readDataFile('redturtle.video_various.txt') is None:
        return

    logger = context.getLogger('your.package')
    portal = context.getSite()
    addKeyToCatalog(portal, logger)
