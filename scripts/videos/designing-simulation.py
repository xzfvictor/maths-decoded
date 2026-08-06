import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, make_term_card, make_equation_card,
    animate_intro, animate_final_definition,
)
from manim import *


class DesigningSimulationScene(Scene):
    def construct(self) -> None:
        animate_intro(self, "Designing a simulation", "Identify, map, run, record, estimate")

        beat = None
        identify = Text("1. Identify the random components", font_size=26, color=BLUE_TERM).move_to(UP * 0.95)
        identify_bg = BackgroundRectangle(identify, color=BLACK, fill_opacity=1, buff=0.18); identify_bg.move_to(identify.get_center())
        real = Text("real chance experiment", font_size=22).move_to(DOWN * 0.05)
        real_bg = BackgroundRectangle(real, color=BLACK, fill_opacity=1, buff=0.15); real_bg.move_to(real.get_center())
        beat = beat_group(beat, identify_bg, identify, real_bg, real)
        self.play(FadeIn(identify_bg), FadeIn(identify), FadeIn(real_bg), FadeIn(real)); self.wait(3)
        mapping = VGroup(
            MathTex(r"1,2,3", color=RED_REJECT), Text("= red", font_size=24, color=RED_REJECT),
            MathTex(r"4,5", color=TEAL_TERM), Text("= blue", font_size=24, color=TEAL_TERM),
        ).arrange(RIGHT, buff=0.35).scale(0.9).move_to(DOWN * 0.75)
        map_bg = BackgroundRectangle(mapping, color=BLACK, fill_opacity=0.95, buff=0.22); map_bg.move_to(mapping.get_center())
        beat = beat_group(beat, map_bg, mapping)
        self.play(FadeIn(map_bg), LaggedStart(*[Write(m) for m in mapping], lag_ratio=0.12)); self.wait(4)
        self.play(FadeOut(beat, run_time=0.8))

        beat = None
        steps = VGroup(*[
            Text("1  identify", font_size=23, color=BLUE_TERM),
            Text("2  map", font_size=23, color=TEAL_TERM),
            Text("3  run many", font_size=23, color=ORANGE_TERM),
            Text("4  record", font_size=23, color=BLUE_TERM),
            Text("5  estimate", font_size=23, color=GREEN_OK),
        ]).arrange(RIGHT, buff=0.28).scale(0.85).move_to(UP * 0.65)
        steps_bg = BackgroundRectangle(steps, color=BLACK, fill_opacity=1, buff=0.2); steps_bg.move_to(steps.get_center())
        beat = beat_group(beat, steps_bg, steps)
        self.play(FadeIn(steps_bg), LaggedStart(*[FadeIn(s, shift=UP * 0.15) for s in steps], lag_ratio=0.18)); self.wait(3)
        record = MathTex(r"\text{estimate} = \frac{\text{event count}}{\text{total runs}}", color=GREEN_OK).scale(1.0).move_to(DOWN * 0.65)
        record_bg = BackgroundRectangle(record, color=BLACK, fill_opacity=1, buff=0.24); record_bg.move_to(record.get_center())
        beat = beat_group(beat, record_bg, record)
        self.play(FadeIn(record_bg), Write(record, run_time=1.7)); self.wait(4)
        self.play(FadeOut(beat, run_time=0.8))

        beat = None
        bad = MathTex(r"1,2,3,4,5=\text{ red};\quad 6=\text{ blue}", color=RED_REJECT).scale(0.95).move_to(UP * 0.45)
        bad_bg = BackgroundRectangle(bad, color=BLACK, fill_opacity=1, buff=0.2); bad_bg.move_to(bad.get_center())
        cross = Cross(bad, color=RED_REJECT, stroke_width=6)
        fix = Text("The number map must preserve the intended probabilities.", font_size=21, color=RED_REJECT).move_to(DOWN * 0.75)
        fix_bg = BackgroundRectangle(fix, color=BLACK, fill_opacity=0.95, buff=0.17); fix_bg.move_to(fix.get_center())
        beat = beat_group(beat, bad_bg, bad, cross, fix_bg, fix)
        self.play(FadeIn(bad_bg), Write(bad)); self.wait(1.5); self.play(Create(cross)); self.play(FadeIn(fix_bg), FadeIn(fix)); self.wait(5)
        self.play(FadeOut(beat, run_time=0.8))

        animate_final_definition(self, r"\text{identify} \to \text{map} \to \text{run} \to \text{record} \to \text{estimate}", "A simulation is a carefully mapped pretend experiment.", final_wait=20)
