.. contents:: **Table of contents**

Introduction
============

A simple video support for Plone, mainly based on `collective.flowplayer`__.

__ http://pypi.python.org/pypi/collective.flowplayer

Features
========

This add to your Plone portal two new types:

* *Video file* for providing a video content directly from a video file compatible with flowplayer
  formats. In the video view you can copy/paste the video embedding code, for seeing this video in other
  sites.
* *Video link* for a remote video resource

Also you can insert the *year* of the video and the *duration*.

A "Look" section will also give you fields for:

* add an optional image field, for the video screenshot/splashscreen data
* video display size

Internal video
--------------

Add to your site a new "Video file", then provide a video format compatible with `Flowplayer`__.
When you save it RedTurtle Video try to take from the video source some metadata like the *duration*
and video size (width and height). Later you can modify those values manually.

__ http://flowplayer.org/

.. image:: http://keul.it/images/plone/redturtle-video-0.4.0-01.png
   :alt: Video file example

If you provided also the image field, this can be used (optionally) as video starting splash image.
All other amazing features came directly from the power of ``collective.flowplayer``.

Remote video
------------

Always wrapping ``collective.flowplayer`` features, you can provide a special kind of link that point to
a compatible format resource. Again you can play with all additional fields, adjusting video size and
metadata.

The link can be to a remote site that host ``flv`` of other compatible types, or a link to an "Video file"
in the same Plone site.

Remote video providers
----------------------

One of the most interesting feature is the support to *URL to 3rd party remote video services* like:

* YouTube (http://www.youtube.com/) - using `collective.rtvideo.youtube`__
* Vimeo (http://vimeo.com/) - still internal feature
* Metacafe (http://www.metacafe.com/) - still internal feature

.. image:: http://keul.it/images/plone/redturtle-video-0.4.0-02.png
   :alt: Video link to a YouTube resource

Enhancing this list with additional providers is quite simple (see the `documentation`__ given with the product).
You are welcome to contribute and release other ``collective.rtvideo.yourpreferredremoteservice`` add-on!

__ http://pypi.python.org/pypi/collective.rtvideo.youtube
__ http://plone.org/products/redturtle.video/documentation/

Portlet
-------

Also this will give you a new "*Video gallery*" portlet, similar to the ones you'll get with
``collective.flowplayer`` ("Video player").

This portlet will show links to a configurable set of videos, displaying in the portlet the splash image.

You can still use basic "Video player" portlet given by ``collective.flowplayer``.

Requirements
============

Tested on Plone 3.2, 3.3 and 4.0.

Installation
============

Using buildout::

    [buildout]
    ...
    eggs =
        ...
        redturtle.video

To add also additional video providers support::

    [buildout]
    ...
    eggs =
        ...
        redturtle.video
        collective.rtvideo.youtube
        ...
        mycompany.myservice

Plone 3.2 or lower users: don't forget ``zcml`` section.

Support
=======

If you find bugs or have a good suggestion, open a ticket at
http://plone.org/products/redturtle.video/issues/

TODO
====

* video transcript field: can be useful?
* move away, to other packages named ``collective.rtvideo.xxx``, all video adapters left.
  It's silly to release a new ``redturtle.video`` version if something change on one of the remote services.

Credits
=======

Developed with the support of:

* `Rete Civica Mo-Net - Comune di Modena`__
  
  .. image:: http://www.comune.modena.it/grafica/logoComune/logoComunexweb.jpg 
     :alt: City of Modena - logo
  
* `Regione Emilia Romagna`__

* `Guardia di Finanza`__
  
All of them supports the `PloneGov initiative`__.

__ http://www.comune.modena.it/
__ http://www.regione.emilia-romagna.it/
__ http://www.gdf.gov.it/
__ http://www.plonegov.it/

Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.net/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/

Thanks to
---------

* *Giorgio Borelli* (gborelli) for adding tests, fixing issues and providing *Vimeo* support.
* *Christian Ledermann* (nan010) for providing Google Video, Metacafe support and, not
  last, good documentation.

Other products
==============

Before choosing this product think about what you want to get from "Plone and Video".
We strongly suggest you to use ``redturtle.video`` only when:

* The simple use of ``collective.flowplayer`` if not enough (you don't like to upload a "File" that magically
  became a Video? You need remote video support? You need a real new plone content type to make Collections?)
* The use of `Plumi`__ suite is "too much" (you don't need a full video site, just a simple video support inside
  you CMS)
* You need to have Video as real CMS contents, not only use them embedded in document text (a task that you can
  reach easily using `collective.embedly`__)

You can also be interested looking at the `Plone Video Suite`__ discussions. 

__ http://plone.org/products/plumi
__ http://projects.quintagroup.com/products/wiki/collective.embedly
__ http://www.coactivate.org/projects/plone-video-sprint/project-home

