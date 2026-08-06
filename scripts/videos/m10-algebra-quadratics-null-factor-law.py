"""Transcript-faithful Manim scene for null-factor-law (m10-algebra-quadratics)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how to solve quadratic equations by factorising, and you'll see how a really handy rule — the null factor law — does most of the heavy lifting for you. A quadratic equation is just one where the highest power of x is a squared term, like x squared plus five x plus six equals zero. The trick is to rewrite it as two sets of brackets multiplied together. When you can do that, the null factor law says something brilliant: if two things multiplied together give zero, then at least one of them must be zero. So you just set each bracket to zero on its own and read off the answers. To find those brackets, you look for two numbers that multiply to give the constant term and add to give the middle coefficient. For x squared plus five x plus six, those numbers are two and three, since two times three is six and two plus three is five. That gives you x plus two times x plus three equals zero, which splits into x equals negative two or x equals negative three. Now let's see it in action."

class M10AlgebraQuadraticsNullFactorLawScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Quadratics Null Factor Law', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how to solve quadratic equations by\nfactorising, and you'll see how a really handy rule — the null factor\nlaw — does most of the heavy lifting for you. So you just set each\nbracket to zero on its own and read off the answers. Now let's see it in\naction.", 'A quadratic equation is just one where the highest power of x is a\nsquared term, like x squared plus five x plus six equals zero. To find\nthose brackets, you look for two numbers that multiply to give the\nconstant term and add to give the middle coefficient.', 'The trick is to rewrite it as two sets of brackets multiplied together.\nFor x squared plus five x plus six, those numbers are two and three,\nsince two times three is six and two plus three is five.', 'When you can do that, the null factor law says something brilliant: if\ntwo things multiplied together give zero, then at least one of them must\nbe zero. That gives you x plus two times x plus three equals zero, which\nsplits into x equals negative two or x equals negative three.']
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
