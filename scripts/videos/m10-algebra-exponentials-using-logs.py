"""Transcript-faithful Manim scene for using-logs (m10-algebra-exponentials)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how to solve exponential equations when the bases just don't match, like when three to the power of x equals twenty. The trick is simple: take a logarithm of both sides. A logarithm is basically the inverse of an exponent, so it lets us bring that unknown x down where we can actually get to it.\n\nHere's how it goes. First, you apply a log to both sides of the equation. Then you use the power law, which says the log of something raised to a power equals that power times the log of the base. So if x is up in the exponent, it comes tumbling down to the front, multiplied by the log of the base. After that, it's just basic algebra — divide both sides by whatever is sitting next to x, and you've got your answer.\n\nQuick tip: you can use any log you like, but the natural log, written ln, is especially handy when you see an e-power on the right, because it cancels things out neatly.\n\nNow let's see it in action."

class M10AlgebraExponentialsUsingLogsScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Exponentials Using Logs', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how to solve exponential equations when\nthe bases just don't match, like when three to the power of x equals\ntwenty. First, you apply a log to both sides of the equation. Quick tip:\nyou can use any log you like, but the natural log, written ln, is\nespecially handy when you see an e-power on the right, because it\ncancels things out neatly.", "The trick is simple: take a logarithm of both sides. Then you use the\npower law, which says the log of something raised to a power equals that\npower times the log of the base. Now let's see it in action.", 'A logarithm is basically the inverse of an exponent, so it lets us bring\nthat unknown x down where we can actually get to it. So if x is up in\nthe exponent, it comes tumbling down to the front, multiplied by the log\nof the base.', "Here's how it goes. After that, it's just basic algebra — divide both\nsides by whatever is sitting next to x, and you've got your answer."]
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
