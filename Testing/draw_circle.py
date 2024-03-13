# # Program to plot a Circle
# # using Parametric equation of a Circle
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# theta = np.linspace(0, 2 * np.pi, 150)
#
# radius = 15
#
# a = radius * np.cos(theta)
# b = radius * np.sin(theta)
#
# figure, axes = plt.subplots(1)
#
# axes.plot(a, b)
# axes.set_aspect(1)
#
# plt.title('Parametric Equation Circle')
# plt.show()

import matplotlib.pyplot as plt


# set axis limits of plot (x=0 to 20, y=0 to 20)

def draw_circle(x1=5, y1=5, rad1=1, fill1=True, x2=10, y2=10, rad2=2, fill2=True, x3=15, y3=13, rad3=3, fill3=True):
    plt.axis([0, 20, 0, 20])
    plt.axis("equal")

    # define circles
    c1 = plt.Circle((x1, y1), radius=rad1, fill=fill1)
    c2 = plt.Circle((x2, y2), radius=rad2, fill=fill2)
    c3 = plt.Circle((x3, y3), radius=rad3, fill=fill3)

    # add circles to plot
    plt.gca().add_artist(c1)
    plt.gca().add_artist(c2)
    plt.gca().add_artist(c3)


draw_circle()
plt.show()
