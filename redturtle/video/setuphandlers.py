# -*- coding: utf-8 -*-

from zope import component
from Products.CMFCore.utils import getToolByName

INDEXES_TO_ADD = (
                  #('hasSplashScreenImage', 'FieldIndex', {'indexed_attrs': 'hasSplashScreenImage', }, ),
                  )


def setupVarious(context):
    portal = context.getSite()
    
    if context.readDataFile('redturtle.video_various.txt') is None: 
        return
    addKeyToCatalog(portal)
    

def addKeyToCatalog(portal):
    '''Takes portal_catalog and adds a key to it
    @param context: context providing portal_catalog 
    '''
    pc = portal.portal_catalog
    pl = portal.plone_log

    indexes = pc.indexes()
    for idx in INDEXES_TO_ADD:
        if idx[0] in indexes:
            pl("Found the '%s' index in the catalog, nothing changed.\n" % idx[0])
        else:
            pc.addIndex(name=idx[0], type=idx[1], extra=idx[2])
            pl("Added '%s' (%s) to the catalog.\n" % (idx[0], idx[1]))
