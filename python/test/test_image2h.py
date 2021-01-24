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

BG_RGB_CHECKERBOARD = [(0, 255, 0), (0, 0, 0),
                       (0, 0, 0), (0, 255, 0)]

BG_RGBA_CHECKERBOARD = [(0, 255, 0, 255), (0, 0, 0, 255),
                        (0, 0, 0, 255), (0, 255, 0, 255)]

BGR_RGB_CHECKERBOARD = [(0, 255, 0), (255, 0, 0),
                       (0, 0, 0), (0, 255, 0)]

BGR_RGBA_CHECKERBOARD = [(0, 255, 0, 255), (255, 0, 0, 255),
                        (0, 0, 0, 255), (0, 255, 0, 255)]

BW_CHECKERBOARD_STRING        = '0x1,0x2,0x0a,\n0x2,0x1,0x0a,\n0x0'
BW_CHECKERBOARD_INVERT_STRING = '0x2,0x1,0x0a,\n0x1,0x2,0x0a,\n0x0'

BWR_CHECKERBOARD_STRING        = '0x1,0x3,0x0a,\n0x2,0x1,0x0a,\n0x0'
BWR_CHECKERBOARD_INVERT_STRING = '0x2,0x3,0x0a,\n0x1,0x2,0x0a,\n0x0'

# 2x2 black+white RGB checkerboard
BW_RGB_CHECKERBOARD_IMAGE = Image.new('RGB', (2,2))
BW_RGB_CHECKERBOARD_IMAGE.putdata(BW_RGB_CHECKERBOARD)

# 2x2 black+white RGBA checkerboard
BW_RGBA_CHECKERBOARD_IMAGE = Image.new('RGBA', (2,2))
BW_RGBA_CHECKERBOARD_IMAGE.putdata(BW_RGBA_CHECKERBOARD)

# 2x2 black+white+red RGB checkerboard
BW_RGB_CHECKERBOARD_IMAGE = Image.new('RGB', (2,2))
BW_RGB_CHECKERBOARD_IMAGE.putdata(BWR_RGB_CHECKERBOARD)

# 2x2 black+white+red RGBA checkerboard
BW_RGBA_CHECKERBOARD_IMAGE = Image.new('RGBA', (2,2))
BW_RGBA_CHECKERBOARD_IMAGE.putdata(BWR_RGBA_CHECKERBOARD)

# 2x2 black+green RGB checkerboad
BG_RGB_CHECKERBOARD_IMAGE = Image.new('RGB', (2,2))
BG_RGB_CHECKERBOARD_IMAGE.putdata(BG_RGB_CHECKERBOARD)

# 2x2 black+green RGBA checkerboard
BG_RGBA_CHECKERBOARD_IMAGE = Image.new('RGBA', (2,2))
BG_RGBA_CHECKERBOARD_IMAGE.putdata(BG_RGBA_CHECKERBOARD)

# 2x2 black+green+red RGB checkerboad
BGR_RGB_CHECKERBOARD_IMAGE = Image.new('RGB', (2,2))
BGR_RGB_CHECKERBOARD_IMAGE.putdata(BGR_RGB_CHECKERBOARD)

# 2x2 black+green+red RGBA checkerboard
BGR_RGBA_CHECKERBOARD_IMAGE = Image.new('RGBA', (2,2))
BGR_RGBA_CHECKERBOARD_IMAGE.putdata(BGR_RGBA_CHECKERBOARD)

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
    assert image2h.image_data_to_str(BW_RGB_CHECKERBOARD_IMAGE, secondary=[255, 0, 0]) == \
        BWR_CHECKERBOARD_STRING

def test_bwr_rgba_checkerboard():
    assert image2h.image_data_to_str(BW_RGBA_CHECKERBOARD_IMAGE, has_alpha=True, secondary=[255, 0, 0]) == \
        BWR_CHECKERBOARD_STRING

def test_bwr_rgb_invert_checkboard():
    assert image2h.image_data_to_str(BW_RGB_CHECKERBOARD_IMAGE, invert=True, secondary=[255, 0, 0]) == \
        BWR_CHECKERBOARD_INVERT_STRING

def test_bwr_rgba_invert_checkerboard():
    assert image2h.image_data_to_str(BW_RGBA_CHECKERBOARD_IMAGE, invert=True, has_alpha=True, secondary=[255, 0, 0]) == \
        BWR_CHECKERBOARD_INVERT_STRING

def test_bg_rgb_checkboard():
    assert image2h.image_data_to_str(BG_RGB_CHECKERBOARD_IMAGE, primary=[0,255,0]) == \
        BW_CHECKERBOARD_STRING

def test_bg_rgba_checkboard():
    assert image2h.image_data_to_str(BG_RGBA_CHECKERBOARD_IMAGE, primary=[0,255,0], has_alpha=True) == \
        BW_CHECKERBOARD_STRING

def test_bg_rgb_invert_checkboard():
    assert image2h.image_data_to_str(BG_RGB_CHECKERBOARD_IMAGE, primary=[0,255,0], invert=True) == \
        BW_CHECKERBOARD_INVERT_STRING

def test_bg_rgba_invert_checkboard():
    assert image2h.image_data_to_str(BG_RGBA_CHECKERBOARD_IMAGE, primary=[0,255,0], has_alpha=True, invert=True) == \
        BW_CHECKERBOARD_INVERT_STRING

def test_bgr_rgb_checkboard():
    assert image2h.image_data_to_str(BGR_RGB_CHECKERBOARD_IMAGE, primary=[0,255,0], secondary=[255,0,0]) == \
        BWR_CHECKERBOARD_STRING

def test_bgr_rgba_checkboard():
    assert image2h.image_data_to_str(BGR_RGBA_CHECKERBOARD_IMAGE, primary=[0,255,0], secondary=[255,0,0], has_alpha=True) == \
        BWR_CHECKERBOARD_STRING

def test_bgr_rgb_invert_checkboard():
    assert image2h.image_data_to_str(BGR_RGB_CHECKERBOARD_IMAGE, primary=[0,255,0], secondary=[255,0,0], invert=True) == \
        BWR_CHECKERBOARD_INVERT_STRING

def test_bgr_rgba_invert_checkboard():
    assert image2h.image_data_to_str(BGR_RGBA_CHECKERBOARD_IMAGE, primary=[0,255,0], secondary=[255,0,0], has_alpha=True, invert=True) == \
        BWR_CHECKERBOARD_INVERT_STRING