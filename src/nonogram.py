class Nonogram:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._rows = []
        self._cols = []
        self._grid = []

    def validate_structure(self):
        pass