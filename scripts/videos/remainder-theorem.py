"""Remainder theorem derived from the polynomial division identity."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import BLUE_TERM, ORANGE_TERM, GREEN_OK, animate_intro, animate_final_definition, beat_group
from manim import *

class RemainderTheoremScene(Scene):
    def construct(self):
        animate_intro(self, "The remainder theorem", "Dividing P(x) by (x - a) leaves the constant P(a)")
        b=beat_group()
        identity=MathTex(r"P(x)=Q(x)(x-a)+r", color=BLUE_TERM).scale(1.05).move_to(UP*.65)
        tags=VGroup(Text("polynomial",font_size=19,color=BLUE_TERM),Text("quotient × divisor",font_size=19,color=ORANGE_TERM),Text("constant remainder",font_size=19,color=GREEN_OK)).arrange(RIGHT,buff=.7).move_to(DOWN*.45)
        b=beat_group(identity,tags); self.play(Write(identity)); self.play(LaggedStart(*[FadeIn(x) for x in tags],lag_ratio=.2)); self.wait(2); self.play(FadeOut(b))

        b=beat_group()
        s1=MathTex(r"P(a)=Q(a)(a-a)+r", color=ORANGE_TERM).scale(1.0).move_to(UP*.65)
        s2=MathTex(r"P(a)=Q(a)\cdot0+r", color=ORANGE_TERM).scale(1.0).move_to(ORIGIN)
        s3=MathTex(r"\therefore\quad P(a)=r", color=GREEN_OK).scale(1.15).move_to(DOWN*.75)
        zero=SurroundingRectangle(s3,color=GREEN_OK,buff=.18)
        b=beat_group(s1,s2,s3,zero); self.play(Write(s1)); self.play(Write(s2)); self.play(Write(s3),Create(zero)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        ex=MathTex(r"P(x)=2x^3-5x+3,\qquad \text{divide by }x-1", color=BLUE_TERM).scale(.88).move_to(UP*.65)
        val=MathTex(r"P(1)=2(1)^3-5(1)+3=0", color=GREEN_OK).scale(.95).move_to(DOWN*.05)
        con=MathTex(r"\text{remainder }0\quad\Longrightarrow\quad x-1\text{ is a factor}", color=GREEN_OK).scale(.9).move_to(DOWN*.85)
        b=beat_group(ex,val,con); self.play(Write(ex)); self.play(Write(val)); self.play(Write(con)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        why=Text("No long division is needed to find the remainder.",font_size=24,color=ORANGE_TERM).move_to(UP*.45)
        two=VGroup(Text("Evaluate P(a) directly",font_size=22),Text("If P(a)=0, the divisor is an exact factor",font_size=22,color=GREEN_OK)).arrange(DOWN,buff=.45).move_to(DOWN*.35)
        b=beat_group(why,two); self.play(FadeIn(why),FadeIn(two)); self.wait(3); self.play(FadeOut(b))
        animate_final_definition(self,r"P(x)=Q(x)(x-a)+r\quad\Rightarrow\quad P(a)=r","Zero remainder means (x - a) is a factor.",final_wait=37)
