"""Transcript-faithful Manim scene for build-read (m10-statistics-two-way)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at how to build and read two-way tables. A two-way table is just a grid that cross-tabulates two categorical variables, meaning one variable goes along the rows, the other goes down the columns, and each cell shows the count of how many observations fall into that row and column combination. That's called the joint count. For example, if you're comparing handedness and gender, a single cell might tell you how many left-handed females there are in your sample. Next, you can sum across a row to get the row total, which represents the overall count for one level of your row variable, and sum down a column to get the column total, which does the same for one level of your column variable. Finally, add up every cell in the table to get the grand total, which is simply the total number of observations you collected. Once you have these totals, the table becomes a powerful summary, because you can see not just the joint counts but also how each variable breaks down on its own. Now let's see it in action."

class M10StatisticsTwoWayBuildReadScene(Scene):
    def construct(self) -> None:
        title = Text('Statistics Two Way Build Read', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at how to build and read two-way tables. Next,\nyou can sum across a row to get the row total, which represents the\noverall count for one level of your row variable, and sum down a column\nto get the column total, which does the same for one level of your\ncolumn variable.", 'A two-way table is just a grid that cross-tabulates two categorical\nvariables, meaning one variable goes along the rows, the other goes down\nthe columns, and each cell shows the count of how many observations fall\ninto that row and column combination. Finally, add up every cell in the\ntable to get the grand total, which is simply the total number of\nobservations you collected.', "That's called the joint count. Once you have these totals, the table\nbecomes a powerful summary, because you can see not just the joint\ncounts but also how each variable breaks down on its own.", "For example, if you're comparing handedness and gender, a single cell\nmight tell you how many left-handed females there are in your sample.\nNow let's see it in action."]
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
