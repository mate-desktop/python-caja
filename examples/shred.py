# Examples: https://github.com/mate-desktop/python-caja/tree/master/examples
#
# Note: Currently there is no Python-Caja example available to configure the
# number of shred iterations via the Preferences, Configure Extension dialog.
# https://github.com/mate-desktop/python-caja/issues/71

import os

import gi
from gi.repository import Caja, GObject, Gio, Gtk


class ShredMenuProvider(GObject.GObject, Caja.MenuProvider):
    # Hard-coded settings
    SHRED_ITERATIONS = 0
    SHRED_EXECUTABLE = 'shred'
    SHRED_ICON = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'icons/shred.png')

    def __init__(self):
        self.shred_args = '-uz -n {}'.format(self.SHRED_ITERATIONS)

    def menu_activate_cb(self, menu, files):
        if not files or not len(files):
            return

        dialog = Gtk.MessageDialog(
            parent=None,
            flags=0,
            message_type=Gtk.MessageType.QUESTION,
            buttons=Gtk.ButtonsType.YES_NO,
            text="Are you sure to shred files?",
        )
        dialog.format_secondary_text("WARNING: This cannot be undone!")
        response = dialog.run()
        dialog.destroy()
        if response == Gtk.ResponseType.NO:
            return

        shred_files = ''
        for shred_file in files:
            shred_files += '"{}" '.format(shred_file.get_location().get_path())
  
        # Start Shred
        cmd = '{} {} {}'.format(self.SHRED_EXECUTABLE, self.shred_args, shred_files)

        # Save command for debugging
        # with open('/tmp/shred.txt', 'w') as f:
        #     f.write(cmd)

        # Start Shred command
        os.system(cmd)

    def get_file_items(self, window, files):
        top_menuitem = Caja.MenuItem(name='ShredMenuProvider::Shred', 
                                     label='Secure delete', 
                                     tip='',
                                     icon=self.SHRED_ICON)
        top_menuitem.connect('activate', self.menu_activate_cb, files)

        return top_menuitem,

    def get_background_items(self, window, file):
        return None,
