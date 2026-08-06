"""Transcript-faithful Manim scene for discriminant (m10-algebra-quadratics)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how to tell, just by glancing at a quadratic, how many real solutions it actually has. The trick is something called the discriminant. It's the bit under the square root in the quadratic formula, and it's calculated by squaring the coefficient of x, subtracting four times the product of the other two coefficients. You write it as delta, and its sign tells you everything. If delta is positive, your quadratic has two distinct real roots, so the parabola crosses the x-axis at two separate points. If delta is exactly zero, there's one repeated real root, meaning the parabola just touches the x-axis at the vertex and turns around. And if delta is negative, there are no real roots at all, because the parabola sits entirely above or below the x-axis and never meets it. So really, before you even solve, you can look at that one expression and know how many answers you're chasing. Now let's see it in action."

class M10AlgebraQuadraticsDiscriminantScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Quadratics Discriminant', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how to tell, just by glancing at a\nquadratic, how many real solutions it actually has. If delta is\npositive, your quadratic has two distinct real roots, so the parabola\ncrosses the x-axis at two separate points. Now let's see it in action.", "The trick is something called the discriminant. If delta is exactly\nzero, there's one repeated real root, meaning the parabola just touches\nthe x-axis at the vertex and turns around.", "It's the bit under the square root in the quadratic formula, and it's\ncalculated by squaring the coefficient of x, subtracting four times the\nproduct of the other two coefficients. And if delta is negative, there\nare no real roots at all, because the parabola sits entirely above or\nbelow the x-axis and never meets it.", "You write it as delta, and its sign tells you everything. So really,\nbefore you even solve, you can look at that one expression and know how\nmany answers you're chasing."]
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
