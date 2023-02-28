# Examples: https://github.com/mate-desktop/python-caja/tree/master/examples
#
# This script adds a new menu `Secure delete` to Caja file browser when
# right-mouse clicking on one or more selected files or directories.
#
# Note: Currently there is no Python-Caja example available to configure the
# number of shred iterations via the Preferences, Configure Extension dialog.
# https://github.com/mate-desktop/python-caja/issues/71
#
# Copy this script to a path defined in $XDG_DATA_DIRS, for example:
#   ~/.local/share/caja-python/extensions

import os
import subprocess

import gi
from gi.repository import Caja, GObject, Gio, Gtk


class ShredMenuProvider(GObject.GObject, Caja.MenuProvider):
    # Hard-coded settings
    SHRED_ITERATIONS = 0
    SHRED_EXECUTABLE = 'shred'
    SHRED_ICON = '/usr/share/pixmaps/caja/erase.png'

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
            text="Are you sure you want to shred selected files?",
        )
        dialog.format_secondary_text("WARNING: This cannot be undone!")
        response = dialog.run()
        dialog.destroy()
        if response == Gtk.ResponseType.YES:
            shred_files = ''
            for shred_file in files:
                shred_files += '"{}" '.format(shred_file.get_location().get_path())

            # Start Shred command
            cmd = '{} {} {}'.format(self.SHRED_EXECUTABLE, self.shred_args, shred_files)
            subprocess.check_call(cmd, shell=True)

    def get_file_items(self, window, files):
        top_menuitem = Caja.MenuItem(name='ShredMenuProvider::Shred', 
                                     label='Secure delete', 
                                     tip='Delete files with the Linux "shred" tool',
                                     icon=self.SHRED_ICON)
        top_menuitem.connect('activate', self.menu_activate_cb, files)

        return top_menuitem,

    def get_background_items(self, window, file):
        return None,
