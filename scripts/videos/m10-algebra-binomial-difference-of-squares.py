"""Transcript-faithful Manim scene for difference-of-squares (m10-algebra-binomial)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at the difference of squares, one of the most useful patterns you'll ever learn for factorising. Here's the big idea to keep in your head: the square of some expression minus the square of another expression always factors neatly into the product of those two expressions, one with a minus and one with a plus. Whenever you spot one perfect square being taken away from another, you can write the answer straight down without hunting for clever number pairs. So why does it work? When you multiply those two brackets out using the standard first, outer, inner, last method, the two middle terms are opposites of each other, so they cancel out, and you're left with just the square of the first minus the square of the second. That's why the middle disappears every single time. The takeaway is to train your eyes to recognise two squares being subtracted, because the factorised form drops out instantly. Now let's see it in action."

class M10AlgebraBinomialDifferenceOfSquaresScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Binomial Difference Of Squares', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at the difference of squares, one of the most\nuseful patterns you'll ever learn for factorising. When you multiply\nthose two brackets out using the standard first, outer, inner, last\nmethod, the two middle terms are opposites of each other, so they cancel\nout, and you're left with just the square of the first minus the square\nof the second.", "Here's the big idea to keep in your head: the square of some expression\nminus the square of another expression always factors neatly into the\nproduct of those two expressions, one with a minus and one with a plus.\nThat's why the middle disappears every single time.", 'Whenever you spot one perfect square being taken away from another, you\ncan write the answer straight down without hunting for clever number\npairs. The takeaway is to train your eyes to recognise two squares being\nsubtracted, because the factorised form drops out instantly.', "So why does it work? Now let's see it in action."]
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
