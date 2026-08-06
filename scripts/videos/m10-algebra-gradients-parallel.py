"""Transcript-faithful Manim scene for parallel (m10-algebra-gradients)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at parallel lines. Picture two straight lines that never meet, no matter how far you extend them. That is what parallel means. The trick to spotting them is simple: parallel lines always have the same slope, but they sit at different heights on the graph, so their y intercepts are different. Think of two train tracks running side by side, perfectly matching in steepness but slightly offset. Now, if you know the equation of one line and you want the equation of a line parallel to it, you just keep the same gradient and change the y intercept. To find that new y intercept, use the point slope form. You plug in the coordinates of a point the new line passes through, along with the shared gradient, and solve for the y intercept. That gives you the full equation. On a graph, any two non-intersecting straight lines you can see are parallel, and you can confirm it by checking that their gradients match while their y intercepts differ. Now let's see it in action."

class M10AlgebraGradientsParallelScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Gradients Parallel', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at parallel lines. Think of two train tracks\nrunning side by side, perfectly matching in steepness but slightly\noffset. That gives you the full equation.", 'Picture two straight lines that never meet, no matter how far you extend\nthem. Now, if you know the equation of one line and you want the\nequation of a line parallel to it, you just keep the same gradient and\nchange the y intercept. On a graph, any two non-intersecting straight\nlines you can see are parallel, and you can confirm it by checking that\ntheir gradients match while their y intercepts differ.', "That is what parallel means. To find that new y intercept, use the point\nslope form. Now let's see it in action.", 'The trick to spotting them is simple: parallel lines always have the\nsame slope, but they sit at different heights on the graph, so their y\nintercepts are different. You plug in the coordinates of a point the new\nline passes through, along with the shared gradient, and solve for the y\nintercept.']
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
