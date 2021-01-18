import image2h
import pytest
from PIL import Image

BW_RGB_CHECKERBOARD = [(255, 255, 255), (0, 0, 0),
                       (0, 0, 0), (255, 255, 255)]

BW_RGBA_CHECKERBOARD = [(255, 255, 255, 255), (0, 0, 0, 255),
                        (0, 0, 0, 255), (255, 255, 255, 255)]

BWR_RGB_CHECKERBOARD = [(255, 255, 255), (255, 0, 0),
                       (0, 0, 0), (255, 255, 255)]

BWR_RGBA_CHECKERBOARD = [(255, 255, 255, 255), (255, 0, 0, 255),
                        (0, 0, 0, 255), (255, 255, 255, 255)]

BW_CHECKERBOARD_STRING        = '0x1,0x2,0x0a,\n0x2,0x1,0x0a,\n0x0'
BW_CHECKERBOARD_INVERT_STRING = '0x2,0x1,0x0a,\n0x1,0x2,0x0a,\n0x0'

BWR_CHECKERBOARD_STRING        = '0x1,0x3,0x0a,\n0x2,0x1,0x0a,\n0x0'
BWR_CHECKERBOARD_INVERT_STRING = '0x2,0x3,0x0a,\n0x1,0x2,0x0a,\n0x0'

# 2x2 b+w RGB checkerboard
BW_RGB_CHECKERBOARD_IMAGE = Image.new('RGB', (2,2))
BW_RGB_CHECKERBOARD_IMAGE.putdata(BW_RGB_CHECKERBOARD)

# 2x2 b+w RGBA checkerboard
BW_RGBA_CHECKERBOARD_IMAGE = Image.new('RGBA', (2,2))
BW_RGBA_CHECKERBOARD_IMAGE.putdata(BW_RGBA_CHECKERBOARD)

# 2x2 b+w+r RGB checkerboard
BW_RGB_CHECKERBOARD_IMAGE = Image.new('RGB', (2,2))
BW_RGB_CHECKERBOARD_IMAGE.putdata(BWR_RGB_CHECKERBOARD)

# 2x2 b+w+r RGBA checkerboard
BW_RGBA_CHECKERBOARD_IMAGE = Image.new('RGBA', (2,2))
BW_RGBA_CHECKERBOARD_IMAGE.putdata(BWR_RGBA_CHECKERBOARD)



def test_bw_rgb_checkboard():
    assert image2h.image_data_to_str(BW_RGB_CHECKERBOARD_IMAGE) == \
        BW_CHECKERBOARD_STRING

def test_bw_rgba_checkerboard():
    assert image2h.image_data_to_str(BW_RGBA_CHECKERBOARD_IMAGE, has_alpha=True) == \
        BW_CHECKERBOARD_STRING

def test_bw_rgb_invert_checkboard():
    assert image2h.image_data_to_str(BW_RGB_CHECKERBOARD_IMAGE, invert=True) == \
        BW_CHECKERBOARD_INVERT_STRING

def test_bw_rgba_invert_checkerboard():
    assert image2h.image_data_to_str(BW_RGBA_CHECKERBOARD_IMAGE, invert=True, has_alpha=True) == \
        BW_CHECKERBOARD_INVERT_STRING

def test_bwr_rgb_checkboard():
    assert image2h.image_data_to_str(BW_RGB_CHECKERBOARD_IMAGE, secondary=(255, 0, 0)) == \
        BWR_CHECKERBOARD_STRING

def test_bwr_rgba_checkerboard():
    assert image2h.image_data_to_str(BW_RGBA_CHECKERBOARD_IMAGE, has_alpha=True, secondary=(255, 0, 0, 255)) == \
        BWR_CHECKERBOARD_STRING

def test_bwr_rgb_invert_checkboard():
    assert image2h.image_data_to_str(BW_RGB_CHECKERBOARD_IMAGE, invert=True, secondary=(255, 0, 0)) == \
        BWR_CHECKERBOARD_INVERT_STRING

def test_bwr_rgba_invert_checkerboard():
    assert image2h.image_data_to_str(BW_RGBA_CHECKERBOARD_IMAGE, invert=True, has_alpha=True, secondary=(255, 0, 0, 255)) == \
        BWR_CHECKERBOARD_INVERT_STRING