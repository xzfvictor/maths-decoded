"""A line and parabola: substitution, both coordinates, checks, and counts."""
import sys
sys.path.insert(0,'/home/victor/maths-decoded/scripts/videos')
from _common import BLUE_TERM, ORANGE_TERM, GREEN_OK, animate_intro, animate_final_definition, beat_group
from manim import *
import numpy as np

class LinearNonlinearScene(Scene):
    def construct(self):
        animate_intro(self,"Linear and non-linear: parabola meets line","Substitute, solve the quadratic, then back-substitute")
        b=beat_group()
        ax=Axes(x_range=[-2.5,3,1],y_range=[-2,4,1],x_length=6.6,y_length=2.7,tips=False,axis_config={"include_numbers":False}).move_to(DOWN*.05)
        par=ax.plot(lambda x:x*x-2,x_range=[-2,2.4],color=BLUE_TERM,stroke_width=4)
        line=ax.plot(lambda x:x+1,x_range=[-2.4,3],color=ORANGE_TERM,stroke_width=4)
        x1=(1-np.sqrt(13))/2; x2=(1+np.sqrt(13))/2; y1=x1+1; y2=x2+1
        d1=Dot(ax.c2p(x1,y1),color=GREEN_OK); d2=Dot(ax.c2p(x2,y2),color=GREEN_OK)
        l1=MathTex(r"(-1.303,-0.303)",color=GREEN_OK).scale(.58).move_to(ax.c2p(-1.15,.45))
        l2=MathTex(r"(2.303,3.303)",color=GREEN_OK).scale(.62).move_to(ax.c2p(1.85,3.65))
        b=beat_group(ax,par,line,d1,d2,l1,l2); self.play(Create(ax),Create(par),Create(line)); self.play(FadeIn(d1),FadeIn(d2),Write(l1),Write(l2)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        sub=MathTex(r"x+1=x^2-2\quad\Rightarrow\quad x^2-x-3=0",color=BLUE_TERM).scale(.85).move_to(UP*.65)
        roots=MathTex(r"x=\frac{1\pm\sqrt{13}}2\approx-1.303,\ 2.303",color=GREEN_OK).scale(.8).move_to(DOWN*.15)
        back=MathTex(r"y=x+1\quad\Rightarrow\quad y\approx-0.303,\ 3.303",color=GREEN_OK).scale(.78).move_to(DOWN*.95)
        b=beat_group(sub,roots,back); self.play(Write(sub)); self.play(Write(roots)); self.play(Write(back)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        checks=VGroup(MathTex(r"(-1.303,-0.303):\ y=x+1=-0.303=x^2-2",color=GREEN_OK),MathTex(r"(2.303,3.303):\ y=x+1=3.303=x^2-2",color=GREEN_OK)).arrange(DOWN,buff=.5).scale(.68).move_to(ORIGIN)
        cap=Text("Check every pair in both original equations.",font_size=23,color=GREEN_OK).move_to(UP*1.1)
        b=beat_group(checks,cap); self.play(FadeIn(cap),Write(checks)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        labels=VGroup(MathTex(r"2\text{ crossings}\Rightarrow2\text{ solutions}"),MathTex(r"\text{tangent}\Rightarrow1\text{ repeated solution}"),MathTex(r"\text{miss}\Rightarrow0\text{ solutions}")).arrange(DOWN,buff=.35).scale(.85).move_to(ORIGIN)
        b=beat_group(labels); self.play(LaggedStart(*[Write(x) for x in labels],lag_ratio=.3)); self.wait(3); self.play(FadeOut(b))
        animate_final_definition(self,r"\text{substitute}\to\text{quadratic}\to\text{back-substitute}","Two pairs here; geometry can give zero, one, or two intersections.",final_wait=33)
