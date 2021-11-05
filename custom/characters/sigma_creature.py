from manim import *
from custom.drawings import SpeechBubble, ThoughtBubble



def sigma_creature(self, mode, color):
    sigma_creature = SVGMobject('number_creature.svg')
    sigma = SVGMobject('sigma.svg')
    speaking = SVGMobject('speaking.svg')
    happy = SVGMobject('happy.svg')
    gracious = SVGMobject('gracious.svg')
    angry = SVGMobject('angry.svg')
    sad = SVGMobject('sad.svg')
    pondering = SVGMobject('pondering.svg')
    
    if mode == 'speaking':
        mouth = speaking
    elif mode == 'happy':
        mouth = happy
    elif mode == 'gracious':
        mouth = gracious
    elif mode == 'sad':
        mouth = sad
    elif mode == 'angry':
        mouth = angry
    elif mode == 'pondering':
        mouth = pondering
    else:
        mouth = happy
        
    if color == None:
        sigma.set_color(GREY_BROWN)
    else:
        sigma.set_color(color)
    sigma.scale(0.85)
    sigma.move_to(sigma_creature[4])
    sigma.shift(0.15 * LEFT + 0.05 * UP)
    sigma_creature.remove(sigma_creature[4])
    sigma_creature.add(sigma)
    sigma_creature.add(mouth[5].next_to(sigma_creature[0:2], 0.5 * DOWN))
    sigma_creature.scale(2)
    sigma_creature[4].move_to(sigma_creature[5])
    sigma_creature.remove(sigma_creature[4])
        
    return sigma_creature
    

    
