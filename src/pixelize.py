#!/usr/local/bin/python3
from PIL import Image, ImageOps, ImageEnhance, ImageFilter, ImageDraw
import argparse
import csv
import pathlib
import pixelize


def image_size(
    filename_input: pathlib.Path) -> tuple[int, int]:
    im = Image.open(filename_input)
    return (im.width, im.height)


def pixelize(
    filename_input: pathlib.Path,
    filename_output: pathlib.Path,
    resolution: tuple = (64, 64),
) -> None:
    # Open The Image to PIXELIZE
    img = Image.open(filename_input)

    # The smallest is the resize, the biggest are the PIXELS
    # imgSmall = img.resize((128, 128), resample=Image.BILINEAR)
    # If you do want ANTIALISING uncomment the line above and comment the one below
    imgSmall = img.resize((resolution[0], resolution[1]))

    # Scale back up using NEAREST to original size
    result = imgSmall.resize(img.size, Image.NEAREST)

    # Save
    result.save(filename_output)


def posterize(
    filename_input: pathlib.Path, filename_output: pathlib.Path, nr_bits: int = 4
) -> None:
    # nr_bits refers to the number of bits to keep per channel
    im1 = Image.open(filename_input)

    # applying posterize method
    im2 = ImageOps.posterize(im1, nr_bits)
    im2.save(filename_output)


def quantize(filename_input: pathlib.Path, filename_output: pathlib.Path, palette=None) -> None:

    # Make tiny palette Image, one black pixel
    palIm = Image.new("P", (1, 1))

    # Make your desired B&W palette containing only 1 pure white, many black and some grey colors
    if palette is None:
        palette = (
            [255, 255, 255] + [0, 0, 0] + [64, 64, 64] + [125, 125, 125]
        )  # + [172, 172, 172] + [200, 200, 200] + [255, 0, 0] + [125, 0,0 ] + [255, 255, 0] + [64, 64, 0]
    else:
        co = []
        for c in palette:
            co += c
        palette = (co)
    # Push in our lovely B&W palette and save just for debug purposes
    palIm.putpalette(palette)
    # palIm.save('DEBUG-palette.png')

    # Load actual image
    actual = Image.open(filename_input).convert("RGB")

    # Quantize actual image to palette
    actual = actual.quantize(palette=palIm, dither=Image.Dither.NONE)

    actual.save(filename_output)


def change_contrast(filename_input, filename_output, factor) -> None:
    img = Image.open(filename_input)

    enhancer = ImageEnhance.Contrast(img)

    im_output = enhancer.enhance(factor)
    im_output.save(filename_output)


def find_edges(input_filename, output_filename):
    # Open the image
    image = Image.open(input_filename)

    # Find edges of the image
    edges = image.filter(ImageFilter.FIND_EDGES)

    # Save the resulting image
    edges.save(output_filename)


def draw_grid(input_filename: pathlib.Path, output_filename: pathlib.Path, step_size: int) -> None:
    image = Image.open(input_filename)

    # Draw some lines
    draw = ImageDraw.Draw(image)
    y_start = 0
    y_end = image.height
    step_size = int(image.width / step_size)

    for x in range(0, image.width, step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=128)

    x_start = 0
    x_end = image.width

    for y in range(0, image.height, step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=128)

    image.save(output_filename)


def resize(input_filename: pathlib.Path, output_filename: pathlib.Path, ratio=2):
    image = Image.open(input_filename)

    maxsize = (int(image.width*ratio), int(image.height*ratio))
    image = image.resize(maxsize)

    image.save(output_filename)


# pixelize.change_contrast(sys.argv[1], 'tmp.png', 10.0)

# pixelize.posterize('tmp.png', 'tmp_posterized.png', nr_bits=2)
# pixelize.quantize('tmp_posterized.png', 'tmp_quantized.png')
# find_edges('tmp_posterized.png', sys.argv[2])
# find_edges(sys.argv[1], sys.argv[2])

def read_palette_from_file(filename: pathlib.Path):
    colors = []
    csv_reader = csv.reader(open(filename, 'r'), delimiter=';')
    for row in csv_reader:
        color = []
        if row == '':
            continue
        for col in row:
            if col == '':
                continue
            color.append(int(col))
        if color == []:
            continue
        colors.append(
            color
        )
    return colors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='pixelizer',
        description='Do its best to pixelize an image',
        epilog='Text at the bottom of help'
    )
    parser.add_argument('--input', dest="input_filename",
        help="File to pixelize"
    )
    parser.add_argument('--output', dest="output_filename",
        help="Pixelized image"
    )
    parser.add_argument('--resolution', dest='resolution',
        help="the resolution of the image as WIDTHxHEIGHT (i.e. 30x30)",
        default="64x64"
    )
    parser.add_argument('--palette_file', dest='palette_filename',
        default=None
    )
    args = parser.parse_args()

    img_f = args.input_filename

    palette = None
    if args.palette_filename is not None:
         palette = read_palette_from_file(args.palette_filename)
         print(palette)

    resolution = args.resolution.split("x")
    resolution = (int(resolution[0]), int(resolution[1]))

    change_contrast(img_f, "img1_contrast.png", 2.0)
    change_contrast("img1_contrast.png", "img1_contrast.png", 2.5)

    pixelize("img1_contrast.png", "img1_pixelized.png", resolution)
    #posterize("img1_pixelized.png", args.output_filename, nr_bits=2)
    quantize("img1_pixelized.png", args.output_filename, palette=palette)
