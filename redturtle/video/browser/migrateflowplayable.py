# -*- coding: utf-8 -*-

from zope.interface import Interface
from zope.formlib import form
try: # >= 4.1
    from five.formlib import formbase
except ImportError: # < 4.1
    from Products.Five.formlib import formbase
from redturtle.video.migrator import migrateFlowplayerToRedTurtleVideo
from Products.statusmessages.interfaces import IStatusMessage

from redturtle.video import videoMessageFactory as _


class IMigrateFlowplayerSchema(Interface):
    pass


class MigrateFlowplayerFile(formbase.PageForm):
    form_fields = form.FormFields(IMigrateFlowplayerSchema)
    label = u'Video files migration'
    description = u'Migrate basic Flowplayer video files to RedTurtle Video'

    @form.action(_(u'Migrate Flowplayer video files'))
    def actionMigrate(self, action, data):
        output = migrateFlowplayerToRedTurtleVideo(self.context)
        if output:
            for o in output:
                IStatusMessage(self.request).addStatusMessage(o, type='info')
        else:
            IStatusMessage(self.request).addStatusMessage(_(u'Nothing to migrate'), type='info')
        return self.request.response.redirect(self.context.absolute_url())

    @form.action(_(u'Cancel'))
    def actionCancel(self, action, data):
        return self.request.response.redirect(self.context.absolute_url())
