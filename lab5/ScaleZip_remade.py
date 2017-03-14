import os
from pygame import image
from pygame.transform import scale


class ScaleZip:
    def process_files(self, zipprocessor):
        """Scale each image in the directory from original size to 640x480"""
        for filename in os.listdir(zipprocessor.temp_directory):
            im = image.load(zipprocessor._full_filename(filename))
            scaled = scale(im, (640, 480))
            image.save(scaled, zipprocessor._full_filename(filename))
