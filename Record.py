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

    def __str__(self):
        text = f"Title: {self.title} Score: {self.score} "
        return text

    def __repr__(self):
        repr_text = f"<Title: {self.title} Score: {self.score} >"
        return repr_text