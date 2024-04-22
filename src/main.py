import sys
from nonogram import Nonogram, NonoLoader
from nonogram import changes_found

def main():
    source_dir = sys.argv[1] + '/'
    nonofile = sys.argv[2]
    nonogram = Nonogram()
    
    # Load the Nonogram
    try:
        NonoLoader(source_dir, nonofile, nonogram)
    except Exception as e:
        print(f'Error: {e}')
        return
    
    print("3,1,3 into '          '")
    print(changes_found([3,1,3], '          '))
    print("3,1,3 into '.         '")
    print(changes_found([3,1,3], '.         '))
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

    nonogram.print()

main()