"""Transcript-faithful Manim scene for interpolation-causation (m10-statistics-scatter)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how to use a line of best fit to make predictions, and why some predictions are way more trustworthy than others. Once you've got that fitted line, you can plug in an x value and read off a y value. When the x you pick sits between data points you already have, that's called interpolation. Think of it like connecting the dots — your model has been tested in that range, so the prediction is usually pretty reliable. But if you pick an x value that's outside the data range, that's extrapolation, and it's risky. The relationship might curve off, or break down entirely, once you stray far from where it was measured, so be cautious with those predictions. Then there's the classic trap: correlation is not causation. Just because two things trend together doesn't mean one is causing the other. Ice-cream sales and drownings both climb in summer, but ice-cream obviously isn't causing drownings — hot weather is the lurking variable pushing both up. So always ask, what's actually driving the pattern? Now let's see it in action."

class M10StatisticsScatterInterpolationCausationScene(Scene):
    def construct(self) -> None:
        title = Text('Statistics Scatter Interpolation Causation', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how to use a line of best fit to make\npredictions, and why some predictions are way more trustworthy than\nothers. But if you pick an x value that's outside the data range, that's\nextrapolation, and it's risky. Ice-cream sales and drownings both climb\nin summer, but ice-cream obviously isn't causing drownings — hot weather\nis the lurking variable pushing both up.", "Once you've got that fitted line, you can plug in an x value and read\noff a y value. The relationship might curve off, or break down entirely,\nonce you stray far from where it was measured, so be cautious with those\npredictions. So always ask, what's actually driving the pattern?", "When the x you pick sits between data points you already have, that's\ncalled interpolation. Then there's the classic trap: correlation is not\ncausation. Now let's see it in action.", "Think of it like connecting the dots — your model has been tested in\nthat range, so the prediction is usually pretty reliable. Just because\ntwo things trend together doesn't mean one is causing the other."]
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
