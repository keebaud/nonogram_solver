import sys
from nonogram import Nonogram, NonoLoader

def main():
    source_dir = sys.argv[1] + '/'
    nonofile = sys.argv[2]
    print(source_dir + nonofile)
    #source_dir = 'nonfiles/'
    #nonofile = 'corners.non'
    nonogram = Nonogram()
    
    # Load the Nonogram
    try:
        NonoLoader(source_dir, nonofile, nonogram)
    except Exception as e:
        print(f'Error: {e}')
        return
    
    # Try to solve the Nonogram
    try:
        nonogram.solve()
    except Exception as e:
        print(f"Cannot solve Nonogram: {e}")
        return
    
    if nonogram.complete():
        print('Nonogram completed')
    else:
        print('Unable to complete Nonogram')

    for j in range(nonogram.num_cols):
        outstring = ''
        for i in range(nonogram.num_rows):
            outstring += nonogram._grid[i][j]
        print(outstring)

main()