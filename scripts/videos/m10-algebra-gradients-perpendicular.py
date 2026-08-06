"""Transcript-faithful Manim scene for perpendicular (m10-algebra-gradients)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at perpendicular lines and how their gradients are secretly linked. Here's the big idea: when two lines cross at a perfect right angle, their gradients always multiply together to give negative one. That means if you know the slope of one line, the slope of the line that's perpendicular to it is completely fixed. To find it, just flip the gradient upside down and switch the sign. Mathematicians call this the negative reciprocal. So picture a line going gently upward with a gradient of one. Its perpendicular partner has to be a line going gently downward with a gradient of negative one, because one times negative one equals negative one. Try a steeper line, say a gradient of two. Flip it and you get one half, then make it negative, so the perpendicular gradient is negative one half. One last quick check, a line with a gradient of negative one third. Flip it to three over one, drop the negative, and the perpendicular line has a gradient of three. See the pattern, flip and swap the sign every time. Now let's see it in action."

class M10AlgebraGradientsPerpendicularScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Gradients Perpendicular', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at perpendicular lines and how their\ngradients are secretly linked. Mathematicians call this the negative\nreciprocal. Flip it and you get one half, then make it negative, so the\nperpendicular gradient is negative one half. Now let's see it in action.", "Here's the big idea: when two lines cross at a perfect right angle,\ntheir gradients always multiply together to give negative one. So\npicture a line going gently upward with a gradient of one. One last\nquick check, a line with a gradient of negative one third.", "That means if you know the slope of one line, the slope of the line\nthat's perpendicular to it is completely fixed. Its perpendicular\npartner has to be a line going gently downward with a gradient of\nnegative one, because one times negative one equals negative one. Flip\nit to three over one, drop the negative, and the perpendicular line has\na gradient of three.", 'To find it, just flip the gradient upside down and switch the sign. Try\na steeper line, say a gradient of two. See the pattern, flip and swap\nthe sign every time.']
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
