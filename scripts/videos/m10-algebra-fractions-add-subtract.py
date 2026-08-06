"""Transcript-faithful Manim scene for add-subtract (m10-algebra-fractions)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at adding and subtracting algebraic fractions, and the good news is they follow exactly the same rules as the number fractions you already know. So when two fractions already share the same denominator, all you do is add or subtract their top numbers, the numerators, and keep that denominator the same. Easy. The only tricky bit is when the denominators are different. In that case, you have to pause and find the lowest common denominator first, which just means the smallest number, or expression, that both denominators divide neatly into. Once you've got it, you rewrite each fraction so it sits over that common denominator, and then you can go back to the simple rule of adding the numerators on top. Quick example to make it stick. Say we had x over three plus two over five. The lowest common denominator is fifteen, so we turn x over three into five x over fifteen, and two over five into six over fifteen, then combine them to get five x plus six over fifteen. Same idea, just with letters. Now let's see it in action with a worked example."

class M10AlgebraFractionsAddSubtractScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Fractions Add Subtract', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at adding and subtracting algebraic\nfractions, and the good news is they follow exactly the same rules as\nthe number fractions you already know. In that case, you have to pause\nand find the lowest common denominator first, which just means the\nsmallest number, or expression, that both denominators divide neatly\ninto. The lowest common denominator is fifteen, so we turn x over three\ninto five x over fifteen, and two over five into six over fifteen, then\ncombine them to get five x plus six over fifteen.", "So when two fractions already share the same denominator, all you do is\nadd or subtract their top numbers, the numerators, and keep that\ndenominator the same. Once you've got it, you rewrite each fraction so\nit sits over that common denominator, and then you can go back to the\nsimple rule of adding the numerators on top. Same idea, just with\nletters.", "Easy. Quick example to make it stick. Now let's see it in action with a\nworked example.", 'The only tricky bit is when the denominators are different. Say we had x\nover three plus two over five.']
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
