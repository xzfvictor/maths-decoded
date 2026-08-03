"""Factor theorem: candidate roots, repeated division, and x-intercepts."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import BAND_CHART_CENTER, BLUE_TERM, ORANGE_TERM, GREEN_OK, animate_intro, animate_final_definition, beat_group
from manim import *
import numpy as np

class FactorTheoremScene(Scene):
    def construct(self):
        animate_intro(self, "The factor theorem", "P(a) = 0  ⇔  (x - a) is a factor of P(x)")
        b = beat_group()
        p = MathTex(r"P(x)=x^3-6x^2+11x-6", color=BLUE_TERM).scale(.95).move_to(UP*.55)
        c = MathTex(r"\text{integer candidates: }\pm1,\ \pm2,\ \pm3,\ \pm6", color=ORANGE_TERM).scale(.83).move_to(DOWN*.35)
        note = Text("Any integer root must divide the constant term.", font_size=21, color=WHITE).move_to(DOWN*1.05)
        b = beat_group(p, c, note); self.play(Write(p), Write(c), FadeIn(note)); self.wait(2); self.play(FadeOut(b))

        b = beat_group()
        tests = VGroup(MathTex(r"P(1)=1-6+11-6=0", color=GREEN_OK), MathTex(r"P(2)=8-24+22-6=0", color=GREEN_OK), MathTex(r"P(3)=27-54+33-6=0", color=GREEN_OK)).arrange(DOWN, buff=.28).scale(.9).move_to(UP*.15)
        br = SurroundingRectangle(tests, color=GREEN_OK, buff=.18); bg = BackgroundRectangle(tests, color=BLACK, fill_opacity=1, buff=.2)
        b = beat_group(tests,br,bg); self.play(FadeIn(bg), Write(tests), Create(br)); self.wait(2)
        q = MathTex(r"P(x)\div(x-1)=x^2-5x+6", color=BLUE_TERM).scale(.9).move_to(DOWN*1.0)
        b = beat_group(b,q); self.play(Write(q)); self.wait(1.5); self.play(FadeOut(b))

        b = beat_group()
        repeat = VGroup(MathTex(r"x^2-5x+6", color=BLUE_TERM), MathTex(r"P(2)\text{ for the quotient}=0\quad\Rightarrow\quad(x-2)", color=GREEN_OK), MathTex(r"x^2-5x+6=(x-2)(x-3)", color=GREEN_OK)).arrange(DOWN, buff=.3).scale(.82).move_to(UP*.05)
        b = beat_group(repeat); self.play(Write(repeat[0])); self.play(Write(repeat[1])); self.play(Write(repeat[2])); self.wait(2); self.play(FadeOut(b))

        b = beat_group()
        ax = Axes(x_range=[0,3.4,1], y_range=[-2,2.5,1], x_length=6.4, y_length=2.4, tips=False, axis_config={"include_numbers":False}).move_to(DOWN*.05)
        curve = ax.plot(lambda x:(x-1)*(x-2)*(x-3), x_range=[.2,3.2], color=BLUE_TERM, stroke_width=4)
        dots = VGroup(*[Dot(ax.c2p(x,0), color=GREEN_OK, radius=.08) for x in (1,2,3)])
        labels = VGroup(*[MathTex(f"x={x}", color=GREEN_OK).scale(.7).next_to(ax.c2p(x,0), DOWN, buff=.18) for x in (1,2,3)])
        cap = Text("Roots are exactly the x-intercepts.", font_size=22, color=GREEN_OK).move_to(UP*1.35)
        b = beat_group(ax,curve,dots,labels,cap); self.play(Create(ax),Create(curve),FadeIn(dots),Write(labels),FadeIn(cap)); self.wait(3); self.play(FadeOut(b))
        animate_final_definition(self, r"P(a)=0\iff(x-a)\text{ is a factor}", "Test divisors, divide, repeat; roots mark x-intercepts.", final_wait=34)
