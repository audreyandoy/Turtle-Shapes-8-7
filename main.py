import turtle

turtle.title("My Turtle Game")
turtle.bgcolor("grey")
turtle.setup(600, 600)
turtle.shape("turtle")

screen = turtle.Screen()
speedy = turtle.Turtle()

input_shape = input("What shape do you want to draw?: ")
input_length = input("Choose how big: ")
input_color = input("Choose color: ")

def triangle(length, color):
  speedy.fillcolor(color)
  speedy.begin_fill()

  x = 0
  while x < 3:
    speedy.forward(int(length))
    speedy.right(120)
    x = x+1
  speedy.end_fill()

def triangle(length, color):
  speedy.fillcolor(color)
  speedy.begin_fill()

  x = 0
  while x < 3:
    speedy.forward(int(length))
    speedy.right(120)
    x = x+1
  speedy.end_fill()
    
def circle(length, color):
  speedy.fillcolor(color)
  speedy.begin_fill()

  x = 0
  while x < 36:
    speedy.forward(int(length))
    speedy.right(10)
    x = x+1
  speedy.end_fill()

def star(length, color):
  speedy.fillcolor(color)
  speedy.begin_fill()

  x = 0
  while x < 5:
    speedy.forward(int(length))
    speedy.right(144)
    x = x+1
  speedy.end_fill()

  
if input_shape.lower() == "triangle":
  triangle(input_length, input_color)
elif input_shape.lower() == "square":
  square(input_length, input_color)
elif input_shape.lower() == "circle":
  circle(input_length, input_color)
elif input_shape.lower() == "star":
  star(input_length, input_color)


