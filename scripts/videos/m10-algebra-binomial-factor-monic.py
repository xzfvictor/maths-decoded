"""Transcript-faithful Manim scene for factor-monic (m10-algebra-binomial)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at factorising monic quadratics, which is really just running the FOIL expansion process backwards. You'll start with something like x squared plus b x plus c, and you want to rewrite it as two brackets multiplied together. The trick is to find two numbers that multiply together to give c and at the same time add together to give b. Once you've spotted those two numbers, you simply pop them into the brackets, and you've factored the quadratic. A quick tip on signs: when c is positive, both numbers share the same sign, so they're either both positive if b is positive, or both negative if b is negative. But when c is negative, the numbers must have opposite signs, because only a positive times a negative gives you a negative. Now let's see it in action."

class M10AlgebraBinomialFactorMonicScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Binomial Factor Monic', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at factorising monic quadratics, which is\nreally just running the FOIL expansion process backwards. A quick tip on\nsigns: when c is positive, both numbers share the same sign, so they're\neither both positive if b is positive, or both negative if b is\nnegative.", "You'll start with something like x squared plus b x plus c, and you want\nto rewrite it as two brackets multiplied together. But when c is\nnegative, the numbers must have opposite signs, because only a positive\ntimes a negative gives you a negative.", "The trick is to find two numbers that multiply together to give c and at\nthe same time add together to give b. Now let's see it in action.", "Once you've spotted those two numbers, you simply pop them into the\nbrackets, and you've factored the quadratic."]
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
