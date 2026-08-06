"""Transcript-faithful Manim scene for dynamic-geometry (m10-space-proofs)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how dynamic geometry software can help you see geometric relationships come alive. Picture tools like GeoGebra or Desmos Geometry, where you can grab a point on the screen and drag it around, while the whole figure reshapes itself in real time. That is incredibly useful for exploring conjectures. You might ask, what happens if I change this angle, or stretch this side? Does the relationship I'm noticing still hold? You can test those ideas in seconds. The software also lets you build visual proofs, like comparing the area of a constructed shape against a reference shape, so the equality is obvious to your eyes. Another neat use is solving problems, such as finding the quadrilateral that gives the shortest path touching all four sides of a rectangle. But here is the catch, and this is really important. A dynamic geometry picture is a demonstration, not a proof. It is perfect for spotting the relationship, but you still need to write the proof on paper. So use the software to explore and to believe, then put your reasoning into words. Now let's see it in action."

class M10SpaceProofsDynamicGeometryScene(Scene):
    def construct(self) -> None:
        title = Text('Space Proofs Dynamic Geometry', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how dynamic geometry software can help you\nsee geometric relationships come alive. Does the relationship I'm\nnoticing still hold? But here is the catch, and this is really\nimportant. Now let's see it in action.", 'Picture tools like GeoGebra or Desmos Geometry, where you can grab a\npoint on the screen and drag it around, while the whole figure reshapes\nitself in real time. You can test those ideas in seconds. A dynamic\ngeometry picture is a demonstration, not a proof.', 'That is incredibly useful for exploring conjectures. The software also\nlets you build visual proofs, like comparing the area of a constructed\nshape against a reference shape, so the equality is obvious to your\neyes. It is perfect for spotting the relationship, but you still need to\nwrite the proof on paper.', 'You might ask, what happens if I change this angle, or stretch this\nside? Another neat use is solving problems, such as finding the\nquadrilateral that gives the shortest path touching all four sides of a\nrectangle. So use the software to explore and to believe, then put your\nreasoning into words.']
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
