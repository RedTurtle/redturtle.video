# -*- coding: utf-8 -*-
import sys
import tempfile
import urllib2
from urlparse import urlparse

from zope.interface import alsoProvides, noLongerProvides
from zope.component import getMultiAdapter, ComponentLookupError

from collective.flowplayer.interfaces import IVideo

from redturtle.video.metadataextractor import extract
from redturtle.video.interfaces import IVideoEmbedCode
from redturtle.video.config import DEFAULT_TIMEOUT

if sys.version_info < (2, 6):
    PLONE4 = False
else:
    PLONE4 = True


def _setVideoMetadata(object, name):
    """Set the metadata taken from the video using hachoir
    """
    metadata = extract(name)
    if metadata is not None:
        # duration
        try:
            duration = metadata.getItems('duration')
            if len(duration) >= 1:
                strdate = str(duration[0].value)
                strdate = strdate.split('.')
                strdate = strdate[0]
                if strdate.startswith('0:'):
                    strdate = '0' + strdate
                object.setDuration(strdate)
        # no valid data
        except ValueError:
            pass
        except IndexError:
            pass

        # size
        try:
            if not object.getWidth():
                width = metadata.getItems('width')[0].value
                object.setWidth(width)
            if not object.getHeight():
                height = metadata.getItems('height')[0].value
                object.setHeight(height)
        # no valid data
        except ValueError:
            pass
        except IndexError:
            pass


def createTempFileInternalVideo(object, event):
    """Create a temporary file for InternalVideo
    """
    if object.getDuration():
        return
    file = object.getFile()
    fd = tempfile.NamedTemporaryFile()
    if type(file.data) == str:
        # *** blob support ***
        fd.write(file.data)
        #name = file.getBlob()._current_filename()
        name = fd.name
    else:
        # *** No blob ***
        fd.write(str(file.data))
        name = fd.name
    _setVideoMetadata(object, name)
    fd.close()
    # noLongerProvides(object, IVideo)
    object.reindexObject()


def createTempFileRemoteVideo(object, event):
    """Create a temporary file for RemoteVideo
    """
    if object.getDuration():
        return
    url = object.getRemoteUrl()
    response = urllib2.urlopen(url)
    fd = tempfile.NamedTemporaryFile()
    fd.write(response.read())
    _setVideoMetadata(object, fd.name)
    object.reindexObject()
    fd.close()


def externalVideoModified(object, event):
    """A remote video has been modified; check is we need to provide to it
    the IFlowPlayable interface (only if it is Flowplayer compatible)"""
    video_site = urlparse(object.getRemoteUrl())[1].replace('www.', '')
    try:
        adapter = getMultiAdapter((object, object.REQUEST),
                                  IVideoEmbedCode,
                                  name=video_site)
        noLongerProvides(object, IVideo)
    except ComponentLookupError:
        adapter = getMultiAdapter((object, object.REQUEST), IVideoEmbedCode)
        alsoProvides(object, IVideo)
    object.reindexObject(idxs=['object_provides'])


def retrieveThumbnail(object, event):
    """
    """
    if object.getImage():
        return

    video_site = urlparse(object.getRemoteUrl())[1].replace('www.', '')

    try:
        adapter = getMultiAdapter((object, object.REQUEST),
                                  IVideoEmbedCode,
                                  name=video_site)
    except ComponentLookupError:
        return

    try:
        thumb_obj = adapter.getThumb()
    except NotImplementedError:
        """
        This means that we are using a plugin not implementing getThumb.
        The fallback it's on the base adapter that raise the exception.
        """
        return

    if PLONE4:
        response = urllib2.urlopen(thumb_obj.url, timeout=DEFAULT_TIMEOUT)
    else:
        response = urllib2.urlopen(thumb_obj.url)

    object.setImage(response.read())
    field = object.getField('image')
    field.setContentType(object, thumb_obj.content_type)
    field.setFilename(object, thumb_obj.filename)
