import argparse
import os, sys
from PIL import Image

def make_transparent(f) -> Image:
    img = Image.open(f)
    img.convert('RGBA')
    # datas = i.getdata()
    # newData = []
    # for item in datas:
    #     if item[0] == 255 and item[1] == 255 and item[2] == 255:
    #         newData.append((255, 255, 255, 0))
    #     else:
    #         newData.append(item)
    # i.putdata(newData)

    pixdata = img.load()

    width, height = img.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y] == (255, 255, 255, 255):
                pixdata[x, y] = (255, 255, 255, 0)
    return img

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('images', nargs='+')
    parser.add_argument('--output-dir', default=None)
    args = parser.parse_args(argv)

    if not args.output_dir:
        args.output_dir = os.path.join(os.getcwd(), 'output')

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    for i in args.images:
        img = make_transparent(i)
        img_name = f'{os.path.splitext(os.path.basename(i))[0]}.png'
        img_path = os.path.join(args.output_dir, img_name)
        img.save(img_path, 'PNG')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))