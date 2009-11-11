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

TODO
----

Right now year and duration are not displayed in the video view.

Other products
==============

**AKA: are you sure you wanna use me?**

If you are using *Plone 3.3* or better, before us this product, take a look at
`Plone Video Suite`__.
The redturtle.video product was developed in sad days, when the only choice was
p4a.video (and this scare us a lot). The Plone Video Suite can became the next generation,
unified, product to use video contents inside Plone!

__ http://www.coactivate.org/projects/plone-video-sprint/project-home

