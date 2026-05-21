import pytest
# import cv2
# import numpy as np
import sys
import os

CLASSES_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, CLASSES_FOLDER)

from utils.image import Image 
from utils.image_stack import ImageStack
from utils.design import DesignAssistant

# test the image class
class TestImage:
    @pytest.fixture
    def img(self):
        img = Image()   
        return img

    def test_load_image_success(self, img):
        img.load_image("../lib/test_images/img0.jpeg")
        assert img.data is not None, "test image loaded"

    def test_load_image_failure(self, img):
        with pytest.raises(ValueError):
            img.load_image("../img2.jpeg")

    def test_resize_image(self, img):
        img.load_image("../lib/test_images/img0.jpeg")
        resized_img = img.resize_image(100, 100)
        assert resized_img.data.shape[:2] == (100, 100), "resized successfully"

    def test_crop_image(self, img):
        img.load_image("../lib/test_images/img0.jpeg")
        cropped = img.crop_image(50, 50)
        assert cropped.shape[:2] == (50, 50), "cropped successfully"

    def test_save_image(self, img):
        img.load_image("../lib/test_images/img0.jpeg")
        img.crop_image(256, 256)
        img.save_image("../lib/outputs/img0_cropped.jpg")
        assert os.path.exists("../lib/outputs/img0_cropped.jpg"), "modified image saved"

class TestImageStack:
    @pytest.fixture
    def img_stack(self):
        img_stack = ImageStack()
        return img_stack

    def test_create_image_stack(self, img_stack):
        img_stack.create_image_stack("../lib/test_images")
        assert len(img_stack.images) == 2, "created image stack"

    def test_resize_images(self, img_stack):
        img_stack.create_image_stack("lib/outputs")
        img_stack.resize_images()
        for img in img_stack.get_images():
            assert img.data.size == (256, 256), "resized image stack"

class TestDesignAssistant:
    @pytest.fixture
    def da(self):
        da = DesignAssistant()
        return da
    
    def test_initialization(self, da):
        assert da.design is None
        assert da.theme is None
        assert da.product == {}
        assert da.creative_level is None
        assert da.image_stack is None

    def test_reset(self, da):
        da.design = "one design"
        da.theme = "timeless"
        da.product = {"product1": "purpose1"}
        da.creative_level = "high"
        da.image_stack = "test stack"
        
        da.reset()
        
        assert da.design is None
        assert da.theme is None
        assert da.product == {}
        assert da.creative_level is None
        assert da.image_stack is None

    def test_set_product(self, da):
        da.set_product("shoes", "used for walking")
        assert da.product["shoes"] == "used for walking"
        da.set_product("shoes", "used for running") # should not update existing product
        assert da.product["shoes"] == "used for running"

    def test_set_creative_level(self, da):
        da.set_creative_level("medium")
        assert da.creative_level == "medium"

    def test_set_image_stack(self, da):
        da.set_image_stack("../lib/test_images")
        assert da.image_stack is not None
        assert len(da.image_stack.get_images()) > 0

    def test_find_coherence(self, da):        
        da.set_image_stack("../lib/test_images")
        results = da.find_coherence(da.image_stack.images)
        assert results is not None
        assert len(results) == len(da.image_stack.images)

if __name__ == "__main__":
    pytest.main()
