from manim import *
from custom.functions import *
from custom.drawings import SpeechBubble, ThoughtBubble


LEFT_EYE_INDEX = 0
RIGHT_EYE_INDEX = 1
LEFT_PUPIL_INDEX = 2
RIGHT_PUPIL_INDEX = 3
BODY_INDEX = 4
MOUTH_INDEX = 5



def sigma_creature(self, mode, color):

    if mode is None:
        body_parts = SVGMobject(get_svg("plain.svg"))
    else:
        body_parts = SVGMobject(get_svg(str(mode) + ".svg"))
    

    body = SVGMobject(get_svg("sigma.svg"))
    eye_parts = body_parts[LEFT_EYE_INDEX : RIGHT_PUPIL_INDEX + 1]
    eye_parts.set_stroke(WHITE)
    mouth = body_parts[MOUTH_INDEX]

    if color is None:
        body.set_color(GREY_BROWN)
    else:
        body.set_color(color)

    mouth.next_to(body.get_top(), DOWN, buff = 0.1)
    mouth.shift(0.10 * RIGHT)
    eye_parts.next_to(body.get_top(), UP, buff = 0.0)
    eye_parts.shift(0.10 * RIGHT)
    eye_parts.add(body, mouth)
    character = eye_parts.scale(1.25)
        
    return character



def look(self, mobject, direction):
    eyes = mobject[LEFT_EYE_INDEX : RIGHT_EYE_INDEX + 1]
    pupils = mobject[LEFT_PUPIL_INDEX : RIGHT_PUPIL_INDEX + 1]
    norm = get_norm(direction)

    if norm == 0:
        return
    direction /= norm

    purposeful_looking_direction = direction

    for pupil, eye in zip(pupils.split(), eyes.split()):
        c = eye.get_center()
        right = eye.get_right() - c
        up = eye.get_top() - c
        vect = direction[0] * right + direction[1] * up
        v_norm = get_norm(vect)
        p_radius = 0.5 * pupil.get_width()
        vect *= (v_norm - 0.75 * p_radius) / v_norm
        pupil.move_to(c + vect)
    pupils[1].align_to(pupils[0], DOWN)



def look_at(self, mobject, point_or_mobject):
    eyes = mobject[LEFT_EYE_INDEX : RIGHT_EYE_INDEX + 1]
    if isinstance(point_or_mobject, Mobject):
        point = point_or_mobject.get_center()
    else:
        point = point_or_mobject
    look(self, mobject, point - eyes.get_center())



def blink_eye(self, mobject, times, delay):
    eye_parts = self.eye_parts = mobject[LEFT_EYE_INDEX : BODY_INDEX]
    eye_parts.save_state()
    eye_bottom_y = eye_parts.get_bottom()[1]

            
    for i in range(times):
        self.play(
            Animation(
                eye_parts.apply_function(
                    lambda p: [p[0], eye_bottom_y, p[2]]
                )
            ),
            run_time = 0.1,
            rate_func = smooth
        )
        self.play(
            Restore(eye_parts),
            run_time = 0.1,
            rate_func = smooth
        )
        self.wait(delay)



def change_mode(self, mobject, new_mode, direction, scale_value):
    body_parts = SVGMobject(get_svg(new_mode + ".svg"))
    body = SVGMobject(get_svg("sigma.svg"))
    body_parts.set_stroke(WHITE, 0.0)
    eye_parts = body_parts[LEFT_EYE_INDEX : RIGHT_PUPIL_INDEX + 1]
    mouth = body_parts[MOUTH_INDEX]

    body.set_color(mobject[BODY_INDEX].get_color())
    mouth.next_to(body.get_top(), DOWN, buff = 0.1)
    mouth.shift(0.10 * RIGHT)
    eye_parts.next_to(body.get_top(), UP, buff = 0.0)
    eye_parts.shift(0.10 * RIGHT)
    eye_parts.add(body, mouth)

    if scale_value is None:
        new_mobject = eye_parts.scale(1.25)
    else:
        new_mobject = eye_parts.scale(1.25 * scale_value)
    
    new_mobject.move_to(mobject)
    look(self, new_mobject, direction)

    return new_mobject

    # self.play(
    #     mobject.animate.become(new_mobject),
    #     # run_time = 0.1,
    #     rate_func = smooth
    # )
