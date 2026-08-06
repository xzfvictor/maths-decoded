"""Transcript-faithful Manim scene for multiply-divide (m10-algebra-fractions)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how to multiply and divide algebraic fractions. First up, multiplying. The rule is simple: multiply the top of the first fraction by the top of the second, and the bottom by the bottom. But here's the trick that saves you a ton of work: always simplify before you multiply. Look across the numerators and denominators, and cancel any common factors you can spot. For example, if you see the same variable on top and bottom, use the exponent laws to cancel them down. Now for dividing. Dividing fractions feels different, but it's actually just multiplying in disguise. You keep the first fraction the same, then flip the second one upside down to get its reciprocal, and finally multiply them together using the same top-times-top, bottom-times-bottom rule. So in short: multiply straight across after cancelling, and divide by flipping the second fraction first. Now let's see it in action with a worked example."

class M10AlgebraFractionsMultiplyDivideScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Fractions Multiply Divide', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how to multiply and divide algebraic\nfractions. Look across the numerators and denominators, and cancel any\ncommon factors you can spot. You keep the first fraction the same, then\nflip the second one upside down to get its reciprocal, and finally\nmultiply them together using the same top-times-top, bottom-times-bottom\nrule.", 'First up, multiplying. For example, if you see the same variable on top\nand bottom, use the exponent laws to cancel them down. So in short:\nmultiply straight across after cancelling, and divide by flipping the\nsecond fraction first.', "The rule is simple: multiply the top of the first fraction by the top of\nthe second, and the bottom by the bottom. Now for dividing. Now let's\nsee it in action with a worked example.", "But here's the trick that saves you a ton of work: always simplify\nbefore you multiply. Dividing fractions feels different, but it's\nactually just multiplying in disguise."]
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
