A simple **video support for Plone**, mainly based on `collective.flowplayer`__.

__ http://pypi.python.org/pypi/collective.flowplayer

.. contents:: **Table of contents**

Deprecation warning: AKA "Easily migration to wildcard.media"
=============================================================

.. note:: **Deprecation warning**
    Although RedTurtle Video will still work for Plone 3.3 to 4.3 (read below), releases from
    1.1.0 and above will be focused on helping people migrate to `wildcard.media`__

__ https://plone.org/products/wildcard.media

Motivations behind this choice
------------------------------

RedTurtle Video have a very long history and we loved it, but it's fate is linked to the status of
``collective.flowplayer``, which is not very clear and still based on a very old
release of Flowplayer, still based on Flash technology.
Plone 4.3 compatibility works... more or less (you will experience some issues originated by
changes done in collective.flowplayer > 3).

But this is not the main problem: meanwhile the web moved on (HTML 5 is here) and a new shiny,
Dexterity based, product is available: **wildcard.media**.

We *really* think that Plone will live better with a single, well done and mainained product
instead of having two or more.

All future versions of RedTurtle Video will help people moving on, migrating to this new
package, and our future work will be probably focused on contributing to *that* package instead.

RedTurtle Video is still your best friend if you need Plone < 4.3 compatibility.

How to migrate?
---------------

Go to you ``portal_setup`` ZMI tool and run the "*RedTurtle Video: migrate to wildcard.media*"
Generic Setup profile.
After that: uninstall RedTurtle Video and remove it from your buildout.

**NB**: ``Products.contentmigration`` is required, and you must rely on
version 2.1.8 or better::

    [buildout]
    ...
    
    [versions]
    ...
    Products.contentmigration = 2.1.8

Limitations
-----------

wildcard.media is not perfect (yet). There's a big feature that is missing: supporting other
remote video sources different by YouTube.

We will work on this in future.

RedTurtle Video Features
========================

(*...in case you still want to use RedTurtle Video...*)

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

Migrate from basic collective.flowplayer file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you already used ``collective.flowplayer`` in your site for manage internal video and now you want
to migrate them to RedTurtle "Video file" contents, you can use the ``@@flowplayer-video-migration`` view.
You need to have installed also `Products.contentmigration`__.

__ http://pypi.python.org/pypi/Products.contentmigration

Please, **backup** your data before trying this!

iOS devices compatibility
~~~~~~~~~~~~~~~~~~~~~~~~~

Using collective.flowplayer you have no compatiblity with iPhone/iPad/iWhatever devices as far as they
don't support Flash technology.

Using RedTurtle Video and providing:

* a splash screen image
* a compatible video format like *mp4*

...you will be able to use also those kind of devices.

.. image:: http://keul.it/images/plone/redturtle.video-0.7.0-01.png
   :alt: A Video file with iPhone

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
* Vimeo (http://www.vimeo.com/) - using `collective.rtvideo.vimeo`__
* Metacafe (http://www.metacafe.com/) - using `collective.rtvideo.metacafe`__

.. image:: http://keul.it/images/plone/redturtle-video-0.4.0-02.png
   :alt: Video link to a YouTube resource

Enhancing this list with additional providers is quite simple (see the `documentation`__ given with the product).
You are welcome to contribute and release other ``collective.rtvideo.yourpreferredremoteservice`` add-on!

__ http://pypi.python.org/pypi/collective.rtvideo.youtube
__ http://pypi.python.org/pypi/collective.rtvideo.vimeo
__ http://pypi.python.org/pypi/collective.rtvideo.metacafe
__ http://plone.org/products/redturtle.video/documentation/

Portlet
-------

Also this will give you a new "*Video gallery*" portlet, similar to the ones you'll get with
``collective.flowplayer`` ("Video player").

This portlet will show links to a configurable set of videos, displaying in the portlet the splash image.

You can still use basic "Video player" portlet given by ``collective.flowplayer``.

Default size
------------

Default video size (that you can change from the "Look" fieldset) is 400x300. You can change this default
going to ZMI, in ``portal_properties`` and change values in ``redturtle_video_properties``.

Requirements
============

Tested on all Plone versions from 3.3 to 4.3, with many compatible collective.flowplayer versions.

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
        collective.rtvideo.youtube
        ...
        mycompany.myservice

Support
=======

If you find bugs or have a good suggestion, open a ticket at
https://github.com/RedTurtle/redturtle.video/issues/

Credits
=======

Developed with the support of:

* `Rete Civica Mo-Net - Comune di Modena`__
  
  .. image:: http://www.comune.modena.it/grafica/logoComune/logoComunexweb.jpg
     :alt: City of Modena - logo
  
* `Regione Emilia Romagna`__

* `Guardia di Finanza`__

* `Camera di Commercio di Ferrara`__
  
  .. image:: http://www.fe.camcom.it/cciaa-logo.png/
     :alt: CCIAA Ferrara - logo

* `S. Anna Hospital, Ferrara`__
  
  .. image:: http://www.ospfe.it/ospfe-logo.jpg 
     :alt: S. Anna Hospital logo

All of them supports the `PloneGov initiative`__.

__ http://www.comune.modena.it/
__ http://www.regione.emilia-romagna.it/
__ http://www.gdf.gov.it/
__ http://www.fe.camcom.it/
__ http://www.ospfe.it/
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
* *Christian Ledermann* (nan010) for providing *Google Video*, *Metacafe* support and, not
  last, very good documentation.
