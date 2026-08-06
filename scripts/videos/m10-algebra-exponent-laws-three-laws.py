"""Transcript-faithful Manim scene for three-laws (m10-algebra-exponent-laws)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at the three fundamental exponent laws you'll use over and over in Methods. Here's the big idea. When you're working with exponents, there are really only three moves you need to remember.\n\nThe first law is the product law. When you multiply two powers that have the same base, you just add the exponents together. So something cubed times something to the fifth gives you something to the eighth, because three plus five is eight.\n\nThe second law is the quotient law. When you divide two powers with the same base, you subtract the exponents. So something to the tenth divided by something to the fourth leaves you with something to the sixth, because ten minus four is six.\n\nThe third law is the power of a power. When you raise a power to another power, you multiply the exponents. So something squared, all raised to the fifth, becomes something to the tenth.\n\nThe good news is, these rules work exactly the same way once you throw algebra into the mix. Just treat the variable as your base and apply the same law. And if there's a coefficient out the front, like two or three, just multiply those together like ordinary numbers. Now let's see it in action."

class M10AlgebraExponentLawsThreeLawsScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Exponent Laws Three Laws', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at the three fundamental exponent laws you'll\nuse over and over in Methods. When you multiply two powers that have the\nsame base, you just add the exponents together. So something to the\ntenth divided by something to the fourth leaves you with something to\nthe sixth, because ten minus four is six. The good news is, these rules\nwork exactly the same way once you throw algebra into the mix.", "Here's the big idea. So something cubed times something to the fifth\ngives you something to the eighth, because three plus five is eight. The\nthird law is the power of a power. Just treat the variable as your base\nand apply the same law.", "When you're working with exponents, there are really only three moves\nyou need to remember. The second law is the quotient law. When you raise\na power to another power, you multiply the exponents. And if there's a\ncoefficient out the front, like two or three, just multiply those\ntogether like ordinary numbers.", "The first law is the product law. When you divide two powers with the\nsame base, you subtract the exponents. So something squared, all raised\nto the fifth, becomes something to the tenth. Now let's see it in\naction."]
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
