"""Transcript-faithful Manim scene for refine (m10-algebra-numerical)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at a simple but powerful trick for solving equations when you can't just draw the graph cleanly. It's called guess-check-and-refine, and it's exactly what it sounds like. You start with a rough estimate of the variable, then check how close it gets you, then refine your guess and try again. Think of it like tuning a radio dial. You turn it a little, listen, and keep adjusting until the signal locks in. So step one, guess a value. Step two, check what each side of the equation gives you, or check the value of the function at that point. Step three, refine: if your function value came out too low, your guess was probably too low, so nudge it higher. Too high? Go lower. Repeat until you're close enough to call it done. Now there's a neat shortcut called bisection. If your function is negative at one end of an interval and positive at the other, you know a root lives somewhere in between. So you test the midpoint, and whichever half the root is in, you keep that half and halve the interval again. It zooms in fast. One last thing, remember that refining from one guess only finds one root. If the graph might cross the axis more than once, scan the whole picture first to spot them all. Now let's see it in action."

class M10AlgebraNumericalRefineScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Numerical Refine', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at a simple but powerful trick for solving\nequations when you can't just draw the graph cleanly. You turn it a\nlittle, listen, and keep adjusting until the signal locks in. Too high?\nIf your function is negative at one end of an interval and positive at\nthe other, you know a root lives somewhere in between. If the graph\nmight cross the axis more than once, scan the whole picture first to\nspot them all.", "It's called guess-check-and-refine, and it's exactly what it sounds\nlike. So step one, guess a value. Go lower. So you test the midpoint,\nand whichever half the root is in, you keep that half and halve the\ninterval again. Now let's see it in action.", "You start with a rough estimate of the variable, then check how close it\ngets you, then refine your guess and try again. Step two, check what\neach side of the equation gives you, or check the value of the function\nat that point. Repeat until you're close enough to call it done. It\nzooms in fast.", "Think of it like tuning a radio dial. Step three, refine: if your\nfunction value came out too low, your guess was probably too low, so\nnudge it higher. Now there's a neat shortcut called bisection. One last\nthing, remember that refining from one guess only finds one root."]
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
