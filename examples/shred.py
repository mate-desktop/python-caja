# Examples: https://github.com/mate-desktop/python-caja/tree/master/examples
#
# This script adds a new menu `Secure delete` to Caja file browser when
# right-mouse clicking on one or more selected files or directories.
# See the used shred command in the statusbar.
#
# WARNING: THIS IS AN EXAMPLE SCRIPT AND THE USER IS RESPONSIBLE
# FOR SHREDDING THE FULL SSD OR HARD DRIVE WHEN ABSOLUTE SECURITY IS
# REQUIRED!
#
# The Linux tool `shred` is used to shred files by filling files with
# zero's or random data and removes filenames. Overwriting files
# multiple times has no effect on SSD's and decreases lifetime. It
# should be used for mechanical hard drives only.
#
# Copy this script to a path defined in $XDG_DATA_DIRS, for example:
#   ~/.local/share/caja-python/extensions

import os
import subprocess

import gi
from gi.repository import Caja, GObject, Gio, Gtk


class ShredMenuProvider(GObject.GObject, Caja.MenuProvider):
    SHRED_ICON = '/usr/share/pixmaps/caja/erase.png'

    def __init__(self):
        pass

    def menu_activate_cb(self, menu, data):
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
            cmd = data['cmd']
            for shred_file in data['files']:
                cmd += ' "{}"'.format(shred_file.get_location().get_path())

            # Start Shred command
            subprocess.check_call(cmd, shell=True)

    def get_file_items(self, window, files):
        top_menuitem = Caja.MenuItem(name='ShredMenuProvider::Shred',
                                     label='Secure delete',
                                     tip='Delete files with the Linux "shred" tool',
                                     icon=self.SHRED_ICON)

        shred_submenu = Caja.Menu()
        top_menuitem.set_submenu(shred_submenu)

        # Shred fill zero's
        shred_cmd = 'shred -uz -n 0'
        shred_1x_zero_menuitem = Caja.MenuItem(name='ShredMenuProvider::Shred1xZero',
                                               label='Fill zero\'s',
                                               tip=shred_cmd + ' FILE... (NOT SECURE!)',
                                               icon=self.SHRED_ICON)
        shred_1x_zero_menuitem.connect('activate', self.menu_activate_cb, {'cmd': shred_cmd, 'files': files})
        shred_submenu.append_item(shred_1x_zero_menuitem)

        # Shred fill random
        shred_cmd = 'shred -u -n 1'
        shred_1x_random_menuitem = Caja.MenuItem(name='ShredMenuProvider::Shred1xRandom',
                                                 label='Fill random',
                                                 tip=shred_cmd + ' FILE... (NOT SECURE!)',
                                                 icon=self.SHRED_ICON)
        shred_1x_random_menuitem.connect('activate', self.menu_activate_cb, {'cmd': shred_cmd, 'files': files})
        shred_submenu.append_item(shred_1x_random_menuitem)

        # Shred 3x overwrite, last zero's
        shred_cmd = 'shred -uz'
        shred_3x_zero_menuitem = Caja.MenuItem(name='ShredMenuProvider::Shred3xLastZero',
                                               label='3x overwrite, last zero\'s',
                                               tip=shred_cmd + ' FILE... (HDD\'s only!)',
                                               icon=self.SHRED_ICON)
        shred_3x_zero_menuitem.connect('activate', self.menu_activate_cb, {'cmd': shred_cmd, 'files': files})
        shred_submenu.append_item(shred_3x_zero_menuitem)

        # Shred 3x overwrite (default)
        shred_cmd = 'shred -u'
        shred_3x_random_menuitem = Caja.MenuItem(name='ShredMenuProvider::Shred3x',
                                                 label='3x overwrite (Default)',
                                                 tip=shred_cmd + ' FILE... (HDD\'s only!)',
                                                 icon=self.SHRED_ICON)
        shred_3x_random_menuitem.connect('activate', self.menu_activate_cb, {'cmd': shred_cmd, 'files': files})
        shred_submenu.append_item(shred_3x_random_menuitem)

        return top_menuitem,

    def get_background_items(self, window, file):
        return None,
