from rembg import remove
import cv2
import sys
import logging

logging.error("THIS LIBRARY SEND YOUR IMAGE TO THE WEB")
i = input("If not sure control c")

def remove_background(input_filename, output_filename) -> None:
    input = cv2.imread(input_filename)
    output = remove(input)
    cv2.imwrite(output_filename, output)

remove_background(sys.argv[1], sys.argv[2])
