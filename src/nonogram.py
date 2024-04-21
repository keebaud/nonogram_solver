import os

class Nonogram:
    def __init__(self, num_rows = 0, num_cols = 0):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._rows = []
        self._cols = []
        self._grid = []

    def solve(self):
        # Check each horizontal and vertical line in turn
        # If a change is made, mark it on the grid
        # If no changes are made for both horizontal or vertical
        # then the puzzle is either solved of unsolvable

        static = False
        while not static:
            static = True
            # Extract the current row from the grid
            for row in range(self.num_rows):
                current_row = ''
                for j in range(self.num_cols):
                    current_row += self._grid[row][j]
                # Analyse clues to find new values and place them in current_row
                change_condition = self.changes_found(self._rows[row], current_row)
                if change_condition[0]:
                    # Mark solutions as non-static
                    static = False
                    # Insert new changes into grid
                    for j in range(self.num_cols):
                        if not change_condition[1][j] == ' ':
                            self._grid[row][j] = change_condition[1][j]

            # Extract the current column from the grid
            for col in range(self.num_cols):
                current_col = ''
                for i in range(self.num_rows):
                    current_col += self._grid[i][col]
                # Analyse clues to find new values and place them in current_row
                change_condition = self.changes_found(self._cols[col], current_col)
                if change_condition[0]:
                    # Mark solutions as non-static
                    static = False
                    # Insert new changes into grid
                    for i in range(self.num_rows):
                        if not change_condition[1][i] == ' ':
                            self._grid[i][col] = change_condition[1][i]

    def changes_found(self, value_array, current_line):
        change_condition = [False, current_line]

        # if current_line is complete, return False to indicate that no changes were made
        if ' ' not in current_line:
            return change_condition
        
        # If there are no entries in the value array, return a line of blank cells
        if not value_array:
            change_condition[0] = True
            change_condition[1] = '.' * len(current_line)
            return change_condition
        
        # create an array of spaces between blocks
        # spaces after blocks will be added later
        spaces = [0]
        for _ in range(len(value_array) - 1):
            spaces.append(1)

        # Resolve valid entries
        space_location = len(spaces) - 1

        ### Code to be added here ###


        ###
        
        # Return change_condition by default
        return change_condition

    def complete(self):
        for j in range(self.num_cols):
            for i in range(self.num_rows):
                if self._grid[i][j] == ' ':
                    return False
        return True


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
        
        # Create unsolved grid
        # ' ' == unsolved cell
        # '.' == blank cell
        # '@' == filled cell

        for i in range(new_nonogram.num_cols):
            new_nonogram._grid.append([])
            for j in range(new_nonogram.num_rows):
                new_nonogram._grid[i].append(' ')

        cell_count = 0
        
        for row in nonoarray[1]:
            if row == '0':
                new_nonogram._rows.append([])
            else:
                new_nonogram._rows.append([int(x) for x in row.split(':')])

        # Count filled in cells in completed nonogram
        for line in new_nonogram._rows:
            for section in line:
                cell_count += section
        
        for col in nonoarray[2]:
            if col == '0':
                new_nonogram._cols.append([])
            else:
                new_nonogram._cols.append([int(x) for x in col.split(':')])

        # Subtract filled in cells in completed nonogram. If matching, result should be 0
        for line in new_nonogram._cols:
            for section in line:
                cell_count -= section

        if not cell_count == 0:
            raise ValueError('Number of filled cells do not match rows and columns')