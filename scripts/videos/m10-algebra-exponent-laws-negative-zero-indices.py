"""Transcript-faithful Manim scene for negative-zero-indices (m10-algebra-exponent-laws)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at two final exponent rules that tie everything together: what happens when the power is zero, and what happens when it's negative. First up, the zero index. Any non-zero number raised to the power of zero equals one. So five to the zero is one, negative three to the zero is one, even something like x plus one all to the power of zero is one. It feels weird, but here's why it makes sense. If you divide any number by itself, the quotient law says you subtract the powers, giving a zero on top. But anything divided by itself is just one, so the result has to be one. Now the negative index. A negative power flips the term upside down into a fraction. So three to the negative two becomes one over three squared, which is one ninth. And x to the negative three becomes one over x cubed. Again, the quotient law explains it. If the bottom power is bigger than the top, subtracting gives you a negative answer, and the leftover on top becomes one over the leftover on the bottom. So remember, zero gives you one, and negative sends it downstairs. Now let's see it in action."

class M10AlgebraExponentLawsNegativeZeroIndicesScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Exponent Laws Negative Zero Indices', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at two final exponent rules that tie\neverything together: what happens when the power is zero, and what\nhappens when it's negative. It feels weird, but here's why it makes\nsense. A negative power flips the term upside down into a fraction. If\nthe bottom power is bigger than the top, subtracting gives you a\nnegative answer, and the leftover on top becomes one over the leftover\non the bottom.", 'First up, the zero index. If you divide any number by itself, the\nquotient law says you subtract the powers, giving a zero on top. So\nthree to the negative two becomes one over three squared, which is one\nninth. So remember, zero gives you one, and negative sends it\ndownstairs.', "Any non-zero number raised to the power of zero equals one. But anything\ndivided by itself is just one, so the result has to be one. And x to the\nnegative three becomes one over x cubed. Now let's see it in action.", 'So five to the zero is one, negative three to the zero is one, even\nsomething like x plus one all to the power of zero is one. Now the\nnegative index. Again, the quotient law explains it.']
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
