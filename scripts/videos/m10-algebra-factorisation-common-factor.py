"""Transcript-faithful Manim scene for common-factor (m10-algebra-factorisation)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how to factorise expressions by pulling out a common factor. The big idea is simple: you hunt for the greatest thing that divides every single term, take it out the front, and leave what's left inside a pair of brackets.\n\nFirst, list the numbers, or coefficients, in front of each term and find the biggest number that divides them all. That's the numerical part of your common factor. Next, look at the variables in each term. Find the smallest power of each variable that shows up everywhere, and that's the variable part. Combine those together, and you've got your greatest common factor.\n\nNow factor it out by writing it once, then opening brackets and dividing every original term by that factor to fill the inside. To check yourself, expand it back out — it should match the expression you started with. This works because factorising is just expansion run backwards: a times the sum of b and c gives a-b plus a-c, so dividing by a and multiplying back lands you exactly where you started.\n\nFor example, six x squared plus nine x, the numbers share a three and the variables share an x, so you pull out three x and get three x times the sum of two x and three. Now let's see it in action."

class M10AlgebraFactorisationCommonFactorScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Factorisation Common Factor', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how to factorise expressions by pulling\nout a common factor. Next, look at the variables in each term. To check\nyourself, expand it back out — it should match the expression you\nstarted with.", "The big idea is simple: you hunt for the greatest thing that divides\nevery single term, take it out the front, and leave what's left inside a\npair of brackets. Find the smallest power of each variable that shows up\neverywhere, and that's the variable part. This works because factorising\nis just expansion run backwards: a times the sum of b and c gives a-b\nplus a-c, so dividing by a and multiplying back lands you exactly where\nyou started.", "First, list the numbers, or coefficients, in front of each term and find\nthe biggest number that divides them all. Combine those together, and\nyou've got your greatest common factor. For example, six x squared plus\nnine x, the numbers share a three and the variables share an x, so you\npull out three x and get three x times the sum of two x and three.", "That's the numerical part of your common factor. Now factor it out by\nwriting it once, then opening brackets and dividing every original term\nby that factor to fill the inside. Now let's see it in action."]
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
