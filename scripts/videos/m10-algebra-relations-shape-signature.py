"""Transcript-faithful Manim scene for shape-signature (m10-algebra-relations)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how to recognise different families of relations just by reading the rule or spotting the shape. Think of each family as having its own signature, both in the equation itself and in the graph it draws. For a linear rule, you'll see something like y equals m times x plus b, which always gives you a perfectly straight line, slanted by m and crossing the y-axis at b. For a quadratic rule, you'll see an x squared term, and the graph is a smooth U-shaped parabola that opens upwards when the leading number is positive. For a reciprocal rule, x lives in the bottom of a fraction, and the graph splits into two separate branches that hug the axes but never touch them. For an exponential rule, the variable x is up in the exponent, and the curve either shoots upwards or decays towards zero, but it never goes negative. And for a circle centred at the origin, the rule adds x squared and y squared together to give a constant, producing that familiar round shape with radius equal to the square root of that constant. The trick is that reading either the rule or the shape is enough to name the family. Now let's see it in action."

class M10AlgebraRelationsShapeSignatureScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Relations Shape Signature', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how to recognise different families of\nrelations just by reading the rule or spotting the shape. For a\nreciprocal rule, x lives in the bottom of a fraction, and the graph\nsplits into two separate branches that hug the axes but never touch\nthem. Now let's see it in action.", 'Think of each family as having its own signature, both in the equation\nitself and in the graph it draws. For an exponential rule, the variable\nx is up in the exponent, and the curve either shoots upwards or decays\ntowards zero, but it never goes negative.', "For a linear rule, you'll see something like y equals m times x plus b,\nwhich always gives you a perfectly straight line, slanted by m and\ncrossing the y-axis at b. And for a circle centred at the origin, the\nrule adds x squared and y squared together to give a constant, producing\nthat familiar round shape with radius equal to the square root of that\nconstant.", "For a quadratic rule, you'll see an x squared term, and the graph is a\nsmooth U-shaped parabola that opens upwards when the leading number is\npositive. The trick is that reading either the rule or the shape is\nenough to name the family."]
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
