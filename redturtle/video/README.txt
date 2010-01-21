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

We have the login portlet, so let's use that.

    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()

Adding a new RTRemoteVideo content item
--------------------------------

We use the 'Add new' menu to add a new content item.

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
    <Image at /plone/rtremotevideo-sample/image_large>

And related views
    >>> browser.open('%s/rtremotevideo-sample/image/image_view' % portal_url)
    >>> print browser.contents
    <!DOCTYPE html PUBLIC...
    ...
    <img src="http://nohost/plone/rtremotevideo-sample/image_preview" alt="RTRemoteVideo Sample" title="RTRemoteVideo Sample" height="256" width="256" />
    ...
    ...</html>

