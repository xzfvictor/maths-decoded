"""Transcript-faithful Manim scene for quadratic-formula (m10-algebra-quadratics)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at the quadratic formula, your reliable backup whenever factorising gets messy. It works for absolutely every quadratic, so it's worth knowing by heart. Here's the game plan. First, you put your equation into standard form: the coefficient of x squared, plus the coefficient of x, plus the constant, all set equal to zero. That gives you three numbers to play with, which we usually call a, b, and c. Next, you work out what's called the discriminant, which is just b squared minus four times a times c. This little number is super important because it tells you what's coming. If the discriminant is greater than zero, you'll get two different real solutions. If it equals zero, you'll get exactly one repeated solution. And if it's less than zero, there are no real solutions at all. Once you know the discriminant, you plug everything into the formula: negative b, plus or minus the square root of the discriminant, all divided by two a. Simplify, and you've got your answers. Now let's see it in action."

class M10AlgebraQuadraticsQuadraticFormulaScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Quadratics Quadratic Formula', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at the quadratic formula, your reliable backup\nwhenever factorising gets messy. That gives you three numbers to play\nwith, which we usually call a, b, and c. If it equals zero, you'll get\nexactly one repeated solution. Now let's see it in action.", "It works for absolutely every quadratic, so it's worth knowing by heart.\nNext, you work out what's called the discriminant, which is just b\nsquared minus four times a times c. And if it's less than zero, there\nare no real solutions at all.", "Here's the game plan. This little number is super important because it\ntells you what's coming. Once you know the discriminant, you plug\neverything into the formula: negative b, plus or minus the square root\nof the discriminant, all divided by two a.", "First, you put your equation into standard form: the coefficient of x\nsquared, plus the coefficient of x, plus the constant, all set equal to\nzero. If the discriminant is greater than zero, you'll get two different\nreal solutions. Simplify, and you've got your answers."]
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
