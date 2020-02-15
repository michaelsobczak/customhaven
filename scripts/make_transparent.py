import argparse
import os, sys
from PIL import Image
import numpy as np



def make_transparent(f) -> Image:
    # i = Image.open(f)
    # i.convert('RGBA')
    # datas = i.getdata()
    # newData = []
    # for item in datas:
    #     if item[0] == 255 and item[1] == 255 and item[2] == 255:
    #         newData.append((255, 255, 255, 0))
    #     else:
    #         newData.append(item)
    # i.putdata(newData)
    # i.show()
    threshold=100
    dist=5
    img=Image.open(f).convert('RGBA')
    # np.asarray(img) is read only. Wrap it in np.array to make it modifiable.
    arr=np.array(np.asarray(img))
    r,g,b,a=np.rollaxis(arr,axis=-1)    
    mask=((r>threshold)
        & (g>threshold)
        & (b>threshold)
        & (np.abs(r-g)<dist)
        & (np.abs(r-b)<dist)
        & (np.abs(g-b)<dist)
        )
    arr[mask,3]=0
    img=Image.fromarray(arr,mode='RGBA')
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