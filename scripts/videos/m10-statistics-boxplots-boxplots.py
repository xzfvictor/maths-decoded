"""Transcript-faithful Manim scene for boxplots (m10-statistics-boxplots)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at boxplots, a really quick way to summarise a whole dataset in one picture. Imagine a number line laid sideways. The middle is a box that stretches from the first quartile, that's the twenty-fifth percentile, up to the third quartile, the seventy-fifth percentile. Right in the middle of that box, a vertical line marks the median, which is the halfway point of the data. Now, thin lines called whiskers stick out from each side of the box, reaching out to the smallest and largest values, or to the most extreme points that aren't outliers. Any outliers show up as separate dots floating beyond the whiskers. So when you read a boxplot, the centre is where that median line sits. The spread is how wide the box is, called the interquartile range, and how long the whiskers are. The shape tells you about skew, so if one whisker is much longer than the other, the data is pulled in that direction. And outliers are those lonely dots on the end. The real power comes when you put two boxplots side by side, because then centre, spread, and shape jump out at you straight away. Now let's see it in action."

class M10StatisticsBoxplotsBoxplotsScene(Scene):
    def construct(self) -> None:
        title = Text('Statistics Boxplots Boxplots', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at boxplots, a really quick way to summarise a\nwhole dataset in one picture. Now, thin lines called whiskers stick out\nfrom each side of the box, reaching out to the smallest and largest\nvalues, or to the most extreme points that aren't outliers. The shape\ntells you about skew, so if one whisker is much longer than the other,\nthe data is pulled in that direction.", 'Imagine a number line laid sideways. Any outliers show up as separate\ndots floating beyond the whiskers. And outliers are those lonely dots on\nthe end.', "The middle is a box that stretches from the first quartile, that's the\ntwenty-fifth percentile, up to the third quartile, the seventy-fifth\npercentile. So when you read a boxplot, the centre is where that median\nline sits. The real power comes when you put two boxplots side by side,\nbecause then centre, spread, and shape jump out at you straight away.", "Right in the middle of that box, a vertical line marks the median, which\nis the halfway point of the data. The spread is how wide the box is,\ncalled the interquartile range, and how long the whiskers are. Now let's\nsee it in action."]
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
