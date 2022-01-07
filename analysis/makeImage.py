from PIL import Image


def mappoint(i):
    if i > 127:
        return 255
    else:
        return 0


def makeimage(imagename):
    img = Image.open(imagename)
    img = img.point(mappoint)
    img = img.getchannel(0)
    [width, height] = img.size
    for x in range(width):
        y = 0
        linefound = False
        while linefound == False and y < height:
            if img.getpixel((x, y)) == (0, 0, 0):
                linefound = True
                img.paste(Image.new('RGB', (1, height-y), (255, 255, 255)), (x, y+1))
            else:
                y += 1
    # img.show()