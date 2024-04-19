from nonogram import Nonogram, NonoLoader

def main():
    source_dir = 'nonfiles/'
    nonofile = 'umbrella.non'
    nonogram = Nonogram()
    try:
        NonoLoader(source_dir, nonofile, nonogram)
    except Exception as e:
        print(f'Error: {e}')
        return

main()