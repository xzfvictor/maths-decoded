"""Transcript-faithful Manim scene for scale (m10-measurement-scaling)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at scale drawings and how to switch between a drawing and the real object it represents. A scale written like one to n just means that one unit on the page stands for n units in real life, so the number n is your scale factor. When you want the actual length, you take the length on the drawing and multiply it by the scale factor. When you want to find how long something should be on the drawing, you do the opposite and divide the real length by the scale factor.\n\nNow, a quick word on units. If your scale is given in centimetres, make sure both measurements are in centimetres before you do any multiplying or dividing, and only switch to metres or millimetres at the very end.\n\nOne more thing to keep in mind. When lengths scale by a factor of k, areas scale by k squared, and volumes scale by k cubed. So if a model is half the size, its surface area is one quarter and its volume is one eighth of the real thing. Now let's see it in action."

class M10MeasurementScalingScaleScene(Scene):
    def construct(self) -> None:
        title = Text('Measurement Scaling Scale', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at scale drawings and how to switch between a\ndrawing and the real object it represents. Now, a quick word on units.\nSo if a model is half the size, its surface area is one quarter and its\nvolume is one eighth of the real thing.", "A scale written like one to n just means that one unit on the page\nstands for n units in real life, so the number n is your scale factor.\nIf your scale is given in centimetres, make sure both measurements are\nin centimetres before you do any multiplying or dividing, and only\nswitch to metres or millimetres at the very end. Now let's see it in\naction.", 'When you want the actual length, you take the length on the drawing and\nmultiply it by the scale factor. One more thing to keep in mind.', 'When you want to find how long something should be on the drawing, you\ndo the opposite and divide the real length by the scale factor. When\nlengths scale by a factor of k, areas scale by k squared, and volumes\nscale by k cubed.']
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
