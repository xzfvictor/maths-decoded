"""Transcript-faithful Manim scene for inverse-proportion (m10-algebra-modelling)."""
from manim import *
from _common import BAND_CHART_CENTER, BAND_TITLE, GREEN_OK, beat_group

SCRIPT = "In this lesson, we'll look at inverse proportion, a relationship where one quantity goes up exactly as the other goes down. Picture it like a seesaw in math form. The classic example is travel time versus speed for a fixed distance. If you drive faster, you get there in less time, so time and speed trade off against each other. Another everyday case is workers and days to finish a job. More workers means fewer days, fewer workers means more days. In every case, the two quantities multiply together to give the same constant number. That's the whole idea of inverse proportion. If you double one side, the other side must halve to keep that product steady. Think of it as a balancing act between the two numbers. Whenever you spot that balancing, you've found an inverse proportion. The rule is simple. The product stays constant no matter how the two values change. Now let's see it in action."

class M10AlgebraModellingInverseProportionScene(Scene):
    def construct(self) -> None:
        title = Text('Algebra Modelling Inverse Proportion', font_size=38).move_to(BAND_TITLE)
        subtitle = Text("Follow the narration, then try the idea yourself.", font_size=22).next_to(title, DOWN, buff=0.35)
        self.add(title, subtitle)
        self.wait(1.0)
        sections = ["In this lesson, we'll look at inverse proportion, a relationship where\none quantity goes up exactly as the other goes down. Another everyday\ncase is workers and days to finish a job. If you double one side, the\nother side must halve to keep that product steady. The product stays\nconstant no matter how the two values change.", "Picture it like a seesaw in math form. More workers means fewer days,\nfewer workers means more days. Think of it as a balancing act between\nthe two numbers. Now let's see it in action.", "The classic example is travel time versus speed for a fixed distance. In\nevery case, the two quantities multiply together to give the same\nconstant number. Whenever you spot that balancing, you've found an\ninverse proportion.", "If you drive faster, you get there in less time, so time and speed trade\noff against each other. That's the whole idea of inverse proportion. The\nrule is simple."]
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
