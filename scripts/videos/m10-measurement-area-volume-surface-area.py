"""Transcript-faithful Manim scene for surface-area (m10-measurement-area-volume)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how to find the surface area of composite solids, which are just shapes made by sticking simpler solids together. Here's the key idea, and it might feel a bit strange at first. Instead of adding things up, you're actually subtracting. When two solids are joined, the faces where they meet disappear from the outside, so you don't count them. Think of it like two ice cubes glued together. The glue faces are now hidden inside, so they aren't part of the outside surface anymore.\n\nNow, let's quickly run through the building blocks you'll need. For a right rectangular prism, the surface area is twice the sum of length times width, length times height, and width times height. For a right circular cylinder, it's two pi r squared for the circular ends, plus two pi r h for the curved side. And for a cube, it's simply six times the side length squared. Super straightforward.\n\nThe biggest mistake students make is just adding the surface areas of the separate parts together. Don't do that. Remember to count only the faces you can actually see from the outside, and skip the ones hidden at the join. Now let's see it in action."

class M10MeasurementAreaVolumeSurfaceAreaScene(Scene):
    def construct(self) -> None:
        title = Text('Measurement Area Volume Surface Area', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how to find the surface area of composite\nsolids, which are just shapes made by sticking simpler solids together.\nThink of it like two ice cubes glued together. For a right circular\ncylinder, it's two pi r squared for the circular ends, plus two pi r h\nfor the curved side. Don't do that.", "Here's the key idea, and it might feel a bit strange at first. The glue\nfaces are now hidden inside, so they aren't part of the outside surface\nanymore. And for a cube, it's simply six times the side length squared.\nRemember to count only the faces you can actually see from the outside,\nand skip the ones hidden at the join.", "Instead of adding things up, you're actually subtracting. Now, let's\nquickly run through the building blocks you'll need. Super\nstraightforward. Now let's see it in action.", "When two solids are joined, the faces where they meet disappear from the\noutside, so you don't count them. For a right rectangular prism, the\nsurface area is twice the sum of length times width, length times\nheight, and width times height. The biggest mistake students make is\njust adding the surface areas of the separate parts together."]
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
