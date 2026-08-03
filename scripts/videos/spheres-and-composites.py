"""Sphere and hemisphere formulas, then a cone-on-cylinder composite."""
import sys
sys.path.insert(0,'/home/victor/maths-decoded/scripts/videos')
from _common import BLUE_TERM, ORANGE_TERM, GREEN_OK, animate_intro, animate_final_definition, beat_group
from manim import *

class SpheresAndCompositesScene(Scene):
    def construct(self):
        animate_intro(self,"Spheres and composite solids","Add volumes, but count only exposed surfaces")
        b=beat_group()
        sph=Circle(radius=1.05,color=BLUE_TERM,fill_color=BLUE_TERM,fill_opacity=.25).move_to(LEFT*3)
        rad=Line(LEFT*3,LEFT*3+RIGHT*1.05,color=ORANGE_TERM); rlab=MathTex('r',color=ORANGE_TERM).scale(.8).next_to(rad,UP,buff=.12)
        f=VGroup(MathTex(r"V=\frac43\pi r^3",color=GREEN_OK),MathTex(r"SA=4\pi r^2",color=BLUE_TERM)).arrange(DOWN,buff=.45).scale(.95).move_to(RIGHT*2.5+UP*.35)
        b=beat_group(sph,rad,rlab,f); self.play(Create(sph),Create(rad),Write(rlab)); self.play(Write(f)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        hemi=VGroup(Arc(radius=1.0,start_angle=0,angle=PI,color=ORANGE_TERM),Line(LEFT,RIGHT,color=ORANGE_TERM)).move_to(LEFT*3)
        hf=VGroup(MathTex(r"V_{hemi}=\frac23\pi r^3",color=GREEN_OK),MathTex(r"CA=2\pi r^2",color=ORANGE_TERM),MathTex(r"TA=3\pi r^2\ (\text{including flat face})",color=BLUE_TERM)).arrange(DOWN,buff=.25).scale(.72).move_to(RIGHT*2.3)
        b=beat_group(hemi,hf); self.play(Create(hemi)); self.play(LaggedStart(*[Write(x) for x in hf],lag_ratio=.2)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        cyl=Cylinder(radius=.9,height=1.35,direction=UP,fill_color=BLUE_TERM,fill_opacity=.3,stroke_width=3).move_to(LEFT*2.8+DOWN*.45)
        cone=Cone(base_radius=.9,height=1.5,direction=UP,fill_color=ORANGE_TERM,fill_opacity=.3,stroke_width=3).move_to(LEFT*2.8+UP*.95)
        total=MathTex(r"V=\underbrace{\pi r^2h}_{\text{cylinder}}+\underbrace{\frac13\pi r^2H}_{\text{cone}}",color=GREEN_OK).scale(.78).move_to(RIGHT*2.3+UP*.45)
        exposed=VGroup(MathTex(r"SA=\pi r^2\ (\text{bottom})",color=BLUE_TERM),MathTex(r"+2\pi rh\ (\text{cylinder side})",color=BLUE_TERM),MathTex(r"+\pi r\ell\ (\text{cone slant})",color=ORANGE_TERM)).arrange(DOWN,buff=.23).scale(.7).move_to(RIGHT*2.3+DOWN*.55)
        cap=Text("The joined circular face is hidden — do not count it.",font_size=19,color=GREEN_OK).move_to(DOWN*1.35)
        b=beat_group(cyl,cone,total,exposed,cap); self.play(FadeIn(cyl),FadeIn(cone)); self.play(Write(total),Write(exposed),FadeIn(cap)); self.wait(3); self.play(FadeOut(b))
        animate_final_definition(self,r"\text{Composite }V=\sum V_i\quad\text{and count exposed surfaces only}","Add or subtract component volumes; joined faces disappear.",final_wait=32)
