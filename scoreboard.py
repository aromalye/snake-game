from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.write(f"score : {self.score}", font=('Arial', 18, 'normal'), align="center")



    def increasing_score(self):
        self.clear()
        self.score += 1
        self.write(f"score : {self.score}", font=('Arial', 18, 'normal'), align="center")

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER !!", font=('Arial', 18, 'normal'), align="center")





