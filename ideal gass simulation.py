import turtle
import random
import numpy as np
wn=turtle.Screen()
wn.bgcolor("black")
wn.tracer(0)
balls=[]
n=50
colors=["red","blue","green","purple","white","orange"]
collision=0
for i in range(n):
    balls.append(turtle.Turtle())
for ball in balls:

    y=random.randint(-300,300)
    x=random.randint(-200,200)
    ball.shape("circle")

    ball.color(random.choice(colors))
    ball.penup()  ## erases the trace line
    ball.speed(0)  ## animation speed
    ball.goto(x, y)  ##initial coordinates
    while True:
        ball.dy = random.randint(-1, 1)
        ball.dx = random.randint(-1, 1)
        if ball.dy !=0 and ball.dx!=0:
            break




while True:                                        ## while true loo run loop infinitely til terminated
   wn.update()                                 ## works with tracer to makescreen smooth
   for ball in balls:

       ball.sety(ball.ycor() + ball.dy)                 ##updates the new coordinates of the ball
       ball.setx(ball.xcor() + ball.dx)


       ## set of boundary conditions

       if ball.ycor() < -300:
           ball.dy *= -1
       if ball.ycor() > 300:
           ball.dy *= -1
       if ball.xcor() > 300:
           ball.dx *= -1
       if ball.xcor() < -300:
           ball.dx *= -1


       for j in range(0,n):
           for k in range(j+1,n):
               if balls[j].xcor() == balls[k].xcor() and balls[j].ycor() == balls[k].ycor() :
                   ball.dx*=-1
                   ball.dy*=-1
                   collision=collision+1
                   print(collision)
                   break

wn.mainloop()