"""Transcript-faithful Manim scene for algebraic-denominators (m10-algebra-linear-fractions)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at what happens when the denominator in a fraction contains a variable, and why that can sneak in answers that aren't really valid. The basic strategy you've used before still works: clear the denominator by multiplying both sides by whatever's on the bottom. But here's the catch, and it's the key idea. When you multiply both sides by something that contains a variable, that something could be zero, and if it is, the whole step is illegal. So the rule is simple. After you solve, take your answer and plug it back into every denominator in the original equation. If any denominator becomes zero, that value is called an extraneous root, and you have to throw it away. It came out of the algebra, but it doesn't actually satisfy the equation. To stay safe, follow a four-step recipe. First, identify the lowest common denominator, including any algebraic factors. Second, multiply through by it. Third, solve the resulting equation. And fourth, substitute your answer back to make sure no denominator is zero. Keep that checklist handy and you'll avoid the trap every time. Now let's see it in action."

class M10AlgebraLinearFractionsAlgebraicDenominatorsScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Linear Fractions Algebraic Denominators', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at what happens when the denominator in a\nfraction contains a variable, and why that can sneak in answers that\naren't really valid. So the rule is simple. To stay safe, follow a four-\nstep recipe. And fourth, substitute your answer back to make sure no\ndenominator is zero.", "The basic strategy you've used before still works: clear the denominator\nby multiplying both sides by whatever's on the bottom. After you solve,\ntake your answer and plug it back into every denominator in the original\nequation. First, identify the lowest common denominator, including any\nalgebraic factors. Keep that checklist handy and you'll avoid the trap\nevery time.", "But here's the catch, and it's the key idea. If any denominator becomes\nzero, that value is called an extraneous root, and you have to throw it\naway. Second, multiply through by it. Now let's see it in action.", "When you multiply both sides by something that contains a variable, that\nsomething could be zero, and if it is, the whole step is illegal. It\ncame out of the algebra, but it doesn't actually satisfy the equation.\nThird, solve the resulting equation."]
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
