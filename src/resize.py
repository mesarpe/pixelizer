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
    help="changed size image"
)
parser.add_argument('--ratio', dest='ratio',
    help='change aspect ratio multiplying by ratio',
    default=2.0,
    type=float
)
args = parser.parse_args()

pixelize.resize(args.input_filename, args.output_filename, args.ratio)

