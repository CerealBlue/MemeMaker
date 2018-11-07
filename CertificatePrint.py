import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except Exception as e:
    print (e)
    sys.exit()

class Template:
    def __init__(self):
        self.Name = ''
        self.Path = ''

        self.Data = {
            'x_TL' : 0,
            'y_TL' : 0,
            'x_BR' : 0,
            'y_BR' : 0
        }

        self.Dimensions = {
            'height' : 0,
            'width' : 0
        }

    def setName(self, name : str):
        self.Name = name

    def setPath(self, path : str):
        self.Path = path

    def getDimensions(self):
        image = Image.open(self.Path)
        self.Dimensions['width'] ,self.Dimensions['height']  = image.size

    def addRect(self, x_TL, y_TL, x_BR, y_BR, color : str):
        TempImage = 'Tmp'+self.Path

        tmpImg = Image.open(self.Path)

        tmpDraw = ImageDraw.Draw(tmpImg)
        tmpDraw.Rectangle( xy = ((x_TL, y_TL), (x_BR, y_BR)), outline = color )

        tmpImg.save(TempImage)

        return TempImage
