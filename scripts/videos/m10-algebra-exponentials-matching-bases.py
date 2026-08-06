"""Transcript-faithful Manim scene for matching-bases (m10-algebra-exponentials)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how to solve simple exponential equations by matching bases. An exponential equation is one where the unknown sits up in the exponent, like two to the x equals eight. The trick is to rewrite both sides so they share the same base. Once you've done that, you can set the exponents equal to each other and solve the resulting simple linear equation. For this matching idea to work nicely, both sides should be powers of small whole numbers, like two, three, five, or ten. So if you spot something like nine to the x equals twenty-seven, you'd rewrite both as powers of three, then line up the exponents and solve. It's a really clean, satisfying method once you get the hang of spotting those shared bases. Now let's see it in action."

class M10AlgebraExponentialsMatchingBasesScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Exponentials Matching Bases', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how to solve simple exponential equations\nby matching bases. For this matching idea to work nicely, both sides\nshould be powers of small whole numbers, like two, three, five, or ten.", "An exponential equation is one where the unknown sits up in the\nexponent, like two to the x equals eight. So if you spot something like\nnine to the x equals twenty-seven, you'd rewrite both as powers of\nthree, then line up the exponents and solve.", "The trick is to rewrite both sides so they share the same base. It's a\nreally clean, satisfying method once you get the hang of spotting those\nshared bases.", "Once you've done that, you can set the exponents equal to each other and\nsolve the resulting simple linear equation. Now let's see it in action."]
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
