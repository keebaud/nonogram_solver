import unittest

from nonogram import ( Nonogram,
                      NonoLoader,
                      construct_line,
                      find_changes
)


class Tests(unittest.TestCase):

    def test_nonogram_create(self):
        source_dir = 'testfiles/'
        nonofile = 'hut.non'
        ntest = Nonogram()
    
        NonoLoader(source_dir, nonofile, ntest)

        testgrid = []
        for i in range(ntest.num_rows):
            add_row = []
            for j in range(ntest.num_cols):
                add_row.append(' ')
            testgrid.append(add_row)
        
        # Test blank structure
        self.assertEqual(ntest.num_rows, 8)
        self.assertEqual(ntest.num_cols, 7)
        self.assertEqual(ntest._grid, testgrid)

    def test_construct_line(self):
        blocks = [1,3,1]
        spaces = [2,1,3]
        test_line = construct_line(blocks, spaces, 12)
        self.assertEqual('..@.@@@...@.', test_line)

    def test_construct_line_overflow(self):
        blocks = [1,3,1]
        spaces = [5,1,3]
        test_line = construct_line(blocks, spaces, 12)
        self.assertEqual('.....@.@@@...@', test_line)

    def test_find_changes_blank(self):
        value_line = [3,1,3]
        current_line = '          '
        test_line = find_changes(value_line, current_line)
        self.assertEqual([True,' @@    @@ '], test_line)

    def test_find_changes_populated(self):
        value_line = [3,1,3]
        current_line = '.         '
        test_line = find_changes(value_line, current_line)
        self.assertEqual([True,'.@@@.@.@@@'], test_line)

    def test_find_changes_conflict(self):
        value_line = [3,1,3]
        current_line = '.        .'
        with self.assertRaises(Exception):
            test_line = find_changes(value_line, current_line)

    def test_find_no_changes(self):
        value_line = [3,1,3]
        current_line = '@@@.@.@@@.'
        test_line = find_changes(value_line, current_line)
        self.assertEqual([False, '@@@.@.@@@.'], test_line)

    def test_nonogram_solve(self):
        source_dir = 'testfiles/'
        nonofile = 'hut.non'
        ntest = Nonogram()
    
        NonoLoader(source_dir, nonofile, ntest)

        ntest.solve()

        testgrid = []
        testgrid.append(['.', '.', '@', '@', '@', '.', '.'])
        testgrid.append(['.', '@', '.', '.', '.', '@', '.'])
        testgrid.append(['@', '@', '@', '@', '@', '@', '@'])
        testgrid.append(['@', '.', '.', '.', '.', '.', '@'])
        testgrid.append(['@', '.', '@', '@', '@', '.', '@'])
        testgrid.append(['@', '.', '@', '.', '@', '.', '@'])
        testgrid.append(['@', '.', '@', '.', '@', '.', '@'])
        testgrid.append(['@', '@', '@', '@', '@', '@', '@'])

        # Test completed structure
        self.assertEqual(ntest._grid, testgrid)

if __name__ == "__main__":
    unittest.main()