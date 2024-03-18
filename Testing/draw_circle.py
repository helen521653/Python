import matplotlib.pyplot as plt
import cv2 as cv


# set axis limits of plot (x=0 to 20, y=0 to 20)

def draw_circle(path_to_img, x_lim_from=0, x_lim_to=20, y_lim_from=0, y_lim_to=20, x1=5, y1=5, rad1=1, fill1=True,
                x2=10, y2=10,
                rad2=2, fill2=True, x3=15, y3=13, rad3=3, fill3=True):
    plt.axis([x_lim_from, x_lim_to, y_lim_from, y_lim_to])
    plt.axis("equal")

    # define circles
    c1 = plt.Circle((x1, y1), radius=rad1, fill=fill1)
    # c2 = plt.Circle((x2, y2), radius=rad2, fill=fill2)
    # c3 = plt.Circle((x3, y3), radius=rad3, fill=fill3)

    # add circles to plot
    plt.gca().add_artist(c1)
    # plt.gca().add_artist(c2)
    # plt.gca().add_artist(c3)
    plt.axis('off')
    plt.savefig(path_to_img)

    return path_to_img

# img = draw_circle(x_lim_from=-40, x_lim_to=40, y_lim_from=-40, y_lim_to=40, x1=1, y1=-5, rad1=15, rad2=0, rad3=0, y2=0,
#                   x2=0, x3=0, y3=0)
# plt.show()


# path = draw_circle('test_image/basic.png')
# img = cv.imread(path)
# cv.imshow('img', img)
# cv.waitKey(0)
# cv.destroyAllWindows()
