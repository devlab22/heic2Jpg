import os
from PIL import Image
import pillow_heif
import sys
import argparse

# format png, jpeg

class Convert:

    def __init__(self, src:str, target='converted', format='jpeg', save=True):

        self.src = os.path.join(os.getcwd(), src)
        self.save = save
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
        if os.path.isdir(self.src):        
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
            if self.save:         
                heif_file = pillow_heif.read_heif(img)
                image = Image.frombytes( heif_file.mode, heif_file.size, heif_file.data, "raw")
                image.save(newFileName, format=self.format)
            else:
                print(f'{img} -> {newFileName}')

        print('end convert', f'save {self.save}')

def main():
    
    print('main')

    try:

        parser = argparse.ArgumentParser(
                        prog = 'imageConverter',
                        description='convert image from .heic',             
        )

        parser.add_argument('-src', default='fotos', type=str, required=False)
        parser.add_argument('-target', default='converted', type=str, required=False)
        parser.add_argument('-format', default='jpeg', type=str, required=False)
        parser.add_argument('-save', action='store_true')
        args = parser.parse_args()

    #print(args)
        
        src = args.src
        target = args.target
        format = args.format
        save = bool(args.save)

        print('src:', src)
        print('target:', target)
        print('format:', format)
        print('save:', save)   

        #sys.exit(0)

        conv = Convert(src=src, target=target, format=format, save=save)
        conv.processData()

    except KeyError as err:
        print('wrong key ->', err)
    except Exception as err:
        print('ERROR ->', err)

if __name__ == '__main__':
    main()
