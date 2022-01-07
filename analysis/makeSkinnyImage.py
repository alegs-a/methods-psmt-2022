from PIL import Image, ImageDraw
import numpy as np

if __name__ == "__main__":
    img = Image.open('dam cropped.png')
    draw = ImageDraw.Draw(img)

    [width, height] = img.size

    for x in range(width):
        print(f'Beginning column {x}')
        lineFound = False
        y = 0
        while lineFound == False:
            print(f'({x}, {y})')
            if img.getpixel((x, y)) == (0, 0, 0):
                lineFound = True
                # make white rectangle from (x, y+1) to (x, height)
                draw.line([x, y+1, x, height], (255, 255, 255), 1)
            y += 1
    img.save('skinnyDam.png')
    img.show()