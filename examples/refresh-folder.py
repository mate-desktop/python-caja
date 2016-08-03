import os

from gi.repository import Caja, GObject


class RefreshFolderExtension(Caja.MenuProvider, GObject.GObject):
    def __init__(self):
        pass
        
    def menu_background_activate_cb(self, menu, file): 
        os.system("xte 'keydown F5' 'keyup F5'")
       
    def get_background_items(self, window, file):
        item = Caja.MenuItem(name='CajaPython::refreshfolder_item',
                             label='Refresh',
                             tip='Reload current folder')
        item.connect('activate', self.menu_background_activate_cb, file)
        return item,
