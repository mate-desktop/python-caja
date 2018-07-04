import os
import os.path
import urllib

from gi.repository import Caja, GObject, Gio


class OpenSymLinksParentDirsExtension(Caja.MenuProvider, GObject.GObject):
    def __init__(self):
        pass

    def _open_parent_dir(self, files):
        for f in files:
            # find the real location of the file (resolves all symlinks)
            path = os.path.realpath(f.get_location().get_path())
            parent = os.path.abspath(os.path.join(path, os.pardir))
            os.system('caja "%s" &' % parent)
        
    def menu_activate_cb(self, menu, files):
        self._open_parent_dir(files)

    def get_file_items(self, window, files):
        if any(f.is_directory() or not self.is_symbolic_link(f) for f in files):
            return
        
        if len(files) == 1:
            lbl = "Open Link's Parent Directory"
        else:
            lbl = "Open Links' Parent Directories"

        item = Caja.MenuItem(name='CajaPython::open_symlink_parent_dirs_item',
                                 label=lbl,
                                 tip=lbl)
        item.connect('activate', self.menu_activate_cb, files)
        return item,

    def is_symbolic_link(self, f):
        f_type = f.get_location().query_file_type(Gio.FileQueryInfoFlags.NOFOLLOW_SYMLINKS)
        return f_type is Gio.FileType.SYMBOLIC_LINK

    def get_background_items(self, window, file):
        return tuple()
