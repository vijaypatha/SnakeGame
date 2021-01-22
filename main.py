from turtle import Turtle, Screen
import time

s = Screen()


s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

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

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for positions in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(positions)
    segments.append(new_segment)


game_is_on = True

while game_is_on:
    s.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)


s.exitonclick()