# -*- coding: utf-8 -*-

from redturtle.video import logger
from redturtle.video import videoMessageFactory as _
try:
    import wildcard.media
    WM_FOUND = True
except ImportError:
    WM_FOUND = False
    

def uninstall(portal, reinstall=False):
    if not reinstall:
        # Don't want to delete all registry values if a Manager simply reinstall the product from ZMI
        setup_tool = portal.portal_setup
        setup_tool.runAllImportStepsFromProfile('profile-redturtle.video:uninstall')
        logger.info("Uninstall done")
        if WM_FOUND:
            logger.warn("You have wildcard.media available. Have you migrated RedTurtle Video types to it?")
            portal.plone_utils.addPortalMessage(_('wildacrdmedia_support_warning',
                                                  default=u"It seems you have wildcard.media product available.\n"
                                                  u"Have you migrated RedTurtle Video types to it?\n"
                                                  u"You can run the \"RedTurtle Video: migrate to wildcard.media\" "
                                                  u"Generic Setup profile."),
                                                type="warning")
