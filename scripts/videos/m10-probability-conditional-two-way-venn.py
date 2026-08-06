"""Transcript-faithful Manim scene for two-way-venn (m10-probability-conditional)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at two visual tools that make conditional probability way easier, two-way tables and Venn diagrams. First up, the two-way table. Imagine a grid with two events, let's call them A and B, split into four squares: both happen, A but not B, B but not A, and neither happens. Add up the rows and columns to get your totals. Now here's the magic trick. A conditional probability is just a fraction inside the table. If you want the probability of A given that B has happened, you only look inside the B column. Take the number where A and B overlap, and divide it by the total of that whole B column. Easy, right? Same idea the other way. For B given A, you stay inside the A row. The overlapping square goes on top, and the total of the A row goes on the bottom. Now, Venn diagrams do the same job, just drawn as two overlapping circles. The overlap is your joint region, and each full circle is your conditioning event. Conditional probability is still just the overlap count divided by the whole circle you're conditioning on. Same fraction, different picture. Now let's see it in action."

class M10ProbabilityConditionalTwoWayVennScene(Scene):
    def construct(self) -> None:
        title = Text('Probability Conditional Two Way Venn', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at two visual tools that make conditional\nprobability way easier, two-way tables and Venn diagrams. Now here's the\nmagic trick. Easy, right? Now, Venn diagrams do the same job, just drawn\nas two overlapping circles. Now let's see it in action.", 'First up, the two-way table. A conditional probability is just a\nfraction inside the table. Same idea the other way. The overlap is your\njoint region, and each full circle is your conditioning event.', "Imagine a grid with two events, let's call them A and B, split into four\nsquares: both happen, A but not B, B but not A, and neither happens. If\nyou want the probability of A given that B has happened, you only look\ninside the B column. For B given A, you stay inside the A row.\nConditional probability is still just the overlap count divided by the\nwhole circle you're conditioning on.", 'Add up the rows and columns to get your totals. Take the number where A\nand B overlap, and divide it by the total of that whole B column. The\noverlapping square goes on top, and the total of the A row goes on the\nbottom. Same fraction, different picture.']
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
