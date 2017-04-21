import turtle

def draw_the_world():
    window = turtle.Screen()
    window.bgcolor('white')
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(2)
    
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    
    
def draw_square(obj):
     
    for i in range(1,5):
        obj.forward(100)
        obj.right(90)
        


def draw_triangle():
    
    any = turtle.Turtle()
    any.shape("triangle")
    any.color("red")
    any.speed(2)
    n = 0
    while n < 3 :
        any.forward(100)
        any.left(120)
        n = n + 1

def draw_circle():
    
    bob = turtle.Turtle()
    bob.shape("arrow")
    bob.color("blue")
    bob.speed(2)
    bob.circle(100)
   


draw_the_world()
    
    