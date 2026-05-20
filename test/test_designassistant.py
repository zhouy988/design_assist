from utils.utils_design import DesignAssistant

class TestDesignAssistant:
    def test_initialization(self):
        da = DesignAssistant()
        assert da.design is None
        assert da.theme is None
        assert da.product == {}
        assert da.creative_level is None
        assert da.image_stack is None

    def test_reset(self):
        da = DesignAssistant()
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

    def test_set_product(self):
        da = DesignAssistant()
        da.set_product("shoes", "used for walking")
        assert da.product == {"shoes": "used for walking"}
        
        da.set_product("shoes", "used for running") # should not update existing product
        assert da.product == {"shoes": "used for walking"}

    def test_set_creative_level(self):
        da = DesignAssistant()
        da.set_creative_level("medium")
        assert da.creative_level == "medium"

    def test_set_image_stack(self):
        da = DesignAssistant()
        da.set_image_stack("../lib/test_images")
        assert da.image_stack is not None
        assert len(da.image_stack.get_images()) > 0

    def test_find_coherence(self):
        da = DesignAssistant()
        da.set_image_stack("../lib/test_images")
        images = da.image_stack.get_images()
        results = da.find_coherence(images)
        assert results is not None
        assert len(results) == len(images)