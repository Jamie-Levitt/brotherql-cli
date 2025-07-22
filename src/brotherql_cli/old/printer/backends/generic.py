class BrotherQLBackendGeneric(object):
    def __init__(self, device_specifier):
        """
        device_specifier can be either a string or an instance
        of the required class type.
        """
        self.write_dev = None
        self.read_dev  = None
        raise NotImplementedError()

    def _write(self, data):
        self.write_dev.write(data) # type: ignore

    def _read(self, length=32):
        return bytes(self.read_dev.read(length)) # type: ignore

    def write(self, data):
        self._write(data)

    def read(self, length=32):
        try:
            ret_bytes = self._read(length)
            return ret_bytes
        except Exception as e:
            raise e

    def dispose(self):
        try:
            self._dispose()
        except:
            pass

    def _dispose(self):
        raise NotImplementedError()

    def __del__(self):
        self.dispose()