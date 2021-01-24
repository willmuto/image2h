# image2h

`image2h` is a way to convert various image formats to a C-style array which can be loaded into an Arduino sketch and used on displays like e-ink.

## Prerequisites

`image2h` requires Pillow (which replaces PIL) for reading images. Click [here](https://pillow.readthedocs.io/en/stable/installation.html#basic-installation) for installation instructions.

## Usage

To run the command:
```bash
image2h.py [input] [output]
```
where input is an image format [supported by Pillow](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html) and output is a .h file.

The command also provides the following options:
```bash
--invert           # Swap on/off values 
--alpha            # Use when input image has alpha 
--secondary        # Specify which additional color is encoded (0-255)
--verbose          # Per-pixel debugging info
```

## Details

For a 4x4 checkerboard, the output will look something like this:

```cpp
#ifndef _IMGDATA_H_
#define _IMGDATA_H_

const byte IMAGEDATA[] = {
0x2,0x2,0x1,0x1,0x0a,
0x2,0x2,0x1,0x1,0x0a,
0x1,0x1,0x2,0x2,0x0a,
0x1,0x1,0x2,0x2,0x0a,
0x0
};
#endif
```

Any pixel that is pure white will be on (`0x2`) and any other color will be off (`0x1`). A sentinel value (`0x0a`) is used to encode the width of the image, with `0x0` specifying the end of the file.

Using the `--invert` flag, the on and off values will be flipped:

```cpp
#ifndef _IMGDATA_H_
#define _IMGDATA_H_

const byte IMAGEDATA[] = {
0x1,0x1,0x2,0x2,0x0a,
0x1,0x1,0x2,0x2,0x0a,
0x2,0x2,0x1,0x1,0x0a,
0x2,0x2,0x1,0x1,0x0a,
0x0
};
#endif
```

If the display supports a secondary color, you can specify a color with `--secondary`, which be encoded with  `0x3`.

```python
--secondary 127         # middle grey, shortand for 127 127 127
--secondary 255 0 0     # red
--secondary 255 0 0 255 # red with alpha
```

## Reading in Arduino

When you add the .h image to your Arduino sketch, you can then include it.

```cpp
#include "myimage.h"
```

The imagedata is then accessed as the array `IMAGEDATA`. 

I have included a utility class for displaying this `IMAGEDATA` on an `Adafruit_EPD` display after it has been initialized:

  ```cpp
  #include "WMuto_EPDImage.h"

  EPDImage epdImage = EPDImage();
  epdImage.draw(IMAGEDATA, display);
  ```

  The `draw()` method also has the option to render a portion of the image by specifying the start and end coordinates. 
  ```cpp
  epdImage.draw(IMAGEDATA, display, startX, startY, endX, endY);
  ```

  The image can be shifted in the display by setting the offset before the `draw()` command (in pixels):

  ```cpp
  epdImage.setOffset(10, -20); // offset 10 in x, -20 in y
  ```

  ## Running Tests

  The unit tests are run with the following command:

  ```python
  cd python
  python -m pytest
  ```