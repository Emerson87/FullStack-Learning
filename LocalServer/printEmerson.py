import turtle

def draw_the_world():
    window = turtle.Screen()
    window.bgcolor('white')
    e = turtle.Turtle()
    e.shape("turtle")
    e.color("green")
    e.speed(2)
    
    draw_e(e)
   
    draw_M(e)
       
    
def draw_e(obj):
    obj.forward(100)
    obj.backward(100)
    obj.left(90)
    obj.forward(100)
    obj.right(90)
    obj.forward(100)
    obj.backward(100)
    obj.left(90)
    obj.forward(100)
    obj.right(90)
    obj.forward(100)
    obj.backward(100)

def draw_M(obj):
    obj.left(90)
    obj.forward(100)
    obj.right(135)
    obj.forward(50)
    obj.right(-90)
    obj.forward(50)
    obj.right(135)
    obj.forward(100)
    


draw_the_world()
