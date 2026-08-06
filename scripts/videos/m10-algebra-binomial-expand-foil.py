"""Transcript-faithful Manim scene for expand-foil (m10-algebra-binomial)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at expanding binomial products using a handy little trick called FOIL. A binomial is just two terms added together, like x plus three, and a binomial product happens when you multiply two binomials. The most common pattern is x plus m, multiplied by x plus n, and the result is always a monic quadratic, meaning the square of x is the leading term. FOIL is a memory aid with four steps. First, you multiply the first terms of each bracket. Outer means the first term of the first bracket times the second term of the second bracket. Inner flips that, taking the second term of the first bracket times the first of the second. Last multiplies the two second terms. When you add everything up, the inner and outer terms combine into a single middle term, so four pieces collapse neatly into three. The general case works the same way for any pair of two-term brackets, just with different letters. Four terms in, three or fewer terms out. Now let's see it in action."

class M10AlgebraBinomialExpandFoilScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Binomial Expand Foil', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at expanding binomial products using a handy\nlittle trick called FOIL. First, you multiply the first terms of each\nbracket. When you add everything up, the inner and outer terms combine\ninto a single middle term, so four pieces collapse neatly into three.", 'A binomial is just two terms added together, like x plus three, and a\nbinomial product happens when you multiply two binomials. Outer means\nthe first term of the first bracket times the second term of the second\nbracket. The general case works the same way for any pair of two-term\nbrackets, just with different letters.', 'The most common pattern is x plus m, multiplied by x plus n, and the\nresult is always a monic quadratic, meaning the square of x is the\nleading term. Inner flips that, taking the second term of the first\nbracket times the first of the second. Four terms in, three or fewer\nterms out.', "FOIL is a memory aid with four steps. Last multiplies the two second\nterms. Now let's see it in action."]
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
