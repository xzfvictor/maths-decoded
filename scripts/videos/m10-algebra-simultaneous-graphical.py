"""Transcript-faithful Manim scene for graphical (m10-algebra-simultaneous)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at how to solve simultaneous linear equations using a graph. Each equation describes a straight line on the plane, and the solution to the system is simply the point where the two lines cross. Think about it this way: each equation is a set of all the points that satisfy it, so the only point that works for both equations at once is the intersection. To do this graphically, first rewrite each equation so the y is by itself on one side, identifying the slope and the y-intercept. Then plot both lines on the same set of axes and just read off where they meet. Graphical methods are especially handy when the numbers get messy and you don't want to wrestle with the algebra. Just keep in mind two special cases: if the lines are parallel with the same slope but different intercepts, they never meet and there's no solution. If they have the same slope and the same intercept, they're actually the same line, so every point on the line is a solution. Now let's see it in action."

class M10AlgebraSimultaneousGraphicalScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Simultaneous Graphical', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at how to solve simultaneous linear equations\nusing a graph. Then plot both lines on the same set of axes and just\nread off where they meet. Now let's see it in action.", "Each equation describes a straight line on the plane, and the solution\nto the system is simply the point where the two lines cross. Graphical\nmethods are especially handy when the numbers get messy and you don't\nwant to wrestle with the algebra.", "Think about it this way: each equation is a set of all the points that\nsatisfy it, so the only point that works for both equations at once is\nthe intersection. Just keep in mind two special cases: if the lines are\nparallel with the same slope but different intercepts, they never meet\nand there's no solution.", "To do this graphically, first rewrite each equation so the y is by\nitself on one side, identifying the slope and the y-intercept. If they\nhave the same slope and the same intercept, they're actually the same\nline, so every point on the line is a solution."]
        for words in sections:
            beat = Text(words, font_size=24, line_spacing=0.8)
            if beat.width > 10.5:
                beat.set_width(10.5)
            beat.move_to(BAND_CHART_CENTER)
            bg = BackgroundRectangle(beat, color=BLACK, fill_opacity=1, buff=0.28)
            bg.move_to(beat.get_center())
            card = beat_group(bg, beat)
            self.add(card)
            self.wait(2.0)
            self.remove(card)
        final = Text("Key idea", font_size=32, color=GREEN_OK).move_to(DOWN * 1.7)
        final_bg = BackgroundRectangle(final, color=BLACK, fill_opacity=1, buff=0.25)
        final_bg.move_to(final.get_center())
        final_box = SurroundingRectangle(final, color=GREEN_OK, buff=0.3)
        self.add(final_bg, final, final_box)
        self.wait(95)
