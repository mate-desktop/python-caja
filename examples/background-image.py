SUPPORTED_FORMATS = 'image/jpeg', 'image/png'
BACKGROUND_SCHEMA = 'org.mate.background'
BACKGROUND_KEY = 'picture-filename'

try:
    # Python 3.
    from urllib.parse import unquote, urlparse
except:
    # Python 2.
    from urllib import unquote
    from urlparse import urlparse

from gi.repository import Caja, GObject, Gio


class BackgroundImageExtension(GObject.GObject, Caja.MenuProvider):
    def __init__(self):
        self.bgsettings = Gio.Settings.new(BACKGROUND_SCHEMA)
    
    def _filepath(self, file):
        try:
            file = file.get_uri()
        except:
            pass
        (scheme, netloc, path, parameters, query, fragment) = urlparse(file)
        if scheme and unquote(scheme) != 'file':
            return None
        return unquote(path)

    def menu_activate_cb(self, menu, file):
        if file.is_gone():
            return
        
        self.bgsettings[BACKGROUND_KEY] = self._filepath(file)
        
    def get_file_items(self, window, files):
        if len(files) != 1:
            return

        file = files[0]

        # We're only going to put ourselves on images context menus
        if not file.get_mime_type() in SUPPORTED_FORMATS:
            return

        # Mate can only handle file:
        # In the future we might want to copy the file locally
        if file.get_uri_scheme() != 'file':
            return

        item = Caja.MenuItem(name='Caja::set_background_image',
                                 label='Use as background image',
                                 tip='Set the current image as a background image')
        item.connect('activate', self.menu_activate_cb, file)
        return item,

    def get_background_items(self, window, file):
        return []
