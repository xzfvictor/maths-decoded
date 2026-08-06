"""Transcript-faithful Manim scene for substitution (m10-algebra-simultaneous)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at the substitution method for solving simultaneous linear equations. The idea is really simple, and once you get it, you'll use it over and over. First, you take one of the two equations and isolate one of the variables on its own. In other words, you rearrange it so that one variable equals some expression involving the other variable. For example, if one equation already shows y equals something in terms of x, perfect — you're already halfway there. Next, you take that expression and substitute it into the other equation, replacing the isolated variable wherever it appears. That leaves you with a single equation in just one variable, which you can solve using normal algebra. Once you've found the value of that variable, you back-substitute it into your first rearranged equation to find the value of the other one. So when is substitution the best choice? It's fastest when one equation already has a variable sitting alone on one side, or when one of the coefficients is just one, because that makes isolating that variable really easy. Now let's see it in action."

class M10AlgebraSimultaneousSubstitutionScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Simultaneous Substitution', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at the substitution method for solving\nsimultaneous linear equations. For example, if one equation already\nshows y equals something in terms of x, perfect — you're already halfway\nthere. So when is substitution the best choice?", "The idea is really simple, and once you get it, you'll use it over and\nover. Next, you take that expression and substitute it into the other\nequation, replacing the isolated variable wherever it appears. It's\nfastest when one equation already has a variable sitting alone on one\nside, or when one of the coefficients is just one, because that makes\nisolating that variable really easy.", "First, you take one of the two equations and isolate one of the\nvariables on its own. That leaves you with a single equation in just one\nvariable, which you can solve using normal algebra. Now let's see it in\naction.", "In other words, you rearrange it so that one variable equals some\nexpression involving the other variable. Once you've found the value of\nthat variable, you back-substitute it into your first rearranged\nequation to find the value of the other one."]
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
