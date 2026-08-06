"""Transcript-faithful Manim scene for graph (m10-algebra-linear-inequalities)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how to graph linear inequalities on a number line once you've solved them. There are really only two things to worry about: the circle at the boundary, and the direction of the ray. First, the circle. If your inequality uses less than or equal to, or greater than or equal to, you draw a closed, filled-in circle at the endpoint, because that endpoint is included in your solution. But if it's a strict less than or greater than, with no equals sign, then you draw an open circle, like a little ring, because the endpoint is not included. Next, the direction. Take an inequality like x is less than five. You put an open circle at five, and then draw a ray extending to the left, showing every smaller number is included. For x greater than or equal to negative two, you put a closed circle at negative two, with a ray stretching to the right. And why a ray? Because the inequality gives you infinitely many values, all the numbers past the boundary in that direction. Now let's see it in action."

class M10AlgebraLinearInequalitiesGraphScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Linear Inequalities Graph', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how to graph linear inequalities on a\nnumber line once you've solved them. But if it's a strict less than or\ngreater than, with no equals sign, then you draw an open circle, like a\nlittle ring, because the endpoint is not included. For x greater than or\nequal to negative two, you put a closed circle at negative two, with a\nray stretching to the right.", 'There are really only two things to worry about: the circle at the\nboundary, and the direction of the ray. Next, the direction. And why a\nray?', 'First, the circle. Take an inequality like x is less than five. Because\nthe inequality gives you infinitely many values, all the numbers past\nthe boundary in that direction.', "If your inequality uses less than or equal to, or greater than or equal\nto, you draw a closed, filled-in circle at the endpoint, because that\nendpoint is included in your solution. You put an open circle at five,\nand then draw a ray extending to the left, showing every smaller number\nis included. Now let's see it in action."]
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
