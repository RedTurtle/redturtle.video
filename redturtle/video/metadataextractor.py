#from hachoir_parser.guess import createParser
#from hachoir_metadata.metadata import extractMetadata
#from hachoir_core.error import HachoirError
#from hachoir_core.stream import InputStreamError

# Includes above someway broke the stdout when used at module level

from redturtle.video import logger

def extract(filename):
    """Extract the metadata from the media file"""

    from hachoir_parser.guess import createParser
    from hachoir_metadata.metadata import extractMetadata
    from hachoir_core.error import HachoirError
    from hachoir_core.stream import InputStreamError

    filename = unicode(filename)

    try:
        parser = createParser(filename)
    except InputStreamError, err:
        logger.warning("Stream error! %s" % unicode(err))
        return None

    if not parser:
        logger.warning("Unable to create parser.")
        return None
    try:
        metadata = extractMetadata(parser)
    except HachoirError, err:
        logger.warning("Stream error! %s" % unicode(err))
        return None

    if metadata is None:
        logger.warning("unable to extract metadata.")
        return None

    return metadata
