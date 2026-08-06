"""Transcript-faithful Manim scene for real-world (m10-measurement-log-scales)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at three real-world scales that all work the same clever way: pH, the Richter scale, and decibels. The big idea is that each step on these scales isn't just adding a little number, it's multiplying the actual thing being measured by ten. So a difference of two steps means a hundred times bigger, three steps means a thousand times, and so on.\n\nLet's start with pH, which measures how acidic something is. Each time pH drops by one, the concentration of hydrogen ions goes up by a factor of ten. Pure water sits right in the middle at pH seven.\n\nNext, the Richter scale measures earthquake amplitude. One step up means the ground shakes ten times more, and the energy released is roughly thirty-one times more. That is why a magnitude six feels so different from a magnitude four.\n\nFinally, decibels measure sound intensity. Ten decibels more is ten times the intensity, and twenty decibels more jumps to a hundred times. Now let's see it in action."

class M10MeasurementLogScalesRealWorldScene(Scene):
    def construct(self) -> None:
        title = Text('Measurement Log Scales Real World', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at three real-world scales that all work the\nsame clever way: pH, the Richter scale, and decibels. Each time pH drops\nby one, the concentration of hydrogen ions goes up by a factor of ten.\nThat is why a magnitude six feels so different from a magnitude four.", "The big idea is that each step on these scales isn't just adding a\nlittle number, it's multiplying the actual thing being measured by ten.\nPure water sits right in the middle at pH seven. Finally, decibels\nmeasure sound intensity.", 'So a difference of two steps means a hundred times bigger, three steps\nmeans a thousand times, and so on. Next, the Richter scale measures\nearthquake amplitude. Ten decibels more is ten times the intensity, and\ntwenty decibels more jumps to a hundred times.', "Let's start with pH, which measures how acidic something is. One step up\nmeans the ground shakes ten times more, and the energy released is\nroughly thirty-one times more. Now let's see it in action."]
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
