#!/bin/bash

DOMAIN=redturtle.video

i18ndude rebuild-pot --pot locales/${DOMAIN}.pot --create $DOMAIN .
i18ndude sync --pot locales/${DOMAIN}.pot locales/*/LC_MESSAGES/${DOMAIN}.po

DOMAIN=plone

i18ndude merge --pot i18n/${DOMAIN}.pot --merge i18n/${DOMAIN}-manual.pot
i18ndude sync --pot i18n/${DOMAIN}.pot i18n/${DOMAIN}-??.po
