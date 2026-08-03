"""Average rate as secant slope, units, and the derivative limit."""
import sys
sys.path.insert(0,'/home/victor/maths-decoded/scripts/videos')
from _common import BLUE_TERM, ORANGE_TERM, GREEN_OK, animate_intro, animate_final_definition, beat_group
from manim import *

class AverageRateOfChangeScene(Scene):
    def construct(self):
        animate_intro(self,"Average rate of change","The secant slope between two points on a curve")
        b=beat_group()
        formula=MathTex(r"\text{average rate}=\frac{\Delta y}{\Delta x}=\frac{f(b)-f(a)}{b-a}",color=GREEN_OK).scale(.95).move_to(UP*.55)
        rise=MathTex(r"\text{rise}\div\text{run}",color=ORANGE_TERM).move_to(DOWN*.3)
        units=Text("distance (m) ÷ time (s) = metres per second (m/s)",font_size=21,color=BLUE_TERM).move_to(DOWN*1.05)
        b=beat_group(formula,rise,units); self.play(Write(formula)); self.play(Write(rise),FadeIn(units)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        ax=Axes(x_range=[0,3.5,1],y_range=[0,10,2],x_length=6.2,y_length=2.5,tips=False,axis_config={"include_numbers":False}).move_to(DOWN*.05)
        curve=ax.plot(lambda x:x*x,x_range=[.2,3.15],color=BLUE_TERM,stroke_width=4)
        p=ax.c2p(1,1); q=ax.c2p(3,9)
        pd=Dot(p,color=GREEN_OK); qd=Dot(q,color=ORANGE_TERM)
        sec=Line(p,q,color=ORANGE_TERM,stroke_width=4)
        label=MathTex(r"m=\frac{9-1}{3-1}=4",color=ORANGE_TERM).scale(.72).move_to([-3.8,1.25,0])
        b=beat_group(ax,curve,pd,qd,sec,label); self.play(Create(ax),Create(curve),FadeIn(pd),FadeIn(qd),Create(sec),Write(label)); self.wait(2)
        for x,col in [(2,ORANGE_TERM),(1.5,ORANGE_TERM),(1.12,GREEN_OK)]:
            nq=ax.c2p(x,x*x); nsec=Line(p,nq,color=col,stroke_width=4)
            self.play(qd.animate.move_to(nq),Transform(sec,nsec),run_time=1.2)
        tangent=ax.plot(lambda x:2*x-1,x_range=[.25,3.2],color=GREEN_OK,stroke_width=4)
        tlabel=MathTex(r"\text{tangent slope}=f'(1)=2",color=GREEN_OK).scale(.72).move_to([3.2,1.25,0])
        b=beat_group(b,tangent,tlabel); self.play(Transform(sec,tangent),Write(tlabel)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        far=Text("Points far apart → average rate",font_size=25,color=ORANGE_TERM).move_to(UP*.55)
        near=Text("Points squeezing together → instantaneous rate",font_size=25,color=GREEN_OK).move_to(DOWN*.15)
        deriv=MathTex(r"\lim_{b\to a}\frac{f(b)-f(a)}{b-a}=f'(a)",color=GREEN_OK).scale(.95).move_to(DOWN*.95)
        b=beat_group(far,near,deriv); self.play(FadeIn(far)); self.play(FadeIn(near)); self.play(Write(deriv)); self.wait(3); self.play(FadeOut(b))
        animate_final_definition(self,r"\frac{\Delta y}{\Delta x}\ \xrightarrow[\Delta x\to0]{}\ f'(a)","A secant gives an average; its limiting tangent gives the derivative.",final_wait=36)
