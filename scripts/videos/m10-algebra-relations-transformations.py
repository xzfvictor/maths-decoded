"""Transcript-faithful Manim scene for transformations (m10-algebra-relations)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at how transformations work across every family of graphs, and the great news is the rules never change. First, vertical shifts. If you take a graph and add a number to the whole function, the whole picture slides up by that many units, or down if the number is negative. Next, horizontal shifts. When you replace x with x minus some number, the graph slides sideways the opposite way, so the graph moves to the right. Then we have vertical stretches. Multiplying the whole function by a number makes the graph taller if the number is bigger than one, or flatter if it's between zero and one, essentially scaling every height. Finally, reflections. Putting a negative sign out the front of the function flips the whole graph upside down across the x-axis, like a mirror image. The really powerful idea here is that once you know what the basic graph looks like, you can sketch any transformed version in seconds, without having to plot a single point from scratch. Now let's see it in action."

class M10AlgebraRelationsTransformationsScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Relations Transformations', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at how transformations work across every\nfamily of graphs, and the great news is the rules never change. When you\nreplace x with x minus some number, the graph slides sideways the\nopposite way, so the graph moves to the right. Putting a negative sign\nout the front of the function flips the whole graph upside down across\nthe x-axis, like a mirror image.", 'First, vertical shifts. Then we have vertical stretches. The really\npowerful idea here is that once you know what the basic graph looks\nlike, you can sketch any transformed version in seconds, without having\nto plot a single point from scratch.', "If you take a graph and add a number to the whole function, the whole\npicture slides up by that many units, or down if the number is negative.\nMultiplying the whole function by a number makes the graph taller if the\nnumber is bigger than one, or flatter if it's between zero and one,\nessentially scaling every height. Now let's see it in action.", 'Next, horizontal shifts. Finally, reflections.']
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
