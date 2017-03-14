import sys
import os
import shutil
import zipfile
from pygame.transform import scale
from pygame import image


class ZipProcessor:
    """This class responds for correct using of zip process"""
    def __init__(self, zipname):
        """setting var`s"""
        self.zipname = zipname
        self.temp_directory = "unzipped-{}".format(zipname[:-4])

    def _full_filename(self, filename):
        """Method returning a full path for given file"""
        return os.path.join(self.temp_directory, filename)

    def process_zip(self):
        """method response for testing other method`s"""
        self.unzip_files()
        self.process_zip()
        self.zip_files()

    def unzip_files(self):
        """unzipping given file"""
        os.mkdir(self.temp_directory)
        zip = zipfile.ZipFile(self.zipname)
        try:
            zip.extractall(self.temp_directory)
        finally:
            zip.close()

    def zip_files(self):
        """zipping given file"""
        file = zipfile.ZipFile(self.zipname, "w")
        for filename in os.listdir(self.temp_directory):
            file.write(self._full_filename(filename), filename)
        shutil.rmtree(self.temp_directory)


class ZipReplace(ZipProcessor):
    """class responds for writing into the file"""
    def __init__(self, filename, search_string, replace_string):
        super().__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self):
        """perform a search and replace on all files in the temporary directory"""
        for filename in os.listdir(self.temp_directory):
            with open(self._full_filename(filename)) as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with open(self._full_filename(filename), "w") as file:
                file.write(contents)


class ScaleZip(ZipProcessor):
    def process_files(self):
        """Scale each image in the directory from original size to 640x480"""
        for filename in os.listdir(self.temp_directory):
            im = image.load(self._full_filename(filename))
            scaled = scale(im, (640, 480))
            image.save(scaled, self._full_filename(filename))


if __name__ == "__main__":
    ScaleZip(*sys.argv[1:4]).process_zip()
