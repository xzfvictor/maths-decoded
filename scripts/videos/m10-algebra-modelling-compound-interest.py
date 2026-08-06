"""Transcript-faithful Manim scene for compound-interest (m10-algebra-modelling)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at compound interest and how it connects to growth and decay models. The big idea is that when you keep adding a percentage onto an amount, and then add that percentage onto the new total, and so on, the value speeds up over time, and that's called compound growth. We write it as the starting amount times one plus the rate, raised to the power of how many periods have passed. So if you start with a thousand dollars and earn five percent each year, after one year you have a thousand times one point zero five, after two years you multiply by one point zero five again, and so on.\n\nThis same form shows up everywhere, so we call it the general growth and decay model, written as y equals a times b to the power of x. Here, a is your starting amount, and b is the growth factor. If b is bigger than one, the quantity grows. If b is between zero and one, the quantity decays, because multiplying by a fraction keeps shrinking it.\n\nA really useful idea in decay problems is half-life, which is just the time it takes for the amount to drop to half of what it was before. You spot it when b equals one half. Now let's see it in action."

class M10AlgebraModellingCompoundInterestScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Modelling Compound Interest', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at compound interest and how it connects to\ngrowth and decay models. This same form shows up everywhere, so we call\nit the general growth and decay model, written as y equals a times b to\nthe power of x. A really useful idea in decay problems is half-life,\nwhich is just the time it takes for the amount to drop to half of what\nit was before.", "The big idea is that when you keep adding a percentage onto an amount,\nand then add that percentage onto the new total, and so on, the value\nspeeds up over time, and that's called compound growth. Here, a is your\nstarting amount, and b is the growth factor. You spot it when b equals\none half.", "We write it as the starting amount times one plus the rate, raised to\nthe power of how many periods have passed. If b is bigger than one, the\nquantity grows. Now let's see it in action.", 'So if you start with a thousand dollars and earn five percent each year,\nafter one year you have a thousand times one point zero five, after two\nyears you multiply by one point zero five again, and so on. If b is\nbetween zero and one, the quantity decays, because multiplying by a\nfraction keeps shrinking it.']
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
