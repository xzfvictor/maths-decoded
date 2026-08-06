"""Transcript-faithful Manim scene for comparing-displays (m10-statistics-boxplots)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how different displays of the same data can tell you totally different stories, so the trick is picking the one that actually answers your question. Let's walk through the four main ones. First, the boxplot. This is your go-to when you want to compare two or more groups side by side, because it lays out the centre, the spread, the skew, and any outliers all at once, almost like a quick summary card for each group. Next, the histogram. Use this when you care about the shape of the data, like spotting peaks, gaps, or whether the distribution is bimodal with two humps. Then there's the cumulative frequency graph, sometimes called an ogive. This is the one you reach for when you need to find a specific percentile, like the median or the ninetieth percentile, because you can read those values straight off the curve. Finally, the dot plot, which is perfect for small data sets where you literally want to see every single observation. So the real skill here is matching the question to the display. Now let's see it in action."

class M10StatisticsBoxplotsComparingDisplaysScene(Scene):
    def construct(self) -> None:
        title = Text('Statistics Boxplots Comparing Displays', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how different displays of the same data\ncan tell you totally different stories, so the trick is picking the one\nthat actually answers your question. Next, the histogram. Finally, the\ndot plot, which is perfect for small data sets where you literally want\nto see every single observation.", "Let's walk through the four main ones. Use this when you care about the\nshape of the data, like spotting peaks, gaps, or whether the\ndistribution is bimodal with two humps. So the real skill here is\nmatching the question to the display.", "First, the boxplot. Then there's the cumulative frequency graph,\nsometimes called an ogive. Now let's see it in action.", 'This is your go-to when you want to compare two or more groups side by\nside, because it lays out the centre, the spread, the skew, and any\noutliers all at once, almost like a quick summary card for each group.\nThis is the one you reach for when you need to find a specific\npercentile, like the median or the ninetieth percentile, because you can\nread those values straight off the curve.']
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
