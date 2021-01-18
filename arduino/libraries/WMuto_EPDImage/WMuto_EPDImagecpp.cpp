/*
    WMuto_EPDImage.cpp
    Utility class for displaying images on an Adafruit EPD
    Will Muto, 2021
*/

#include "WMuto_EPDImage.h"
#include "Adafruit_EPD.h"

#define EOL 0x0a

EPDImage::EPDImage() 
{
    //
}

int EPDImage::getWidth(const byte imageData[])
{
    // Determine image width from sentinel
    int widthTest = 0;
    while (true)
    {
        byte check = imageData[widthTest];

        // If for some reason the end of the line cannot be
        // found, max out at 10k. Otherwise look for sentinel.
        if (check == EOL || widthTest > 10000)
        {
            break;
        }
        else
        {
            widthTest++;
        }
    }

    return widthTest;
}

void EPDImage::draw(const byte imageData[], Adafruit_EPD & display)
{
    int imgWidth = getWidth(imageData);

    int width;
    if (display.width() < imgWidth) {
        width = display.width();
    } else {
        width = imgWidth;
    }


    uint16_t color;
    for (int i = 0; i < display.height(); i++)
    {
        for (int j = imgWidth; j > 0; j--) 
        {
            if (imageData[j + (i * imgWidth) + i] == 1) 
            {
                display.drawPixel(i, width - j, EPD_BLACK);
            }
            else if (imageData[j + (i * imgWidth) + i] == 2)
            {
                display.drawPixel(i, width - j, EPD_RED);
            }
        }
    }

    return;
}