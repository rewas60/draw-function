import turtle
def draw(shape,*polygon,ratio=1):
    """choose shape from [right angled triangle/regular angled triangle/square/Rectangle/Obtuse angle triangle/regular polygon/circle] and you can choose the lenth and choose the number of sides of regular_polygon """
    x = turtle.Turtle()
    ratio=int(ratio)
 
#Right-angled triangle

    if "right angled triangle" in str(shape):
        x.forward(9*ratio)
        x.right(90)
        x.forward(16*ratio)
        x.right(150)
        x.forward(19*ratio)
   
   #####################################################

#regular angled triangle
    elif "regular angled triangle" in str(shape):
        x.forward(100*ratio)
        x.right(120)
        x.forward(100*ratio)
        x.right(120)
        x.forward(100*ratio)
        x.right(120)

    ######################################################

#Obtuse angle triangle
    elif "Obtuse angle triangle" in str(shape):
        x.forward(100*ratio)
        x.right(60)
        x.forward(100*ratio)
        x.right(150)
        x.forward(175*ratio)
        x.right(150)


   #####################################################
#square
    elif "square" in str(shape):
        for i in range(4):
            x.forward(100*ratio)
            x.right(90)

    #####################################################

#circle
    elif "circle" in str(shape):
        x.speed(1000)
        for i in range(360):
            x.forward(1*ratio)
            x.right(1)
     #####################################################
#Rectangle
    elif "Rectangle" in str(shape):
        x.forward(100*ratio)
        x.right(90)
        x.forward(70*ratio)
        x.right(90)
        x.forward(100*ratio)
        x.right(90)
        x.forward(70*ratio)
        x.right(90)

       #####################################################
    elif "regular polygon" in str(shape):
        f = int(polygon)
        for i in range(f):
            x.forward(100*ratio)
            x.right(360/f)


    else:
        raise Exception("the shape you enterd isnt't available right now please contact us in (rewashossam2006@gmail.com)if you want to add new shape to the function")
    
draw("right angled triangle")