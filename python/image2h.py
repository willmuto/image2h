#! /usr/bin/python

"""
Writes out a monochromatic image to a C array header file, so it can 
be included into an Arduino project (for e-ink, etc.)
"""

import sys
import argparse
from PIL import Image

C1 = '0x1'
C2 = '0x2'
C3 = '0x3'
EOL = '0x0a'
EOF = '0x0'

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
   parser.add_argument('-p', '--primary', type=int, nargs='+', default=[255, 255, 255], help='Specify primary color. Default: (%(default)s)')
   parser.add_argument('-s', '--secondary', type=int, nargs='+', default=[], help='Specify secondary color if supported by display.')
   parser.add_argument('-v', '--verbose', action='store_true', help='Per-pixel debugging output.')

   return parser.parse_args()

def image_data_to_str(image_data,invert=False, has_alpha=False, primary=[255, 255, 255],
                      secondary=[], verbose=False):
   """
   Converts a PIL.Image object to a data string that is then added to the
   header file. String is hex values, lines terminated by "0x0a,\n"

   :param image_data PIL.Image: 
   :param invert bool: Invert the on/off colors in the returned data string.
   :param has_alpha bool: True of the image uses an alpha channel.
   :param primary list: RGB of primary color
   :param secondary list: RGB of secondary color 
   :param verbose bool: Enable additional debug output.
   :return: A string of hex values.
   :rtype str:
   """
   on = C2 if invert else C1
   off = C1 if invert else C2

   if has_alpha:
      primary = primary + [255]

      if secondary:
         secondary = secondary + [255]

   primary = tuple(primary)
   secondary = tuple(secondary)

   line = []
   data = ""
   for i, d in enumerate(image_data.getdata()):
         if verbose:
            print(i, d)

         if d == primary:
            line.append(on)
         elif secondary and d == secondary:
            line.append(C3)
         else:
            line.append(off)

         col = i + 1 
         if col % float(image_data.width) == 0:
            data = "".join([data, ','.join(line), ',', EOL, ',\n'])
            line = []

   data = "{}{}".format(data, EOF)

   return data

def main():
   args = parse_args()

   try:
      im = Image.open(args.input)
   except IOError:
      print("Unable to load {}".format(args.input))

   if args.secondary:
      if len(args.secondary) == 1:
         args.secondary = [args.secondary[0], args.secondary[0], args.secondary[0]]
      elif len(args.secondary) == 2:
         args.secondary = [args.secondary[0], args.secondary[1], 0]
      elif len(args.secondary) == 3:
         args.secondary = [args.secondary[0], args.secondary[1], args.secondary[2]]
      elif len(args.secondary) == 4:
         args.secondary = args.secondary
      else:
         print("Error: Unsupported number of values for secondary color.")
         return

   with open(args.output, 'w') as f:
      data_str = image_data_to_str(im, args.invert, args.alpha, args.primary, 
                                    args.secondary, args.verbose)
      f.write(TEMPLATE.format(data_str))

   print("wrote {}".format(args.output))

if __name__ == "__main__":
    main()