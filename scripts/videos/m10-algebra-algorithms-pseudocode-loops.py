"""Transcript-faithful Manim scene for pseudocode-loops (m10-algebra-algorithms)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at pseudocode and loops, the building blocks of any algorithm. Pseudocode is just a simple way to describe what an algorithm does without getting tangled up in the exact rules of any one programming language. The basic building blocks are pretty straightforward. First, there's assignment, which means storing a value in a variable so you can use it later. Then come loops, which let you repeat actions. One type of loop runs once for each value in a range, and another type keeps repeating as long as a condition stays true. Conditionals are the third piece, letting your algorithm branch one way or another depending on whether a test comes out true or false. Finally, when you want to understand what an algorithm does, you trace it, which means keeping a little table of how each variable changes as each line runs. Now let's see it in action."

class M10AlgebraAlgorithmsPseudocodeLoopsScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Algorithms Pseudocode Loops', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at pseudocode and loops, the building blocks\nof any algorithm. Then come loops, which let you repeat actions. Now\nlet's see it in action.", 'Pseudocode is just a simple way to describe what an algorithm does\nwithout getting tangled up in the exact rules of any one programming\nlanguage. One type of loop runs once for each value in a range, and\nanother type keeps repeating as long as a condition stays true.', 'The basic building blocks are pretty straightforward. Conditionals are\nthe third piece, letting your algorithm branch one way or another\ndepending on whether a test comes out true or false.', "First, there's assignment, which means storing a value in a variable so\nyou can use it later. Finally, when you want to understand what an\nalgorithm does, you trace it, which means keeping a little table of how\neach variable changes as each line runs."]
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
