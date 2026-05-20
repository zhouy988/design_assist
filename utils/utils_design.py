from utils.utils_image import Image
from utils.utils_image_stack import ImageStack

class DesignAssistant:
    def __init__(self):
        self.design = None
        self.theme = None
        self.product = {}
        self.creative_level = None
        self.image_stack = None

    def reset(self):
        self.design = None
        self.theme = None
        self.product = {}
        self.creative_level = None

    def set_product(self, product, purpose):
        if product not in self.product:
            self.product[product] = purpose
        else:
            self.product[product] = purpose

    def set_creative_level(self, level):
        self.creative_level = level

    def find_coherence(self, images):
        # input a list of image objects and check for coherence
        results = []
        for image in images:
            try:
                img = Image(image)
                img.reset()
                quality, coherence = img.quality_check(), img.check_coherence(image)
                results.append((image, quality, coherence))
                return results
            except Exception as e:
                print(f"invalid {image}: {e}")
                return None
            
    def set_image_stack(self, img_folder):
        self.image_stack = ImageStack()
        self.image_stack.clear_images()
        self.image_stack.create_image_stack(img_folder)
        self.image_stack.resize_images()

    def design_supplies(self, order):
        # check the coherence of the design, and return supplies suggestions
        inspiration_diversity = self.find_coherence()