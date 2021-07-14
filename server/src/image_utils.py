import os
import random
from PIL import Image
import tempfile
from .settings import IMAGE_MAX_PIXEL, SNACKS_COMPANIONS


def ratio(width, height):
    ratio = float(width) / float(height)
    return ratio

def clean(value):
    value = int(value)
    if value > IMAGE_MAX_PIXEL:
        return IMAGE_MAX_PIXEL
    return value

def get_size(image, width=None, height=None):
    current_width, current_height = image.size
    current_ratio = ratio(current_width, current_height)

    if width:
        width = clean(width)
        height = int(width / ratio)
    elif height:
        height = clean(height)
        width= int(height * ratio)

    return width, height



class Retriever():
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

    def _get_temp_file(self, image, width, height):
        return f'{tempfile.gettempdir()}/{width}_{height}_{image}'

    def get_byte_image(self, width, height):
        image_bytes = b''
        try:
            chosen_image = random.choice(os.listdir(self.image_path))
        except FileNotFoundError:
            return b''
            
        full_path = f'{self.image_path}/{chosen_image}'

        img = Image.open(full_path)
        img = img.resize((width, height), resample=Image.BICUBIC)
        new_file_path = self._get_temp_file(chosen_image, width, height)
        img.save(new_file_path)
        
        with open(new_file_path, 'rb') as image:
            image_bytes = image.read()
        mimetype = self._guess_mimetypes(chosen_image)
        
        return image_bytes, mimetype
