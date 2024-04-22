# Nonogram_solver

This application is created as part of the BOOT.DEV Personal Project 1 exercise

The intention of this program is to open a file containing the structure of a nonogram
and to attempt to solve the nonogram. A visual representation of the solution will be
provided. The program is developed in Python, eventually using tkinker frameword for
graphical feedback.

The format will be *filename*.non

> num_rows, num_cols
> row1, row2, ..., row_num_rows
> col1, col2, ..., col_num_cols

Each line will be formatted as:
> 0            - blank line
> n            - single solid line
> n1:n2:...:nx - broken line with x segments

The program will check each possible arrangement for each row and column
and find fixed positions that are either blank or solid. These will be marked
and added as restrictions for the other rows and columns.

In a well constructed nonogram, this should result in a solution. There are probably
more complex cases which will not work with this solution, but they can be addressed
at a future time.

I chose this project as I enjoy doing nonograms in my spare time and this follows on
quite well I feel from previous BOOT.DEV exercises.