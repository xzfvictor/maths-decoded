"""Transcript-faithful Manim scene for isosceles-properties (m10-space-proofs)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at how to take theorems you already know and use them to figure out new facts. The big idea is that proofs are often just a chain of these results, one leading to the next. Start with a classic: in an isosceles triangle, the base angles are equal. The neat way to see it is to drop a perpendicular from the top vertex, and use the right-angle, hypotenuse, side rule to show the two smaller triangles are congruent, then the matching angles fall out. From there, you can move to parallel lines. When a straight line cuts two parallel lines, the co-interior angles on the same side add to a hundred and eighty degrees. Vertically opposite angles, where two lines cross, are always equal too. And here is a handy shortcut, the exterior angle of a triangle equals the sum of the two non-adjacent interior angles, so you often don't even need to find both remote angles. In practice, a proof usually goes prove two triangles congruent, then use corresponding parts to deduce an angle or a side. Now let's see it in action."

class M10SpaceProofsIsoscelesPropertiesScene(Scene):
    def construct(self) -> None:
        title = Text('Space Proofs Isosceles Properties', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at how to take theorems you already know and\nuse them to figure out new facts. From there, you can move to parallel\nlines. In practice, a proof usually goes prove two triangles congruent,\nthen use corresponding parts to deduce an angle or a side.", "The big idea is that proofs are often just a chain of these results, one\nleading to the next. When a straight line cuts two parallel lines, the\nco-interior angles on the same side add to a hundred and eighty degrees.\nNow let's see it in action.", 'Start with a classic: in an isosceles triangle, the base angles are\nequal. Vertically opposite angles, where two lines cross, are always\nequal too.', "The neat way to see it is to drop a perpendicular from the top vertex,\nand use the right-angle, hypotenuse, side rule to show the two smaller\ntriangles are congruent, then the matching angles fall out. And here is\na handy shortcut, the exterior angle of a triangle equals the sum of the\ntwo non-adjacent interior angles, so you often don't even need to find\nboth remote angles."]
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
