SUPPORTED_FORMATS = 'image/jpeg', 'image/png'
BACKGROUND_SCHEMA = 'org.mate.background'
BACKGROUND_KEY = 'picture-filename'

from gi.repository import Caja, GObject, Gio


class BackgroundImageExtension(GObject.GObject, Caja.MenuProvider):
    def __init__(self):
        self.bgsettings = Gio.Settings.new(BACKGROUND_SCHEMA)
    
    def menu_activate_cb(self, menu, file):
        if file.is_gone():
            return

        if file.get_uri_scheme() == 'file':
            self.bgsettings[BACKGROUND_KEY] = file.get_location().get_path()
        
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
        return [item]

    def get_background_items(self, window, file):
        return []
