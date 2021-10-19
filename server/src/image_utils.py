import os
import random
from PIL import Image
import tempfile
from .settings import IMAGE_MAX_PIXEL, SNACKS_COMPANIONS


class ImageManager():
    def __init__(self, path):
        self.path = path
        self.image = Image.open(self.path)

    def read(self, path):
        with open(path, 'rb') as image:
            image_bytes = image.read()
        return image_bytes

    def resize(self, new_dir, width=None, height=None):
        width, height = self._calculate_size(width, height)
        
        img = self.image.resize((width, height), resample=Image.BICUBIC)
        img.save(new_dir)
        return self.path

    def _ratio(self, width, height):
        ratio = float(width) / float(height)
        return ratio

    def _clean(self, value):
        value = int(value)
        if value > IMAGE_MAX_PIXEL:
            return IMAGE_MAX_PIXEL
        return value

    def _calculate_size(self, width=None, height=None):
        if width and height:
            # If the users passes both width and height
            # we return the image as he wants
            return self._clean(width), self._clean(height)

        current_width, current_height = self.image.size

        if width is None and height is None:
            return current_width, current_height

        current_ratio = self._ratio(current_width, current_height)

        if width:
            width = self._clean(width)
            height = int(width / current_ratio)
        elif height:
            height = self._clean(height)
            width= int(height * current_ratio)

        return width, height


class Companions():
    image_path = './server/static/image/{mate}/'
    def __init__(self, mate=None):
        if mate is None:
            mate = random.choice(SNACKS_COMPANIONS)
        self.image_path = self.image_path.format(mate=mate.lower())

    def _guess_mimetypes(self, image):
        default_mime = 'image/png'
        if '.png' in image:
            return default_mime
        elif '.jpeg' in image:
            return 'image/jpeg'
        elif '.gif' in image:
            return 'image/gif'
        else: 
            return default_mime

    def _get_temp_file_dir(self, image, width, height):
        return f'{tempfile.gettempdir()}/{width}_{height}_{image}'

    def get_byte_image(self, width=None, height=None):
        image_bytes = b''
        try:
            chosen_image = random.choice(os.listdir(self.image_path))
        except FileNotFoundError:
            return b'', None
            
        # TODO: Save on cache the image 
        full_path = f'{self.image_path}/{chosen_image}'

        new_file_path = self._get_temp_file_dir(chosen_image, width, height)

        image_manager = ImageManager(full_path)
        tmp_path = image_manager.resize(new_file_path, width, height)
        image_bytes = image_manager.read(tmp_path)
        mimetype = self._guess_mimetypes(chosen_image)
        
        return image_bytes, mimetype
