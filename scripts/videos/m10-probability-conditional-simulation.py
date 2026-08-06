"""Transcript-faithful Manim scene for simulation (m10-probability-conditional)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how to estimate probabilities when the maths just gets too messy to solve directly. The trick is simple: instead of calculating, we run a simulation many times and count how often our event happens. So here's the workflow. First, you model the situation using random numbers. For example, if you're flipping a coin, you might say any even digit means heads and any odd digit means tails. Then you run that experiment, say, a thousand or ten thousand times, because the more you repeat it, the more your relative frequency settles down to a stable value. After all those runs, you just count how many times your event of interest occurred, and divide by the total number of trials. That ratio, the count over N, is your empirical probability, and it's a solid estimate of the true probability. This approach is especially handy for counterintuitive puzzles, like the Monty Hall three-door problem, or the birthday problem, where the real answer often surprises people. Now let's see it in action."

class M10ProbabilityConditionalSimulationScene(Scene):
    def construct(self) -> None:
        title = Text('Probability Conditional Simulation', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how to estimate probabilities when the\nmaths just gets too messy to solve directly. For example, if you're\nflipping a coin, you might say any even digit means heads and any odd\ndigit means tails. This approach is especially handy for\ncounterintuitive puzzles, like the Monty Hall three-door problem, or the\nbirthday problem, where the real answer often surprises people.", "The trick is simple: instead of calculating, we run a simulation many\ntimes and count how often our event happens. Then you run that\nexperiment, say, a thousand or ten thousand times, because the more you\nrepeat it, the more your relative frequency settles down to a stable\nvalue. Now let's see it in action.", "So here's the workflow. After all those runs, you just count how many\ntimes your event of interest occurred, and divide by the total number of\ntrials.", "First, you model the situation using random numbers. That ratio, the\ncount over N, is your empirical probability, and it's a solid estimate\nof the true probability."]
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
