/*
    WMuto_EPDImage.h
    Utility class for displaying images on an Adafruit EPD
    Will Muto, 2021
    License: Attribution 4.0
    https://creativecommons.org/licenses/by/4.0/
*/

#ifndef WMuto_EPDImage_h
#define WMuto_EPDImage_h

#include "Adafruit_EPD.h"

class EPDImage 
{
    public: 
        EPDImage();
        void draw(const byte imageData[], Adafruit_EPD & display);
        void draw(const byte imageData[], Adafruit_EPD & display, const int startX,
                    const int startY, const int endX, const int endY);
        int getSize(const byte imageData[]);
        int getWidth(const byte imageData[]);
        int getHeight(const byte imageData[]);

        void setOffset(const int x, const int y);

    private:
        int _offsetX;
        int _offsetY;
        
};

#endif