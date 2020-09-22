import turtle

#window options
wnd = turtle.Screen()   #window
wnd.title("Ping Pong Game @ Shad Reza") #title on window
wnd.bgcolor("black")    #window background
wnd.setup(width=800,height=600) #window screen height , weight
wnd.tracer(0)   #tracer 0 stops the window from updating & manually update it

#left bar
left_bar = turtle.Turtle()
left_bar.speed(0)
left_bar.shape("square")
left_bar.color("green")
left_bar.penup()
left_bar.goto(-380,0)
left_bar.shapesize(stretch_wid=6 , stretch_len=1)

#right bar
right_bar = turtle.Turtle()
right_bar = turtle.Turtle()
right_bar.speed(0)
right_bar.shape("square")
right_bar.color("blue")
right_bar.penup()
right_bar.goto(375,0)
right_bar.shapesize(stretch_wid=6 , stretch_len=1)

#ball
ball = turtle.Turtle()
ball = turtle.Turtle()
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 0.25
ball.dy = -0.25

#points
point_right=0
point_left=0

#scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.goto(0,260)
scoring.write("Left : 0  ||  Right : 0" , align="center" , font=("Courier" , 20 , "normal"))
scoring.hideturtle()

#borders
border_right = turtle.Turtle()
border_right.color("yellow")
border_right.speed(0)
border_right.penup()
border_right.goto(390,0)
border_right.shape("square")
border_right.shapesize(stretch_wid=40,stretch_len=0.25)

border_left = turtle.Turtle()
border_left.color("yellow")
border_left.speed(0)
border_left.penup()
border_left.goto(-398,0)
border_left.shape("square")
border_left.shapesize(stretch_wid=40,stretch_len=0.25)

border_up = turtle.Turtle()
border_up.color("yellow")
border_up.speed(0)
border_up.penup()
border_up.goto(0,300)
border_up.shape("square")
border_up.shapesize(stretch_wid=0.35,stretch_len=400)

border_down = turtle.Turtle()
border_down.color("yellow")
border_down.speed(0)
border_down.penup()
border_down.goto(0,-290)
border_down.shape("square")
border_down.shapesize(stretch_wid=0.35,stretch_len=400)

# functions
def left_bar_move_up():
    if left_bar.ycor() + 60 <= 300:
        y = left_bar.ycor()
        y+=20
        left_bar.sety(y)

def left_bar_move_down():
    if left_bar.ycor() - 60 >= -300:
        y = left_bar.ycor()
        y-=20
        left_bar.sety(y)

def right_bar_move_up():
    if right_bar.ycor() + 60 <= 300:
        y = right_bar.ycor()
        y+=20
        right_bar.sety(y)

def right_bar_move_down():
    if right_bar.ycor() - 60 >= -300:
        y = right_bar.ycor()
        y-=20
        right_bar.sety(y)

def escape():
    ball.dx=0
    ball.dy=0
    win = turtle.Turtle()
    win.color("green")
    win.speed(0)
    win.penup()
    win.hideturtle()
    if(point_left>point_right):
        win.write("Winner : Left", align="center",
                      font=("Courier", 40, "normal"))

    elif (point_left < point_right):
        win.write("Winner : Right", align="center",
                       font=("Courier", 40, "normal"))

    else:
        win.color("red")
        win.write("Draw", align="center",
                  font=("Courier", 40, "normal"))

#inverse direction of y cordinate
def inverse_y(x):
    ball.sety(x)
    ball.dy *= -1

#inverse direction of x cordinate
def inverse_x(x):
    ball.setx(x)
    ball.dx *= -1

def total_points():
    return point_left+point_right

#listen for keyboard
wnd.listen()
wnd.onkeypress(left_bar_move_up,"w")
wnd.onkeypress(left_bar_move_down, "s")
wnd.onkeypress(right_bar_move_up,"Up")
wnd.onkeypress(right_bar_move_down,"Down")
wnd.onkeypress(escape,"Escape")

#main game loop
while True:
    wnd.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border check
    if ball.ycor() > 290:
        inverse_y(290)
    if ball.xcor() > 390:
        ball.sety(0)
        inverse_x(0)
        point_left+=1
        scoring.clear()
        scoring.write("Left : {}  ||  Right : {}".format(point_left, point_right), align="center",
                      font=("Courier", 20, "normal"))
        if (total_points() > 0 and total_points() % 5 == 0):
            ball.dx *= 1.05
            ball.dy *= 1.05
    if ball.ycor()<-290:
        inverse_y(-290)
    if ball.xcor()<-390:
        ball.sety(0)
        inverse_x(0)
        point_right+=1
        scoring.clear()
        scoring.write("Left : {}  ||  Right : {}".format(point_left, point_right), align="center",
                      font=("Courier", 20, "normal"))
        if(total_points()>0 and total_points()%5==0):
            ball.dx*=1.25
            ball.dy*=1.25
    if (ball.xcor()>=365 and (ball.ycor()<=right_bar.ycor()+60 and ball.ycor()>=right_bar.ycor()-60)):
        inverse_x(ball.xcor())
    if (ball.xcor()<=-370 and (ball.ycor()<=left_bar.ycor()+60 and ball.ycor()>=left_bar.ycor()-60)):
        inverse_x(ball.xcor())
