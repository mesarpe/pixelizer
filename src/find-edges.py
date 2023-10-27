from PIL import Image, ImageFilter
import sys

import pixelize

def find_edges(input_filename, output_filename):
    # Open the image
    image = Image.open(input_filename)

    # Find edges of the image
    edges = image.filter(ImageFilter.FIND_EDGES)

    # Save the resulting image
    edges.save(output_filename)

#pixelize.change_contrast(sys.argv[1], 'tmp.png', 10.0)

#pixelize.posterize('tmp.png', 'tmp_posterized.png', nr_bits=2)
#pixelize.quantize('tmp_posterized.png', 'tmp_quantized.png')
#find_edges('tmp_posterized.png', sys.argv[2])
find_edges(sys.argv[1], sys.argv[2])



