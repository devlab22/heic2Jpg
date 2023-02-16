import os
from PIL import Image
import pillow_heif

# format png, jpeg

class Convert:

    def __init__(self, src:str, target='converted', format='jpeg'):

        self.src = os.path.join(os.getcwd(), src)
        self.target = os.path.join(os.getcwd(), target)
        self.format = format

    def processData(self):

        image_to_convert = []
        if os.path.isdir(self.src):
           image_to_convert = self.__readData()
        elif self.src.endswith(".heic") or self.src.endswith(".HEIC"):
            image_to_convert.append(self.src)

        self.__convertData(image_to_convert)

    def __readData(self):

        data = []
        if not os.path.isdir(self.src):
            raise Exception('{0} is not directory'.format(self.src))
        
        for filename in os.listdir(self.src):
            if filename.endswith(".heic") or filename.endswith(".HEIC"):
                absolute_filename = os.path.join(self.src, filename)
                data.append(absolute_filename)

        return data
    
    def __convertData(self, toConvert):

        print('start convert')
        if not os.path.exists(self.target):
            os.mkdir(self.target)
            
        for img in toConvert:
            newFileName = os.path.join(self.target, os.path.basename(img).split('.')[0] + f".{self.format}")           
            heif_file = pillow_heif.read_heif(img)
            image = Image.frombytes( heif_file.mode, heif_file.size, heif_file.data, "raw")
            image.save(newFileName, format=self.format)

        print('end convert')


