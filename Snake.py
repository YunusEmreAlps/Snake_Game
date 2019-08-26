# Snake Game

import turtle # Graphical package
import random
import time

turtle.hideturtle()

slp = 0.1 # sleep time
score = 0
high_score = 0

spd = 0 # speed
lvl = 1 # level

# Screen
window = turtle.Screen()
window.title("Snake")
window.bgcolor("white") # bg : background
window.setup(width=600,height=600)
window.direction="white"

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"


# Snake Move
def U(): # Up
    head.direction = "up"
def D(): # Down
    head.direction = "down"
def R(): # Right
    head.direction = "right"
def L(): # Left
    head.direction = "left"

def move():
    if head.direction =="up":
        y = head.ycor()
        head.sety(y+20)
    elif head.direction =="down":
        y = head.ycor()
        head.sety(y-20)
    elif head.direction =="right":
        x = head.xcor()
        head.setx(x+20)
    elif head.direction =="left":
        x = head.xcor()
        head.setx(x-20)

# Keyboard 
def key():
    
    window.onkeypress(U, "Up")
    window.onkeypress(D, "Down")
    window.onkeypress(R, "Right")
    window.onkeypress(L, "Left")
    window.onkeypress(U, "w")
    window.onkeypress(D, "s")
    window.onkeypress(R, "d")
    window.onkeypress(L, "a")
    window.listen()
# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(100,100)
food.direction = "stop"

body = [] # list

# Eat
def eat():
    if(head.distance(food)<20):
        food.direction = "eat"
        x_cor = random.randint(-290,290)
        y_cor = random.randint(-290,290)
        food.goto(x_cor,y_cor)
# Add Body
        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.shape("circle")
# Color
        cl = (
         "Medium Aquamarine","Aquamarine","Dark Green","Dark Olive Green",	 
         "Dark Sea Green","Sea Green","Medium Sea Green","Light Sea Green",	 
         "Pale Green","Spring Green","Lawn Green","Chartreuse","Medium Spring Green",	 
         "Green Yellow","Lime Green","Yellow Green","Forest Green","Olive Drab",	 
         "Dark Khaki","Khaki")
        
        a = random.choice(cl)
        
        head.color(a)
        new_part.color(a)
        
        new_part.penup()
        body.append(new_part)
        
    for i in range(len(body)-1,0,-1):
        x = body[i-1].xcor() 
        y = body[i-1].ycor() 
        body[i].goto(x,y) 
        
    if len(body)> 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)
        
# Wall
def wall():
    x_h = head.xcor()
    y_h = head.ycor()
    
    if((x_h > 290 or x_h < -290)or(y_h > 290 or y_h <-290)):
        head.goto(0,0)
        head.direction = "stop"
        for i in body:
            i.goto(800,800)
        body.clear()

# Eat Myself
def eat_myself():
    for i in body:
        if(i.distance(head)<20):
             head.goto(0,0)
             head.direction = "stop"
             for i in body:
                 i.goto(800,800)
             body.clear()
            
# Score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write("Score : 0 , High Score : 0 ",align="center",font=("arial",24,"normal"))


# Level
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.shape("square")
pen1.color("black")
pen1.penup()
pen1.goto(200,-290)
pen1.hideturtle()
pen1.write("Level : 1 ",align="center",font=("arial",12,"normal"))
    
# Main Function
while 1 : 
    window.update()    
    eat()
    key()
    move()
    eat_myself()
    wall()
    if food.direction == "eat":
        score += 10
        if score > high_score:
            high_score = score
        if(score >= 50*lvl):
            lvl += 1
            slp -= 0.001
            
        pen.clear()
        pen.write("Score : {} , High Score : {} ".format(score,high_score),align="center",font=("arial",24,"normal"))
        pen1.clear()
        pen1.write("Level : {} ".format(lvl),align="center",font=("arial",12,"normal"))
        food.direction = "stop"
    if head.direction == "stop":
        score = 0
        slp = 0.1
        lvl = 1

    time.sleep(slp)
    
window.mainloop()