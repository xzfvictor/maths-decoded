"""Transcript-faithful Manim scene for pointers (m10-algebra-algorithms)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at pointers, which are a fundamental idea in algorithms and data structures. A pointer is just a variable that holds the address of another element, like a slot in an array or a node in a linked list, rather than holding an actual value itself. Think of it like a sticky note with someone's name on it that points you to where they really are. So why do we use them? In linked lists, trees, and graphs, each node stores some data along with a pointer to the next node, which lets us chain things together. Pointers also let us pass things by reference, meaning when you change something through a pointer, you're actually changing the original. And they let us work with memory that's allocated while the program is running. Now, the two things you do with a pointer are reading and writing. Reading means looking at the value the pointer points to, while writing means changing that value through the pointer. The big idea is simple: a pointer is one step removed from the value itself. Now let's see it in action."

class M10AlgebraAlgorithmsPointersScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Algorithms Pointers', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at pointers, which are a fundamental idea in\nalgorithms and data structures. In linked lists, trees, and graphs, each\nnode stores some data along with a pointer to the next node, which lets\nus chain things together. Reading means looking at the value the pointer\npoints to, while writing means changing that value through the pointer.", "A pointer is just a variable that holds the address of another element,\nlike a slot in an array or a node in a linked list, rather than holding\nan actual value itself. Pointers also let us pass things by reference,\nmeaning when you change something through a pointer, you're actually\nchanging the original. The big idea is simple: a pointer is one step\nremoved from the value itself.", "Think of it like a sticky note with someone's name on it that points you\nto where they really are. And they let us work with memory that's\nallocated while the program is running. Now let's see it in action.", 'So why do we use them? Now, the two things you do with a pointer are\nreading and writing.']
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
