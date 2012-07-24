# -*- coding: utf-8 -*-


class RemoteThumb(object):
    """
    An object with thumbnail infos
    """
    def __init__(self, url, content_type, filename):
        self.url = url
        self.content_type = content_type
        self.filename = filename
