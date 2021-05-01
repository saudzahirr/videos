from manim import *

class ThreeBodiesInSpace(SpecialThreeDScene):
    CONFIG = {
        "masses": [1, 6, 3],
        "colors": [RED_E, GREEN_E, BLUE_E],
        "G": 0.5,
        "play_time": 60,
    }

    def construct(self):
        self.add_axes()
        self.add_bodies()
        self.add_trajectories()
        self.let_play()

    def add_axes(self):
        axes = self.axes = self.get_axes()
        axes.set_stroke(width=0.5)
        self.add(axes)

        # Orient
        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-110 * DEGREES,
        )
        self.begin_ambient_camera_rotation()

    def add_bodies(self):
        masses = self.masses
        colors = self.colors

        bodies = self.bodies = VGroup()
        velocity_vectors = VGroup()

        centers = self.get_initial_positions()

        for mass, color, center in zip(masses, colors, centers):
            body = self.get_sphere(
                checkerboard_colors=[
                    color, color
                ],
                color=color,
                stroke_width=0.1,
            )
            body.set_opacity(0.75)
            body.mass = mass
            body.radius = 0.08 * np.sqrt(mass)
            body.set_width(2 * body.radius)

            body.point = center
            body.move_to(center)

            body.velocity = self.get_initial_velocity(
                center, centers, mass
            )

            vect = self.get_velocity_vector_mob(body)

            bodies.add(body)
            velocity_vectors.add(vect)

        total_mass = np.sum([body.mass for body in bodies])
        center_of_mass = reduce(op.add, [
            body.mass * body.get_center() / total_mass
            for body in bodies
        ])
        average_momentum = reduce(op.add, [
            body.mass * body.velocity / total_mass
            for body in bodies
        ])
        for body in bodies:
            body.shift(-center_of_mass)
            body.velocity -= average_momentum

    def get_initial_positions(self):
        return [
            np.dot(
                4 * (np.random.random(3) - 0.5),
                [RIGHT, UP, OUT]
            )
            for x in range(len(self.masses))
        ]

    def get_initial_velocity(self, center, centers, mass):
        to_others = [
            center - center2
            for center2 in centers
        ]
        velocity = 0.2 * mass * normalize(np.cross(*filter(
            lambda diff: get_norm(diff) > 0,
            to_others
        )))
        return velocity

    def add_trajectories(self):
        def update_trajectory(traj, dt):
            new_point = traj.body.point
            if get_norm(new_point - traj.get_points()[-1]) > 0.01:
                traj.add_smooth_curve_to(new_point)

        for body in self.bodies:
            traj = VMobject()
            traj.body = body
            traj.start_new_path(body.point)
            traj.set_stroke(body.color, 1, opacity=0.75)
            traj.add_updater(update_trajectory)
            self.add(traj, body)

    def let_play(self):
        bodies = self.bodies
        bodies.add_updater(self.update_bodies)
        # Break it up to see partial files as
        # it's rendered
        self.add(bodies)
        for x in range(int(self.play_time)):
            self.wait()

    #
    def get_velocity_vector_mob(self, body):
        def draw_vector():
            center = body.get_center()
            vect = Arrow(
                center,
                center + body.velocity,
                buff=0,
                color=RED,
            )
            vect.set_shade_in_3d(True)
            return vect
            # length = vect.get_length()
            # if length > 2:
            #     vect.scale(
            #         2 / length,
            #         about_point=vect.get_start(),
            #     )
        return always_redraw(draw_vector)

    def update_bodies(self, bodies, dt):
        G = self.G

        num_mid_steps = 1000
        for x in range(num_mid_steps):
            for body in bodies:
                acceleration = np.zeros(3)
                for body2 in bodies:
                    if body2 is body:
                        continue
                    diff = body2.point - body.point
                    m2 = body2.mass
                    R = get_norm(diff)
                    acceleration += G * m2 * diff / (R**3)
                body.point += body.velocity * dt / num_mid_steps
                body.velocity += acceleration * dt / num_mid_steps
        for body in bodies:
            body.move_to(body.point)
        return bodies


class AltThreeBodiesInSpace(ThreeBodiesInSpace):
    CONFIG = {
        "random_seed": 6,
        "masses": [1, 2, 6],
    }


class TwoBodiesInSpace(ThreeBodiesInSpace):
    CONFIG = {
        "colors": [GREY, BLUE],
        "masses": [6, 36],
        "play_time": 60,
    }

    def construct(self):
        self.add_axes()
        self.add_bodies()
        self.add_trajectories()
        self.add_velocity_vectors()
        self.add_force_vectors()
        self.let_play()

    def add_bodies(self):
        super().add_bodies()
        for body in self.bodies:
            body.point = 3 * normalize(body.get_center())
            # body.point += 2 * IN
            # body.velocity += (4 / 60) * OUT
            body.move_to(body.point)

    def get_initial_positions(self):
        return [
            np.dot(
                6 * (np.random.random(3) - 0.5),
                [RIGHT, UP, ORIGIN]
            )
            for x in range(len(self.masses))
        ]

    def get_initial_velocity(self, center, centers, mass):
        return 0.75 * normalize(np.cross(center, OUT))

    def add_velocity_vectors(self):
        vectors = VGroup(*[
            self.get_velocity_vector(body)
            for body in self.bodies
        ])
        self.velocity_vectors = vectors
        self.add(vectors)

    def get_velocity_vector(self, body):
        def create_vector(b):
            v = Vector(
                b.velocity,
                color=RED,
                max_stroke_width_to_length_ratio=3,
            )
            v.set_stroke(width=3)
            v.shift(
                b.point + b.radius * normalize(b.velocity) -
                v.get_start(),
            )
            v.set_shade_in_3d(True)
            return v
        return always_redraw(lambda: create_vector(body))

    def add_force_vectors(self):
        vectors = VGroup(*[
            self.get_force_vector(b1, b2)
            for (b1, b2) in (self.bodies, self.bodies[::-1])
        ])
        self.force_vectors = vectors
        self.add(vectors)

    def get_force_vector(self, body1, body2):
        def create_vector(b1, b2):
            r = b2.point - b1.point
            F = r / (get_norm(r)**3)
            v = Vector(
                4 * F,
                color=YELLOW,
                max_stroke_width_to_length_ratio=3,
            )
            v.set_stroke(width=3)
            v.shift(
                b1.point + b1.radius * normalize(F) -
                v.get_start(),
            )
            v.set_shade_in_3d(True)
            return v
        return always_redraw(lambda: create_vector(body1, body2))


class TwoBodiesWithZPart(TwoBodiesInSpace):
    def add_bodies(self):
        super().add_bodies()
        for body in self.bodies:
            body.point += 3 * IN
            body.velocity += (6 / 60) * OUT
