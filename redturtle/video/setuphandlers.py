# -*- coding: utf-8 -*-

import logging
from Products.CMFCore.utils import getToolByName

PROFILE_ID = 'profile-redturtle.video:default'

_PROPERTIES = [
    dict(name='default_videosize_w', type_='int', value=400),
    dict(name='default_videosize_h', type_='int', value=300),
]

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
#    if len(indexables) > 0:
#        logger.info("Indexing new indexes %s.", ', '.join(indexables))
#        catalog.manage_reindexIndex(ids=indexables)


def registerProperties(context, logger=None):
    ptool = getToolByName(context, 'portal_properties')
    props = ptool.redturtle_video_properties
    
    for prop in _PROPERTIES:
        if not props.hasProperty(prop['name']):
            props.manage_addProperty(prop['name'], prop['value'], prop['type_'])
            logger.info("Added missing %s property" % prop['name'])

def setupVarious(context):
    if context.readDataFile('redturtle.video_various.txt') is None:
        return

    logger = context.getLogger('redturtle.video')
    portal = context.getSite()
    addKeyToCatalog(portal, logger)
    registerProperties(portal, logger)


def migrateTo060rc1(context, logger=None):
    if logger is None:
        logger = logging.getLogger('redturtle.video')
    setup_tool = getToolByName(context, 'portal_setup')
    setup_tool.runImportStepFromProfile(PROFILE_ID, 'propertiestool')
    registerProperties(context, logger)
    logger.info("Migrated to 0.6.0")

