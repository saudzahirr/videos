"""
These Scene are made in 3Blue1Brown's Manim.
These Scenes will be considered as Externally Animated Scenes.
"""

from manimlib import *
from numpy import *


class KleinBottle(ThreeDScene):
    def construct(self):
        frame = self.camera.frame
        frame.reorient(-45, 70)
        frame.add_updater(
            lambda m, dt: m.increment_theta(2 * dt * DEGREES)
        )
        light = self.camera.light_source
        light.move_to([-10, -10, 20])
        self.add(frame)

        klein_bottle = ParametricSurface(
            lambda u, v : np.array([
                (-2/15)*cos(u)*( 3*cos(v) - 30*sin(u) + 90*(cos(u)**4)*sin(u) - 60*(cos(u)**6)*sin(u) + 5*cos(u)*cos(v)*sin(u) ),
                (-1/15)*sin(u)*( 3*cos(v) - 3*(cos(u)**2)*cos(v) - 48*(cos(u)**4)*cos(v) + 48*(cos(u)**6)*cos(v) - 60*sin(u) + 5*cos(u)*cos(v)*sin(u) 
                - 5*(cos(u)**3)*cos(v)*sin(u) - 80*(cos(u)**5)*cos(v)*sin(u) + 80*(cos(u)**7)*cos(v)*sin(u) ),
                (2/15)*( 3 + 5*cos(u)*sin(u) )*sin(v)
                ]),
            u_range = [0, np.pi],
            v_range = [0, 2*np.pi]
        )
        klein_bottle.set_gloss(1.0)
        klein_bottle.set_opacity(0.5)
        klein_bottle.sort_faces_back_to_front(DOWN)
        mesh = SurfaceMesh(klein_bottle, resolution = (21, 11))
        mesh.set_stroke(BLUE, 1, 1)
        klein_bottle = Group(klein_bottle, mesh)
        klein_bottle.move_to(ORIGIN)
        klein_bottle.scale(2)
        self.add(klein_bottle)
        self.wait(2)
