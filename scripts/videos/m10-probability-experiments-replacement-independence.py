"""Transcript-faithful Manim scene for replacement-independence (m10-probability-experiments)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at the difference between drawing with replacement and drawing without replacement, and what that means for whether events are independent.\n\nImagine a bag with some coloured balls. If you draw a ball, note it down, and then put it back before the next draw, that's with replacement. Because the bag is exactly the same each time, what you draw on the first go doesn't affect what you draw next. We call those draws independent. In a tree diagram, every branch out of each stage has the same set of probabilities.\n\nNow, without replacement means you keep the ball out. The bag actually shrinks, so the chances change. If you pulled out a red ball first, there are fewer reds left for the next draw. So the second set of branches on your tree looks different from the first. Knowing the first draw did change the probability of the second, which means the events are not independent.\n\nA quick way to check independence is whether the chance of both events happening equals the chance of the first times the chance of the second. If they're not equal, the events are dependent.\n\nNow let's see it in action."

class M10ProbabilityExperimentsReplacementIndependenceScene(Scene):
    def construct(self) -> None:
        title = Text('Probability Experiments Replacement Independence', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at the difference between drawing with\nreplacement and drawing without replacement, and what that means for\nwhether events are independent. We call those draws independent. If you\npulled out a red ball first, there are fewer reds left for the next\ndraw. If they're not equal, the events are dependent.", "Imagine a bag with some coloured balls. In a tree diagram, every branch\nout of each stage has the same set of probabilities. So the second set\nof branches on your tree looks different from the first. Now let's see\nit in action.", "If you draw a ball, note it down, and then put it back before the next\ndraw, that's with replacement. Now, without replacement means you keep\nthe ball out. Knowing the first draw did change the probability of the\nsecond, which means the events are not independent.", "Because the bag is exactly the same each time, what you draw on the\nfirst go doesn't affect what you draw next. The bag actually shrinks, so\nthe chances change. A quick way to check independence is whether the\nchance of both events happening equals the chance of the first times the\nchance of the second."]
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
