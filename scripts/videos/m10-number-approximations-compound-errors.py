"""Transcript-faithful Manim scene for compound-errors (m10-number-approximations)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how small rounding mistakes can snowball when you repeat the same calculation over and over. First, let's talk about why it matters in chains. Imagine you're rounding off a few cents in every transaction. One transaction, who cares? But after a thousand of them, those few cents have turned into real dollars. The same thing happens in geometry. If you chop off decimal places while calculating a surface area or a volume, the final number can be off by a few percent. Then there's recursion, which is when an algorithm feeds its previous answer back in as the next input, like Newton's method or a simulation. Every tiny error gets carried forward and stacks on top of the last one. Even simple interest does this. Round a few cents per day and your running total will quietly drift away from the exact formula. So what's the rule of thumb? If you need the exact answer, keep extra decimal places while you're working, and only round at the very end. If the answer is a measurement, round it to the precision of the data you started with. Now let's see it in action."

class M10NumberApproximationsCompoundErrorsScene(Scene):
    def construct(self) -> None:
        title = Text('Number Approximations Compound Errors', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how small rounding mistakes can snowball\nwhen you repeat the same calculation over and over. But after a thousand\nof them, those few cents have turned into real dollars. Every tiny error\ngets carried forward and stacks on top of the last one. If you need the\nexact answer, keep extra decimal places while you're working, and only\nround at the very end.", "First, let's talk about why it matters in chains. The same thing happens\nin geometry. Even simple interest does this. If the answer is a\nmeasurement, round it to the precision of the data you started with.", "Imagine you're rounding off a few cents in every transaction. If you\nchop off decimal places while calculating a surface area or a volume,\nthe final number can be off by a few percent. Round a few cents per day\nand your running total will quietly drift away from the exact formula.\nNow let's see it in action.", "One transaction, who cares? Then there's recursion, which is when an\nalgorithm feeds its previous answer back in as the next input, like\nNewton's method or a simulation. So what's the rule of thumb?"]
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
