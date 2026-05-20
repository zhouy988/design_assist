import cv2
import numpy as np

class Image:
    def __init__(self, path):
        self.path = path
        self.data = None
        self.load_image()

    def reset(self):
        self.data = None

    def load_image(self):
        try:
            self.data = cv2.imread(self.path)
        except Exception as e:
            raise ValueError(f"invalid image source: {e}")
        
    def resize_image(self, target_rows=256, target_cols=256):
        self.data = cv2.resize(self.data, (target_cols, target_rows))
        return self.data
    
    def crop_image(self, x, y, width=256, height=256):
        self.data = self.data[y:y+height, x:x+width]
        return self.data
    
    def convert_to_grayscale(self):
        self.data = cv2.cvtColor(self.data, cv2.COLOR_BGR2GRAY)
        return self.data

    def quality_check(self, threshold=100):
        if self.data is None:
            raise ValueError("invalid image")
        laplacian_var = cv2.Laplacian(self.data, cv2.CV_64F).var()
        return laplacian_var >= threshold # lower laplacian variance means more blurry image
    
    def normalize_image(self):
        self.data = cv2.normalize(self.data, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
        return self.data