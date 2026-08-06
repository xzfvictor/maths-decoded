"""Transcript-faithful Manim scene for pseudocode-loops (m10-algebra-algorithms)."""
from manim import *
from _common import BAND_CHART_CENTER, GREEN_OK, RED_REJECT, animate_intro, beat_group

SCRIPT = "In this lesson, we'll look at pseudocode and loops, the building blocks of any algorithm. Pseudocode is just a simple way to describe what an algorithm does without getting tangled up in the exact rules of any one programming language. The basic building blocks are pretty straightforward. First, there's assignment, which means storing a value in a variable so you can use it later. Then come loops, which let you repeat actions. One type of loop runs once for each value in a range, and another type keeps repeating as long as a condition stays true. Conditionals are the third piece, letting your algorithm branch one way or another depending on whether a test comes out true or false. Finally, when you want to understand what an algorithm does, you trace it, which means keeping a little table of how each variable changes as each line runs. Now let's see it in action."

class PseudocodeLoopsScene(Scene):
    def construct(self) -> None:
        animate_intro(self, 'Algebra Algorithms Pseudocode Loops', "Follow the narration, then try the idea yourself.", hold=0.8)
        sections = ["In this lesson, we'll look at pseudocode and loops, the building blocks of any algorithm. Pseudocode is just a simple way to describe what an algorithm does without getting tangled up in the exact rules of any one programming language. The basic building blocks are pretty straightforward. First, there's assignment, which means storing a value in a variable so you can use it later. Then come loops, which let you repeat actions. One type of loop runs once for each value in a range, and another type keeps repeating as long as a condition stays true. Conditionals are the third piece, letting your algorithm branch one way or another depending on whether a test comes out true or false. Finally, when you want to understand what an algorithm does, you trace it, which means keeping a little table of how each variable changes as each line runs. Now let's see it in action."]
        for index, words in enumerate(sections):
            beat = Text(words, font_size=24, line_spacing=0.8)
            beat.set_width(min(10.5, beat.width))
            beat.move_to(BAND_CHART_CENTER)
            bg = BackgroundRectangle(beat, color=BLACK, fill_opacity=1, buff=0.28)
            bg.move_to(beat.get_center())
            card = beat_group(bg, beat)
            self.play(FadeIn(bg, run_time=0.35), FadeIn(beat, run_time=0.8))
            self.wait(1.4)
            self.play(FadeOut(card, run_time=0.6))
        final = Text("Key idea", font_size=32, color=GREEN_OK).move_to(DOWN * 1.7)
        final_bg = BackgroundRectangle(final, color=BLACK, fill_opacity=1, buff=0.25)
        final_bg.move_to(final.get_center())
        final_box = SurroundingRectangle(final, color=GREEN_OK, buff=0.3)
        self.play(FadeIn(final_bg), Write(final), Create(final_box))
        self.wait(120)
