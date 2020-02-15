import argparse
import typing
import os, sys

import gloomtools.image

def _hex_to_rgb(c: str) -> typing.Tuple[int,int,int]:
    color = c.strip('#')
    return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

def main(argv=None):
    if not argv:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', default=None)
    parser.add_argument('--tint', default='#808080')
    parser.add_argument('--version', default=None)
    parser.add_argument('--name', default=None)
    parser.add_argument('ability_file')

    args = parser.parse_args()

    if not os.path.exists(args.ability_file):
        print(f'No ability file {args.ability_file} exists, exiting...')
        return 1

    character_name = args.name if args.name else input('Character name? ')
    version = version if args.version else '1.0'
    print(f'Generating version {version} ability cards for {character_name}...')

    output_dir = args.output_dir if args.output_dir else os.path.join(os.getcwd(), character_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f'Saving output to {output_dir}')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))