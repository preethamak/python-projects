import turtle
import winsound

#get window screen 
window = turtle.Screen()

#title for the window
window.title = ("PONG GAME")

#background color
window.bgcolor("black")

#getting the sizes
window.setup(width = 800, height = 600)

#speeding up the program
window.tracer(0) 

#score
score_a = 0
score_b = 0  

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid= 5, stretch_len=0.5)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid= 5, stretch_len=0.5)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("purple")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.6    #speed reqired
ball.dy = 0.6

#mid line
midline1 = turtle.Turtle()
midline1.speed(0)
midline1.shape("square")
midline1.color("red")
midline1.penup()
midline1.goto(0, 0)
midline1.shapesize(stretch_wid= 800, stretch_len=0.2)

#midline2 = turtle.Turtle()
#midline2.speed(0)
#midline2.shape("square")
#midline2.color("red")
#midline2.penup()
#midline2.goto(-70, 0)
#midline2.shapesize(stretch_wid= 800, stretch_len=0.2)

#score board
pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

#for the border on right side
#border1 = turtle.Turtle()
#border1.speed(0)
#border1.shape("square")
#border1.color("red")
#border1.penup()
#border1.goto(-397, 0)
#border1.shapesize(stretch_wid= 800, stretch_len=0.2)

#for the border on right side
#border2 = turtle.Turtle()
#border2.speed(0)
#border2.shape("square")
#border2.color("red")
#border2.penup()
#border2.goto(390, 0)
#border2.shapesize(stretch_wid= 800, stretch_len=0.2)

#for the border of top
#border3 = turtle.Turtle()
#border3.speed(0)
#border3.shape("square")
#border3.color("red")
#border3.penup()
#border3.goto(0,297.5)
#border3.shapesize(stretch_wid= 0.2, stretch_len=600)

#for the border of bottom
#border4 = turtle.Turtle()
#border4.speed(0)
#border4.shape("square")
#border4.color("red")
#border4.penup()
#border4.goto(0,-290)
#border4.shapesize(stretch_wid= 0.2, stretch_len=600)

#moving function for paddle A
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
    
#moving paddle A down
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

#moving paddle B up
def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
    
#moving paddle B down
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)


#keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

#main game loop
while True:
    window.update()
    
    #move the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)
    
    #ball hitting the border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
            
    #border for left and right side
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
    #collision with the paddles
    #right paddle
    if (ball.xcor()>340 and ball.xcor()<350 and (ball.ycor()< paddle_b.ycor()+40 and ball.ycor()> paddle_b.ycor()-50)):
        ball.setx(340)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
    #left side
    if (ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor()< paddle_a.ycor()+40 and ball.ycor()> paddle_a.ycor()-50)):
        ball.setx(-340)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
        #AI Player1
    if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor())>10:
        paddle_b_up()
           
    elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor())>10:
        paddle_b_down() 
       
       #For AI Player2  
   # if paddle_a.ycor() < ball.ycor()and abs(paddle_a.ycor() - ball.ycor())>10:
    #    paddle_a_up()
           
   # elif paddle_a.ycor() > ball.ycor()and abs(paddle_a.ycor() - ball.ycor())>10:
    #    paddle_a_down() 
    