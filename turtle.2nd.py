Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> from turtle import Turtle, Screen
>>> 
>>> jun = Turtle()
>>> jun.shape("turtle")
>>> screen = Screen()
>>> 
>>> def move_fd():
...     jun.forward(100)
...     jun.left(90)
...     jun.forward(100)
...     jun.right(90)
...     jun.forward(100)
...     jun.right(90)
...     jun.forward(100)
...     jun.left(90)
...     jun.forward(100)
... 
...     
>>> screen.onkey(key = "r" , fun = move_fd)
>>> screen.listen()
>>> screen.exitonclick()
