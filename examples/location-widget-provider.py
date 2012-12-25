from gi.repository import Caja, Gtk, GObject

class LocationProviderExample(GObject.GObject, Caja.LocationWidgetProvider):
    def __init__(self):
        pass
    
    def get_widget(self, uri, window):
        entry = Gtk.Entry()
        entry.set_text(uri)
        entry.show()
        return entry
