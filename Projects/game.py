# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random


def set_background(image_filename):
    screen = turtle.Screen()
    try:
        screen.bgpic(f"Backgrounds/{image_filename}.png")
    except:
        screen.bgpic(f"Backgrounds/{image_filename}.gif")


def set_image(sprite, image_filename):
    image_file = f"Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)


def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x, y)
    return sprite


def get_distance(s1, s2):
    dx = s1.xcor() - s2.xcor()
    dy = s1.ycor() - s2.ycor()
    return math.sqrt(dx * dx + dy * dy)


window = turtle.Screen()
window.tracer(0)
## define location##

## CREATE_Variables ###
timer = 0
other_timer = 0

oven_top = -60
oven_bottom = -190
oven_right = 290
oven_left = 190


bunny_follow_emptybowl = False
bunny_follow_strawberry = False
bunny_follow_milk = False
bunny_follow_egg = False
bunny_follow_frosting = False
bunny_follow_cake_mix = False
bunny_follow_wisk = False


bear_follow_emptybowl = False
bear_follow_strawberry = False
bear_follow_milk = False
bear_follow_egg = False
bear_follow_frosting = False
bear_follow_cake_mix = False
bear_follow_wisk = False
cake_made = False


### SECTION_2:_Setup ###
set_background("kitchen")
s1 = create_sprite("jelly cat bunny", -200, -190)
s2 = create_sprite("jelly cat teddy bear", 200, -190)
s3 = create_sprite("milk", 5, 40)
s4 = create_sprite("frosting", 70, 30)
s6 = create_sprite("timer 1", -70, 20)
s7 = create_sprite("cake mix", -100, 30)
s8 = create_sprite("empty bowl", -190, 50)
s11 = create_sprite("whole egg", 90, 10)
s12 = create_sprite("wisk", -270, 50)
s13 = create_sprite("strawberrys", 200, -10)


### SECTION_2:_DEFINE_MOVEMENT_CONTROLS ###

#### bunny follow definitions


def bunny_change_follow_emptybowl():
    global bunny_follow_emptybowl
    bunny_follow_emptybowl = not bunny_follow_emptybowl


def bunny_change_follow_cake_mix():
    global bunny_follow_cake_mix
    bunny_follow_cake_mix = not bunny_follow_cake_mix


def bunny_change_follow_strawberry():
    global bunny_follow_strawberry
    bunny_follow_strawberry = not bunny_follow_strawberry


def bunny_change_follow_frosting():
    global bunny_follow_frosting
    bunny_follow_frosting = not bunny_follow_frosting


def bunny_change_follow_milk():
    global bunny_follow_milk
    bunny_follow_milk = not bunny_follow_milk


def bunny_change_follow_egg():
    global bunny_follow_egg
    bunny_follow_egg = not bunny_follow_egg


def bunny_change_follow_wisk():
    global bunny_follow_wisk
    bunny_follow_wisk = not bunny_follow_wisk


### Bear follow defintions


def bear_change_follow_emptybow():
    global bear_follow_emptybowl
    bear_follow_emptybowl = not bear_follow_emptybowl


def bear_change_follow_cake_mix():
    global bear_follow_cake_mix
    bear_follow_cake_mix = not bear_follow_cake_mix


def bear_change_follow_strawberry():
    global bear_follow_strawberry
    bear_follow_strawberry = not bear_follow_strawberry


def bear_change_follow_frosting():
    global bear_follow_frosting
    bear_follow_frosting = not bear_follow_frosting


def bear_change_follow_milk():
    global bear_follow_milk
    bear_follow_milk = not bear_follow_milk


def bear_change_follow_egg():
    global bear_follow_egg
    bear_follow_egg = not bear_follow_egg


def bear_change_follow_wisk():
    global bear_follow_wisk
    bear_follow_wisk = not bear_follow_wisk


def bear_change_follow_emptybowl():
    global bear_follow_emptybowl
    bear_follow_emptybowl = not bear_follow_emptybowl


### more set up
def image(image_filename):
    return f"Images/{image_filename}.gif"


def start_timer():
    global cake_made
    while not cake_made:
        time.sleep(1)
        window.update()
        timer += 1


#### define costum changes
def costume_change1():
    screen = turtle.Screen()
    screen.register_shape(image("cracked egg"))
    s11.shape(image("cracked egg"))


def costume_change_fullbowl():
    screen = turtle.Screen()
    screen.register_shape(image("full bowl"))
    s8.shape(image("full bowl"))


def costume_change_cake():
    screen = turtle.Screen()
    screen.register_shape(image("plain cake"))
    s8.shape(image("plain cake"))


def costume_change_cake_with_frosting():
    screen = turtle.Screen()
    screen.register_shape(image("cake"))
    s8.shape(image("cake"))


