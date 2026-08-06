"""Transcript-faithful Manim scene for proportion (m10-measurement-scaling)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = 'In this lesson, we\'ll look at direct and inverse proportion, two ideas that show up everywhere in Methods. Let\'s start with direct proportion. Imagine two quantities, say y and x, and notice that whenever x doubles, y doubles too, and whenever x halves, y halves. That relationship is direct proportion. It means y equals some constant k multiplied by x. The trick is, you only need one pair of values to find k. Just divide y by x, and that\'s your k. Then you can use it to find y for any other x. The wording clue is usually "more x, more y."\n\nNow, inverse proportion works the other way. Here, as x gets bigger, y gets smaller, like "more x, less y." The rule is that y equals the same constant k, but this time divided by x. The handy shortcut is that the product of x and y is always equal to k, so if you know one pair, you can find any other pair by keeping that product fixed. \n\nSo remember, direct means multiply by a constant, inverse means a constant divided by x, and one good pair unlocks every other. Now let\'s see it in action.'

class M10MeasurementScalingProportionScene(Scene):
    def construct(self) -> None:
        title = Text('Measurement Scaling Proportion', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ['In this lesson, we\'ll look at direct and inverse proportion, two ideas\nthat show up everywhere in Methods. It means y equals some constant k\nmultiplied by x. The wording clue is usually "more x, more y."  Now,\ninverse proportion works the other way. Now let\'s see it in action.', 'Let\'s start with direct proportion. The trick is, you only need one pair\nof values to find k. Here, as x gets bigger, y gets smaller, like "more\nx, less y." The rule is that y equals the same constant k, but this time\ndivided by x.', "Imagine two quantities, say y and x, and notice that whenever x doubles,\ny doubles too, and whenever x halves, y halves. Just divide y by x, and\nthat's your k. The handy shortcut is that the product of x and y is\nalways equal to k, so if you know one pair, you can find any other pair\nby keeping that product fixed.", 'That relationship is direct proportion. Then you can use it to find y\nfor any other x. So remember, direct means multiply by a constant,\ninverse means a constant divided by x, and one good pair unlocks every\nother.']
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
