"""Transcript-faithful Manim scene for substitute (m10-algebra-formulas)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how to plug numbers into a formula and get the right answer. A formula is just a rule that connects variables, and substitution means swapping those variables for the values you're given. The trick is to follow the order of operations carefully. That means brackets first, then powers like squaring a number, then multiplication and division, and finally addition and subtraction. Your calculator will do this automatically as long as you type the expression in properly, so pay attention to where the brackets go. One more thing, always check the units before you start. If a formula mixes things like kilometres and metres, or hours and minutes, convert everything to the same units first or your answer will be off. Once you've got that sorted, the substitution itself is usually pretty quick. Now let's see it in action with a worked example."

class M10AlgebraFormulasSubstituteScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Formulas Substitute', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how to plug numbers into a formula and get\nthe right answer. Your calculator will do this automatically as long as\nyou type the expression in properly, so pay attention to where the\nbrackets go. Now let's see it in action with a worked example.", "A formula is just a rule that connects variables, and substitution means\nswapping those variables for the values you're given. One more thing,\nalways check the units before you start.", 'The trick is to follow the order of operations carefully. If a formula\nmixes things like kilometres and metres, or hours and minutes, convert\neverything to the same units first or your answer will be off.', "That means brackets first, then powers like squaring a number, then\nmultiplication and division, and finally addition and subtraction. Once\nyou've got that sorted, the substitution itself is usually pretty quick."]
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
