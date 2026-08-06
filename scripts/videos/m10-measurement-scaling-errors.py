"""Transcript-faithful Manim scene for errors (m10-measurement-scaling)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at how uncertainty travels through your calculations. Every measurement you make has some wiggle room, and that wiggle room doesn't just disappear when you start doing maths with the numbers. So the big question is, what happens when you add, subtract, multiply, or divide measurements that are all a bit uncertain? Let's break it into two cases. First, when you add or subtract measurements, the absolute errors add together. Absolute error just means the size of the uncertainty, like plus or minus a certain amount. So if one measurement is uncertain by two units and another is uncertain by three, the sum is uncertain by about five. Makes sense, right? Second, when you multiply or divide, it's the relative errors that add. Relative error is the uncertainty compared to the size of the measurement, usually written as a percentage. So a five percent uncertainty on one thing and a three percent uncertainty on another gives roughly eight percent uncertainty on the product or quotient. And here's a handy rule of thumb for reporting your final answer. Match the precision of the least precise measurement you started with. Now let's see it in action."

class M10MeasurementScalingErrorsScene(Scene):
    def construct(self) -> None:
        title = Text('Measurement Scaling Errors', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at how uncertainty travels through your\ncalculations. First, when you add or subtract measurements, the absolute\nerrors add together. Second, when you multiply or divide, it's the\nrelative errors that add. Match the precision of the least precise\nmeasurement you started with.", "Every measurement you make has some wiggle room, and that wiggle room\ndoesn't just disappear when you start doing maths with the numbers.\nAbsolute error just means the size of the uncertainty, like plus or\nminus a certain amount. Relative error is the uncertainty compared to\nthe size of the measurement, usually written as a percentage. Now let's\nsee it in action.", 'So the big question is, what happens when you add, subtract, multiply,\nor divide measurements that are all a bit uncertain? So if one\nmeasurement is uncertain by two units and another is uncertain by three,\nthe sum is uncertain by about five. So a five percent uncertainty on one\nthing and a three percent uncertainty on another gives roughly eight\npercent uncertainty on the product or quotient.', "Let's break it into two cases. Makes sense, right? And here's a handy\nrule of thumb for reporting your final answer."]
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
