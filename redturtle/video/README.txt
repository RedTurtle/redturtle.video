Introduction
============

A simple video support for Plone, based on `collective.flowplayer`__.

__ http://pypi.python.org/pypi/collective.flowplayer

This add to your Plone portal two new content types:

* *Video file* for providing a video content directly from a video file compatible with flowplayer
  formats
* *Video link* for a remote video resource


Video Link - RTRemoteVideo
--------------------------
We can add a Video link content type to display youtube video in Plone.

First, we must perform some setup.
    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> portal_url = self.portal.absolute_url()
    >>> self.portal.error_log._ignored_exceptions = ()
    >>> from Products.PloneTestCase.setup import portal_owner, default_password

With that in place, we can go to the portal front page and log in. We will
do this using the default user from PloneTestCase:

    >>> browser.open(portal_url)

We move on, to the login page.

    >>> browser.open(portal_url+'/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()

Adding a new RTRemoteVideo content item
---------------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.open(portal_url)
    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Video Link' and click the 'Add' button to get to the add form.
    >>> browser.getControl('Video link').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'RTRemoteVideo' in browser.contents
    True

Now we fill the form and submit it.
    >>> browser.getControl(label='Title').value = 'RTRemoteVideo Sample'
    >>> browser.getControl(label='Description').value = 'RTRemoteVideo short description'
    >>> browser.getControl(label='URL').value = 'http://www.youtube.com/watch?v=f7OLg1AZvr4'

We can add some additional data to video as 'year' and 'duration'
    >>> browser.getControl(label='Year').value = '2007'
    >>> browser.getControl(label='Duration').value = '2.25min'

    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

    >>> print browser.contents
    <!DOCTYPE html PUBLIC...
    ...
    <div class="video-remote">
    <object width="425" height="344">
      <param name="movie"
             value="http://www.youtube.com/v/f7OLg1AZvr4" />
      <param name="allowFullScreen" value="true" />
      <param name="allowscriptaccess" value="always" />
      <embed src="http://www.youtube.com/v/f7OLg1AZvr4"
             type="application/x-shockwave-flash"
             allowscriptaccess="always" allowfullscreen="true"
             width="425" height="344"></embed>
    </object>
    ...
    ...</html>

We can add a screenshot/splash image to display it in listing views
    >>> browser.getLink('Edit').click()
    >>> import cStringIO
    >>> imagefile = cStringIO.StringIO(self.getImage())
    >>> image_control = browser.getControl(name='image_file')
    >>> image_control.add_file(imagefile, 'image/png', 'plone_logo.png')

    >>> browser.getControl('Save').click()
    >>> 'Changes saved.' in browser.contents
    True

Now our video link have a image
    >>> video_link = portal['rtremotevideo-sample']
    >>> video_link.unrestrictedTraverse('image_large')
    <Image... at /plone/rtremotevideo-sample/image_large>

And related views
    >>> browser.open('%s/rtremotevideo-sample/image/image_view_fullscreen' % portal_url)
    >>> print browser.contents
    <!DOCTYPE html PUBLIC...
    ...
    ...<img src="http://nohost/plone/rtremotevideo-sample/image" alt="RTRemoteVideo Sample" title="RTRemoteVideo Sample" height="256" width="256" />...
    ...

How to support additional remote services for Video link
--------------------------------------------------------

We use Metacafe as an example. Metacafe is now part of redturtle.video, but in general you don't need
to modifiy the redturtle.video source for this kind of task.

Goto the video on the videosite::

    http://www.metacafe.com/watch/4950343/stone_trailer/

Select embed video and copy the embedcode::

    <div style="background:#000000;width:440px;height:272px">
    <embed flashVars="playerVars=showStats=yes|autoPlay=no|videoTitle=STONE: Trailer"
           src="http://www.metacafe.com/fplayer/4950343/stone_trailer.swf"
           width="440" height="272" wmode="transparent" allowFullScreen="true"
           allowScriptAccess="always" name="Metacafe_4950343"
           pluginspage="http://www.macromedia.com/go/getflashplayer"
           type="application/x-shockwave-flash">
    </embed></div>
    <div style="font-size:12px;">
    <a href="http://www.metacafe.com/watch/4950343/stone_trailer/">STONE: Trailer</a>.
    Watch more top selected videos about:
    <a href="http://www.metacafe.com/topics/Robert_De_Niro/" title="Robert_De_Niro">Robert De Niro</a>,
    <a href="http://www.metacafe.com/topics/Stone_(2010_film)/"
       title="Stone_(2010_film)">Stone (2010 film)</a>
    </div>

Get rid of all markup that is not really needed to embed the video::

    <embed
        src="http://www.metacafe.com/fplayer/4950343/stone_trailer.swf"
        width="440"
        height="272"
        allowFullScreen="true"
        allowScriptAccess="always"
        type="application/x-shockwave-flash">
        </embed>

Now create your package, like *collective.rtvideo.metacafe* (again, remember this is an example).

In this prodoct, like redturtle.video does, create a new template like *metacafeembedcode_template.pt*::

    <embed id=VideoPlayback
    width="440"
    height="272"
    tal:attributes="src view/getVideoLink"
    allowFullScreen="true"
    allowScriptAccess="always"
    type="application/x-shockwave-flash" />

Create also a *videoembedcode.py* and add a new class *MetacafeEmbedCode*.

Copy and paste from the classes you'll find in *redturtle.video*.
The main task is to find out how to translate the URL on the site to the
url of the embedded video. For Metacafe the getVideoLink method looks like this::

    def getVideoLink(self):
        qs = urlparse(self.context.getRemoteUrl())[-2]
        return 'http://www.metacafe.com/fplayer/%s/%s.swf' % qs

Now configure your adapter for your embed code::

    <adapter
	      for = "redturtle.video.interfaces.IRTRemoteVideo
	             zope.publisher.interfaces.browser.IHTTPRequest"
	      provides = "redturtle.video.interfaces.IVideoEmbedCode"
	      factory = "redturtle.video.browser.videoembedcode.MetacafeEmbedCode"
	      name= 'www.metacafe.com'
	  />


write some tests that everything is OK and thats it ;-)

