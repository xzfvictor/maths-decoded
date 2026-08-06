"""Transcript-faithful Manim scene for cycle (m10-statistics-investigations)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at the statistical investigation cycle, which is basically your roadmap for any data project. It has six steps, and you keep circling through them. First, you pose a question. Think about what variable you're actually interested in, and what other variable might help explain it, your explanatory variable. Next, you collect data. That can be primary, like running your own survey or experiment, or secondary, meaning you grab an existing data set someone else made. Then you represent it, usually with a scatterplot to see the relationship, a two-way table for categories, or a time-series plot if time is involved. After that, you analyse. Describe the shape of the distribution, fit a model like a line or a curve, and check the residuals to see how well it fits. Step five is to conclude. Actually answer your original question, and be upfront about your assumptions and methods. Finally, reflect on limitations, things like a small sample, potential bias, or lurking variables you didn't account for. Now let's see it in action."

class M10StatisticsInvestigationsCycleScene(Scene):
    def construct(self) -> None:
        title = Text('Statistics Investigations Cycle', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at the statistical investigation cycle, which\nis basically your roadmap for any data project. Next, you collect data.\nDescribe the shape of the distribution, fit a model like a line or a\ncurve, and check the residuals to see how well it fits. Now let's see it\nin action.", 'It has six steps, and you keep circling through them. That can be\nprimary, like running your own survey or experiment, or secondary,\nmeaning you grab an existing data set someone else made. Step five is to\nconclude.', 'First, you pose a question. Then you represent it, usually with a\nscatterplot to see the relationship, a two-way table for categories, or\na time-series plot if time is involved. Actually answer your original\nquestion, and be upfront about your assumptions and methods.', "Think about what variable you're actually interested in, and what other\nvariable might help explain it, your explanatory variable. After that,\nyou analyse. Finally, reflect on limitations, things like a small\nsample, potential bias, or lurking variables you didn't account for."]
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
