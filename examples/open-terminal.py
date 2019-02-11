# This example is contributed by Martin Enlund
import os

from gi.repository import Caja, GObject, Gio

TERMINAL_SCHEMA = 'org.mate.applications-terminal'
TERMINAL_KEY = 'exec'

class OpenTerminalExtension(Caja.MenuProvider, GObject.GObject):
    def __init__(self):
        self.gsettings = Gio.Settings.new(TERMINAL_SCHEMA)
        
    def _open_terminal(self, file):
        filename = file.get_location().get_path()
        terminal = self.gsettings[TERMINAL_KEY]

        os.chdir(filename)
        os.system('%s &' % terminal)
        
    def menu_activate_cb(self, menu, file):
        self._open_terminal(file)
        
    def menu_background_activate_cb(self, menu, file): 
        self._open_terminal(file)
       
    def get_file_items(self, window, files):
        if len(files) != 1:
            return
        
        file = files[0]
        if not file.is_directory() or file.get_uri_scheme() != 'file':
            return
        
        item = Caja.MenuItem(name='CajaPython::openterminal_file_item',
                                 label='Open Terminal' ,
                                 tip='Open Terminal In %s' % file.get_name())
        item.connect('activate', self.menu_activate_cb, file)
        return [item]

    def get_background_items(self, window, file):
        item = Caja.MenuItem(name='CajaPython::openterminal_item',
                                 label='Open Terminal Here',
                                 tip='Open Terminal In This Directory')
        item.connect('activate', self.menu_background_activate_cb, file)
        return [item]
