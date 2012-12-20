from gi.repository import Caja, GObject

class UpdateFileInfoAsync(GObject.GObject, Caja.InfoProvider):
    def __init__(self):
        pass
    
    def update_file_info_full(self, provider, handle, closure, file):
        print "update_file_info_full"
        gobject.timeout_add_seconds(3, self.update_cb, provider, handle, closure)
        return Caja.OperationResult.IN_PROGRESS
        
    def update_cb(self, provider, handle, closure):
        print "update_cb"
        Caja.info_provider_update_complete_invoke(closure, provider, handle, Caja.OperationResult.FAILED)
