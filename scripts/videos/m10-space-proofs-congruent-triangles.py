"""Transcript-faithful Manim scene for congruent-triangles (m10-space-proofs)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = 'Hey there! In this lesson we\'ll look at how to prove two triangles are congruent, which basically means showing they\'re identical in size and shape. The big idea is that you only need a few key pieces of information to lock everything else in. There are four quick tests you can pick from. The first is SSS, where all three pairs of sides match up. Next is SAS, where two sides match and so does the angle sitting right between them. Then there\'s AAS, where two angles match along with a side that\'s not between those angles. And finally RHS, which is for right triangles specifically, and that stands for a right angle, the hypotenuse, and one more side. Here\'s the really cool part: once you\'ve proven two triangles are congruent using any of these tests, you automatically get every other matching length and angle for free, free through a rule called CPCTC, or "corresponding parts of congruent triangles are congruent." So your game plan is simple. First, write down what the diagram already tells you. Then ask yourself which of the four tests fits those clues. Match the corresponding vertices, write your congruence statement, and the missing length or angle basically drops into your lap. Now let\'s see it in action.'

class M10SpaceProofsCongruentTrianglesScene(Scene):
    def construct(self) -> None:
        title = Text('Space Proofs Congruent Triangles', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ['Hey there! The first is SSS, where all three pairs of sides match up.\nHere\'s the really cool part: once you\'ve proven two triangles are\ncongruent using any of these tests, you automatically get every other\nmatching length and angle for free, free through a rule called CPCTC, or\n"corresponding parts of congruent triangles are congruent." So your game\nplan is simple. Now let\'s see it in action.', "In this lesson we'll look at how to prove two triangles are congruent,\nwhich basically means showing they're identical in size and shape. Next\nis SAS, where two sides match and so does the angle sitting right\nbetween them. First, write down what the diagram already tells you.", "The big idea is that you only need a few key pieces of information to\nlock everything else in. Then there's AAS, where two angles match along\nwith a side that's not between those angles. Then ask yourself which of\nthe four tests fits those clues.", 'There are four quick tests you can pick from. And finally RHS, which is\nfor right triangles specifically, and that stands for a right angle, the\nhypotenuse, and one more side. Match the corresponding vertices, write\nyour congruence statement, and the missing length or angle basically\ndrops into your lap.']
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
