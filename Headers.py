class Headers:

    def __init__(self, headers_limit, from_best=True):
        self.headers_limit = headers_limit
        self.from_best = from_best

        self._records = []

    @property
    def records(self):
        return self._records

    def add_record(self, record=None):
        if record is not None:
            self.records.append(record)