#-----Just for declaration-------
def turn_left():
    turn_left()
def at_goal():
    at_goal()
def front_is_clear():
    front_is_clear()
def right_is_clear():
    right_is_clear()
def wall_in_front():
    wall_in_front()
def move():
    move()


#------Actual Solution-------
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front() and right_is_clear():
        turn_right()
    else:
      turn_left()