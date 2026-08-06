"""Transcript-faithful Manim scene for arrays-matrices (m10-algebra-algorithms)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at three really handy data structures that show up everywhere in algorithms. First, arrays. Think of an array as a simple list of values lined up in a row, where each value sits at its own numbered slot starting from zero. You walk through an array using a loop, and arrays are perfect for storing sequences like a list of numbers or names. Next, matrices, which are basically arrays in two dimensions. Imagine a grid with rows and columns, where you reach into any cell by giving its row and column. Matrices aren't just for storing tables though. They're also a way to describe geometric transformations. Multiplying a point by a translation matrix shifts it across the plane, and other matrices can rotate or reflect shapes. Finally, pointers. A pointer doesn't hold a value itself, it just holds the address of another element somewhere in memory. So when you read or write through a pointer, you're really changing that underlying thing. Pointers are what make linked lists, trees, and graphs possible. Now let's see it in action."

class M10AlgebraAlgorithmsArraysMatricesScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Algorithms Arrays Matrices', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at three really handy data structures that\nshow up everywhere in algorithms. Next, matrices, which are basically\narrays in two dimensions. Multiplying a point by a translation matrix\nshifts it across the plane, and other matrices can rotate or reflect\nshapes. Pointers are what make linked lists, trees, and graphs possible.", "First, arrays. Imagine a grid with rows and columns, where you reach\ninto any cell by giving its row and column. Finally, pointers. Now let's\nsee it in action.", "Think of an array as a simple list of values lined up in a row, where\neach value sits at its own numbered slot starting from zero. Matrices\naren't just for storing tables though. A pointer doesn't hold a value\nitself, it just holds the address of another element somewhere in\nmemory.", "You walk through an array using a loop, and arrays are perfect for\nstoring sequences like a list of numbers or names. They're also a way to\ndescribe geometric transformations. So when you read or write through a\npointer, you're really changing that underlying thing."]
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
