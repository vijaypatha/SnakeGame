# TODO: 1. Three Turtles line up next to each other.
# TODO: 2. Combine the turtles in a one snake
# TODO: 3. Make the Snake Move
# TODO: 4. In TODO 3, Snake is moving three segments,
#  so need a 1 seg Snake
# TODO: 5. Turn the snake


from turtle import Screen, Turtle
import time

screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)  # TODO 4 The tracer() function turns automatic screen updates on or off -- on by default
# -- and also sets the update() delay

# start_positions = [(-200, 0), (-200, 100), (-200, -100)]
# segment_1 = Turtle()
# segment_1.shape("square")
# segment_1.color("white")
#
#
# segment_2 = Turtle()
# segment_2.penup()
# segment_2.shape("square")
# segment_2.color("pink")
# segment_2.goto(-20, 0)
#
# segment_3 = Turtle()
# segment_3.penup()
# segment_3.shape("square")
# segment_3.color("red")
# segment_3.goto(-40, 0)

# TODO 1
start_positions = [(0, 0), (-20, 0), (-40, 0)]
combine_segments = []  # TODO 2

for position in start_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    combine_segments.append(segment)  # TODO 2

game_is_on = True

# TODO 3
while game_is_on:
    time.sleep(0.1)
    screen.update()  # TODO 4 Update the screen only when segments have moved forward
    # for seg in combine_segments:
    #     seg.forward(20)

# TODO 5
    for seg_num in range(len(combine_segments)-1, 0, -1):
        new_x = combine_segments[seg_num - 1].xcor()
        new_y = combine_segments[seg_num - 1].ycor()
        combine_segments[seg_num].goto(new_x, new_y)
    combine_segments[0].forward(20)
    combine_segments[0].left(90)

screen.exitonclick()
