"""Transcript-faithful Manim scene for grouping-in-pairs (m10-algebra-factorisation)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at grouping in pairs, a neat trick when no single factor is shared by every term. The idea is simple: instead of forcing one factor out of everything, you regroup the terms into two pairs, and each pair gets its own factor. Here's the recipe. First, re-arrange the terms so that each pair shares something in common. Next, factor each pair separately. Now here's the magic step: those two pair-factors should both contain the same bracket, and you pull that common bracket out front. Whatever's left inside each pair multiplies together to form the second bracket. For example, if you have x times the quantity x plus one, plus two times the same quantity x plus one, the bracket x plus one is shared, so it comes out, leaving x plus two behind. Think of the bracket as a single object you're sliding out. If your pairs don't seem to work at first, try swapping partners, since a different grouping might reveal the matching bracket. Now let's see it in action with a real problem."

class M10AlgebraFactorisationGroupingInPairsScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Factorisation Grouping In Pairs', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at grouping in pairs, a neat trick when no\nsingle factor is shared by every term. Next, factor each pair\nseparately. Think of the bracket as a single object you're sliding out.", "The idea is simple: instead of forcing one factor out of everything, you\nregroup the terms into two pairs, and each pair gets its own factor. Now\nhere's the magic step: those two pair-factors should both contain the\nsame bracket, and you pull that common bracket out front. If your pairs\ndon't seem to work at first, try swapping partners, since a different\ngrouping might reveal the matching bracket.", "Here's the recipe. Whatever's left inside each pair multiplies together\nto form the second bracket. Now let's see it in action with a real\nproblem.", 'First, re-arrange the terms so that each pair shares something in\ncommon. For example, if you have x times the quantity x plus one, plus\ntwo times the same quantity x plus one, the bracket x plus one is\nshared, so it comes out, leaving x plus two behind.']
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
