# -*- coding: utf-8 -*-

import logging
from Products.CMFCore.utils import getToolByName

PROFILE_ID = 'profile-redturtle.video:default'

_PROPERTIES = [
    dict(name='default_videosize_w', type_='int', value=400),
    dict(name='default_videosize_h', type_='int', value=300),
]

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
    registerProperties(portal, logger)


def migrateTo060rc1(context, logger=None):
    if logger is None:
        logger = logging.getLogger('redturtle.video')
    setup_tool = getToolByName(context, 'portal_setup')
    setup_tool.runImportStepFromProfile(PROFILE_ID, 'propertiestool')
    registerProperties(context, logger)
    logger.info("Migrated to 0.6.0")

