"""Transcript-faithful Manim scene for model (m10-algebra-linear-eq)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = 'In this lesson we\'ll look at how to turn a word problem into a simple linear equation and actually answer the question it asks. The trick is to slow down and set things up carefully before you start solving. First, decide what the unknown is, and define it in words, like, let x be the number of tickets, or let x be the amount of money Alice started with. Then go through the problem sentence by sentence and translate each piece into an expression or an equation. Once you have an equation with just one variable, you solve it the usual way. But here\'s the part students often forget: once you\'ve got a number, put it back into the original context and answer in words, with the right units. So instead of just saying x equals twelve, you\'d say, Alice started with twelve dollars. Spotting the right phrasing really helps. Things like "five more than twice a number is seventeen" just means twice the number, plus five, equals seventeen. Or, after spending some money, she has thirty dollars left, so the starting amount minus what she spent equals thirty. Now let\'s see it in action.'

class M10AlgebraLinearEqModelScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Linear Eq Model', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ['In this lesson we\'ll look at how to turn a word problem into a simple\nlinear equation and actually answer the question it asks. Once you have\nan equation with just one variable, you solve it the usual way. Things\nlike "five more than twice a number is seventeen" just means twice the\nnumber, plus five, equals seventeen.', "The trick is to slow down and set things up carefully before you start\nsolving. But here's the part students often forget: once you've got a\nnumber, put it back into the original context and answer in words, with\nthe right units. Or, after spending some money, she has thirty dollars\nleft, so the starting amount minus what she spent equals thirty.", "First, decide what the unknown is, and define it in words, like, let x\nbe the number of tickets, or let x be the amount of money Alice started\nwith. So instead of just saying x equals twelve, you'd say, Alice\nstarted with twelve dollars. Now let's see it in action.", 'Then go through the problem sentence by sentence and translate each\npiece into an expression or an equation. Spotting the right phrasing\nreally helps.']
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
