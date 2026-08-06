"""Transcript-faithful Manim scene for solve (m10-algebra-linear-eq)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at how to solve linear equations. A linear equation is just one where the variable sits to the first power, so no squares or square roots yet. The big idea is to use inverse operations to peel away everything around the variable until you're left with it alone.\n\nFirst, expand any brackets using the distributive law. Next, collect the variable terms on one side of the equals sign and the plain numbers, called constants, on the other side. Then combine any like terms so each side looks as simple as possible. Finally, divide both sides by the number sitting in front of the variable, known as the coefficient, and that gives you your answer.\n\nWhy does this work? Because every operation is reversible. Subtracting the same number from both sides, or adding it, keeps the equation balanced, and so does multiplying or dividing by the same non-zero number on both sides. Always finish by popping your answer back into the original equation to check it really works. Now let's see it in action."

class M10AlgebraLinearEqSolveScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Linear Eq Solve', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at how to solve linear equations. Next,\ncollect the variable terms on one side of the equals sign and the plain\nnumbers, called constants, on the other side. Because every operation is\nreversible.", 'A linear equation is just one where the variable sits to the first\npower, so no squares or square roots yet. Then combine any like terms so\neach side looks as simple as possible. Subtracting the same number from\nboth sides, or adding it, keeps the equation balanced, and so does\nmultiplying or dividing by the same non-zero number on both sides.', "The big idea is to use inverse operations to peel away everything around\nthe variable until you're left with it alone. Finally, divide both sides\nby the number sitting in front of the variable, known as the\ncoefficient, and that gives you your answer. Always finish by popping\nyour answer back into the original equation to check it really works.", "First, expand any brackets using the distributive law. Why does this\nwork? Now let's see it in action."]
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