### Movement controls
def bunny_move_up():
    s1.setheading(90)
    s1.forward(10)

    if bunny_follow_strawberry == True:
        s13.setheading(90)
        s13.forward(10)
    if bunny_follow_milk == True:
        s3.setheading(90)
        s3.forward(10)
    if bunny_follow_egg == True:
        s11.setheading(90)
        s11.forward(10)
    if bunny_follow_frosting == True:
        s4.setheading(90)
        s4.forward(10)
    if bunny_follow_cake_mix == True:
        s7.setheading(90)
        s7.forward(10)
    if bunny_follow_wisk == True:
        s12.setheading(90)
        s12.forward(10)
    if bunny_follow_emptybowl:
        s8.setheading(90)
        s8.forward(10)


def bunny_move_down():
    s1.setheading(270)
    s1.forward(10)

    if bunny_follow_strawberry == True:
        s13.setheading(270)
        s13.forward(10)
    if bunny_follow_milk == True:
        s3.setheading(270)
        s3.forward(10)
    if bunny_follow_egg == True:
        s11.setheading(270)
        s11.forward(10)
    if bunny_follow_frosting == True:
        s4.setheading(270)
        s4.forward(10)
    if bunny_follow_cake_mix == True:
        s7.setheading(270)
        s7.forward(10)
    if bunny_follow_wisk == True:
        s12.setheading(270)
        s12.forward(10)
    if bunny_follow_wisk == True:
        s12.setheading(270)
        s12.forward(10)
    if bunny_follow_emptybowl:
        s8.setheading(270)
        s8.forward(10)


def bunny_move_left():
    s1.setheading(180)
    s1.forward(10)
    if bunny_follow_strawberry == True:
        s13.setheading(180)
        s13.forward(10)
    if bunny_follow_milk == True:
        s3.setheading(180)
        s3.forward(10)
    if bunny_follow_egg == True:
        s11.setheading(180)
        s11.forward(10)
    if bunny_follow_frosting == True:
        s4.setheading(180)
        s4.forward(10)
    if bunny_follow_cake_mix == True:
        s7.setheading(180)
        s7.forward(10)
    if bunny_follow_wisk == True:
        s12.setheading(180)
        s12.forward(10)
    if bunny_follow_emptybowl:
        s8.setheading(180)
        s8.forward(10)


def bunny_move_right():
    s1.setheading(0)
    s1.forward(10)
    if bunny_follow_strawberry == True:
        s13.setheading(0)
        s13.forward(10)
    if bunny_follow_milk == True:
        s3.setheading(0)
        s3.forward(10)
    if bunny_follow_egg == True:
        s11.setheading(0)
        s11.forward(10)
    if bunny_follow_frosting == True:
        s4.setheading(0)
        s4.forward(10)
    if bunny_follow_cake_mix == True:
        s7.setheading(0)
        s7.forward(10)
    if bunny_follow_wisk == True:
        s12.setheading(0)
        s12.forward(10)
    if bunny_follow_emptybowl:
        s8.setheading(0)
        s8.forward(10)


def bear_move_up():
    s2.setheading(90)
    s2.forward(10)
    if bear_follow_emptybowl == True:
        s8.setheading(90)
        s8.forward(10)

    if bear_follow_strawberry == True:
        s13.setheading(90)
        s13.forward(10)
    if bear_follow_milk == True:
        s3.setheading(90)
        s3.forward(10)
    if bear_follow_egg == True:
        s11.setheading(90)
        s11.forward(10)
    if bear_follow_frosting == True:
        s4.setheading(90)
        s4.forward(10)
    if bear_follow_cake_mix == True:
        s7.setheading(90)
        s7.forward(10)
    if bear_follow_wisk == True:
        s12.setheading(90)
        s12.forward(10)


def bear_move_down():
    s2.setheading(270)
    s2.forward(10)

    if bear_follow_emptybowl == True:
        s8.setheading(270)
        s8.forward(10)

    if bear_follow_strawberry == True:
        s13.setheading(270)
        s13.forward(10)
    if bear_follow_milk == True:
        s3.setheading(270)
        s3.forward(10)
    if bear_follow_egg == True:
        s11.setheading(270)
        s11.forward(10)
    if bear_follow_frosting == True:
        s4.setheading(270)
        s4.forward(10)
    if bear_follow_cake_mix == True:
        s7.setheading(270)
        s7.forward(10)
    if bear_follow_wisk == True:
        s12.setheading(270)
        s12.forward(10)


