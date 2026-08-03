"""Four circle theorems: tangent-radius, alternate segment, equal chords, cyclic."""
import sys
sys.path.insert(0,'/home/victor/maths-decoded/scripts/videos')
from _common import BLUE_TERM, TEAL_TERM, ORANGE_TERM, GREEN_OK, animate_intro, animate_final_definition, beat_group
from manim import *
import numpy as np

class ChordsTangentsScene(Scene):
    def construct(self):
        animate_intro(self,"Four circle theorems","Tangent-radius, alternate segment, equal chords, cyclic opposite angles")
        cx,cy,r=-3.3,-.1,1.0
        c1=Circle(radius=r,color=WHITE).move_to([cx,cy,0])
        oa=Line([cx,cy,0],[cx+r,cy,0],color=BLUE_TERM)
        t_dir=np.array([0,1,0])
        a_pt=np.array([cx+r,cy,0])
        tan=Line(a_pt-1.4*t_dir,a_pt+1.4*t_dir,color=ORANGE_TERM,stroke_width=4)
        right=RightAngle(oa,tan,length=.25,color=GREEN_OK)
        t1=Text("Tangent ⊥ radius at the point of contact.",font_size=22,color=ORANGE_TERM).move_to([2.6,1.0,0])
        f1=MathTex(r"\angle=90^\circ",color=GREEN_OK).scale(.95).move_to([2.6,.2,0])
        b=beat_group(c1,oa,tan,right,t1,f1); self.play(Create(c1),Create(oa),Create(tan),Create(right),FadeIn(t1),Write(f1)); self.wait(3); self.play(FadeOut(b))

        c2=Circle(radius=r,color=WHITE).move_to([cx,cy,0])
        a_pt=np.array([cx+r,cy,0])
        tan=Line(a_pt-1.4*t_dir,a_pt+1.4*t_dir,color=ORANGE_TERM,stroke_width=4)
        b_pt=np.array([cx+r*np.cos(np.deg2rad(210)),cy+r*np.sin(np.deg2rad(210)),0])
        chord=Line(a_pt,b_pt,color=BLUE_TERM,stroke_width=4)
        c_pt=np.array([cx+r*np.cos(np.deg2rad(150)),cy+r*np.sin(np.deg2rad(150)),0])
        ca=Line(c_pt,a_pt,color=TEAL_TERM); cb=Line(c_pt,b_pt,color=TEAL_TERM)
        ang_a=Angle(Line(a_pt,a_pt-t_dir*.8),chord,radius=.3,color=GREEN_OK)
        ang_c=Angle(ca,cb,radius=.3,color=GREEN_OK)
        t2=Text("Alternate segment theorem.",font_size=23,color=TEAL_TERM).move_to([2.6,1.0,0])
        f2=MathTex(r"\angle_{\text{tan–chord}}=\angle_{\text{alternate}}",color=GREEN_OK).scale(.78).move_to([2.6,.0,0])
        b=beat_group(c2,tan,chord,ca,cb,ang_a,ang_c,t2,f2); self.play(Create(c2),Create(tan),Create(chord),Create(ca),Create(cb),Create(ang_a),Create(ang_c),FadeIn(t2),Write(f2)); self.wait(3); self.play(FadeOut(b))

        c3=Circle(radius=r,color=WHITE).move_to([cx,cy,0])
        ang1,ang2=np.deg2rad(40),np.deg2rad(150)
        a1=np.array([cx+r*np.cos(ang1),cy+r*np.sin(ang1),0])
        a2=np.array([cx+r*np.cos(-ang1),cy+r*np.sin(-ang1),0])
        b1=np.array([cx+r*np.cos(np.pi-ang2),cy+r*np.sin(np.pi-ang2),0])
        b2=np.array([cx+r*np.cos(np.pi+ang2),cy+r*np.sin(np.pi+ang2),0])
        ch1=Line(a1,a2,color=BLUE_TERM,stroke_width=4)
        ch2=Line(b1,b2,color=ORANGE_TERM,stroke_width=4)
        d1=DashedLine([cx,cy,0],a1,color=BLUE_TERM); d2=DashedLine([cx,cy,0],a2,color=BLUE_TERM)
        d3=DashedLine([cx,cy,0],b1,color=ORANGE_TERM); d4=DashedLine([cx,cy,0],b2,color=ORANGE_TERM)
        t3=Text("Equal chords → equidistant from centre.",font_size=22,color=BLUE_TERM).move_to([2.6,1.0,0])
        f3=MathTex(r"d_1=d_2",color=GREEN_OK).scale(1.0).move_to([2.6,.0,0])
        b=beat_group(c3,ch1,ch2,d1,d2,d3,d4,t3,f3); self.play(Create(c3),Create(ch1),Create(ch2),Create(d1),Create(d2),Create(d3),Create(d4),FadeIn(t3),Write(f3)); self.wait(3); self.play(FadeOut(b))

        c4=RegularPolygon(4,color=WHITE).scale(1.1).move_to([cx,cy,0]).rotate(PI/4)
        circ=Circle(radius=1.45,color=BLUE_TERM).move_to([cx,cy,0])
        verts=[circ.point_from_proportion(i/4) for i in range(4)]
        quad=Polygon(*verts,color=BLUE_TERM,fill_color=BLUE_TERM,fill_opacity=.15)
        ang_p=Angle(Line(verts[1],verts[0]),Line(verts[3],verts[0]),radius=.3,color=GREEN_OK,other_angle=True)
        ang_q=Angle(Line(verts[0],verts[1]),Line(verts[2],verts[1]),radius=.3,color=GREEN_OK,other_angle=True)
        t4=Text("Cyclic quadrilateral: opposite angles add to 180°.",font_size=22,color=TEAL_TERM).move_to([2.6,1.0,0])
        f4=MathTex(r"\angle A+\angle C=180^\circ",color=GREEN_OK).scale(.85).move_to([2.6,.0,0])
        b=beat_group(circ,quad,ang_p,ang_q,t4,f4); self.play(Create(circ),Create(quad),Create(ang_p),Create(ang_q),FadeIn(t4),Write(f4)); self.wait(3); self.play(FadeOut(b))
        animate_final_definition(self,r"\text{Tangent–radius, alternate segment, equal chords, cyclic opposite angles}",r"Four workhorses for angle questions on circles.",final_wait=42)
