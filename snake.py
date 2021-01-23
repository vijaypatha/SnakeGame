from turtle import Turtle
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # This is a constant. So ALL CAPs.
MOVE_DISTANCE = 20


class Snake:
    from turtle import Turtle

    def __init__(self):
        # the code in here what should happen when we initialize a new snake object
        # i.e when snake = Snake() is executed then we will call create_snake method
        self.combine_segments = []
        self.create_snake()


    def create_snake(self):
        for position in START_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.combine_segments.append(segment)  # TODO 2

    def move(self):
        for seg_num in range(len(self.combine_segments) - 1, 0, -1):
            new_x = self.combine_segments[seg_num - 1].xcor()
            new_y = self.combine_segments[seg_num - 1].ycor()
            self.combine_segments[seg_num].goto(new_x, new_y)
        self.combine_segments[0].forward(MOVE_DISTANCE)
        #self.combine_segments[0].left(90)
