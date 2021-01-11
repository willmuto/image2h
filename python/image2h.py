#! /usr/bin/python

"""
Writes out a monochromatic image to a C array header file, so it can 
be included into an Arduino project (for e-ink, etc.)
"""

import sys
import argparse
from PIL import Image

TEMPLATE = '''#ifndef _IMGDATA_H_
#define _IMGDATA_H_

const byte IMAGEDATA[] = {{
{}
}};
#endif'''

def parse_args():
   parser = argparse.ArgumentParser(description='Convert an image to a C array')
   parser.add_argument('input', help='Input image (.png, .jpg, .gif, etc)')
   parser.add_argument('output', help='Output C array (.h)')

   parser.add_argument('-i', '--invert', action='store_true', help='Invert on/off values')
   parser.add_argument('-a', '--alpha', action='store_true', help='Image has alpha channel')
   parser.add_argument('-v', '--verbose', action='store_true', help='Per-pixel debugging output.')

   return parser.parse_args()

def image_data_to_str(image_data, invert=False, 
                           has_alpha=False, verbose=False):
   """
   Converts a PIL.Image object to a data string that is then added to the
   header file. String is hex values, lines terminated by "0x0a,\n"

   :param image_data PIL.Image: 
   :param invert bool: Invert the on/off colors in the returned data string.
   :param has_alpha bool: True of the image uses an alpha channel.
   :param verbose bool: Enable additional debug output.
   :return: A string of hex values.
   :rtype str:
   """
   on = 1 if invert else 0
   off = 0 if invert else 1

   check_color = (255, 255, 255, 255) if has_alpha else (255, 255, 255)

   line = []
   data = ""
   for i, d in enumerate(image_data.getdata()):
         if verbose:
            print(i, d)

         if d == check_color:
            line.append(hex(on))
         else:
            line.append(hex(off))

         col = i + 1 
         if col % float(image_data.width) == 0:
            data = "".join([data, ','.join(line), ',0x0a,\n'])
            line = []

   return data

def main():
   args = parse_args()

   try:
      im = Image.open(args.input)
   except IOError:
      print("Unable to load {}".format(args.input))

   with open(args.output, 'w') as f:
      data_str = image_data_to_str(im, args.invert, args.alpha, args.verbose)
      f.write(TEMPLATE.format(data_str))

   print("wrote {}".format(args.output))

if __name__ == "__main__":
    main()