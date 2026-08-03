"""Symmetry + periodicity: period, even/odd, supplementary, unit circle."""
import sys
sys.path.insert(0,'/home/victor/maths-decoded/scripts/videos')
from _common import BLUE_TERM, ORANGE_TERM, GREEN_OK, animate_intro, animate_final_definition, beat_group
from manim import *
import numpy as np

class SymmetryPeriodicityScene(Scene):
    def construct(self):
        animate_intro(self,"Symmetry and periodicity of trig","Predictable waves — once a cycle is known, every cycle is known")
        b=beat_group()
        period=MathTex(r"\sin(x+2\pi)=\sin x,\qquad\cos(x+2\pi)=\cos x",color=BLUE_TERM).scale(.9).move_to(UP*.55)
        deg=MathTex(r"2\pi\ \text{rad}=360^\circ",color=ORANGE_TERM).scale(.9).move_to(DOWN*.1)
        ring=Text("One cycle, then the pattern repeats forever.",font_size=21,color=GREEN_OK).move_to(DOWN*.95)
        b=beat_group(period,deg,ring); self.play(Write(period)); self.play(Write(deg)); self.play(FadeIn(ring)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        even=MathTex(r"\cos(-x)=\cos x\quad(\text{even, mirror about y-axis})",color=BLUE_TERM).scale(.82).move_to(UP*.55)
        odd=MathTex(r"\sin(-x)=-\sin x\quad(\text{odd, symmetry about origin})",color=ORANGE_TERM).scale(.82).move_to(DOWN*.1)
        b=beat_group(even,odd); self.play(Write(even)); self.play(Write(odd)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        supp=MathTex(r"\sin(\pi-\theta)=\sin\theta",color=GREEN_OK).scale(.85).move_to(UP*.55)
        supp2=MathTex(r"\cos(\pi-\theta)=-\cos\theta",color=GREEN_OK).scale(.85).move_to(DOWN*.05)
        comp=MathTex(r"\sin(\tfrac\pi2-\theta)=\cos\theta,\qquad\cos(\tfrac\pi2-\theta)=\sin\theta",color=BLUE_TERM).scale(.75).move_to(DOWN*.95)
        b=beat_group(supp,supp2,comp); self.play(Write(supp)); self.play(Write(supp2)); self.play(Write(comp)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        unit=Circle(radius=1.1,color=WHITE).move_to(LEFT*2.6)
        x_ax=Line(LEFT*4,RIGHT*1.2,color=WHITE).move_to(unit.get_center())
        y_ax=Line(LEFT*2.6+UP*1.3,LEFT*2.6+UP*-.9,color=WHITE)
        angle=np.deg2rad(40); pt=unit.point_from_proportion(angle/(2*PI))
        proj=Line(pt,np.array([pt[0],unit.get_center()[1],0]),color=ORANGE_TERM)
        proj2=Line(pt,np.array([unit.get_center()[0],pt[1],0]),color=GREEN_OK)
        dp=Dot(pt,color=BLUE_TERM)
        coord=MathTex(r"(\cos\theta,\sin\theta)",color=GREEN_OK).scale(.75).move_to(RIGHT*1.8+UP*.4)
        cap=Text("Every angle gives the point (cos θ, sin θ).",font_size=21,color=WHITE).move_to(RIGHT*1.8+DOWN*.25)
        b=beat_group(unit,x_ax,y_ax,proj,proj2,dp,coord,cap); self.play(Create(unit),Create(x_ax),Create(y_ax),Create(proj),Create(proj2),FadeIn(dp),Write(coord),FadeIn(cap)); self.wait(3); self.play(FadeOut(b))
        animate_final_definition(self,r"\sin(x+2\pi)=\sin x,\ \cos\text{ even},\ \sin\text{ odd}","Period plus the supplementary/complementary identities are why trig works.",final_wait=42)
