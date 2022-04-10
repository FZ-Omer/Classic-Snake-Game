from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")  # It's A TUPLE (str, int, str)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as score:
            self.high_score = int(score.read())

        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-25, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score}  High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode='w') as new_score:
                new_score.write(f"{self.high_score}")
        # Resetting score value to 0, after checking high score.
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("lime green")
    #     self.write(arg="GAME OVER!!", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
