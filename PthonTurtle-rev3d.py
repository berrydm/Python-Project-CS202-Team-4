import turtle
import time

# rev 0 - original game downloaded
# rev 1 -  added a second ball, changed screen color,
# rev 2a - add paddles to top and bottom, changed paddle color
# rev 3c - changed keys for top and bottom paddles;
#          added start by hitting "e" and stop play after score, and quit
# rev 3d - removed quit and stopplay - made play too jerky

# Create screen
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("blue")
sc.setup(width=1000, height=600)

# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("red")  # rev 2: changed from black to red
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")  
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

# start mod to add top and bottom paddles -rev2
# top paddle:  copy left_pad and change left to top
top_pad = turtle.Turtle()                       # rev 2
top_pad.speed(0)                                # rev 2
top_pad.shape("square")                         # rev 2
top_pad.color("red")                            # rev 2: change black to red
top_pad.shapesize(stretch_wid=2, stretch_len=6) # rev 2: swap wid and len
top_pad.penup()                                 # rev 2
top_pad.goto(0, 200)                            # rev 2: from -400,0 to 0,200 
                                                # rev 2
# Bottom paddle:  copy right pad and change right to bottom
bottom_pad = turtle.Turtle()                    # rev 2
bottom_pad.speed(0)                             # rev 2
bottom_pad.shape("square")                      # rev 2
bottom_pad.color("black")                       # rev 2: leave black
bottom_pad.shapesize(stretch_wid=2, stretch_len=6) # rev 2: swap wid and len
bottom_pad.penup()                              # rev 2
bottom_pad.goto(0, -200)                        # rev 2: from 400,0 to 0,-200
# end of rev 2 paddle mod

# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(4)  # Adjusted speed
hit_ball.shape("circle")
hit_ball.color("white")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 0 # Set the ball speed to zero at the start of the game (Rev1b)
hit_ball.dy = 0

# Ball2 of circle shape
hit_ball2 = turtle.Turtle()
hit_ball2.speed(4)  # Adjusted speed
hit_ball2.shape("circle")
hit_ball2.color("black")
hit_ball2.penup()
hit_ball2.goto(0, 0)
hit_ball2.dx = 0 # Set the ball speed to zero at the start of the game (Rev3a)
hit_ball2.dy = 0

# Initialize the score
left_player = 0
right_player = 0

# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("black")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0    Right_player: 0",
             align="center", font=("Courier", 24, "normal"))

# Functions to move paddles


def paddleaup():
    y = left_pad.ycor()
    if y < 250:  # Limit paddle movement
        y += 20
        left_pad.sety(y)


def paddleadown():
    y = left_pad.ycor()
    if y > -240:  # Limit paddle movement
        y -= 20
        left_pad.sety(y)


def paddlebup():
    y = right_pad.ycor()
    if y < 250:  # Limit paddle movement
        y += 20
        right_pad.sety(y)


def paddlebdown():
    y = right_pad.ycor()
    if y > -240:  # Limit paddle movement
        y -= 20
        right_pad.sety(y)
# Functions that add a start delay (Rev1b/Rev3a)

def startplay():
    hit_ball.dx = 5
    hit_ball.dy = -5
    hit_ball2.dx = -5
    hit_ball2.dy = -5

def stopplay():
    hit_ball.dx = 0
    hit_ball.dy = 0
    hit_ball2.dx = 0
    hit_ball2.dy = 0

#def Quit():  # quit not working
#    Quit()


# rev 2 copy paddle movements and change to move top and bottom paddles
#
# changes:  y to x; left to top; right to bottom; 250 to 450;  240 to 440
# rev 2
def paddlecright():                         # rev 2
    x = top_pad.xcor()                      # rev 2
    if x < 450:  # Limit paddle movement    # rev 2
        x += 20                             # rev 2
        top_pad.setx(x)                     # rev 2
                                            # rev 2
                                            # rev 2
