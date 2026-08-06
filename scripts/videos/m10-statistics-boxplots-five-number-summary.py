"""Transcript-faithful Manim scene for five-number-summary (m10-statistics-boxplots)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at a really handy way to describe a whole pile of data using just five numbers. It's called the five-number summary, and it's the cheapest, most useful snapshot of a continuous data set you'll come across. Here's how it works. First, you line up your data from smallest to largest. Then you find five key values. The minimum, which is just the smallest value you have. Then the first quartile, often called Q one, which is the median of the lower half of your data, so it's like the twenty-fifth percentile mark. Next comes the median itself, the middle value that splits your data in half. Then the third quartile, Q three, the median of the upper half, sitting at the seventy-fifth percentile. And finally the maximum, the biggest value. Put those five together and you've got a neat summary of where your data sits. From those numbers we get the interquartile range, or IQR, which is just Q three minus Q one. It's a brilliant measure of spread because it ignores the really extreme outliers. In fact, any value that sits more than one and a half times the IQR below Q one or above Q three is flagged as a possible outlier. Now let's see it in action."

class M10StatisticsBoxplotsFiveNumberSummaryScene(Scene):
    def construct(self) -> None:
        title = Text('Statistics Boxplots Five Number Summary', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at a really handy way to describe a whole\npile of data using just five numbers. Then you find five key values.\nThen the third quartile, Q three, the median of the upper half, sitting\nat the seventy-fifth percentile. It's a brilliant measure of spread\nbecause it ignores the really extreme outliers.", "It's called the five-number summary, and it's the cheapest, most useful\nsnapshot of a continuous data set you'll come across. The minimum, which\nis just the smallest value you have. And finally the maximum, the\nbiggest value. In fact, any value that sits more than one and a half\ntimes the IQR below Q one or above Q three is flagged as a possible\noutlier.", "Here's how it works. Then the first quartile, often called Q one, which\nis the median of the lower half of your data, so it's like the twenty-\nfifth percentile mark. Put those five together and you've got a neat\nsummary of where your data sits. Now let's see it in action.", 'First, you line up your data from smallest to largest. Next comes the\nmedian itself, the middle value that splits your data in half. From\nthose numbers we get the interquartile range, or IQR, which is just Q\nthree minus Q one.']
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
