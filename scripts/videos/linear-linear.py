"""Solve two linear equations by substitution, elimination, then graph-check."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _common import BLUE_TERM, ORANGE_TERM, GREEN_OK, animate_intro, animate_final_definition, beat_group
from manim import *

class LinearLinearScene(Scene):
    def construct(self):
        animate_intro(self,"Linear–linear simultaneous equations","Substitution or elimination finds the shared pair (x, y)")
        b=beat_group()
        system=MathTex(r"\begin{cases}y=2x+1\\y=-x+4\end{cases}",color=BLUE_TERM).scale(.9).move_to(UP*.75)
        sub=MathTex(r"2x+1=-x+4\Rightarrow3x=3\Rightarrow x=1",color=GREEN_OK).scale(.9).move_to(DOWN*.05)
        back=MathTex(r"y=2(1)+1=3\quad\Rightarrow\quad(1,3)",color=GREEN_OK).scale(.9).move_to(DOWN*.85)
        b=beat_group(system,sub,back); self.play(Write(system)); self.play(Write(sub)); self.play(Write(back)); self.wait(2); self.play(FadeOut(b))

        b=beat_group()
        h=Text("Elimination",font_size=25,color=ORANGE_TERM).move_to(UP*1.25)
        eqs=MathTex(r"\begin{aligned}2x-y&=-1\\x+y&=4\\\hline3x&=3\end{aligned}",color=BLUE_TERM).scale(.9).move_to(UP*.15)
        elim=MathTex(r"x=1,\qquad y=3",color=GREEN_OK).scale(1.05).move_to(DOWN*1.0)
        b=beat_group(h,eqs,elim); self.play(FadeIn(h),Write(eqs)); self.play(Write(elim)); self.wait(2); self.play(FadeOut(b))

        b=beat_group()
        ax=Axes(x_range=[-1,3,1],y_range=[-1,5,1],x_length=6.2,y_length=2.5,tips=False,axis_config={"include_numbers":False}).move_to(DOWN*.1)
        l1=ax.plot(lambda x:2*x+1,x_range=[-.5,1.9],color=BLUE_TERM,stroke_width=4)
        l2=ax.plot(lambda x:-x+4,x_range=[-.5,3],color=ORANGE_TERM,stroke_width=4)
        dot=Dot(ax.c2p(1,3),color=GREEN_OK,radius=.09)
        lab=MathTex(r"(1,3)",color=GREEN_OK).scale(.8).move_to(ax.c2p(1.45,3.45))
        e1=MathTex(r"y=2x+1",color=BLUE_TERM).scale(.7).move_to([-3.9,1.15,0])
        e2=MathTex(r"y=-x+4",color=ORANGE_TERM).scale(.7).move_to([3.9,1.15,0])
        cap=Text("Graph check: both lines pass through the algebraic solution.",font_size=20,color=GREEN_OK).move_to(DOWN*1.32)
        b=beat_group(ax,l1,l2,dot,lab,e1,e2,cap); self.play(Create(ax),Create(l1),Create(l2)); self.play(FadeIn(dot),Write(lab),FadeIn(e1),FadeIn(e2),FadeIn(cap)); self.wait(3); self.play(FadeOut(b))
        animate_final_definition(self,r"\text{substitute or eliminate}\quad\Longrightarrow\quad(x,y)=(1,3)","The graph confirms the same intersection point.",final_wait=29)
