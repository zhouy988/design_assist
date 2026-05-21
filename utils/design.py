from utils.image import Image
from utils.image_stack import ImageStack

class DesignAssistant:
    """
    Class name: DesignAssistant
    Description:
    - This class serves to manage image assets from ImageStack class and perform query based operations
    Parameters:
    - design: a design output object
    - theme: a string represent the theme of the design
    - product: a "list" of products with their purposes, each product stores its purpose of use
    - creative_level: variations in creativity (for image modification)
    - image_stack: src image management class
    """
    def __init__(self):
        """
        initialize a design assistant piece
        """
        self.design = None
        self.theme = None
        self.product = {}
        self.creative_level = None
        self.image_stack = None

    def reset(self):
        """
        reset all the parameters
        """
        self.design = None
        self.theme = None
        self.product = {}
        self.creative_level = None
        self.image_stack = None

    def set_product(self, product, purpose):
        """
        set/update product and its purpose within the design assistant product dictionary
        """
        if product not in self.product:
            self.product[product] = purpose
        else:
            self.product[product] = purpose

    def set_creative_level(self, level):
        """
        creative level for further design assistance
        """
        self.creative_level = level

    def find_coherence(self, src_images):
        """
        find coherence among the images (blurriness)
        """
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
        """
        set image stack if given image source
        """
        self.image_stack = ImageStack()
        self.image_stack.set_image_stack(img_folder)