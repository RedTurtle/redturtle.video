#from hachoir_parser.guess import createParser
#from hachoir_metadata.metadata import extractMetadata
#from hachoir_core.error import HachoirError
#from hachoir_core.stream import InputStreamError

# Includes above someway broke the stdout when used at module level

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
        print "stream error! %s\n" % unicode(err)
        return None

    if not parser:
        print "Unable to create parser.\n"
        return None
    try:
        metadata = extractMetadata(parser)
    except HachoirError, err:
        print "stream error! %s\n" % unicode(err)
        return None

    if metadata is None:
        print "unable to extract metadata.\n"
        return None

    return metadata