def bear_move_left():
    s2.setheading(180)
    s2.forward(10)
    if bear_follow_emptybowl == True:
        s8.setheading(180)
        s8.forward(10)
    if bear_follow_strawberry == True:
        s13.setheading(180)
        s13.forward(10)
    if bear_follow_milk == True:
        s3.setheading(180)
        s3.forward(10)
    if bear_follow_egg == True:
        s11.setheading(180)
        s11.forward(10)
    if bear_follow_frosting == True:
        s4.setheading(180)
        s4.forward(10)
    if bear_follow_cake_mix == True:
        s7.setheading(180)
        s7.forward(10)
    if bear_follow_wisk == True:
        s12.setheading(180)
        s12.forward(10)


def bear_move_right():
    s2.setheading(0)
    s2.forward(10)
    if bear_follow_emptybowl == True:
        s8.setheading(0)
        s8.forward(10)
    if bear_follow_strawberry == True:
        s13.setheading(0)
        s13.forward(10)
    if bear_follow_milk == True:
        s3.setheading(0)
        s3.forward(10)
    if bear_follow_egg == True:
        s11.setheading(0)
        s11.forward(10)
    if bear_follow_frosting == True:
        s4.setheading(0)
        s4.forward(10)
    if bear_follow_cake_mix == True:
        s7.setheading(0)
        s7.forward(10)
    if bear_follow_wisk == True:
        s12.setheading(0)
        s12.forward(10)


### hiding and unhiding
def hide_egg():
    s11.hideturtle


def hide_milk():
    s3.hideturtle


def hide_frosting():
    s4.hideturtle


def hide_strawberry():
    s13.hideturtle


def hide_cake_mix():
    s7.hideturtle


def hide_emtybowl():
    s8.showturtle


def show_egg():
    s11.showturtle


def show_milk():
    s3.showturtle


def show_frosting():
    s4.showturtle


def show_strawberry():
    s13.showturtle


def show_cake_mix():
    s7.showturtle


def show_emtybowl():
    s8.showturtle


### grabing items ####


def bunny_grab():
    if (
        get_distance(s1, s12) < get_distance(s1, s11)
        and get_distance(s1, s12) < get_distance(s1, s3)
        and get_distance(s1, s12) < get_distance(s1, s4)
        and get_distance(s1, s12) < get_distance(s1, s13)
        and get_distance(s1, s12) < get_distance(s1, s7)
        and get_distance(s1, s12) < get_distance(s1, s8)
    ):
        bunny_change_follow_wisk()
    elif (
        get_distance(s1, s11) < get_distance(s1, s12)
        and get_distance(s1, s11) < get_distance(s1, s3)
        and get_distance(s1, s11) < get_distance(s1, s4)
        and get_distance(s1, s11) < get_distance(s1, s13)
        and get_distance(s1, s11) < get_distance(s1, s7)
        and get_distance(s1, s11) < get_distance(s1, s8)
    ):
        bunny_change_follow_egg()
    elif (
        get_distance(s1, s3) < get_distance(s1, s12)
        and get_distance(s1, s3) < get_distance(s1, s11)
        and get_distance(s1, s3) < get_distance(s1, s4)
        and get_distance(s1, s3) < get_distance(s1, s13)
        and get_distance(s1, s3) < get_distance(s1, s7)
        and get_distance(s1, s3) < get_distance(s1, s8)
    ):
        bunny_change_follow_milk()
    elif (
        get_distance(s1, s4) < get_distance(s1, s12)
        and get_distance(s1, s4) < get_distance(s1, s3)
        and get_distance(s1, s4) < get_distance(s1, s11)
        and get_distance(s1, s4) < get_distance(s1, s13)
        and get_distance(s1, s4) < get_distance(s1, s7)
        and get_distance(s1, s4) < get_distance(s1, s8)
    ):
        bunny_change_follow_frosting()
    elif (
        get_distance(s1, s13) < get_distance(s1, s12)
        and get_distance(s1, s13) < get_distance(s1, s11)
        and get_distance(s1, s13) < get_distance(s1, s4)
        and get_distance(s1, s13) < get_distance(s1, s3)
        and get_distance(s1, s13) < get_distance(s1, s7)
        and get_distance(s1, s13) < get_distance(s1, s8)
    ):
        bunny_change_follow_strawberry()
    elif (
        get_distance(s1, s7) < get_distance(s1, s12)
        and get_distance(s1, s7) < get_distance(s1, s3)
        and get_distance(s1, s7) < get_distance(s1, s11)
        and get_distance(s1, s7) < get_distance(s1, s13)
        and get_distance(s1, s4) > get_distance(s1, s7)
        and get_distance(s1, s7) < get_distance(s1, s8)
    ):
        bunny_change_follow_cake_mix()
    elif (
        get_distance(s1, s8) < get_distance(s1, s12)
        and get_distance(s1, s8) < get_distance(s1, s11)
        and get_distance(s1, s8) < get_distance(s1, s4)
        and get_distance(s1, s8) < get_distance(s1, s3)
        and get_distance(s1, s8) < get_distance(s1, s7)
        and get_distance(s1, s8) < get_distance(s1, s13)
    ):
        bunny_change_follow_emptybowl()


