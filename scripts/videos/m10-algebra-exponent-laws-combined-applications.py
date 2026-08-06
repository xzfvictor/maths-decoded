"""Transcript-faithful Manim scene for combined-applications (m10-algebra-exponent-laws)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at what happens when you mix all the exponent rules together in one simplification. The good news is, numbers behave like numbers, and exponents follow their own set of rules, so you tackle them as two separate jobs. First, combine the coefficients just like ordinary numbers, multiplying or dividing them as the expression requires. Then turn your attention to the variables and count how each one's exponent moves depending on what's happening. If you're multiplying terms with the same base, you add the exponents. If you're dividing, you subtract. If something is raised to a power, you multiply the exponents. Watch out for anything raised to the zero index, because that simply drops out and equals one. And if you hit a negative index, rewrite it as a reciprocal at the end so the answer looks tidy. The trick is to work in the right order so nothing trips you up. Now let's see it in action."

class M10AlgebraExponentLawsCombinedApplicationsScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Exponent Laws Combined Applications', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at what happens when you mix all the exponent\nrules together in one simplification. If you're multiplying terms with\nthe same base, you add the exponents. And if you hit a negative index,\nrewrite it as a reciprocal at the end so the answer looks tidy.", "The good news is, numbers behave like numbers, and exponents follow\ntheir own set of rules, so you tackle them as two separate jobs. If\nyou're dividing, you subtract. The trick is to work in the right order\nso nothing trips you up.", "First, combine the coefficients just like ordinary numbers, multiplying\nor dividing them as the expression requires. If something is raised to a\npower, you multiply the exponents. Now let's see it in action.", "Then turn your attention to the variables and count how each one's\nexponent moves depending on what's happening. Watch out for anything\nraised to the zero index, because that simply drops out and equals one."]
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
