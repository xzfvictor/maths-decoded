"""Secant slope of y = x² at x = 3 with h → 0 and 0/0 explained."""
import sys
sys.path.insert(0,'/home/victor/maths-decoded/scripts/videos')
from _common import BLUE_TERM, ORANGE_TERM, GREEN_OK, animate_intro, animate_final_definition, beat_group
from manim import *

class TangentAsLimitScene(Scene):
    def construct(self):
        animate_intro(self,"Tangent as a limiting secant","Let h → 0: the secant becomes the tangent line")
        b=beat_group()
        setup=MathTex(r"f(x)=x^2,\quad a=3\quad\Rightarrow\quad f(3)=9,\quad f(3+h)=(3+h)^2=9+6h+h^2",color=BLUE_TERM).scale(.78).move_to(UP*.55)
        hstep=MathTex(r"\text{secant slope}=\frac{f(3+h)-f(3)}{h}=\frac{6h+h^2}{h}=6+h",color=ORANGE_TERM).scale(.85).move_to(DOWN*.2)
        note=Text("Plugging in h = 0 gives 0/0, so sneak up on the limit instead.",font_size=21,color=ORANGE_TERM).move_to(DOWN*1.05)
        b=beat_group(setup,hstep,note); self.play(Write(setup)); self.play(Write(hstep)); self.play(FadeIn(note)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        rows=VGroup(
            MathTex(r"h=0.1\ \Rightarrow\ \frac{f(3.1)-f(3)}{0.1}=6.1",color=BLUE_TERM),
            MathTex(r"h=0.01\ \Rightarrow\ \frac{f(3.01)-f(3)}{0.01}=6.01",color=BLUE_TERM),
            MathTex(r"h=0.001\ \Rightarrow\ \frac{f(3.001)-f(3)}{0.001}=6.001",color=BLUE_TERM),
        ).arrange(DOWN,buff=.32).scale(.78).move_to(UP*.1)
        lim=MathTex(r"\text{slope}\to6\quad\Rightarrow\quad\text{tangent: }y=6x-9",color=GREEN_OK).scale(1.0).move_to(DOWN*1.2)
        b=beat_group(rows,lim); self.play(LaggedStart(*[Write(r) for r in rows],lag_ratio=.4)); self.play(Write(lim)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        ax=Axes(x_range=[0,5,1],y_range=[-2,16,2],x_length=6.4,y_length=2.6,tips=False,axis_config={"include_numbers":False}).move_to(DOWN*.05)
        curve=ax.plot(lambda x:x*x,x_range=[.4,4],color=BLUE_TERM,stroke_width=4)
        p=ax.c2p(3,9); pd=Dot(p,color=GREEN_OK,radius=.08)
        tan=ax.plot(lambda x:6*x-9,x_range=[.4,2.5],color=GREEN_OK,stroke_width=4)
        cap=Text("Base point (3, 9), tangent slope 6: y = 6x - 9.",font_size=20,color=GREEN_OK).move_to(UP*1.32)
        b=beat_group(ax,curve,pd,tan,cap); self.play(Create(ax),Create(curve),FadeIn(pd),Create(tan),FadeIn(cap)); self.wait(3); self.play(FadeOut(b))
        animate_final_definition(self,r"\lim_{h\to0}\frac{f(3+h)-f(3)}{h}=6","As h shrinks the secant becomes the tangent y = 6x - 9.",final_wait=40)
