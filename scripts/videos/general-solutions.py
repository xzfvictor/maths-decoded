"""General solutions: period, family, sin/cos/tan, and sin(2θ) scaling."""
import sys
sys.path.insert(0,'/home/victor/maths-decoded/scripts/videos')
from _common import BLUE_TERM, ORANGE_TERM, GREEN_OK, animate_intro, animate_final_definition, beat_group
from manim import *

class GeneralSolutionsScene(Scene):
    def construct(self):
        animate_intro(self,"General solutions and periods","One angle spawns an infinite family — but a domain cuts it down")
        b=beat_group()
        sin_card=MathTex(r"\sin(\theta+2\pi k)=\sin\theta,\quad\text{period }T=2\pi",color=BLUE_TERM).scale(.85).move_to(UP*.65)
        cos_card=MathTex(r"\cos(\theta+2\pi k)=\cos\theta,\quad T=2\pi",color=BLUE_TERM).scale(.85).move_to(UP*.0)
        tan_card=MathTex(r"\tan(\theta+\pi k)=\tan\theta,\quad T=\pi",color=ORANGE_TERM).scale(.85).move_to(DOWN*.65)
        b=beat_group(sin_card,cos_card,tan_card); self.play(Write(sin_card)); self.play(Write(cos_card)); self.play(Write(tan_card)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        unit=Circle(radius=1.0,color=WHITE).move_to(LEFT*2.5+UP*.15)
        x_ax=Line(LEFT*4+UP*.15,RIGHT*.5+UP*.15,color=WHITE); y_ax=Line(LEFT*2.5+UP*1.15,LEFT*2.5+UP*-.85,color=WHITE)
        a_pt=unit.point_from_proportion(1/12); b_pt=unit.point_from_proportion(5/12)
        ad=Dot(a_pt,color=BLUE_TERM); bd=Dot(b_pt,color=ORANGE_TERM)
        at=MathTex(r"\alpha",color=BLUE_TERM).scale(.7).next_to(ad,UR,buff=.08)
        bt=MathTex(r"\pi-\alpha",color=ORANGE_TERM).scale(.7).next_to(bd,UL,buff=.08)
        family=MathTex(r"\theta=\alpha+2\pi k\quad\text{or}\quad\theta=\pi-\alpha+2\pi k",color=GREEN_OK).scale(.78).move_to(RIGHT*2.6+UP*.4)
        note=Text("Without a domain there are infinitely many solutions.",font_size=21,color=WHITE).move_to(RIGHT*2.6+DOWN*.25)
        b=beat_group(unit,x_ax,y_ax,ad,bd,at,bt,family,note); self.play(Create(unit),Create(x_ax),Create(y_ax),FadeIn(ad),FadeIn(bd),Write(at),Write(bt),Write(family),FadeIn(note)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        domain=MathTex(r"[0,2\pi]:\quad\theta=\frac{\pi}{6},\frac{5\pi}{6}",color=GREEN_OK).scale(.85).move_to(UP*.45)
        d2=MathTex(r"[-90^\circ,90^\circ]:\quad\tan\theta=\sqrt3\Rightarrow\theta=60^\circ",color=ORANGE_TERM).scale(.78).move_to(DOWN*.15)
        b=beat_group(domain,d2); self.play(Write(domain)); self.play(Write(d2)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        inside=MathTex(r"\sin(2\theta)=\frac12\quad\Rightarrow\quad 2\theta=\frac{\pi}{6}+2\pi k\ \text{ or }\ \frac{5\pi}{6}+2\pi k",color=BLUE_TERM).scale(.74).move_to(UP*.55)
        divided=MathTex(r"\theta=\frac{\pi}{12}+\pi k\quad\text{or}\quad\theta=\frac{5\pi}{12}+\pi k",color=GREEN_OK).scale(.85).move_to(DOWN*.05)
        period=Text("Period shrinks: T = 2π/2 = π.",font_size=22,color=ORANGE_TERM).move_to(DOWN*1.05)
        b=beat_group(inside,divided,period); self.play(Write(inside)); self.play(Write(divided)); self.play(FadeIn(period)); self.wait(3); self.play(FadeOut(b))
        animate_final_definition(self,r"\theta=\alpha+2\pi k\ \text{or}\ \pi-\alpha+2\pi k,\qquad\sin(n\theta):\ T=\frac{2\pi}n","Combine family (period) with domain; sin(nθ) scales the period.",final_wait=40)
