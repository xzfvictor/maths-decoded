"""Transcript-faithful Manim scene for pythagoras-trig (m10-measurement-trig)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson we'll look at the two essential formula sets you need for any right-triangle problem: Pythagoras' theorem and the three trigonometric ratios. Picture a right-angled triangle, with the right angle sitting opposite the longest side, which we call the hypotenuse, and the other two sides labelled a and b, with an angle theta squeezed between side a and the hypotenuse. With Pythagoras' theorem, if you know any two sides, you can always find the third, because the square of the hypotenuse equals the square of side a plus the square of side b. For the trig ratios, the trick is simply to match the side you know with the side you want. If you know the adjacent side and need the opposite side, use tangent, which is opposite over adjacent. If you know the hypotenuse and need the opposite side, use sine, which is opposite over hypotenuse. And if you know the hypotenuse and need the adjacent side, use cosine, which is adjacent over hypotenuse. So really, every right-triangle question comes down to picking the right formula from these two sets. Now let's see it in action."

class M10MeasurementTrigPythagorasTrigScene(Scene):
    def construct(self) -> None:
        title = Text('Measurement Trig Pythagoras Trig', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson we'll look at the two essential formula sets you need for\nany right-triangle problem: Pythagoras' theorem and the three\ntrigonometric ratios. If you know the adjacent side and need the\nopposite side, use tangent, which is opposite over adjacent. Now let's\nsee it in action.", 'Picture a right-angled triangle, with the right angle sitting opposite\nthe longest side, which we call the hypotenuse, and the other two sides\nlabelled a and b, with an angle theta squeezed between side a and the\nhypotenuse. If you know the hypotenuse and need the opposite side, use\nsine, which is opposite over hypotenuse.', "With Pythagoras' theorem, if you know any two sides, you can always find\nthe third, because the square of the hypotenuse equals the square of\nside a plus the square of side b. And if you know the hypotenuse and\nneed the adjacent side, use cosine, which is adjacent over hypotenuse.", 'For the trig ratios, the trick is simply to match the side you know with\nthe side you want. So really, every right-triangle question comes down\nto picking the right formula from these two sets.']
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
