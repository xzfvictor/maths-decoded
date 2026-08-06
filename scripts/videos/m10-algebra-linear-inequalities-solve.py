"""Transcript-faithful Manim scene for solve (m10-algebra-linear-inequalities)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at solving linear inequalities, which are just comparisons between two expressions using symbols like less than, greater than, less than or equal to, and greater than or equal to.\n\nThe good news is that you solve them almost exactly like equations, by isolating the variable using inverse operations to undo what's been done to it. For example, if you have three times x less than twelve, you'd divide both sides by three to get x less than four. Straightforward so far.\n\nBut here's the one critical rule you have to remember. Whenever you multiply or divide both sides of an inequality by a negative number, the inequality symbol flips around. So if you had negative three times x less than twelve, and you divide by negative three, you'd flip the symbol and get x greater than negative four.\n\nThe same rule applies when you multiply by a negative. For instance, negative two times x greater than six becomes x less than negative three, because you flipped it after dividing.\n\nNow let's see it in action."

class M10AlgebraLinearInequalitiesSolveScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Linear Inequalities Solve', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at solving linear inequalities, which are\njust comparisons between two expressions using symbols like less than,\ngreater than, less than or equal to, and greater than or equal to. But\nhere's the one critical rule you have to remember. For instance,\nnegative two times x greater than six becomes x less than negative\nthree, because you flipped it after dividing.", "The good news is that you solve them almost exactly like equations, by\nisolating the variable using inverse operations to undo what's been done\nto it. Whenever you multiply or divide both sides of an inequality by a\nnegative number, the inequality symbol flips around. Now let's see it in\naction.", "For example, if you have three times x less than twelve, you'd divide\nboth sides by three to get x less than four. So if you had negative\nthree times x less than twelve, and you divide by negative three, you'd\nflip the symbol and get x greater than negative four.", 'Straightforward so far. The same rule applies when you multiply by a\nnegative.']
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
