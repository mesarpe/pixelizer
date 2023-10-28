import pixelize
import argparse
import sys

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
parser.add_argument('--step-size', dest='step_size',
    help='divide the grid in X blocks',
    default=10,
    type=int
)
parser.add_argument('--resolution', dest='resolution',
    help="the resolution of the image as WIDTHxHEIGHT (i.e. 30x30)",
    default="64x64"
)
args = parser.parse_args()

pixelize.draw_grid(args.input_filename, args.output_filename, args.step_size)

