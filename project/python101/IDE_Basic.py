#  IDE_Basic.py

from manim import *
from manim.utils.unit import Pixels
import numpy as np
import sys
sys.path.insert(0, "modules")
import NAugxst as NAugxst
import Python as Python

#     ___    __    __   _   __
#    | |_)  / /\  ( (` | | / /`
#    |_|_) /_/--\ _)_) |_| \_\_

class Basic(MovingCameraScene):
    def draw_code_all_lines_at_a_time(self, code, **kwargs):
        self.play(LaggedStart(*[
                Write(code[i])
                for i in range(code.__len__())
            ]),
            **kwargs
        )

    def get_remark_rectangle(
            self,
            code,
            line,
            fill_opacity=0.2,
            stroke_width=0,
            fill_color=YELLOW,
            **kwargs):
        lines = VGroup(code[2],code[1])
        w, h = getattr(lines, "width"), getattr(lines, "height")
        frame = Rectangle(width=w,height=h)

        code_line = code[1][line-1]
        line_rectangle = Rectangle(
            width=w,
            height=getattr(code[1][line-1],"height")*1.5,
            fill_opacity=fill_opacity,
            stroke_width=stroke_width,
            fill_color=fill_color,
            **kwargs
        )
        line_rectangle.set_y(code_line.get_y())
        line_rectangle.scale([1.1,1,1])
        return line_rectangle

    def change_line(self, code, rect, next_line, *args, **kwargs):
        self.play(
            Transform(
                rect,
                self.get_remark_rectangle(code, next_line),
            ),
            *args,
            **kwargs,
        )

    def construct(self):
        self.introduction()
        self.intro()
        self.ide()
        self.colab()
        self.print_func1()
        self.print_func2()
        self.print_func3()
        self.print_func4()
        self.input_func()
        self.beforenewchapter()
        self.outro()

    def introduction(self):
        self.wait(5)

        text_q1 = Text("เครื่องมือพัฒนาโปรแกรม", font="Sarabun").scale(0.7)
        text_q1.move_to([0, 1, 0])
        rect_q1 = Rectangle(height=text_q1.height+0.4, width=text_q1.width+0.4).move_to(text_q1)
        q1 = Group(text_q1, rect_q1).set_color(WHITE)
        self.play(FadeIn(q1))
        self.wait(4)

        text_q2 = Text("การเขียนโปรแกรมอย่างง่าย", font="Sarabun").scale(0.7)
        text_q2.move_to([0, -1, 0])
        rect_q2 = Rectangle(height=text_q2.height+0.4, width=text_q2.width+0.4).move_to(text_q2)
        q2 = Group(text_q2, rect_q2).set_color(WHITE)
        self.play(FadeIn(q2))
        self.wait(3)

        self.wait(1)
        self.remove(q1, q2)

    def intro(self):
        logo = NAugxst.NAugxstLogo()
        self.add_sound("assets/Intro_sound.wav")
        self.play(FadeIn(logo))
        self.wait(0.5)

        path = Line([0, 0, 0], [0, 1, 0])
        self.play(MoveAlongPath(logo, path))
        self.wait(0.5)

        vector_text = np.array([0, -1, 0])

        text = Tex("NAugxst")
        text.move_to(vector_text)
        self.play(Create(text))
        self.wait(4)
        self.remove(logo)
        self.remove(text)

    def ide(self):
        text1 = Text("เครื่องมือพัฒนาโปรแกรม", font="Sarabun").scale(0.7)
        line = Line(LEFT*6.5, RIGHT*6.5)
        text1.to_edge(UP)
        line.next_to(text1, DOWN, buff=0.1)
        self.wait(1)
        self.play(Create(text1))
        self.play(Create(line))
        self.wait(1)

        self.wait(6)

        divide = Line([0, 2.5, 0], [0, -3.5, 0])
        self.play(Create(divide))

        self.wait(3)

        offline = Tex(r"\underline{Offline}")
        online = Tex(r"\underline{Online}")
        offline.move_to([-5.8, 2.1, 0])
        online.move_to([1, 2.1, 0])
        self.play(Create(offline))
        self.wait(7)
        self.play(Create(online))
        self.wait(8)
        
        self.wait(4)

        ide1 = Tex("Py", "Charm")
        ide1[0].set_color(YELLOW)
        ide1[1].set_color(GREEN)
        ide2 = Tex("Visual Studio Code").set_color(BLUE)
        ide3 = Tex("Atom").set_color(GREEN)
        etc1 = Tex("etc.")
        group_offline = VGroup(ide1, ide2, ide3, etc1).arrange(direction=DOWN, aligned_edge=LEFT)
        group_offline.scale_in_place(1).next_to(offline, DR, buff=0.25)
        pycharm = ImageMobject("assets\PyCharmLogo.png").scale(13/60).move_to([-5.8, -2.5, 0])
        vscode = ImageMobject("assets\VSCodeLogo.png").scale(13/120).move_to([-3.8, -2.5, 0])
        atom = ImageMobject("assets\AtomLogo.png").scale(65/512).move_to([-1.8, -2.5, 0])
        self.play(Create(group_offline.submobjects[0]), FadeIn(pycharm))
        self.wait(1)
        self.play(Create(group_offline.submobjects[1]), FadeIn(vscode))
        self.wait(2)
        self.play(Create(group_offline.submobjects[2]), FadeIn(atom))
        self.play(Create(group_offline.submobjects[3]))
        self.wait(2)

        self.wait(4)

        ide4 = Tex("Google Colab").set_color(YELLOW)
        ide5 = Tex("Replit").set_color(BLUE)
        etc2 = Tex("etc.")
        group_online = VGroup(ide4, ide5, etc2).arrange(direction=DOWN, aligned_edge=LEFT)
        group_online.scale_in_place(1).next_to(online, DR, buff=0.25)
        colab = ImageMobject("assets\ColabLogo.png").scale(1/2).move_to([2, -2.5, 0])
        replit = ImageMobject("assets\ReplitLogo.png").scale(13/120).move_to([4, -2.5, 0])
        self.play(Create(group_online.submobjects[0]), FadeIn(colab))
        self.wait(1)
        self.play(Create(group_online.submobjects[1]), FadeIn(replit))
        self.play(Create(group_online.submobjects[2]))
        self.wait(2)

        self.wait(1)
        self.wait(6)
        self.play(ide4.animate.scale(1.2))
        self.play(colab.animate.scale(2))
        self.wait(1)

        self.play(FadeOut(text1, line, divide, offline, online, group_online, group_offline,
                          pycharm, vscode, atom, colab, replit))
        self.wait(1)

    def colab(self):
        text = Text("Google Colab", font="Sarabun").scale(0.7)
        line = Line(LEFT*6.5, RIGHT*6.5)
        text.to_edge(UP)
        line.next_to(text, DOWN, buff=0.1)
        self.wait(1)
        self.play(Create(text))
        self.play(Create(line))
        self.wait(1)
        self.wait(6)

        link = Tex("https://colab.research.google.com").scale(1.1).move_to(ORIGIN)
        self.play(Create(link))
        self.wait(2)
        self.play(Uncreate(link))
        self.wait(5)

        colab1 = ImageMobject("assets\python101\Basic\colab1.jpg").set_z_index(-1).move_to([0, -0.5, 0])
        self.play(FadeIn(colab1))
        self.wait(4)
        move_r_cl1 = np.array([2.625, -2.95, 0])
        rect_colab1 = Rectangle(width=135*Pixels, height=38*Pixels).set_color(YELLOW)
        rect_colab1.move_to(move_r_cl1)
        self.play(Create(rect_colab1))
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(move_r_cl1).set(width=135*Pixels).scale(2))
        self.wait(4)
        self.play(Restore(self.camera.frame))
        self.play(FadeOut(colab1, rect_colab1))

        colab2 = ImageMobject("assets\python101\Basic\colab2.jpg").set_z_index(-1)
        colab2.scale(0.7).move_to(ORIGIN)
        self.play(FadeIn(colab2))
        self.wait(7)
        self.wait(4)
        move_r_cl2_1 = np.array([-4.025, 2.3, 0])
        rect_colab2_1 = Rectangle(width=193*Pixels, height=37*Pixels).set_color(YELLOW)
        rect_colab2_1.scale(0.7).move_to(move_r_cl2_1)
        self.play(Create(rect_colab2_1))
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(move_r_cl2_1).set(width=135*Pixels).scale(2))
        self.wait(1)
        self.play(Restore(self.camera.frame))
        self.play(FadeOut(rect_colab2_1))

        move_r_cl2_2 = np.array([-3.55, 2, 0])
        rect_colab2_2 = Rectangle(width=420*Pixels, height=74*Pixels).set_color(YELLOW)
        rect_colab2_2.scale(0.7).move_to(move_r_cl2_2)
        self.play(Create(rect_colab2_2))
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(move_r_cl2_2).set(width=155*Pixels).scale(2))
        self.wait(1)
        self.play(Restore(self.camera.frame))
        self.play(FadeOut(rect_colab2_2))

        move_r_cl2_3 = np.array([4.15, 1.65, 0])
        rect_colab2_3 = Rectangle(width=282*Pixels, height=41*Pixels).set_color(YELLOW)
        rect_colab2_3.scale(0.7).move_to(move_r_cl2_3)
        self.play(Create(rect_colab2_3))
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(move_r_cl2_3).set(width=135*Pixels).scale(2))
        self.wait(2)
        self.play(Restore(self.camera.frame))
        self.play(FadeOut(rect_colab2_3, colab2, text, line))
        self.wait(1)

        self.wait(4)
        filename = Tex("Basic.ipynb").scale(1.1).move_to(ORIGIN)
        self.play(Create(filename))
        self.wait(4)
        self.play(Uncreate(filename))
        self.wait(1)
        
    def print_func1(self):
        raw_code1 = '''print("Hello, World!")'''
        code1 = Code(code=raw_code1, tab_width=4, background="window", language="Python", font="Monospace")
        code1.move_to(ORIGIN)
        self.draw_code_all_lines_at_a_time(code1, run_time=2)
        self.wait(8)
        self.play(code1.animate.to_edge(UP).scale(1.2))
        self.wait(6)

        FRAME_SCALE = 0.45
        frame = Rectangle(
            width=config["frame_width"],
            height=config["frame_height"],
        )
        frame.scale(FRAME_SCALE)
        frame.next_to(code1,DOWN)

        self.wait(7)
        self.wait(3)

        self.play(Create(frame))
        self.wait(1)
        line = self.get_remark_rectangle(code1, 1)
        line.save_state()
        line.stretch(0.01,0)
        self.add(line)
        self.play(Restore(line))
        self.wait(9)
        output1 = Tex("Hello, World!")
        output1.scale(FRAME_SCALE*2)

        beforeul = frame.get_vertices()
        ul = beforeul[1] + np.array([1.4, -0.4, 0])

        output1.move_to(ul)
        self.play(Create(output1))
        self.wait(8)
        self.play(FadeOut(code1, frame, line, output1))

    def print_func2(self):
        raw_code2 = '''print("8-2")
print(8-2)
'''
        code2 = Code(code=raw_code2, tab_width=4, background="window", language="Python", font="Monospace")
        code2.move_to(ORIGIN)
        self.wait(15)
        self.draw_code_all_lines_at_a_time(code2, run_time=2)
        self.wait(8)
        self.play(code2.animate.to_edge(UP).scale(1.2))
        self.wait(6)

        FRAME_SCALE = 0.45
        frame = Rectangle(
            width=config["frame_width"],
            height=config["frame_height"],
        )
        frame.scale(FRAME_SCALE)
        frame.next_to(code2,DOWN)

        self.wait(9)
        self.wait(3)

        self.play(Create(frame))
        self.wait(1)
        line = self.get_remark_rectangle(code2, 1)
        line.save_state()
        line.stretch(0.01,0)
        self.add(line)
        self.play(Restore(line))
        self.wait(11)
        output1 = Tex("8-2")
        output1.scale(FRAME_SCALE*2)

        beforeul = frame.get_vertices()
        ul = beforeul[1] + np.array([0.4, -0.4, 0])

        output1.move_to(ul)
        self.play(Create(output1))
        self.wait(1)

        self.change_line(code2, line, 2)
        self.wait(10)
        output2 = Tex("6")
        output2.scale(FRAME_SCALE*2)
        output2.next_to(output1, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(Create(output2))
        self.wait(1)

        self.play(FadeOut(code2, frame, line, output1, output2))

    def print_func3(self):
        raw_code3 = '''language = "Python"
print(language)
'''
        code3 = Code(code=raw_code3, tab_width=4, background="window", language="Python", font="Monospace")
        code3.move_to(ORIGIN)
        self.wait(15)
        self.draw_code_all_lines_at_a_time(code3, run_time=2)
        self.wait(8)
        self.play(code3.animate.to_edge(UP).scale(1.2))
        self.wait(6)

        FRAME_SCALE = 0.45
        frame = Rectangle(
            width=config["frame_width"],
            height=config["frame_height"],
        )
        frame.scale(FRAME_SCALE)
        frame.next_to(code3,DOWN)

        self.wait(6)
        self.wait(3)

        self.play(Create(frame))
        self.wait(1)
        line = self.get_remark_rectangle(code3, 1)
        line.save_state()
        line.stretch(0.01,0)
        self.add(line)
        self.play(Restore(line))
        self.wait(5)
        output1 = SingleStringMathTex(r'\text{language} \to \ "\text{Python}"').set_color(GREY)
        output1.scale(FRAME_SCALE*2)

        beforeul = frame.get_vertices()
        ul = beforeul[1] + np.array([0.85, -0.4, 0])

        output1.move_to([0, -2.7, 0])
        self.play(Create(output1))
        self.wait(1)

        self.change_line(code3, line, 2)
        self.wait(7)
        self.wait(9)
        output2 = Tex("Python")
        output2.scale(FRAME_SCALE*2)
        output2.move_to(ul)
        self.play(Create(output2))
        self.wait(1)

        self.play(FadeOut(code3, frame, line, output1, output2))
        self.wait(1)

    def print_func4(self):
        raw_code4 = '''number = 12
print(number)
'''
        code4 = Code(code=raw_code4, tab_width=4, background="window", language="Python", font="Monospace")
        code4.move_to(ORIGIN)
        self.wait(15)
        self.draw_code_all_lines_at_a_time(code4, run_time=2)
        self.wait(8)
        self.play(code4.animate.to_edge(UP).scale(1.2))
        self.wait(6)

        FRAME_SCALE = 0.45
        frame = Rectangle(
            width=config["frame_width"],
            height=config["frame_height"],
        )
        frame.scale(FRAME_SCALE)
        frame.next_to(code4,DOWN)

        self.wait(6)
        self.wait(3)

        self.play(Create(frame))
        self.wait(1)
        line = self.get_remark_rectangle(code4, 1)
        line.save_state()
        line.stretch(0.01,0)
        self.add(line)
        self.play(Restore(line))
        self.wait(5)
        output1 = SingleStringMathTex(r'\text{number} \to \ 12').set_color(GREY)
        output1.scale(FRAME_SCALE*2)

        beforeul = frame.get_vertices()
        ul = beforeul[1] + np.array([0.4, -0.4, 0])

        output1.move_to([0, -2.7, 0])
        self.play(Create(output1))
        self.wait(1)

        self.change_line(code4, line, 2)
        self.wait(7)
        self.wait(9)
        output2 = Tex("12")
        output2.scale(FRAME_SCALE*2)
        output2.move_to(ul)
        self.play(Create(output2))
        self.wait(1)

        self.play(FadeOut(code4, frame, line, output1, output2))
        self.wait(1)

    def input_func(self):
        raw_code5 = '''book = input("Enter your book name: ")
print(book)
'''
        code5 = Code(code=raw_code5, tab_width=4, background="window", language="Python", font="Monospace")
        code5.move_to(ORIGIN)
        self.wait(15)
        self.draw_code_all_lines_at_a_time(code5, run_time=2)
        self.wait(8)
        self.play(code5.animate.to_edge(UP).scale(1.2))
        self.wait(6)

        FRAME_SCALE = 0.45
        frame = Rectangle(
            width=config["frame_width"],
            height=config["frame_height"],
        )
        frame.scale(FRAME_SCALE)
        frame.next_to(code5,DOWN)

        self.wait(5)
        self.wait(6)
        self.wait(3)

        self.play(Create(frame))
        self.wait(1)
        line = self.get_remark_rectangle(code5, 1)
        line.save_state()
        line.stretch(0.01,0)
        self.add(line)
        self.play(Restore(line))
        self.wait(11)
        self.wait()
        ask1 = Tex("Enter your book name: ", "Python 101").scale(0.5)
        ask1[1].set_color(YELLOW)
        output1 = SingleStringMathTex(r'\text{book} \to \ "\text{Python 101}"').set_color(GREY)
        output1.scale(FRAME_SCALE*2)

        beforeul = frame.get_vertices()
        ul = beforeul[1] + np.array([2, -0.4, 0])

        ask1.move_to(ul)
        self.play(Create(ask1[0]))
        self.wait(1)
        self.play(AddTextLetterByLetter(ask1[1]), run_time=3)
        self.wait(1)
        self.wait(3)

        output1.move_to([0, -2.7, 0])
        self.play(Create(output1))
        self.wait(2)

        self.change_line(code5, line, 2)
        self.wait(6)
        self.wait(6)
        output2 = Tex("Python 101").scale(0.5)
        output2.next_to(ask1, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(Create(output2))
        self.wait(6)

        self.play(FadeOut(code5, frame, line, ask1, output1, output2))
        self.wait(1)
        
    def beforenewchapter(self):
        raw_code1 = '''a = 5
b = -4
c = a - b
print(c)
'''
        code1 = Code(code=raw_code1, tab_width=4, background="window",
                            language="Python", font="Monospace").move_to([0, 1.5, 0])

        raw_code2 = '''x = int(input("x = "))
y = x**2 + 4
print("y =", y)
'''
        code2 = Code(code=raw_code2, tab_width=4, background="window",
                            language="Python", font="Monospace").move_to([0, -1.5, 0])

        self.play(Create(code1), run_time=2)
        self.play(Create(code2), run_time=2)
        self.wait(2)
        self.play(FadeOut(code1, code2), run_time=2)
        self.wait(1)

    def outro(self):
        youtube = ImageMobject("assets/YoutubeLogo.png").scale(15/128)
        twitter = ImageMobject("assets/TwitterLogo.png").scale(1/5)
        github = ImageMobject("assets/GithubLogo.png")
        youtube.move_to(np.array([-3, 2, 0]))
        twitter.move_to(np.array([-3, 0, 0]))
        github.move_to(np.array([-3, -2, 0]))

        youtube_text = Tex("NAugxst").next_to(youtube, RIGHT, buff=0.5)
        twitter_text = Tex("@AugxstN").next_to(twitter, RIGHT, buff=0.5)
        github_text = Tex("NAugxst").next_to(github, RIGHT, buff=0.5)

        self.wait(2)
        self.wait(10)

        self.play(FadeIn(youtube))
        self.play(FadeIn(twitter))
        self.play(FadeIn(github))

        self.play(Create(youtube_text))
        self.play(Create(twitter_text))
        self.play(Create(github_text))

        self.wait(10)

#    _____  _     _     _      ___   _       __    _   _
#     | |  | |_| | | | | |\/| | |_) | |\ |  / /\  | | | |
#     |_|  |_| | \_\_/ |_|  | |_|_) |_| \| /_/--\ |_| |_|__

class Thumbnail(Scene):
    def construct(self):
        logo = Python.PythonLogo(0.3)
        text = Tex("101")
        logo.move_to([-2, 0, 0])
        text.move_to([1, 0, 0])
        text.scale(4)
        first_group = Group(logo, text)
        first_group.move_to([0, 2, 0])
        self.add(first_group)

        number = Tex("1)")
        number.scale(4)
        number.next_to(logo, LEFT, buff=1.25)
        self.add(number)

        line = Line(LEFT*6.5, RIGHT*6.5)
        line.move_to(ORIGIN)
        self.add(line)

        c1_1 = Text("เครื่องมือพัฒนาโปรแกรม", font="Sarabun").set_color(WHITE).scale(1.5)
        c1_2 = Text("การเขียนโปรแกรมอย่างง่าย", font="Sarabun").set_color(WHITE).scale(1.5)
        c1_1.move_to([0, -1, 0])
        c1_2.move_to([0, -3, 0])
        self.add(c1_1, c1_2)
