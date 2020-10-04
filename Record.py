class Record:
    def __init__(self, title, score):
        self.title = title
        self._score = score

    @property
    def score(self):
        return self._score
    
    @staticmethod
    def get_score(record):
        return record.score