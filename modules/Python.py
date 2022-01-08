from manim import *
import numpy as np

def PythonLogo(scale_factor):
    logo = ImageMobject("assets/PythonLogo.png")
    logo.scale(scale_factor)
    return logo