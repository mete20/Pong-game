import turtle as t
import os


# Score varibales

player_a_score = 0
player_b_score = 0

#Create the screen

sc = t.Screen()
sc.title = ("Pong Game")
sc.bgcolor = ("black")
sc.setup(width=800, height=6600)

# Left paddle
left_pad = t.Turtle()
left_pad.shape("square")
left_pad.color("red")
left_pad.shapesize(stretch_wid=6, stretch_len=1)
left_pad.penup()
left_pad.goto(-350, 0)

# Right paddle
right_pad = t.Turtle()
right_pad.shape("square")
right_pad.color("red")
right_pad.shapesize(stretch_wid=6, stretch_len=1)
right_pad.penup()
right_pad.goto(350, 0)

# Ball of circle shape
ball = t.Turtle()
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)

# Ball's speed
ball.dx = 10
ball.dy = -10

# Creating a pen for updating the Score

pen = t.Turtle()
pen.speed(0)
pen.color('skyblue')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0                    Player B: 0 ",align="center",font=('Monaco',24,"normal"))

# Moving the left paddle
def paddleaup():
    y = left_pad.ycor()
    y += 15
    left_pad.sety(y)

def paddleadown():
    y = left_pad.ycor()
    y -= 15
    left_pad.sety(y)

# Moving the right paddle
def paddlebup():
    y = right_pad.ycor()
    y += 15
    right_pad.sety(y)

def paddlebdown():
    y = right_pad.ycor()
    y -= 15
    right_pad.sety(y)

# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")




#Game Loop

game_paused = False

def pause_game():
    global game_paused
    game_paused = True

def resume_game():
    global game_paused
    game_paused = False

sc.listen()
sc.onkeypress(pause_game, "p")
sc.onkeypress(resume_game, "r")


def game_loop():
    global game_paused, player_a_score, player_b_score, left_pad, right_pad, ball, pen
    if not game_paused:
    # Moving the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

    # Border collision
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            player_a_score = player_a_score + 1
            pen.clear()
            pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
            os.system("afplay wallhit.wav&")

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            player_b_score = player_b_score + 1
            pen.clear()
            pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
            os.system("afplay wallhit.wav&")
        

    # Paddle collision
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_pad.ycor() + 50 and ball.ycor() > right_pad.ycor() - 50):
            print("hello")
            ball.setx(340)
            ball.color("blue")
            ball.dx *= -1
            os.system("afplay paddle.wav&")


        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_pad.ycor() + 50 and ball.ycor() > left_pad.ycor() - 50):
            ball.setx(-340)
            ball.color("red")
            ball.dx *= -1
            os.system("afplay paddle.wav&")
    sc.ontimer(game_loop, 20)

game_loop()

sc.mainloop()

        





            

