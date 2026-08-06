"""Transcript-faithful Manim scene for elevation-depression (m10-measurement-trig)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at angles of elevation and depression, two ideas that sound tricky but are actually pretty straightforward once you see the picture. Imagine you're standing somewhere, and you draw an imaginary flat line going straight out from your eyes. That's called the horizontal. Now, the angle of elevation is the angle you tilt your head upward from that horizontal line to look at something higher up, like the top of a tree or a hill. The angle of depression is the same idea but downward, so it's the angle you look down from the horizontal to see something lower, like the base of that tree. Here's the cool part that makes problems easier. The angle of depression from one person looking at another is exactly the same as the angle of elevation from the second person looking back at the first. They are equal because of alternate angles on that horizontal line, so you only ever need to deal with one of them. The trick is always to draw that horizontal line first, then label the angle from it. Now let's see it in action."

class M10MeasurementTrigElevationDepressionScene(Scene):
    def construct(self) -> None:
        title = Text('Measurement Trig Elevation Depression', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at angles of elevation and depression, two\nideas that sound tricky but are actually pretty straightforward once you\nsee the picture. The angle of depression is the same idea but downward,\nso it's the angle you look down from the horizontal to see something\nlower, like the base of that tree. The trick is always to draw that\nhorizontal line first, then label the angle from it.", "Imagine you're standing somewhere, and you draw an imaginary flat line\ngoing straight out from your eyes. Here's the cool part that makes\nproblems easier. Now let's see it in action.", "That's called the horizontal. The angle of depression from one person\nlooking at another is exactly the same as the angle of elevation from\nthe second person looking back at the first.", 'Now, the angle of elevation is the angle you tilt your head upward from\nthat horizontal line to look at something higher up, like the top of a\ntree or a hill. They are equal because of alternate angles on that\nhorizontal line, so you only ever need to deal with one of them.']
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
