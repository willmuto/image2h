/*
    WMuto_EPDImage.h
    Utility class for displaying images on an Adafruit EPD
    Will Muto, 2021
*/

#ifndef WMuto_EPDImage_h
#define WMuto_EPDImage_h

#include "Adafruit_EPD.h"

class EPDImage 
{
    public: 
        EPDImage();
        void draw(const byte imageData[], Adafruit_EPD & display);
        int getSize(const byte imageData[]);
        int getWidth(const byte imageData[]);
        int getHeight(const byte imageData[]);

    private:
        
};

#endif