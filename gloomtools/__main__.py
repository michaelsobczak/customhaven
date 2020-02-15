import argparse
import typing
import os, sys
import csv
from gloomtools.image import draw_ability_card

from PIL import Image

def _hex_to_rgb(c: str) -> typing.Tuple[int,int,int]:
    color = c.strip('#')
    return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))


# draw_ability_card(title: str, initiative: int, toplines: List[str], bottomlines: List[str], color) 

def parse_abilities_file(path: str, tint: typing.Tuple[int,int,int]):
    cards = []
    with open(path, 'r') as abilities_file:
        reader = csv.reader(abilities_file)
        lines = [ l for l in reader ]
        headers = lines[0]
        abilities = lines[1:]
        for a in abilities:
            name, init, top, toploss, bottom, bottomloss, level = [ s.strip() for s in a ]
            ability_card = draw_ability_card(
                title=name,
                initiative=init,
                toplines=top.split(';'),
                bottomlines=bottom.split(';'),
                color=tint,
                level=level,
                toploss=toploss,
                bottomloss=bottomloss
            )
            cards.append(ability_card)
    return cards


def main(argv=None):
    if not argv:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', default=None)
    parser.add_argument('--tint', default='#808080')
    parser.add_argument('--version', default=None)
    parser.add_argument('--name', default=None)
    parser.add_argument('abilities_file')

    args = parser.parse_args()

    if not os.path.exists(args.abilities_file):
        print(f'No ability file {args.abilities_file} exists, exiting...')
        return 1

    character_name = args.name if args.name else input('Character name? ')
    version = version if args.version else '1.0'
    print(f'Generating version {version} ability cards for {character_name}...')

    output_dir = args.output_dir if args.output_dir else os.path.join(os.getcwd(), character_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f'Saving output to {output_dir}...')

    cards = parse_abilities_file(args.abilities_file, _hex_to_rgb(args.tint))
    for c in cards:
        c.show()




if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))