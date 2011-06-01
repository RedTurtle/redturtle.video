# -*- coding: utf-8 -*-

from zope.interface import Interface
from zope.formlib import form
try: # >= 4.1
    from five.formlib import formbase
except ImportError: # < 4.1
    from Products.Five.formlib import formbase
from redturtle.video.migrator import migrateRTInternalVideo
from Products.statusmessages.interfaces import IStatusMessage

from redturtle.video import videoMessageFactory as _

try:
    import Products.contentmigration
    MIGRATION_MODULE = True
except ImportError:
    MIGRATION_MODULE = False

class IMigrateBlobsSchema(Interface):
    pass


class MigrateBlobs(formbase.PageForm):
    form_fields = form.FormFields(IMigrateBlobsSchema)
    label = u'Blobs Migration'
    description = u'Migrate video, making it use plone.app.blob'

    @form.action(_(u'Migrate Internal video'))
    def actionMigrate(self, action, data):
        if MIGRATION_MODULE:
            output = migrateRTInternalVideo(self.context)
            IStatusMessage(self.request).addStatusMessage(output, type='info')
            return self.request.response.redirect(self.context.absolute_url())
        else:
            output = _(u'migration_error_msg',
                       default=u'You need to install "Products.contentmigration" product for perform the task')
            IStatusMessage(self.request).addStatusMessage(output, type='error')
            return self.request.response.redirect(self.context.absolute_url()+'/@@migrateblobs')
        

    @form.action(_(u'Cancel'))
    def actionCancel(self, action, data):
        return self.request.response.redirect(self.context.absolute_url())
