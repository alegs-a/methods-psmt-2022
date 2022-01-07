from PIL import Image
import numpy as np
from numpy.polynomial.polynomial import polyval, polyfit
import csv
import makeImage

def mappoint(i):
    if i > 127:
        return 255
    else:
        return 0

def variancesquared(mean, true):
    output = 0
    for y in true:
        output += (mean - y) ** 2
    return output

def rsquared(x, y, degree):
    varMean = variancesquared(np.mean(y), y)
    varModel = polyfit(x, y, degree, full=True)[1][0][0]
    return((varMean - varModel)/varMean)


if __name__ == "__main__":
    img = Image.open('dam cropped.png')

    [width, height] = img.size
    rowslist = []
    xvals = []
    yvals = []
    regressionDegree = 10

    # make image binary (each pixel is either white or black)
    img = img.point(mappoint)

    # find coordinates of black pixels
    for x in range(width):
        for y in range(height):
            if img.getpixel((x, y)) == (0, 0, 0):
                # print(x, y, img.getpixel((x, y)))
                rowslist.append([x, height - 1 - y])
                xvals.append(x)
                yvals.append(height - 1 - y)


    with open('points.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(rowslist)

    print('csv done')

    polynomial = polyfit(xvals, yvals, regressionDegree)
    polynomial = polynomial.tolist()
    print('coefficients:', polynomial)
    print('POLYNOMIAL FULL OUTPUT:', polyfit(xvals, yvals, regressionDegree, full=True))

    with open('coefficients.txt', 'w') as file:
        for i in range(len(polynomial)):
            file.write(f'{polynomial[i]:.20f}*x^{i}+')

    makeImage.makeimage('dam cropped.png')
    # print('R^2:', rsquared(xvals, yvals, regressionDegree))