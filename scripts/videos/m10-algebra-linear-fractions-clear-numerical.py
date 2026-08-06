"""Transcript-faithful Manim scene for clear-numerical (m10-algebra-linear-fractions)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at clearing the numerical denominators in a linear equation, which is honestly the slickest trick when fractions show up. The idea is simple: instead of wrestling with each fraction one by one, you multiply every term across the whole equation by a single magic number called the LCD, or least common denominator. That's just the smallest number that every denominator divides into evenly. Once you do that, every fraction collapses into a nice whole number, and you're left with a regular linear equation you already know how to solve. The recipe goes like this. First, spot the LCD. Then multiply every single term on both sides by it. Next, cancel those denominators so the fractions disappear. Then just solve the equation like normal, and finally, plug your answer back in to check it really works. For example, suppose you have x over three plus x over four equals seven. The LCD is twelve, so you multiply everything by twelve, and suddenly you've got a clean equation with no fractions at all. Now let's see it in action with a worked example."

class M10AlgebraLinearFractionsClearNumericalScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Linear Fractions Clear Numerical', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at clearing the numerical denominators in a\nlinear equation, which is honestly the slickest trick when fractions\nshow up. The recipe goes like this. Then just solve the equation like\nnormal, and finally, plug your answer back in to check it really works.", 'The idea is simple: instead of wrestling with each fraction one by one,\nyou multiply every term across the whole equation by a single magic\nnumber called the LCD, or least common denominator. First, spot the LCD.\nFor example, suppose you have x over three plus x over four equals\nseven.', "That's just the smallest number that every denominator divides into\nevenly. Then multiply every single term on both sides by it. The LCD is\ntwelve, so you multiply everything by twelve, and suddenly you've got a\nclean equation with no fractions at all.", "Once you do that, every fraction collapses into a nice whole number, and\nyou're left with a regular linear equation you already know how to\nsolve. Next, cancel those denominators so the fractions disappear. Now\nlet's see it in action with a worked example."]
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
