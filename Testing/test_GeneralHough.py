import matplotlib.pyplot as plt
import pytest
from GeneralHough import GenHough
from HoughCV import HoughCV
from radius_measure import radius_measure
from comparision import mse


# rad=(radius_measure(image) / 2.7)
@pytest.mark.parametrize(
    "image",
    [
        'test_images\\small.png',
        'test_images\\intersect.png',
        'test_images\\partly_showen.png',
        'test_images\\circ_sq_intersect.png',
        'test_images\\several_obj.png',
    ]
)
def test_GeneralHough(image):
    img1 = GenHough(image, rad=(radius_measure(image) / 2.7))
    img2 = HoughCV(image)
    error, diff = mse(img1, img2)
    assert (error <= 5)

# def test_rect(image="test_images\\rect.png"):
#     result = GenHough(image)
#     plt.imshow(result)
#     plt.show()
#     pass


# test_rect()


# def test_several_obj(image="test_images\\several_obj.png"):
#     result = GenHough(image)
#     plt.imshow(result)
#     plt.show()
#     pass
#
#
# test_several_obj()


# def test_partly_showen(image="test_images\\partly_showen.PNG"):
#     result = GenHough(image)
#     plt.imshow(result)
#     plt.show()
#     pass
#
#
# test_partly_showen()


# def test_circ_sq_intersect(image="test_images\\circ_sq_intersect.png"):
#     result = GenHough(image)
#     plt.imshow(result)
#     plt.show()
#     pass
#
#
# test_circ_sq_intersect()


# def test_diff_rad(image="test_images\\diff_rad.png"):
#     result = GenHough(image)
#     plt.imshow(result)
#     plt.show()
#     pass
#
#
# test_diff_rad()


# def test_intersect(image="test_images\\intersect.png"):
#     result = GenHough(image)
#     plt.imshow(result)
#     plt.show()
#     pass
#
# test_intersect()