def paddlecleft():                          # rev 2
    x = top_pad.xcor()                      # rev 2
    if x > -440:  # Limit paddle movement   # rev 2
        x -= 20                             # rev 2
        top_pad.setx(x)                     # rev 2
                                            # rev 2
                                            # rev 2
def paddledright():                         # rev 2
    x = bottom_pad.xcor()                   # rev 2
    if x < 450:  # Limit paddle movement    # rev 2
        x += 20                             # rev 2
        bottom_pad.setx(x)                  # rev 2
                                            # rev 2
                                            # rev 2
def paddledleft():                          # rev 2
    x = bottom_pad.xcor()                   # rev 2
    if x > -440:  # Limit paddle movement   # rev 2
        x -= 20                             # rev 2
        bottom_pad.setx(x)                  # rev 2
                                            # rev 2
# end of rev 2: paddle movements for top and bottom paddles

# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "w")  # Changed to 'w'
sc.onkeypress(paddleadown, "s")  # Changed to 's'
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")

# Rev1b
sc.onkeypress(startplay, "e")
#sc.onkeypress(Quit, "q") # removed quit

# rev 2: copy and modify key bindings to add top and bottom paddle movements
#  changes:  a to c; b to d; up to left; down to right
# rev 2: "1" key moves top paddle left
sc.onkeypress(paddlecleft, "a")  # Changed to 'w'(original comment) (Rev3a) (Switched '1' to 'a')
# rev 2: "2" key moves top paddle right
sc.onkeypress(paddlecright, "d")  # Changed to 's' (original comment)(Rev3a) (Switched '2' to 'd')
# rev 2: "8" key moves bottom paddle left
# rev 3: Changed movement from '8' to 'Left'
sc.onkeypress(paddledleft, "Left")
# rev 2: "9" key moves bottom paddle right
# rev 3: Changed movement from '9' to 'Right'
sc.onkeypress(paddledright, "Right")
#
# rev 2:  end of top and bottom key bindings

# Main game loop
while True:
    sc.update()
    time.sleep(0.01)  # Add delay to make game smoother

    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)
    
# Ball 2
    
    hit_ball2.setx(hit_ball2.xcor() + hit_ball2.dx)
    hit_ball2.sety(hit_ball2.ycor() + hit_ball2.dy)
    
   
    # Checking borders

# rev 2: with top, bottom paddles active will comment out 2 if statements for y coordinates
# rev 2:  these made balls bounce off of top and bottom sides
#    if hit_ball.ycor() > 280:  # rev 2: commented out bounce so can score on top and bottom
#        hit_ball.sety(280)     # rev 2: commented out bounce so can score on top and bottom
#        hit_ball.dy *= -1      # rev 2: commented out bounce so can score on top and bottom
        
   
#    if hit_ball.ycor() < -280: # rev 2: commented out bounce so can score on top and bottom
#        hit_ball.sety(-280)    # rev 2: commented out bounce so can score on top and bottom
#        hit_ball.dy *= -1      # rev 2: commented out bounce so can score on top and bottom
# rev 2: add "or" statements for y coordinate (top and bottom) scores for passed balls
# rev 2: (was)   if hit_ball.xcor() > 500:
# Define scoring for ball 1
    if hit_ball.xcor() > 500 or hit_ball.ycor() < -300:  # rev 2: added "or hit_ball.ycor() < -300"
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

# rev 2: (was)   if hit_ball.xcor() < -500:
    if hit_ball.xcor() < -500 or hit_ball.ycor() > 300:  #rev 2: added "or hit_ball.ycor() > 300"
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

   # Ball 2 boarders
# rev 2: for ball 2
# rev 2:    with top, bottom paddles active will comment out 2 if statements for y coordinates
# rev 2:    these made balls bounce off of top and bottom sides    
#    if hit_ball2.ycor() > 280:     # rev 2: commented out bounce so can score on top and bottom
#        hit_ball2.sety(280)        # rev 2: commented out bounce so can score on top and bottom
#        hit_ball2.dy *= -1         # rev 2: commented out bounce so can score on top and bottom

