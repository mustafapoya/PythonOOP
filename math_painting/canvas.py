import numpy as np
from PIL import Image


class Canvas:
    def __init__(self, height, width, color):
        self.color = color
        self.height = height
        self.width = width

        # create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # change [0, 0, 0] with user given values for color
        self.data[:] = self.color

    def make(self, image_path):
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)
