"""Transcript-faithful Manim scene for rounding-truncation (m10-number-approximations)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at rounding versus truncation — two common ways a calculator gives you a shorter version of a number. Both start the same way: you pick a place value to stop at, like ones, tens, or two decimal places, and then you decide what to do with the digits that come after. With truncation, the job is super simple — you just chop off every digit past your stopping point, no questions asked. It's quick, but it's harsh, and it always biases the result downward for positive numbers. With rounding, you peek at the very next digit after your stopping point. If that digit is five or more, you bump the digit you're keeping up by one; if it's four or less, you leave it alone. So rounding sometimes goes up and sometimes goes down, which makes it a fairer estimate on average. One small heads-up: if the next digit is exactly five with nothing after it, that's a tie, and different systems break the tie differently — many round to the nearest even digit, though in class we'll stick with the simple round-half-up rule. Now let's see it in action."

class M10NumberApproximationsRoundingTruncationScene(Scene):
    def construct(self) -> None:
        title = Text('Number Approximations Rounding Truncation', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at rounding versus truncation — two common\nways a calculator gives you a shorter version of a number. With\nrounding, you peek at the very next digit after your stopping point. Now\nlet's see it in action.", "Both start the same way: you pick a place value to stop at, like ones,\ntens, or two decimal places, and then you decide what to do with the\ndigits that come after. If that digit is five or more, you bump the\ndigit you're keeping up by one; if it's four or less, you leave it\nalone.", 'With truncation, the job is super simple — you just chop off every digit\npast your stopping point, no questions asked. So rounding sometimes goes\nup and sometimes goes down, which makes it a fairer estimate on average.', "It's quick, but it's harsh, and it always biases the result downward for\npositive numbers. One small heads-up: if the next digit is exactly five\nwith nothing after it, that's a tie, and different systems break the tie\ndifferently — many round to the nearest even digit, though in class\nwe'll stick with the simple round-half-up rule."]
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
