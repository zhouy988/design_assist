from utils.image import Image
from utils.image_stack import ImageStack

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
        self.image_stack = None

    def set_product(self, product, purpose):
        if product not in self.product:
            self.product[product] = purpose
        else:
            self.product[product] = purpose

    def set_creative_level(self, level):
        self.creative_level = level

    def find_coherence(self, src_images):
        # input a list of image objects and check for coherence
        results = []
        img = Image()
        # coherence features was removed, and quality check will be the only check
        # try & catch block was removed with assumption of valid input
        for image in src_images:
            img.reset()
            img.load_image(image.path)
            quality = img.quality_check()
            results.append(quality)
        return results

    def set_image_stack(self, img_folder):
        self.image_stack = ImageStack()
        self.image_stack.set_image_stack(img_folder)