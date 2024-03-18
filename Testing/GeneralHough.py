import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from draw_circle import draw_circle

fn = "test_image/one_circle.png"  # путь к файлу с картинкой


# fn = draw_circle('test_image/one_circle.png', x_lim_from=-40, x_lim_to=40, y_lim_from=-40, y_lim_to=40, x1=1, y1=-5,
#                  rad1=15, rad2=0, rad3=0, y2=0,
#                  x2=0, x3=0, y3=0)


def GenHough(image, rad=88):
    img = cv.imread(image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    nRows, nCols = len(gray), len(gray[0])

    window_name = ('Sobel Demo - Simple Edge Detector')
    scale = 1
    delta = 0
    ddepth = cv.CV_16S
    grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)

    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)

    grad = cv.addWeighted(abs_grad_x, 1, abs_grad_y, 1, 0)

    _, th3 = cv.threshold(grad, 0.65 * 255, 255, cv.THRESH_BINARY)

    row, col = np.where(th3 == 255)
    res = np.zeros_like(th3, dtype=np.uint32)  # Инициализация массива для накопления результатов
    for k in range(row.shape[0]):
        x = np.arange(th3.shape[0])[:, None] - row[k]  # Разность координат x
        y = np.arange(th3.shape[1])[None, :] - col[k]  # Разность координат y
        distance = np.round(np.sqrt(x ** 2 + y ** 2))  # Округленное расстояние от центра
        res[distance == rad] += 1  # Увеличиваем счетчик для соответствующих пикселей

    filtered = np.piecewise(res, [res < 60, res >= 60], [0, 255])
    row1, col1 = np.where(filtered == 255)

    for k in range(len(col1)):
        for i in range(nRows):
            for j in range(nCols):
                if np.ceil(np.sqrt((i - row1[k]) ** 2 + (j - col1[k]) ** 2)) == rad:
                    img[i][j][0] = 0
                    img[i][j][1] = 255
                    img[i][j][2] = 0

    return img

# res_img = GenHough(fn)
# plt.imshow(cv.cvtColor(res_img, cv.COLOR_BGR2RGB))
# plt.show()
