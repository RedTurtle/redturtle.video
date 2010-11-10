Introduction
============

A simple video support for Plone, based on `collective.flowplayer`__.

__ http://pypi.python.org/pypi/collective.flowplayer

This add to your Plone portal two new content types:

* *Video file* for providing a video content directly from a video file compatible with flowplayer
  formats
* *Video link* for a remote video resource

New content types have mandatory image field, for the video screenshot/splash data.
Also you can insert the *year* of the video and the *duration*. This last info is also taken
automatically from the video (only for internal video).

All other given feature cames directly from collective.flowplayer.

Portlet
-------

Also this will give you a new "*Video gallery*" portlet, similar to the ones you'll get with
collective.flowplayer. This new portlet shows image fields content taken from videos.

Support for remote video services
---------------------------------

The *Video link* content type handle URL not only to .flv or other compatible flowplayer resource, but
also to 3rd party video services.

Right now URL to those services are handled:

* Youtube (http://www.youtube.com/)
* Vimeo (http://vimeo.com/)

You are invited to help us extending also to other services.

TODO
----

* video transcript
* can be integrated with `stxnext.transform.avi2flv`__?
* can be integrated wtih `collective.transcode`__?

__ http://pypi.python.org/pypi/stxnext.transform.avi2flv/
__ http://pypi.python.org/pypi/collective.transcode.star

Credits
=======

Developed with the support of `Comune di Modena`__; Comune di Modena supports the
`PloneGov initiative`__.

.. image:: http://www.ausl.fe.it/logo_ausl.gif
   :alt: Azienda USL's logo

__ http://www.comune.modena.it/
__ http://www.plonegov.it/

Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.net/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.net/

Thanks to
---------

* *Giorgio Borelli* (gborelli) for adding tests, fixing issues and providing *Vimeo* support.
* *Christian Ledermann* (nan010) for providing Google Video, Metacafe support and, not
  last, good documentation.

Other products
==============

Before choosing this product, if you think you need a site with huge video features or simply
wanna explore where Plone is going when talking of video, take a look at:

* `Plumi`__
* `Plone Video Suite`__ 

__ http://plone.org/products/plumi
__ http://www.coactivate.org/projects/plone-video-sprint/project-home

