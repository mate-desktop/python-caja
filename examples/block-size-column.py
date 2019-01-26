import os

try:
    # Python 3.
    from urllib.parse import unquote
except:
    # Python 2.
    from urllib import unquote

from gi.repository import GObject, Caja

class ColumnExtension(GObject.GObject, Caja.ColumnProvider, Caja.InfoProvider):
    def __init__(self):
        pass
    
    def get_columns(self):
        return Caja.Column(name="CajaPython::block_size_column",
                               attribute="block_size",
                               label="Block size",
                               description="Get the block size"),

    def update_file_info(self, file):
        if file.get_uri_scheme() != 'file':
            return
        
        filename = unquote(file.get_uri()[7:])
        
        file.add_string_attribute('block_size', str(os.stat(filename).st_blksize))
