# 1)
# """
# A spiral hexagon...
# Download tkinter!
# """
# import turtle
# colors = [ "pink","yellow","blue","green","white","red"]
# sketch = turtle.Pen()
# turtle.bgcolor("black")

# # 1)
# for i in range(200):
#    sketch.pencolor(colors[i % 6])
#    sketch.width(i/100 + 1)
#    sketch.forward(i)
#    sketch.left(59)

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(-20*np.pi, 10*np.pi,0.01)
# y = 2*np.cos(x-2)+np.sin(2*x-4)
# plt.plot(x,y)
# plt.show()

# # 3)
# import turtle  #Inside_Out
# wn = turtle.Screen()
# wn.bgcolor("light yellow")
# skk = turtle.Turtle()
# skk.color("red")


# def sqrfunc(size):
#     for i in range(4):
#         skk.fd(size)
#         size = size + 5
#         skk.left(200)

# sqrfunc(6)
# sqrfunc(26)
# sqrfunc(46)
# sqrfunc(66)
# sqrfunc(86)
# sqrfunc(106)
# sqrfunc(126)
# sqrfunc(146)


# # ♥♥♥♥♥♥♥♥♥♥♥♥♥♥