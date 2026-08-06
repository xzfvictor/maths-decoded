"""Transcript-faithful Manim scene for percentages-association (m10-statistics-two-way)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how percentages can reveal whether two categorical variables are actually related to each other. The key idea is turning raw counts into comparable rates. A row percentage is simply the count in a single cell divided by the total for that row, and it tells you how that row breaks down. A column percentage is the cell count divided by the column total, telling you how that column breaks down. Once you have those, spotting association is straightforward. If you look across the rows and the percentages stay roughly the same from row to row, that means the variables aren't really related, so there's no association. But if the percentages shift noticeably between rows, the variables are connected, and there is an association. Think of it like comparing two recipes: if the proportions of ingredients change whenever you switch cooks, the choice of cook matters. Now let's see it in action with a real two-way table."

class M10StatisticsTwoWayPercentagesAssociationScene(Scene):
    def construct(self) -> None:
        title = Text('Statistics Two Way Percentages Association', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how percentages can reveal whether two\ncategorical variables are actually related to each other. Once you have\nthose, spotting association is straightforward. Now let's see it in\naction with a real two-way table.", "The key idea is turning raw counts into comparable rates. If you look\nacross the rows and the percentages stay roughly the same from row to\nrow, that means the variables aren't really related, so there's no\nassociation.", 'A row percentage is simply the count in a single cell divided by the\ntotal for that row, and it tells you how that row breaks down. But if\nthe percentages shift noticeably between rows, the variables are\nconnected, and there is an association.', 'A column percentage is the cell count divided by the column total,\ntelling you how that column breaks down. Think of it like comparing two\nrecipes: if the proportions of ingredients change whenever you switch\ncooks, the choice of cook matters.']
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
