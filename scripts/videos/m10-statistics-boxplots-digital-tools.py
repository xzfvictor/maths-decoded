"""Transcript-faithful Manim scene for digital-tools (m10-statistics-boxplots)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how digital tools can do the heavy lifting when you're comparing distributions with boxplots and histograms. The key idea is simple — let the software crunch the numbers, and you focus on what the picture is telling you.\n\nHere's the workflow. First, enter or load your data into a tool like Excel, Google Sheets, R, or Python. Then ask for the five-number summary or a boxplot, and the software will calculate the median and quartiles for you. If you want to compare two groups, just overlay two boxplots on the same axis so you can see them side by side. And when you want to understand the shape of your data — whether it's symmetric, skewed, or has more than one peak — a histogram is your best friend.\n\nThe most important step is interpretation. Don't get lost in the numbers. Instead, read the story from the picture. Where's the centre? How wide is the spread? Are there any outliers? Is the shape balanced or lopsided?\n\nNow let's see it in action."

class M10StatisticsBoxplotsDigitalToolsScene(Scene):
    def construct(self) -> None:
        title = Text('Statistics Boxplots Digital Tools', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how digital tools can do the heavy lifting\nwhen you're comparing distributions with boxplots and histograms. Then\nask for the five-number summary or a boxplot, and the software will\ncalculate the median and quartiles for you. Don't get lost in the\nnumbers. Are there any outliers?", 'The key idea is simple — let the software crunch the numbers, and you\nfocus on what the picture is telling you. If you want to compare two\ngroups, just overlay two boxplots on the same axis so you can see them\nside by side. Instead, read the story from the picture. Is the shape\nbalanced or lopsided?', "Here's the workflow. And when you want to understand the shape of your\ndata — whether it's symmetric, skewed, or has more than one peak — a\nhistogram is your best friend. Where's the centre? Now let's see it in\naction.", 'First, enter or load your data into a tool like Excel, Google Sheets, R,\nor Python. The most important step is interpretation. How wide is the\nspread?']
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
