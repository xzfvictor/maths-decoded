"""Transcript-faithful Manim scene for volume (m10-measurement-area-volume)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how to find the volume of composite solids, which are just two or more familiar shapes joined together. The trick is simple: split the solid into pieces you recognise, work out the volume of each piece, then add them all up. You'll usually break things down into a few common shapes. There's the rectangular prism, where you multiply length, width, and height. There's the cylinder, where you multiply pi by the radius squared and then by the height. And there's the cube, which is just side length cubed, or side multiplied by itself three times. Now, sometimes it's the opposite problem. Imagine a solid with a chunk cut out of it, like a cylinder with a hole drilled through it. In that case, you don't add, you subtract. You find the volume of the whole solid first, then subtract the volume of the bit that's been removed. The net volume is just the whole minus the cut. Once you're comfortable splitting shapes and choosing the right rule for each piece, these problems start to feel like a puzzle you already know how to solve. Now let's see it in action."

class M10MeasurementAreaVolumeVolumeScene(Scene):
    def construct(self) -> None:
        title = Text('Measurement Area Volume Volume', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how to find the volume of composite\nsolids, which are just two or more familiar shapes joined together.\nThere's the cylinder, where you multiply pi by the radius squared and\nthen by the height. In that case, you don't add, you subtract. Now let's\nsee it in action.", "The trick is simple: split the solid into pieces you recognise, work out\nthe volume of each piece, then add them all up. And there's the cube,\nwhich is just side length cubed, or side multiplied by itself three\ntimes. You find the volume of the whole solid first, then subtract the\nvolume of the bit that's been removed.", "You'll usually break things down into a few common shapes. Now,\nsometimes it's the opposite problem. The net volume is just the whole\nminus the cut.", "There's the rectangular prism, where you multiply length, width, and\nheight. Imagine a solid with a chunk cut out of it, like a cylinder with\na hole drilled through it. Once you're comfortable splitting shapes and\nchoosing the right rule for each piece, these problems start to feel\nlike a puzzle you already know how to solve."]
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
