"""Right pyramids and cones: volume, surface area, slant height, units."""
import sys
sys.path.insert(0,'/home/victor/maths-decoded/scripts/videos')
from _common import BLUE_TERM, ORANGE_TERM, GREEN_OK, animate_intro, animate_final_definition, beat_group
from manim import *
import numpy as np

class PyramidsAndConesScene(Scene):
    def construct(self):
        animate_intro(self,"Right pyramids and right cones","Apex above the base centre: volume, surface area, and slant height")
        b=beat_group()
        pyramid=VGroup(Polygon([-4,-1,0],[-1.7,-1,0],[-2.1,-1.35,0],[-4.4,-1.35,0],color=BLUE_TERM),*[Line([-3.05,1.15,0],p,color=BLUE_TERM) for p in ([-4,-1,0],[-1.7,-1,0],[-2.1,-1.35,0],[-4.4,-1.35,0])])
        cone=VGroup(Ellipse(width=2.4,height=.45,color=ORANGE_TERM).move_to([2.9,-1.1,0]),Line([2.9,1.15,0],[1.7,-1.1,0],color=ORANGE_TERM),Line([2.9,1.15,0],[4.1,-1.1,0],color=ORANGE_TERM))
        h1=DashedLine([-3.05,1.15,0],[-3.05,-1.15,0],color=GREEN_OK); h2=DashedLine([2.9,1.15,0],[2.9,-1.1,0],color=GREEN_OK)
        vol=MathTex(r"V=\frac13Ah",color=GREEN_OK).scale(1.05).move_to([0,.15,0])
        note=Text("Same base and vertical height as a prism/cylinder — one-third the volume.",font_size=19).move_to(DOWN*1.38)
        b=beat_group(pyramid,cone,h1,h2,vol,note); self.play(Create(pyramid),Create(cone),Create(h1),Create(h2)); self.play(Write(vol),FadeIn(note)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        sa1=MathTex(r"SA_{\rm pyramid}=A_{\rm base}+\frac12P\ell",color=BLUE_TERM).scale(.9).move_to(UP*.7)
        sa2=MathTex(r"SA_{\rm cone}=\pi r^2+\pi r\ell",color=ORANGE_TERM).scale(.95).move_to(DOWN*.1)
        explain=Text("P is base perimeter; ℓ runs down the middle of a sloping face.",font_size=21,color=WHITE).move_to(DOWN*1.0)
        b=beat_group(sa1,sa2,explain); self.play(Write(sa1)); self.play(Write(sa2)); self.play(FadeIn(explain)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        tri=Polygon([-3,-1,0],[-3,1.1,0],[-.7,-1,0],color=WHITE)
        right=RightAngle(Line([-3,-1,0],[-3,1.1,0]),Line([-3,-1,0],[-.7,-1,0]),length=.25,color=GREEN_OK)
        labs=VGroup(MathTex("h").move_to([-3.25,.05,0]),MathTex("r").move_to([-1.85,-1.25,0]),MathTex(r"\ell",color=ORANGE_TERM).move_to([-1.7,.2,0]))
        eq=MathTex(r"\ell^2=h^2+r^2\quad\Rightarrow\quad\ell=\sqrt{h^2+r^2}",color=GREEN_OK).scale(.88).move_to([3,.1,0])
        b=beat_group(tri,right,labs,eq); self.play(Create(tri),Create(right),FadeIn(labs)); self.play(Write(eq)); self.wait(3); self.play(FadeOut(b))

        b=beat_group()
        units=VGroup(Text("Lengths: cm",font_size=25,color=BLUE_TERM),Text("Surface area: cm²",font_size=25,color=ORANGE_TERM),Text("Volume: cm³",font_size=25,color=GREEN_OK)).arrange(DOWN,buff=.4).move_to(ORIGIN)
        b=beat_group(units); self.play(LaggedStart(*[FadeIn(x) for x in units],lag_ratio=.25)); self.wait(3); self.play(FadeOut(b))
        animate_final_definition(self,r"V=\frac13Ah,\quad SA_{p}=A+\frac12P\ell,\quad SA_c=\pi r^2+\pi r\ell","Use vertical h for volume, slant ℓ for surface area, and consistent units.",final_wait=38)
