"""Manim scene aligned to the Year 10A what-is-algorithm narration."""

import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')

from manim import *
from _common import (
    BAND_CHART_CENTER, BLUE_TERM, TEAL_TERM, ORANGE_TERM, RED_REJECT,
    GREEN_OK, beat_group, animate_intro, animate_final_definition,
)


class WhatIsAlgorithmL10aAaScene(Scene):
    def construct(self) -> None:
        animate_intro(
            self,
            "What is an algorithm?",
            "A finite, ordered, repeatable list of steps that always finishes.",
        )

        head = Text("Input → steps → output", font_size=26, color=BLUE_TERM)
        head.move_to(BAND_CHART_CENTER + UP * 1.42)
        head_bg = BackgroundRectangle(head, color=BLACK, fill_opacity=0.95, buff=0.15)
        properties = VGroup(
            Text("FINITE", font_size=23, color=BLUE_TERM),
            Text("ORDERED", font_size=23, color=TEAL_TERM),
            Text("REPEATABLE", font_size=23, color=ORANGE_TERM),
        ).arrange(RIGHT, buff=0.7).move_to(BAND_CHART_CENTER + UP * 0.35)
        boxes = VGroup(*[
            SurroundingRectangle(item, color=item.get_color(), buff=0.18)
            for item in properties
        ])
        terminate = Text("It must terminate — it cannot loop forever.", font_size=22, color=GREEN_OK)
        terminate.move_to(BAND_CHART_CENTER + DOWN * 0.62)
        terminate_bg = BackgroundRectangle(terminate, color=BLACK, fill_opacity=0.96, buff=0.14)
        flow = MathTex(r"\text{input}\ \longrightarrow\ \text{ordered steps}\ \longrightarrow\ \text{output}").scale(0.8)
        flow.move_to(BAND_CHART_CENTER + DOWN * 1.18)
        flow_bg = BackgroundRectangle(flow, color=BLACK, fill_opacity=1, buff=0.12)
        beat2 = beat_group(head_bg, head, properties, boxes, terminate_bg, terminate, flow_bg, flow)
        self.play(FadeIn(head_bg), FadeIn(head))
        for item, box in zip(properties, boxes):
            self.play(FadeIn(item), Create(box), run_time=0.7)
        self.play(FadeIn(terminate_bg), FadeIn(terminate))
        self.play(FadeIn(flow_bg), Write(flow))
        self.wait(2.5)
        self.play(FadeOut(beat2, run_time=0.8))

        # The exact largest-of-three procedure described by the narrator.
        head3 = Text("Example: find the biggest of three values", font_size=25, color=GREEN_OK)
        head3.move_to(BAND_CHART_CENTER + UP * 1.48)
        head3_bg = BackgroundRectangle(head3, color=BLACK, fill_opacity=0.95, buff=0.15)
        pseudo = VGroup(
            Text("READ a, b, c", font_size=21, color=WHITE),
            Text("largest ← a", font_size=21, color=BLUE_TERM),
            Text("IF b > largest, THEN largest ← b", font_size=21, color=TEAL_TERM),
            Text("IF c > largest, THEN largest ← c", font_size=21, color=ORANGE_TERM),
            Text("OUTPUT largest", font_size=21, color=GREEN_OK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(BAND_CHART_CENTER + DOWN * 0.03)
        pseudo_bgs = VGroup(*[
            BackgroundRectangle(line, color=BLACK, fill_opacity=0.97, buff=0.1)
            for line in pseudo
        ])
        beat3 = beat_group(head3_bg, head3, pseudo_bgs, pseudo)
        self.play(FadeIn(head3_bg), FadeIn(head3))
        for bg, line in zip(pseudo_bgs, pseudo):
            self.play(FadeIn(bg, run_time=0.15), FadeIn(line, shift=RIGHT * 0.1, run_time=0.65))
            self.wait(0.35)
        self.wait(2.5)
        self.play(FadeOut(beat3, run_time=0.8))

        head4 = Text("Pseudocode: informal, readable instructions", font_size=24, color=TEAL_TERM)
        head4.move_to(BAND_CHART_CENTER + UP * 1.46)
        head4_bg = BackgroundRectangle(head4, color=BLACK, fill_opacity=0.95, buff=0.15)
        simple = VGroup(
            Text("READ x", font_size=22),
            MathTex(r"\text{IF }x<0,\ \text{SET }x\leftarrow -x", color=ORANGE_TERM).scale(0.82),
            Text("OUTPUT x", font_size=22, color=GREEN_OK),
        ).arrange(DOWN, buff=0.28).move_to(BAND_CHART_CENTER + UP * 0.12)
        simple_bgs = VGroup(*[
            BackgroundRectangle(line, color=BLACK, fill_opacity=0.97, buff=0.11)
            for line in simple
        ])
        iterative = Text("Iterate, check, refine: bisection and Newton's method", font_size=20, color=BLUE_TERM)
        iterative.move_to(BAND_CHART_CENTER + DOWN * 1.08)
        iterative_bg = BackgroundRectangle(iterative, color=BLACK, fill_opacity=0.96, buff=0.12)
        beat4 = beat_group(head4_bg, head4, simple_bgs, simple, iterative_bg, iterative)
        self.play(FadeIn(head4_bg), FadeIn(head4))
        for bg, line in zip(simple_bgs, simple):
            self.play(FadeIn(bg), FadeIn(line), run_time=0.65)
        self.play(FadeIn(iterative_bg), FadeIn(iterative))
        self.wait(3.0)
        self.play(FadeOut(beat4, run_time=0.8))

        animate_final_definition(
            self,
            r"\text{Algorithm}=\text{finite, ordered, repeatable steps}",
            "It takes an input, produces an output, and always terminates.",
            final_wait=62.0,
        )
