"""Transcript-faithful Manim scene for elimination (m10-algebra-simultaneous)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at the elimination method for solving two equations with two unknowns. Picture two straight lines, and the solution is just the single point where both lines cross, that pair of x and y values that makes both equations true at the same time. Here's the core idea. If a variable already has the same size coefficient in both equations but opposite signs, you just add the equations together and that variable vanishes. If the coefficients are the same sign, you subtract instead. If they don't match yet, you multiply one or both equations by a clever number first so a variable lines up, then add or subtract to cancel it. Once one variable is gone, you solve the simple one equation that's left, then plug that value back into either original equation to find the other one. Elimination is usually the quickest choice when the coefficients already look like opposites, or when one is just a small multiple of the other, so the setup takes almost no effort. Now let's see it in action."

class M10AlgebraSimultaneousEliminationScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Simultaneous Elimination', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at the elimination method for solving two\nequations with two unknowns. If the coefficients are the same sign, you\nsubtract instead. Now let's see it in action.", "Picture two straight lines, and the solution is just the single point\nwhere both lines cross, that pair of x and y values that makes both\nequations true at the same time. If they don't match yet, you multiply\none or both equations by a clever number first so a variable lines up,\nthen add or subtract to cancel it.", "Here's the core idea. Once one variable is gone, you solve the simple\none equation that's left, then plug that value back into either original\nequation to find the other one.", 'If a variable already has the same size coefficient in both equations\nbut opposite signs, you just add the equations together and that\nvariable vanishes. Elimination is usually the quickest choice when the\ncoefficients already look like opposites, or when one is just a small\nmultiple of the other, so the setup takes almost no effort.']
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