def bear_grab():
    if (
        get_distance(s2, s12) < get_distance(s2, s11)
        and get_distance(s2, s12) < get_distance(s2, s3)
        and get_distance(s2, s12) < get_distance(s2, s4)
        and get_distance(s2, s12) < get_distance(s2, s13)
        and get_distance(s2, s12) < get_distance(s2, s7)
        and get_distance(s2, s12) < get_distance(s2, s8)
    ):
        bear_change_follow_wisk()
    elif (
        get_distance(s2, s11) < get_distance(s2, s12)
        and get_distance(s2, s11) < get_distance(s2, s3)
        and get_distance(s2, s11) < get_distance(s2, s4)
        and get_distance(s2, s11) < get_distance(s2, s13)
        and get_distance(s2, s11) < get_distance(s2, s7)
        and get_distance(s2, s11) < get_distance(s2, s8)
    ):
        bear_change_follow_egg()
    elif (
        get_distance(s2, s3) < get_distance(s2, s12)
        and get_distance(s2, s3) < get_distance(s2, s11)
        and get_distance(s2, s3) < get_distance(s2, s4)
        and get_distance(s2, s3) < get_distance(s2, s13)
        and get_distance(s2, s3) < get_distance(s2, s7)
        and get_distance(s2, s3) < get_distance(s2, s8)
    ):
        bear_change_follow_milk()
    elif (
        get_distance(s2, s4) < get_distance(s2, s12)
        and get_distance(s2, s4) < get_distance(s2, s3)
        and get_distance(s2, s4) < get_distance(s2, s11)
        and get_distance(s2, s4) < get_distance(s2, s13)
        and get_distance(s2, s4) < get_distance(s2, s7)
        and get_distance(s2, s4) < get_distance(s2, s8)
    ):
        bear_change_follow_frosting()
    elif (
        get_distance(s2, s13) < get_distance(s2, s12)
        and get_distance(s2, s13) < get_distance(s2, s11)
        and get_distance(s2, s13) < get_distance(s2, s4)
        and get_distance(s2, s13) < get_distance(s2, s3)
        and get_distance(s2, s13) < get_distance(s2, s7)
        and get_distance(s2, s13) < get_distance(s2, s8)
    ):
        bear_change_follow_strawberry()
    elif (
        get_distance(s2, s7) < get_distance(s2, s12)
        and get_distance(s2, s7) < get_distance(s2, s3)
        and get_distance(s2, s7) < get_distance(s2, s11)
        and get_distance(s2, s7) < get_distance(s2, s13)
        and get_distance(s2, s4) > get_distance(s2, s7)
        and get_distance(s2, s7) < get_distance(s2, s8)
    ):
        bear_change_follow_cake_mix()
    elif (
        get_distance(s2, s8) < get_distance(s2, s12)
        and get_distance(s2, s8) < get_distance(s2, s11)
        and get_distance(s2, s8) < get_distance(s2, s4)
        and get_distance(s2, s8) < get_distance(s2, s3)
        and get_distance(s2, s8) < get_distance(s2, s7)
        and get_distance(s2, s8) < get_distance(s2, s13)
    ):
        bear_change_follow_emptybowl()


## APPLY_DEFINITIONS_OF_MOVEMENT ###

window.onkeypress(bunny_move_up, "Up")
window.onkeypress(bunny_move_down, "Down")
window.onkeypress(bunny_move_right, "Right")
window.onkeypress(bunny_move_left, "Left")

window.onkeypress(bear_move_up, "w")
window.onkeypress(bear_move_down, "s")
window.onkeypress(bear_move_right, "d")
window.onkeypress(bear_move_left, "a")
### Apply_Grab_Funtions ###
window.onkeypress(bunny_grab, " ")
window.onkeypress(bear_grab, "q")


## loaction funtion ##
def in_oven(sprite):
    return (
        sprite.xcor() < oven_right
        and sprite.xcor() > oven_left
        and sprite.ycor() < oven_top
        and sprite.ycor() > oven_bottom
    )


# Section 4: Game Loop
window.listen()
timer = 0
while True:
    time.sleep(0.1)
    other_timer += 0.1
    window.update()
    if get_distance(s12, s8) < 10:
        costume_change_fullbowl()
    if in_oven(s8):
        timer += 0.1

    if timer == 3 or timer > 3:
        costume_change_cake()
    print(get_distance(s4, s8))
    if get_distance(s4, s8) < 30:
        time.sleep(0.2)
        costume_change_cake_with_frosting()
        cake_made = True

        if other_timer == 120:
            s1.write("you ran out of time :(", font=("arial", 40, "normal"))
        if cake_made:
            s1.write("you win :)", font=("arial", 40, "normal"))
