# Examples: https://github.com/mate-desktop/python-caja/tree/master/examples

import os

from gi.repository import Caja, GObject


class MeldMenuProvider(GObject.GObject, Caja.MenuProvider):
    MELD_EXECUTABLE = 'meld'
    MELD_ICON = '/usr/share/icons/hicolor/scalable/apps/org.gnome.Meld.svg'

    def __init__(self):
        pass
    
    def menu_activate_cb(self, menu, files=None):
        args = ''

        if files and len(files):           
            # Set working directory
            os.chdir(os.path.dirname(files[0].get_location().get_path()))
            
            # Start Meld with 1..3 files or directories
            for i in range(0, 3):
                if i >= len(files):
                    break
                args += '"{}" '.format(files[i].get_location().get_path())
        
        # Start Meld
        cmd = '{} {} &'.format(self.MELD_EXECUTABLE, args)
        os.system(cmd)

    def get_file_items(self, window, files):
        top_menuitem = Caja.MenuItem(name='MeldMenuProvider::Meld', 
                                     label='Meld compare', 
                                     tip='',
                                     icon=self.MELD_ICON)
        top_menuitem.connect('activate', self.menu_activate_cb, files)

        return top_menuitem,

    def get_background_items(self, window, file):
        bg_menuitem_meld = Caja.MenuItem(name='MeldMenuProvider::MeldBg', 
                                         label='Meld', 
                                         tip='',
                                         icon=self.MELD_ICON)
        bg_menuitem_meld.connect('activate', self.menu_activate_cb)

        return bg_menuitem_meld,
