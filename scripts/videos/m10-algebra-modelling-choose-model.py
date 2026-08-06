"""Transcript-faithful Manim scene for choose-model (m10-algebra-modelling)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how to pick the right function family when you're modelling a set of numbers. The big idea is simple, just look at how consecutive values change, and that change tells you what kind of model fits. First up, the constant difference test. Subtract each term from the one after it. If those differences are all the same number, you've got a linear model, the classic straight line. Next, the constant second difference test. If the first differences aren't constant, take the difference of the differences. If those second differences are constant, then your data follows a quadratic shape, a parabola. Finally, the constant ratio test. Instead of subtracting, divide each term by the one before it. If that ratio stays the same every step, you're dealing with an exponential model, where values grow by multiplying. So remember, subtract for linear, subtract again for quadratic, and divide for exponential. Now let's see it in action."

class M10AlgebraModellingChooseModelScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Modelling Choose Model', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how to pick the right function family when\nyou're modelling a set of numbers. If those differences are all the same\nnumber, you've got a linear model, the classic straight line. Finally,\nthe constant ratio test. Now let's see it in action.", 'The big idea is simple, just look at how consecutive values change, and\nthat change tells you what kind of model fits. Next, the constant second\ndifference test. Instead of subtracting, divide each term by the one\nbefore it.', "First up, the constant difference test. If the first differences aren't\nconstant, take the difference of the differences. If that ratio stays\nthe same every step, you're dealing with an exponential model, where\nvalues grow by multiplying.", 'Subtract each term from the one after it. If those second differences\nare constant, then your data follows a quadratic shape, a parabola. So\nremember, subtract for linear, subtract again for quadratic, and divide\nfor exponential.']
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
