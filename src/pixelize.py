#!/usr/local/bin/python3
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import argparse
import pathlib
import pixelize


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


def quantize(filename_input: pathlib.Path, filename_output: pathlib.Path) -> None:

    # Make tiny palette Image, one black pixel
    palIm = Image.new("P", (1, 1))

    # Make your desired B&W palette containing only 1 pure white, many black and some grey colors
    palette = (
        [255, 255, 255] + [0, 0, 0] + [64, 64, 64] + [125, 125, 125]
    )  # + [172, 172, 172] + [200, 200, 200] + [255, 0, 0] + [125, 0,0 ] + [255, 255, 0] + [64, 64, 0]
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


# pixelize.change_contrast(sys.argv[1], 'tmp.png', 10.0)

# pixelize.posterize('tmp.png', 'tmp_posterized.png', nr_bits=2)
# pixelize.quantize('tmp_posterized.png', 'tmp_quantized.png')
# find_edges('tmp_posterized.png', sys.argv[2])
# find_edges(sys.argv[1], sys.argv[2])


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
    args = parser.parse_args()

    img_f = args.input_filename
    resolution = args.resolution.split("x")
    resolution = (int(resolution[0]), int(resolution[1]))

    change_contrast(img_f, "img1_contrast.png", 2.0)
    change_contrast("img1_contrast.png", "img1_contrast.png", 2.5)

    pixelize("img1_contrast.png", "img1_pixelized.png", resolution)
    posterize("img1_pixelized.png", args.output_filename, nr_bits=2)