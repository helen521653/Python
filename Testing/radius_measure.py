import cv2 as cv


def radius_measure(path_to_img):
    image = cv.imread(path_to_img)

    circle_count = 0

    circle_sum_x = 0
    circle_sum_y = 0

    circle_min_x = 0
    circle_max_x = 0

    white = [255, 255, 255]

    for y in range(image.shape[1]):
        for x in range(image.shape[0]):
            if image[x, y] is not white:
                circle_count += 1

                circle_sum_x += x
                circle_sum_y += y

                circle_min_x = min(circle_min_x, x)
                circle_max_x = max(circle_max_x, x)

    if circle_count == 0:
        print("No circle found!")
    else:
        circle_center_x = circle_sum_x / circle_count
        circle_center_y = circle_sum_y / circle_count
        circle_radius = (circle_max_x - circle_min_x) / 2

    return circle_radius

# path = "test_image/one_circle.png"
# rad = radius_measure(path)
# print(rad)
