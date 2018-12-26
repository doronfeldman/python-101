class AlgoResult:
    def __init__(self, is_success, data=None, error=None):
        self._is_success = is_success
        self._data = data
        self._error = error

    def get_is_success(self):
        return self._is_success


class AlgoError:
    def __init__(self):
        self._desc
