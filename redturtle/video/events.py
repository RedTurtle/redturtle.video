# -*- coding: utf-8 -*-

import tempfile
import urllib2
from urlparse import urlparse

from zope.interface import alsoProvides, noLongerProvides
from zope.component import getMultiAdapter, ComponentLookupError

from collective.flowplayer.interfaces import IFlowPlayable

from redturtle.video.metadataextractor import extract
from redturtle.video.interfaces import IVideoEmbedCode

def _setVideoMetadata(object, name):
    """Set the metadata taken from the video using hachoir
    """
    metadata = extract(name)
    if metadata is not None:
        # duration
        try:
            duration = metadata.getItems('duration')
            if len(duration) >= 1:
                strdate=str(duration[0].value)
                strdate=strdate.split('.')
                strdate=strdate[0]
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
            width = metadata.getItems('width')[0].value
            height = metadata.getItems('height')[0].value
            object.setWidth(width)
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
    file=object.getFile()
    fd=tempfile.NamedTemporaryFile()
    if type(file.data)==str:
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
    url=object.getRemoteUrl()
    response = urllib2.urlopen(url)
    fd=tempfile.NamedTemporaryFile()
    fd.write(response.read())
    _setVideoMetadata(object, fd.name)
    object.reindexObject()
    fd.close()


def externalVideoModified(object, event):
    """A remote video has been modified; check is we need to provide to it
    the IFlowPlayable interface (only if it is Flowplayer compatible)"""
    video_site = urlparse(object.getRemoteUrl())[1].replace('www.','')
    try:
        adapter = getMultiAdapter((object, object.REQUEST), IVideoEmbedCode, name = video_site)
        noLongerProvides(object, IFlowPlayable)
    except ComponentLookupError:
        adapter = getMultiAdapter((object, object.REQUEST), IVideoEmbedCode)            
        alsoProvides(object, IFlowPlayable)
    object.reindexObject(idxs=['object_provides'])

    