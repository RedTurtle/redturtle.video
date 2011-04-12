Introduction
============

A simple video support for Plone, based on `collective.flowplayer`__.

__ http://pypi.python.org/pypi/collective.flowplayer

This add to your Plone portal two new content types:

* *Video file* for providing a video content directly from a video file compatible with flowplayer
  formats. In the video view you can copy/paste the video embedding code, for seeing this video in other
  sites.
* *Video link* for a remote video resource

New content types have mandatory image field, for the video screenshot/splash data.
Also you can insert the *year* of the video and the *duration*. This last info is also taken
automatically from the video (only for internal video).

You can also (again, automatically taken) change the video size.

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
* Metacafe (http://www.metacafe.com/)
* Google Video (http://video.google.com/)

You are invited to help us extending also to other services.

Support
=======

If you find bugs or have a good suggestione, open a ticket at
http://plone.org/products/redturtle.video/issues/

TODO
====

* video transcript field can be useful?
* move away, to other packages, all video adapters. It's silly to release a new redturtle.video version if
  something change on remote services.

Credits
=======

Developed with the support of `Comune di Modena`__; Comune di Modena supports the
`PloneGov initiative`__.

.. image:: http://www.comune.modena.it/grafica/logoComune/logoComunexweb.jpg 
   :alt: Rete Civica Mo-Net logo

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

Before choosing this product think about what you want to get from "Plone and Video". We suggest you to use
redturtle.video when:

* The simple use of collective.flowplayer if not enough (you don't like to upload a "File" that magically
  became a Video? You need remote video support? You need a real new plone content type to make Collections?)
* The use of `Plumi`__ suite is "too much" (you don't need a full video site, just a simple video support inside
  you CMS)
* You need to have Video as real CMS contents, not only use them embedded in document text (a task that you can
  reach easilly using `collective.embedly`__)

You can also be interested looking at the `Plone Video Suite`__ discussions. 

__ http://plone.org/products/plumi
__ http://projects.quintagroup.com/products/wiki/collective.embedly
__ http://www.coactivate.org/projects/plone-video-sprint/project-home

