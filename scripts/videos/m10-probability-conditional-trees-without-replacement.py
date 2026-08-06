"""Transcript-faithful Manim scene for trees-without-replacement (m10-probability-conditional)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at how to handle multi-step experiments using tree diagrams and arrays, especially when one event depends on another. Let's start with tree diagrams. Think of a tree as a branching path where each fork represents one possible outcome at a particular step, and the labels on the branches show the probabilities. You multiply along any single path to find the chance of that whole sequence, and when several paths end in the same result, you add those probabilities together. Next, arrays. Imagine a grid with the outcomes of one variable running down the side and the outcomes of the other running across the top, so every cell is a unique combination. Arrays are super handy when both things you're tracking are categories. Finally, the big idea, independent versus dependent. If you're flipping a coin twice, the second toss doesn't care what the first one showed, so the branch probabilities stay the same. But if you're pulling cards without replacement, the second draw depends on what you pulled first, so the branches shrink or shift to match what's left. Keep that replacement rule in mind and you'll be fine. Now let's see it in action."

class M10ProbabilityConditionalTreesWithoutReplacementScene(Scene):
    def construct(self) -> None:
        title = Text('Probability Conditional Trees Without Replacement', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at how to handle multi-step experiments using\ntree diagrams and arrays, especially when one event depends on another.\nNext, arrays. If you're flipping a coin twice, the second toss doesn't\ncare what the first one showed, so the branch probabilities stay the\nsame.", "Let's start with tree diagrams. Imagine a grid with the outcomes of one\nvariable running down the side and the outcomes of the other running\nacross the top, so every cell is a unique combination. But if you're\npulling cards without replacement, the second draw depends on what you\npulled first, so the branches shrink or shift to match what's left.", "Think of a tree as a branching path where each fork represents one\npossible outcome at a particular step, and the labels on the branches\nshow the probabilities. Arrays are super handy when both things you're\ntracking are categories. Keep that replacement rule in mind and you'll\nbe fine.", "You multiply along any single path to find the chance of that whole\nsequence, and when several paths end in the same result, you add those\nprobabilities together. Finally, the big idea, independent versus\ndependent. Now let's see it in action."]
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
