"""Transcript-faithful Manim scene for graphical (m10-algebra-numerical)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how to solve equations graphically. Sometimes an equation is just too messy to rearrange neatly, and that's totally fine, because a sketch can do the work for you. The first idea is the graphical method itself. You take your equation, move everything to one side so you've got an expression in x equal to zero, then think of that expression as a y-value. Sketch the curve, and the solutions are simply the spots where the curve crosses the x-axis. If you need a more precise answer, zoom in around that crossing, or use your calculator to refine it. The next thing to remember is to scan the whole graph. It's tempting to only look at the obvious bit, but a curve might cross the x-axis more than once, and a sketch makes those extra solutions visible. Finally, a useful fact about polynomials: a polynomial of degree n has at most n real roots, and the end behaviour of the graph, which way it points up or down at the edges, is set by the sign of the leading coefficient. Now let's see it in action."

class M10AlgebraNumericalGraphicalScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Numerical Graphical', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how to solve equations graphically. Sketch\nthe curve, and the solutions are simply the spots where the curve\ncrosses the x-axis. Finally, a useful fact about polynomials: a\npolynomial of degree n has at most n real roots, and the end behaviour\nof the graph, which way it points up or down at the edges, is set by the\nsign of the leading coefficient.", "Sometimes an equation is just too messy to rearrange neatly, and that's\ntotally fine, because a sketch can do the work for you. If you need a\nmore precise answer, zoom in around that crossing, or use your\ncalculator to refine it. Now let's see it in action.", 'The first idea is the graphical method itself. The next thing to\nremember is to scan the whole graph.', "You take your equation, move everything to one side so you've got an\nexpression in x equal to zero, then think of that expression as a\ny-value. It's tempting to only look at the obvious bit, but a curve\nmight cross the x-axis more than once, and a sketch makes those extra\nsolutions visible."]
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
