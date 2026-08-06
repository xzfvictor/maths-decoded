"""Transcript-faithful Manim scene for completing-square (m10-algebra-quadratics)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at a neat trick called completing the square, which turns a quadratic into a perfect square plus a leftover number. Here's the idea. If you've got something like x squared plus bx plus c, you take half of b, square it, and use that to rewrite the whole thing as a bracket squared, with a small adjustment to the constant. So x squared plus bx plus c becomes the quantity x plus b over two, all squared, plus c minus b squared over four. That leftover piece is what makes it not quite a perfect square yet, but once you move it aside, the bracket part is exactly square. To actually solve, you move that constant to the other side of the equation, complete the square on the left so it looks like a bracket squared equals some number, then take the square root of both sides, remembering there are two answers, one positive and one negative. From there you just isolate x and you're done. Now let's see it in action."

class M10AlgebraQuadraticsCompletingSquareScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Quadratics Completing Square', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at a neat trick called completing the square,\nwhich turns a quadratic into a perfect square plus a leftover number.\nThat leftover piece is what makes it not quite a perfect square yet, but\nonce you move it aside, the bracket part is exactly square.", "Here's the idea. To actually solve, you move that constant to the other\nside of the equation, complete the square on the left so it looks like a\nbracket squared equals some number, then take the square root of both\nsides, remembering there are two answers, one positive and one negative.", "If you've got something like x squared plus bx plus c, you take half of\nb, square it, and use that to rewrite the whole thing as a bracket\nsquared, with a small adjustment to the constant. From there you just\nisolate x and you're done.", "So x squared plus bx plus c becomes the quantity x plus b over two, all\nsquared, plus c minus b squared over four. Now let's see it in action."]
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
