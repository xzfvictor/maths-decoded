"""Transcript-faithful Manim scene for scatter-fit (m10-statistics-scatter)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how to draw a scatterplot and sketch a line of best fit. First, pick two numerical variables and pair them up, one for each observation. Then decide which one is the explanatory variable — that's the one you think explains the other — and put it on the horizontal axis. The response variable goes on the vertical axis. Now plot each pair as a single dot, and you'll start to see a pattern emerge.\n\nNext comes the line of best fit. It's a straight line that passes as close as possible to all the points, with roughly equal numbers above and below it. You eyeball it through the middle of the cloud. You can use this line to interpolate, which means estimating values that fall between your data points, and that works pretty well. But be careful with extrapolation, which is estimating beyond the range of your data, because the pattern might not hold out there.\n\nWhen you describe the relationship, comment on its strength, direction, and shape. Now let's see it in action."

class M10StatisticsScatterScatterFitScene(Scene):
    def construct(self) -> None:
        title = Text('Statistics Scatter Scatter Fit', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how to draw a scatterplot and sketch a\nline of best fit. Now plot each pair as a single dot, and you'll start\nto see a pattern emerge. You can use this line to interpolate, which\nmeans estimating values that fall between your data points, and that\nworks pretty well.", 'First, pick two numerical variables and pair them up, one for each\nobservation. Next comes the line of best fit. But be careful with\nextrapolation, which is estimating beyond the range of your data,\nbecause the pattern might not hold out there.', "Then decide which one is the explanatory variable — that's the one you\nthink explains the other — and put it on the horizontal axis. It's a\nstraight line that passes as close as possible to all the points, with\nroughly equal numbers above and below it. When you describe the\nrelationship, comment on its strength, direction, and shape.", "The response variable goes on the vertical axis. You eyeball it through\nthe middle of the cloud. Now let's see it in action."]
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
