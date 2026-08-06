"""Transcript-faithful Manim scene for conditional-language (m10-probability-conditional)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = 'In this lesson, we\'ll untangle two phrases that look similar but actually flip the direction of the question. First, imagine someone says "the probability of A given B." That means B has already happened, and you want the chance of A next. You\'re shrinking the world down to just the cases where B occurred, and asking how often A shows up inside that smaller world. Second, there\'s the phrase "the probability of B of A." That sounds almost the same, but it reverses the fraction. Here you\'re starting with all the A\'s, and asking what slice of them were B. So "given" shrinks to B first, while "of" shrinks to A first. A really common mistake is swapping these two. The famous medical test trap is a perfect example. A test that\'s ninety-nine percent accurate can still flag loads of healthy people when the disease is rare, because the condition points the wrong way. Keep the sample space shrinking in mind, and you\'ll avoid that trap. Now let\'s see it in action.'

class M10ProbabilityConditionalConditionalLanguageScene(Scene):
    def construct(self) -> None:
        title = Text('Probability Conditional Conditional Language', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll untangle two phrases that look similar but\nactually flip the direction of the question. Here you're starting with\nall the A's, and asking what slice of them were B. A test that's ninety-\nnine percent accurate can still flag loads of healthy people when the\ndisease is rare, because the condition points the wrong way.", 'First, imagine someone says "the probability of A given B." That means B\nhas already happened, and you want the chance of A next. So "given"\nshrinks to B first, while "of" shrinks to A first. Keep the sample space\nshrinking in mind, and you\'ll avoid that trap.', "You're shrinking the world down to just the cases where B occurred, and\nasking how often A shows up inside that smaller world. A really common\nmistake is swapping these two. Now let's see it in action.", 'Second, there\'s the phrase "the probability of B of A." That sounds\nalmost the same, but it reverses the fraction. The famous medical test\ntrap is a perfect example.']
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
