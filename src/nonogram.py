import os

class Nonogram:
    def __init__(self, num_rows = 0, num_cols = 0):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._rows = []
        self._cols = []
        self._grid = []

    def validate_structure(self):
        pass

class NonoLoader:
    def __init__(self, source_dir, nonofile, new_nonogram):
        
        # Load file into nonoarray for processing
        nonoarray = [line.strip().split(',') for line in open(source_dir + nonofile, 'r')]
        
        # Initialize Nonogram with checks
        if not nonoarray:
            raise Exception('Empty file found')
        if not len(nonoarray[0]) == 2:
            raise Exception('Nonogram dimensions not defined correctly')
        new_nonogram.num_rows = int(nonoarray[0][0])
        new_nonogram.num_cols = int(nonoarray[0][1])
        if not len(nonoarray[1]) == new_nonogram.num_rows:
            raise ValueError(f'Incorrect number of rows detected in file {nonofile}.\r\nExpected {new_nonogram.num_rows}, found {len(nonoarray[1])}')
        if not len(nonoarray[2]) == new_nonogram.num_cols:
            raise ValueError(f'Incorrect number of columns detected in file {nonofile}\r\nExpected {new_nonogram.num_cols}, found {len(nonoarray[2])}')
        
        for row in nonoarray[1]:
            if row == '0':
                new_nonogram._rows.append([])
            else:
                new_nonogram._rows.append([int(x) for x in row.split(':')])

        for col in nonoarray[2]:
            if col == '0':
                new_nonogram._cols.append([])
            else:
                new_nonogram._cols.append([int(x) for x in col.split(':')])