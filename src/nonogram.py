import time

class Nonogram:
    def __init__(self, num_rows = 0, num_cols = 0):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._rows = []
        self._cols = []
        self._grid = []

    def print(self):
        for j in range(self.num_cols):
            outstring = ''
            for i in range(self.num_rows):
                outstring += self._grid[i][j]
            print(outstring)

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
                change_condition = find_changes(self._cols[col], current_col)
                if change_condition[0]:
                    # Mark solutions as non-static
                    static = False
                    # Insert new changes into grid
                    for i in range(self.num_rows):
                        if not change_condition[1][i] == ' ':
                            self._grid[i][col] = change_condition[1][i]

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
        
def construct_line(blocks, spaces, stringlength):
    return_string = ''
    for i in range(len(blocks)):
        return_string += '.' * spaces[i]
        return_string += '@' * blocks[i]
    if stringlength > len(return_string):
        return_string += '.' * (stringlength - len(return_string))
    return return_string

def changes_found(value_array, current_line):
    # if current_line is complete, return False to indicate that no changes were made
    if ' ' not in current_line:
        return [False, current_line]
        
    # If there are no entries in the value array, return a line of blank cells
    if not value_array:
        return [True, '.' * len(current_line)]
        
    # create an array of spaces between blocks
    # spaces after blocks will be added later
    spaces = [0]
    for _ in range(len(value_array) - 1):
        spaces.append(1)

    # Resolve valid entries
    space_location = len(spaces) - 1

    # Store template of possible values
    possible_values = []
    for i in range(len(current_line)):
        possible_values.append('-')

    # Build lines and check for valid entries
    # Create a template to be added to current_line
    while space_location > -1:
        check_string = construct_line(value_array, spaces, len(current_line))
        if len(check_string) > len(current_line):
            space_location -= 1
            for i in range(space_location + 1, len(spaces)):
                spaces[i] = 1
            if space_location > -1:
                spaces[space_location] += 1
        else:
            # Create an initial valid string in possible_values
            for i in range(len(current_line)):
                if possible_values[i] == '-':
                    possible_values[i] = check_string[i]
            valid = True
            for i in range(len(current_line)):
                # Determine if possible_values conflicts with current_line
                if not(current_line[i] == ' ') and possible_values[i] != current_line[i]:
                    print(i, possible_values, current_line)
                    valid = False
            if valid:
                for i in range(len(current_line)):
                    # Remove possible values that could be either . or @
                    if not possible_values[i] == check_string[i]:
                        possible_values[i] = ' '
            space_location = len(spaces) - 1
            spaces[space_location] += 1
        time.sleep(1)

    # create possible_values string
    return_string = ''
    for i in possible_values:
        return_string += i

    # Update change condition with possible values and return
    if '-' in return_string:
        print(return_string)
        raise Exception('changes_found failed to add values correctly')
    return [True, return_string]
