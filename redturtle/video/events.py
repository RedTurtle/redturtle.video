import tempfile
import urllib2
from redturtle.video.metadataextractor import extract

def _setDurationVideo(object, name):
    """Set the duration field of video
    """
    metadata = extract(name)
    if metadata is not None:
        try:
            data = metadata.getItems('duration')
        except ValueError, e:
            # no valid data
            return
        if len(data) >= 1:
            strdate=str(data[0].value)
            strdate=strdate.split('.')
            strdate=strdate[0]
            object.setDuration(strdate)
            
def createTempFileInternalVideo(object, event):
    """Create a temporary file for InternalVideo
    """
    if object.getDuration():
        return
    file=object.getFile()
    fd=tempfile.NamedTemporaryFile()
    fd.write(file.data.data)
    _setDurationVideo(object,fd.name)
    object.reindexObject()
    fd.close()
    
def createTempFileRemoteVideo(object, event):
    """Create a temporary file for RemoteVideo
    """
    if object.getDuration():
        return
    url=object.getRemoteUrl()
    response = urllib2.urlopen(url)
    fd=tempfile.NamedTemporaryFile()
    fd.write(response.read())
    _setDurationVideo(object,fd.name)
    object.reindexObject()
    fd.close()

    