# This Python caja extension only consider files/folders with a mixed
# upper/lower case name. For those, the following is featured:
# - an emblem on the icon,
# - contextual menu entry.
# - a list view "Mixed" column,
# - a property page,
# - A top area widget.

import os

try:
    # Python 3.
    from urllib.parse import unquote, urlparse
except:
    # Python 2.
    from urllib import unquote
    from urlparse import urlparse

from gi.repository import Caja, GObject, Gtk


class Mixed(GObject.GObject,
                Caja.InfoProvider,
                Caja.ColumnProvider,
                Caja.MenuProvider,
                Caja.PropertyPageProvider,
                Caja.LocationWidgetProvider):

    emblem = 'favorite-symbolic.symbolic'       # Use one of the stock emblems.

    # Private methods.

    def _basename(self, uri):
        try:
            uri = uri.get_uri()         # In case a CajaFile is given.
        except:
            pass
        (scheme, netloc, path, parameters, query, fragment) = urlparse(uri)
        return os.path.basename(unquote(path))

    def _file_has_mixed_name(self, cajafile):
        name = self._basename(cajafile)
        if name.upper() != name and name.lower() != name:
            return 'mixed'
        return ''

    # Caja.InfoProvider implementation.

    def update_file_info(self, cajafile):
        mixed = self._file_has_mixed_name(cajafile)
        cajafile.add_string_attribute('mixed', mixed)
        if mixed:
            cajafile.add_emblem(self.emblem)

    # Caja.ColumnProvider implementation.

    def get_columns(self):
        return [
            Caja.Column(
                name        = 'Mixed::mixed_column',
                attribute   = 'mixed',
                label       = 'Mixed',
                description = 'Column added by the mixed extension'
            )
        ]

    # Caja.MenuProvider implementation.

    def get_file_items(self, window, cajafiles):
        menuitems = []
        if len(cajafiles) == 1:
            for cajafile in cajafiles:
                mixed = cajafile.get_string_attribute('mixed')
                if mixed:
                    filename = self._basename(cajafile)
                    menuitem = Caja.MenuItem(
                        name  = 'Mixed::FileMenu',
                        label = 'Mixed: %s has a mixed case name' % filename,
                        tip   = '',
                        icon  = ''
                    )
                    menuitems.append(menuitem)

        return menuitems

    def get_background_items(self, window, folder):
        mixed = self._file_has_mixed_name(folder)
        if not mixed:
            return []
        return [
            Caja.MenuItem(
                name  = 'Mixed::BackgroundMenu',
                label = 'Mixed: you are browsing a directory with a mixed case name',
                tip   = '',
                icon  = ''
            )
        ]

    # Caja.PropertyPageProvider implementation.

    def get_property_pages(self, cajafiles):
        pages = []
        if len(cajafiles) == 1:
            for cajafile in cajafiles:
                if self._file_has_mixed_name(cajafile):
                    page_label = Gtk.Label('Mixed')
                    page_label.show()
                    hbox = Gtk.HBox(homogeneous = False, spacing = 4)
                    hbox.show()
                    name_label = Gtk.Label(self._basename(cajafile))
                    name_label.show()
                    comment_label = Gtk.Label('has a mixed-case name')
                    comment_label.show()
                    hbox.pack_start(name_label, False, False, 0)
                    hbox.pack_start(comment_label, False, False, 0)
                    pages.append(
                        Caja.PropertyPage(
                            name  = 'Mixed::PropertyPage',
                            label = page_label,
                            page  = hbox
                        )
                    )

        return pages

    # Caja.LocationWidgetProvider implementation.

    def get_widget(self, uri, window):
        filename = self._basename(uri)
        if not self._file_has_mixed_name(filename):
            return None
        label = Gtk.Label('In mixed-case directory %s' % filename)
        label.show()
        return label
