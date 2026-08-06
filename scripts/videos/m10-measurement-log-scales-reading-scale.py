"""Transcript-faithful Manim scene for reading-scale (m10-measurement-log-scales)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how to read a logarithmic scale, which is a special kind of number line where each gridline jumps by a factor of ten rather than by one. The big idea is this: even though the gridlines look evenly spaced on the page, the numbers they represent grow really, really fast. So starting from one at the first mark, the next mark is ten, then one hundred, then one thousand, then ten thousand, and so on. Each step multiplies the previous value by ten, which is why the visual spacing stays equal while the numerical spacing explodes. You'll usually see this kind of scale whenever the numbers you're dealing with cover a huge range, like from one all the way up to ten million, because it squashes everything onto one neat chart. It also comes in handy when something is growing exponentially, like an epidemic or compound interest, because that fast growth shows up as a straight line on a log plot instead of a runaway curve. And finally, it's perfect for comparing ratios, which is why it's used for things like the pH scale and the Richter scale. Now let's see it in action."

class M10MeasurementLogScalesReadingScaleScene(Scene):
    def construct(self) -> None:
        title = Text('Measurement Log Scales Reading Scale', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how to read a logarithmic scale, which is\na special kind of number line where each gridline jumps by a factor of\nten rather than by one. You'll usually see this kind of scale whenever\nthe numbers you're dealing with cover a huge range, like from one all\nthe way up to ten million, because it squashes everything onto one neat\nchart.", 'The big idea is this: even though the gridlines look evenly spaced on\nthe page, the numbers they represent grow really, really fast. It also\ncomes in handy when something is growing exponentially, like an epidemic\nor compound interest, because that fast growth shows up as a straight\nline on a log plot instead of a runaway curve.', "So starting from one at the first mark, the next mark is ten, then one\nhundred, then one thousand, then ten thousand, and so on. And finally,\nit's perfect for comparing ratios, which is why it's used for things\nlike the pH scale and the Richter scale.", "Each step multiplies the previous value by ten, which is why the visual\nspacing stays equal while the numerical spacing explodes. Now let's see\nit in action."]
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
