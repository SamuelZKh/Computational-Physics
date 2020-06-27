import turtle
import random
wn=turtle.Screen()
wn.bgcolor("black")
##wn.tracer(0)
balls=[]

for i in range(3):
    balls.append(turtle.Turtle())
for ball in balls:

    x=random.randint(-200,200)
    ball.shape("circle")
    ball.color("green")
    ball.penup()  ## erases the trace line
    ball.speed(0)  ## animation speed
    ball.goto(x, 100)  ##initial coordinates

    ball.dy = 0
    ball.dx = 1



gravity=0.9



while True:                                        ## while true loo run loop infinitely til terminated
  ## wn.update()                                 ## works with tracer to makescreen smooth
   for ball in balls:
       ball.dy -= gravity
       ball.sety(ball.ycor() + ball.dy)                 ##updates the new coordinates of the ball
       ball.setx(ball.xcor() + ball.dx)

       ## set of boundary conditions

       if ball.ycor() < -300:
           ball.dy *= -1
       if ball.xcor() > 320:
           ball.dx *= -1
       if ball.xcor() < -320:
           ball.dx *= -1





wn.mainloop()