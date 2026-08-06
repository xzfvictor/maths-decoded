"""Transcript-faithful Manim scene for pointers (m10-algebra-algorithms)."""
from manim import *
from _common import BAND_CHART_CENTER, GREEN_OK, RED_REJECT, animate_intro, beat_group

SCRIPT = "In this lesson, we'll look at pointers, which are a fundamental idea in algorithms and data structures. A pointer is just a variable that holds the address of another element, like a slot in an array or a node in a linked list, rather than holding an actual value itself. Think of it like a sticky note with someone's name on it that points you to where they really are. So why do we use them? In linked lists, trees, and graphs, each node stores some data along with a pointer to the next node, which lets us chain things together. Pointers also let us pass things by reference, meaning when you change something through a pointer, you're actually changing the original. And they let us work with memory that's allocated while the program is running. Now, the two things you do with a pointer are reading and writing. Reading means looking at the value the pointer points to, while writing means changing that value through the pointer. The big idea is simple: a pointer is one step removed from the value itself. Now let's see it in action."

class PointersScene(Scene):
    def construct(self) -> None:
        animate_intro(self, 'Algebra Algorithms Pointers', "Follow the narration, then try the idea yourself.", hold=0.8)
        sections = ["In this lesson, we'll look at pointers, which are a fundamental idea in algorithms and data structures. A pointer is just a variable that holds the address of another element, like a slot in an array or a node in a linked list, rather than holding an actual value itself. Think of it like a sticky note with someone's name on it that points you to where they really are. So why do we use them? In linked lists, trees, and graphs, each node stores some data along with a pointer to the next node, which lets us chain things together. Pointers also let us pass things by reference, meaning when you change something through a pointer, you're actually changing the original. And they let us work with memory that's allocated while the program is running. Now, the two things you do with a pointer are reading and writing. Reading means looking at the value the pointer points to, while writing means changing that value through the pointer. The big idea is simple: a pointer is one step removed from the value itself. Now let's see it in action."]
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
