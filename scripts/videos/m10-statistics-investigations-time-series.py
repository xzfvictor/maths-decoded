"""Transcript-faithful Manim scene for time-series (m10-statistics-investigations)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how a quantity changes over time, using something called a time-series plot. The idea is simple: you put time on the horizontal axis and the measurement, like monthly rainfall, a share price, or population, on the vertical axis. Time is doing the job of your explanatory variable.\n\nAs you read the plot, watch for three things. First, the trend, which is the overall direction the data is moving in, whether it looks roughly straight, curving up like exponential growth, or repeating in cycles. Second, seasonality, those regular ups and downs you see within a year, like sales spiking every December. Third, outliers or sudden jumps, which usually mean something interesting happened and is worth investigating.\n\nWhen it comes to modelling, if the trend looks straight you fit a least-squares line through the points. If it's exponential, you transform to a log scale first. And if there's a clear seasonal pattern, you can break the data into trend, seasonal, and random noise.\n\nNow let's see it in action."

class M10StatisticsInvestigationsTimeSeriesScene(Scene):
    def construct(self) -> None:
        title = Text('Statistics Investigations Time Series', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how a quantity changes over time, using\nsomething called a time-series plot. First, the trend, which is the\noverall direction the data is moving in, whether it looks roughly\nstraight, curving up like exponential growth, or repeating in cycles. If\nit's exponential, you transform to a log scale first.", "The idea is simple: you put time on the horizontal axis and the\nmeasurement, like monthly rainfall, a share price, or population, on the\nvertical axis. Second, seasonality, those regular ups and downs you see\nwithin a year, like sales spiking every December. And if there's a clear\nseasonal pattern, you can break the data into trend, seasonal, and\nrandom noise.", "Time is doing the job of your explanatory variable. Third, outliers or\nsudden jumps, which usually mean something interesting happened and is\nworth investigating. Now let's see it in action.", 'As you read the plot, watch for three things. When it comes to\nmodelling, if the trend looks straight you fit a least-squares line\nthrough the points.']
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
