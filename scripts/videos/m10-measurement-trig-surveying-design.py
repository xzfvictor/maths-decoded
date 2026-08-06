"""Transcript-faithful Manim scene for surveying-design (m10-measurement-trig)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how surveyors and designers tackle three‑dimensional problems by breaking them into two simple right triangles. The big idea is decomposition. Instead of staring at a scary 3D shape, you split it into a horizontal footprint and a vertical rise, and each of those becomes its own right‑angled triangle. Step one is the base triangle. You use Pythagoras to find the horizontal distance across the ground. That distance then becomes one of the legs of your second triangle, the height triangle, which sits on top and gives you the vertical rise. You do Pythagoras again, and now you've got the full 3D measurement. A classic example is the smallest box that fits a long rod. The rod is angled through space, and the box just needs to match the rod's shadow on each axis, so its width, depth, and height are exactly the three projections of the rod. Same two‑triangle trick, just done once per direction. Now let's see it in action."

class M10MeasurementTrigSurveyingDesignScene(Scene):
    def construct(self) -> None:
        title = Text('Measurement Trig Surveying Design', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how surveyors and designers tackle\nthree‑dimensional problems by breaking them into two simple right\ntriangles. You use Pythagoras to find the horizontal distance across the\nground. The rod is angled through space, and the box just needs to match\nthe rod's shadow on each axis, so its width, depth, and height are\nexactly the three projections of the rod.", 'The big idea is decomposition. That distance then becomes one of the\nlegs of your second triangle, the height triangle, which sits on top and\ngives you the vertical rise. Same two‑triangle trick, just done once per\ndirection.', "Instead of staring at a scary 3D shape, you split it into a horizontal\nfootprint and a vertical rise, and each of those becomes its own\nright‑angled triangle. You do Pythagoras again, and now you've got the\nfull 3D measurement. Now let's see it in action.", 'Step one is the base triangle. A classic example is the smallest box\nthat fits a long rod.']
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
