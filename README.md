# image2h

`image2h` is a way to convert various image formats to a C-style array which can be loaded into an Arduino sketch and used on displays like e-ink.

## Prerequisites

`image2h` requires Pillow (which replaces PIL) for reading images. Click [here](https://pillow.readthedocs.io/en/stable/installation.html#basic-installation) for installation instructions.

## Usage

To run the command:
```
image2h.py [input] [output]
```
where input is an image format [supported by Pillow](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html) and output is a .h file.

The command also provides the following options:
```
--invert           # Swap on/off values 
--alpha            # Use when input image has alpha 
--verbose          # Per-pixel debugging info
```

## Details

For a 4x4 checkerboard, the output will look something like this:

```
#ifndef _IMGDATA_H_
#define _IMGDATA_H_

const byte IMAGEDATA[] = {
0x1,0x1,0x0,0x0,0x0a,
0x1,0x1,0x0,0x0,0x0a,
0x0,0x0,0x1,0x1,0x0a,
0x0,0x0,0x1,0x1,0x0a,

};
#endif
```

Any pixel that is pure white will be on (`0x1`) and any other color will be off (`0x0`). A sentinel value (`0x0a`) is used to encode the width of the image.

Using the `--invert` flag, the on and off values will be flipped:

```
#ifndef _IMGDATA_H_
#define _IMGDATA_H_

const byte IMAGEDATA[] = {
0x0,0x0,0x1,0x1,0x0a,
0x0,0x0,0x1,0x1,0x0a,
0x1,0x1,0x0,0x0,0x0a,
0x1,0x1,0x0,0x0,0x0a,

};
#endif
```

## Reading in Arduino

When you add the .h image to your Arduino sketch, you can then include it.

```
#include "myimage.h"
```

The imagedata is then accessed as the array `IMAGEDATA`. Here is some example code for displaying the image on a CircuitPlayground e-ink display:

```
  display.clearBuffer();
  display.fillScreen(EPD_WHITE);

  /* Determine the width of the image */
  int imgWidth = 0;
  while (true) {
    char eol = IMAGEDATA[imgWidth];
    if (imgWidth > 10000) {
      // If for some reason the width of the image
      // cannot be determined, quit after 10k pixels
      return;
    }
    if (eol == 0x0a) {
      break;
    }
    imgWidth++;
  }

  /* Determine crop */
  int width;
  if (display.width() < imgWidth) {
    width = display.width();
  } else {
    width = imgWidth;
  }

  /* Draw */
  for (int i = 0; i < display.height(); i++) {
    for (int j = width; j > 0; j--) {
      // This is reversed due to the e-ink display
      // where 0,0 is top-right, not top-left.
      if (IMAGEDATA[j + (i * imgWidth) + i] == 1) {
        display.drawPixel(i, width - j, EPD_BLACK);
      }
    }
  }
  
  display.display();
  ```