# TODO: 1. Three Turtles line up next to each other.
# TODO: 2. Combine the turtles in a one snake
# TODO: 3. Make the Snake Move
# TODO: 4. In TODO 3, Snake is moving three segments,
#  so need a 1 seg Snake


from turtle import Screen, Turtle
screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(600, 600)

# start_positions = [(-200, 0), (-200, 100), (-200, -100)]

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
    for seg in combine_segments:
        seg.forward(20)


screen.exitonclick()
