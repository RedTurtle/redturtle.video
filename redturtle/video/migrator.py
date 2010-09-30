# -*- coding: utf-8 -*-

from plone.app.blob.migrations import migrate


def migrateRTInternalVideo(context):
    return migrate(context, 'RTInternalVideo')
