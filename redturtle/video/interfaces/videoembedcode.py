from zope.interface import Interface


class IVideoEmbedCode(Interface):
    """Marker interface to provide a video embed html code"""

    def getVideoLink():
        """Return a link to the remote video resource"""
    
    def getWidth():
        """Obtain video width in pixel"""

    def getHeight():
        """Obtain video height in pixel"""

