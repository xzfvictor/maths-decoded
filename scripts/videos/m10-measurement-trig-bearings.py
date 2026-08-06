"""Transcript-faithful Manim scene for bearings (m10-measurement-trig)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at bearings, which are a really practical way to describe directions on a map or in the air. A bearing is just an angle measured clockwise from North, and we always write it as a three digit number. So North itself is zero zero zero degrees, East is zero nine zero, South is one eight zero, and West is two seven zero. Think of standing at a point and turning clockwise like the hands of a clock, and the number you land on is your bearing.\n\nWhen you get a bearing problem, the first thing to do is draw a line from your starting point to your destination, then mark the bearing angle from the North line at your start. After that, drop a perpendicular so you build a nice right triangle, either along the North-South line or the East-West line. Once you can see the opposite and adjacent sides, just pick the trig ratio, sine, cosine or tangent, that matches the angle you know and the side you want to find. Now let's see it in action."

class M10MeasurementTrigBearingsScene(Scene):
    def construct(self) -> None:
        title = Text('Measurement Trig Bearings', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at bearings, which are a really practical way\nto describe directions on a map or in the air. When you get a bearing\nproblem, the first thing to do is draw a line from your starting point\nto your destination, then mark the bearing angle from the North line at\nyour start.", 'A bearing is just an angle measured clockwise from North, and we always\nwrite it as a three digit number. After that, drop a perpendicular so\nyou build a nice right triangle, either along the North-South line or\nthe East-West line.', 'So North itself is zero zero zero degrees, East is zero nine zero, South\nis one eight zero, and West is two seven zero. Once you can see the\nopposite and adjacent sides, just pick the trig ratio, sine, cosine or\ntangent, that matches the angle you know and the side you want to find.', "Think of standing at a point and turning clockwise like the hands of a\nclock, and the number you land on is your bearing. Now let's see it in\naction."]
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
