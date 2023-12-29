import pathlib
import sys
from PIL import ImageFilter, Image
import pixelize

def emboss(filename_input: pathlib.Path, output_filename: pathlib.Path):
    im = Image.open(filename_input)

    im1 = im.filter(ImageFilter.SHARPEN)
    im2 = im1.filter(ImageFilter.EMBOSS)
    im3 = im2.filter(ImageFilter.SHARPEN)
    im4 = im3.filter(ImageFilter.EMBOSS)

    im3.save(output_filename)

if __name__ == '__main__':
    pixelize.change_contrast(sys.argv[1], 'tmp.jpg', 1)
    emboss('tmp.jpg', sys.argv[2])

