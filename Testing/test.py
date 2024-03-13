import matplotlib.pyplot as plt

from HelensPython.Testing.GeneralHough import GenHough


def test_small(image="test_images\\small.png"):
    result = GenHough(image)
    plt.imshow(result)
    plt.show()
    pass


test_small()


def test_rect(image="test_images\\rect.png"):
    result = GenHough(image)
    plt.imshow(result)
    plt.show()
    pass


test_rect()


def test_several_obj(image="test_images\\several_obj.png"):
    result = GenHough(image)
    plt.imshow(result)
    plt.show()
    pass


test_several_obj()


def test_partly_showen(image="test_images\\partly_showen.PNG"):
    result = GenHough(image)
    plt.imshow(result)
    plt.show()
    pass


test_partly_showen()


def test_circ_sq_intersect(image="test_images\\circ_sq_intersect.png"):
    result = GenHough(image)
    plt.imshow(result)
    plt.show()
    pass


test_circ_sq_intersect()


def test_diff_rad(image="test_images\\diff_rad.png"):
    result = GenHough(image)
    plt.imshow(result)
    plt.show()
    pass


test_diff_rad()


def test_intersect(image="test_images\\intersect.png"):
    result = GenHough(image)
    plt.imshow(result)
    plt.show()
    pass

test_intersect()
