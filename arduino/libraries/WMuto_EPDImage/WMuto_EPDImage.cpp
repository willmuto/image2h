/*
    WMuto_EPDImage.cpp
    Utility class for displaying images on an Adafruit EPD
    Will Muto, 2021
    License: Attribution 4.0
    https://creativecommons.org/licenses/by/4.0/
*/

#include <cstdlib> 

#include "WMuto_EPDImage.h"
#include "Adafruit_EPD.h"

#define EOL 0x0a    // End of Line
#define EOF 0x0     // End of File
#define C1  0x1     // Blank
#define C2  0x2     // Color A
#define C3  0x3     // Color B

EPDImage::EPDImage() {
    _offsetX = 0;
    _offsetY = 0;
}

int EPDImage::getWidth(const byte imageData[])
{
    // Determine image width from sentinel
    int width = 0;
    while (true)
    {
        byte check = imageData[width];

        // If for some reason the end of the line cannot be
        // found, max out at 5k. Otherwise look for sentinel.
        if (check == EOL || width > 5120)
        {
            break;
        }
        else
        {
            width++;
        }
    }

    return width;
}

int EPDImage::getSize(const byte imageData[])
{
    int size = 0;
    int counter = 0;
    while (true)
    {
        byte check = imageData[counter];

        if (check == EOF)
        {
            break;
        }
        else 
        {
            if (check == C1 || check == C2 || check == C3)
            {
                size++;
            }
        }
        counter++;
         
    }
    return size;
}

int EPDImage::getHeight(const byte imageData[])
{
    int width = getWidth(imageData);
    int height = getSize(imageData) / width;

    return height;
}

void EPDImage::setOffset(const int x, const int y)
{
    _offsetX = x;
    _offsetY = y;
}

void EPDImage::draw(const byte imageData[], Adafruit_EPD & display, const int startX,
                    const int startY, const int endX, const int endY)
{
    int imgWidth = getWidth(imageData);
    int imgHeight = getHeight(imageData);

    int drawStartX;
    int drawStartY;
    int drawEndX;
    int drawEndY;

    if (startX < 0)
    {
        drawStartX = 0;
    }
    else
    {
        drawStartX = startX;
    }

    if (startY < 0)
    {
        drawStartY = 0;
    }
    else
    {
        drawStartY = startY;
    }

    if (endX > imgWidth)
    {
        drawEndX = imgWidth;
    }
    else
    {
        drawEndX = endX;
    }
    
    if (endY > imgHeight)
    {
        drawEndY = imgHeight;
    }
    else
    {
        drawEndY = endY;
    }

    int width;
    if (display.width() < imgWidth) {
        width = display.width();
    } 
    else 
    {
        width = imgWidth;
    }

    int height;
    if (display.height() < imgHeight) {
        height = display.height();
    } 
    else
    {
        height = imgHeight;
    }



    for (int i = startY; i < endY; i++)
    {
        for (int j = endX; j > startX; j--) 
        {
            if (imageData[j + (i * imgWidth) + i] == C2) 
            {
                display.drawPixel(i + _offsetY, width - j + _offsetX, EPD_BLACK);
            }
            else if (imageData[j + (i * imgWidth) + i] == C3)
            {
                display.drawPixel(i + _offsetY, width - j + _offsetX, EPD_RED);
            }
        }
    }

    return;
}

void EPDImage::draw(const byte imageData[], Adafruit_EPD & display)
{
    int imgWidth = getWidth(imageData);
    int imgHeight = getHeight(imageData);

    int width;
    if (display.width() < imgWidth) {
        width = display.width();
    } 
    else 
    {
        width = imgWidth;
    }

    int height;
    if (display.height() < imgHeight) {
        height = display.height();
    } 
    else
    {
        height = imgHeight;
    }
    
    draw(imageData, display, 0, 0, width, height);

    return;
}