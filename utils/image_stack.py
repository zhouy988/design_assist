import os
from utils.image import Image

class ImageStack:
    """
    Class name: ImageStack
    Description:
    - This class helps with the image asset management
    Parameters:
    - images: list of image path
    """
    def __init__(self):
        """
        initialize an image stack
        """
        self.images = []

    def set_image_stack(self, img_folder):
        """
        set image stack for valid folder
        """
        if not os.path.isdir(img_folder):
            print(f"invalid path: {img_folder}")
        self.clear_images()
        self.create_image_stack(img_folder)
        self.resize_images()
    
    def add_image(self, image):
        """
        add an image item to the image stack
        """
        if image is not None:
            self.images.append(image)
        else:
            raise ValueError("invalid image")
    
    def get_images(self):
        """
        get the current image stack
        """
        return self.images
    
    def clear_images(self):
        """
        clear images
        """
        self.images = []

    def create_image_stack(self, image_folder):
        """
        create a stack with valid src image folder
        """
        if not os.path.isdir(image_folder):
            print(f"Error: {image_folder} is not a valid directory.")
            return
        valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')
        try:
            for filename in os.listdir(image_folder):
                if filename.lower().endswith(valid_extensions):
                    image_path = os.path.join(image_folder, filename)
                    img = Image()
                    img.load_image(image_path)
                    self.add_image(img)
        except Exception as e:
            print(f"something went wrong at {image_folder}: {e}")

    def resize_images(self):
        """
        resize the images to an uniform size
        """
        for image in self.images:
            image.crop_image(width=256, height=256)
            image.resize_image(target_rows=256, target_cols=256)