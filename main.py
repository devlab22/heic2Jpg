from Heic2Jpg import Convert

def main():
    print('main')

    src = 'fotos'
    target = 'convertedJPEG'

    conv = Convert(src, target)
    conv.processData()

if __name__ == '__main__':
    main()