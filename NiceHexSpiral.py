#NiceHexSpiral.py
import turtle   
colors=['red', 'purple', 'blue',
        'green', 'yellow', 'orange']
sides = 5 # this was modified by git web
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x*3/sides+x) # this is another changed line 
    t.forward(360/sides+1) #the 3rd changed place        
    t.left(59)
