from PIL import Image
from PIL import ImageChops


class ImageUtils:

    def compare_images(self, path_one, path_two):
        image_one = Image.open(path_one)
        image_two = Image.open(path_two)
        diff = ImageChops.difference(image_one, image_two)

        if diff.getbbox() is None:
            return True
        else:
            return False
