"""Transcript-faithful Manim scene for rearrange (m10-algebra-formulas)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at rearranging formulas so a chosen variable stands alone on one side. Think of it as tidying up an equation so it answers the exact question you want to ask. The idea is simple. You do to one side exactly what you undo on the other, using inverse operations.\n\nHere's the recipe. If a term is being added, subtract it from both sides. If something is being multiplied, divide both sides by it. If a variable is raised to a power, take the matching root to undo it. You just keep peeling off the layers, one operation at a time, until the variable you're after is sitting by itself.\n\nAlways double-check by substituting a test value back into both the original and the rearranged formula. They should give the same answer every time. If they don't, you've missed a step, so go back and look again.\n\nRemember, rearranging a formula is really just the same skill you use when you solve an equation, you're just being a bit more careful to keep the formula balanced.\n\nNow let's see it in action."

class M10AlgebraFormulasRearrangeScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Formulas Rearrange', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at rearranging formulas so a chosen variable\nstands alone on one side. Here's the recipe. You just keep peeling off\nthe layers, one operation at a time, until the variable you're after is\nsitting by itself. Remember, rearranging a formula is really just the\nsame skill you use when you solve an equation, you're just being a bit\nmore careful to keep the formula balanced.", "Think of it as tidying up an equation so it answers the exact question\nyou want to ask. If a term is being added, subtract it from both sides.\nAlways double-check by substituting a test value back into both the\noriginal and the rearranged formula. Now let's see it in action.", 'The idea is simple. If something is being multiplied, divide both sides\nby it. They should give the same answer every time.', "You do to one side exactly what you undo on the other, using inverse\noperations. If a variable is raised to a power, take the matching root\nto undo it. If they don't, you've missed a step, so go back and look\nagain."]
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
