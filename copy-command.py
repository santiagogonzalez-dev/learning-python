# 12:00
import argparse

def copy_directory(src, dest):
    pass

def copy_file(src, dest):
    pass

def cop(src, dest):
    pass

def cli():
    parser = argparse.ArgumentParser(
            prog='cp',
            description='cp command inplementation in Python',
            )
    parser.add_argument(
            'source',
            help="Source directory or file"
            )
    parser.add_argument(
            'destination',
            help="Destination directory or file"
            )
    return parser.parse_args()

def main():
    args = cli()
    print(args)

if __name__ == '__main__':
    main()