#    if hit_ball2.ycor() < -280:    # rev 2: commented out bounce so can score on top and bottom
#        hit_ball2.sety(-280)       # rev 2: commented out bounce so can score on top and bottom
#        hit_ball2.dy *= -1         # rev 2: commented out bounce so can score on top and bottom
#  Define scoring for ball 2

    if hit_ball2.xcor() > 500 or hit_ball2.ycor() < -300: #rev 2: added "or hit_ball2.ycor() < -300"
        hit_ball2.goto(0, 0)
#        stopplay()   # rev3d removed stopplay - game freezes too often;  also, if implement, need to do on both balls
        hit_ball2.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

    if hit_ball2.xcor() < -500 or hit_ball2.ycor() > 300: #rev 2: added "or hit_ball2.ycor() > 300"
        hit_ball2.goto(0, 0)
#        stopplay()     # rev3d removed stopplay - game freezes too often;  also, if implement, need to do on both balls
        hit_ball2.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))




    # Paddle ball collision
    #right paddle
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and \
            (hit_ball.ycor() < right_pad.ycor() + 50 and hit_ball.ycor() > right_pad.ycor() - 50):
        hit_ball.setx(360)
        hit_ball.dx *= -1

    # left paddle
    if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370) and \
            (hit_ball.ycor() < left_pad.ycor() + 50 and hit_ball.ycor() > left_pad.ycor() - 50):
        hit_ball.setx(-360)
        hit_ball.dx *= -1
        
# rev 2 add for top and bottom paddles; swap x and y; change 360 to 160 and 370 to 170
    #top paddle # rev 2
    if (hit_ball.ycor() > 160 and hit_ball.ycor() < 170) and \
            (hit_ball.xcor() < top_pad.xcor() + 50 and hit_ball.xcor() > top_pad.xcor() - 50): # rev 2
        hit_ball.sety(160) # rev 2
        hit_ball.dy *= -1 # rev 2

    # bottom paddle # rev 2
    if (hit_ball.ycor() < -160 and hit_ball.ycor() > -170) and \
            (hit_ball.xcor() < bottom_pad.xcor() + 50 and hit_ball.xcor() > bottom_pad.xcor() - 50): # rev 2
        hit_ball.sety(-160) # rev 2
        hit_ball.dy *= -1 # rev 2

# end of rev 2 changes for ball 1

# Paddle ball collision for Ball 2
    if (hit_ball2.xcor() > 360 and hit_ball2.xcor() < 370) and \
            (hit_ball2.ycor() < right_pad.ycor() + 50 and hit_ball2.ycor() > right_pad.ycor() - 50):
        hit_ball2.setx(360)
        hit_ball2.dx *= -1

    if (hit_ball2.xcor() < -360 and hit_ball2.xcor() > -370) and \
            (hit_ball2.ycor() < left_pad.ycor() + 50 and hit_ball2.ycor() > left_pad.ycor() - 50):
        hit_ball2.setx(-360)
        hit_ball2.dx *= -1
        
# rev 2 add for top and bottom paddles; use previous rev 2 changes and change ball1 to ball2
    #top paddle # rev 2
    if (hit_ball2.ycor() > 160 and hit_ball2.ycor() < 170) and \
            (hit_ball2.xcor() < top_pad.xcor() + 50 and hit_ball2.xcor() > top_pad.xcor() - 50): # rev 2
        hit_ball2.sety(160) # rev 2
        hit_ball2.dy *= -1 # rev 2

    # bottom paddle # rev 2
    if (hit_ball2.ycor() < -160 and hit_ball2.ycor() > -170) and \
            (hit_ball2.xcor() < bottom_pad.xcor() + 50 and hit_ball2.xcor() > bottom_pad.xcor() - 50): # rev 2
        hit_ball2.sety(-160) # rev 2
        hit_ball2.dy *= -1 # rev 2

# end of rev 2 changes for ball 1
