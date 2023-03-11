
import os
import argparse
import glob


def find_files(directory, name=None, ftype=None):
    search_path = os.path.join(directory, '**', '*' + name if name else '')
    files = glob.glob(search_path, recursive=True)

    if ftype:
        if ftype == 'f':
            files = [f for f in files if os.path.isfile(f)]
        elif ftype == 'd':
            files = [f for f in files if os.path.isdir(f)]
        elif ftype == 'l':
            files = [f for f in files if os.path.islink(f)]

    return files


def main():
    parser = argparse.ArgumentParser(description='A tool for finding files in a directory and its subdirectories')
    parser.add_argument('directory', type=str, help='The directory to search in')
    parser.add_argument('-n', '--name', type=str, help='The name of the file to search for')
    parser.add_argument('-t', '--type', type=str, choices=['f', 'd', 'l'], help='The type of file to search for')
    args = parser.parse_args()

    files = find_files(args.directory, args.name, args.type)

    for file in files:
        print(file)


if __name__ == '__main__':
    main()
