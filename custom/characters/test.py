from manimce import *


class SigmaCreature(Scene):
  def construct(self):
      self.camera.background_color = GREY_E
      teacher = sigma_creature(self, mode = 'speaking', color = MAROON_B).to_edge(LEFT + 2*DOWN)
      self.add(teacher)
      speech_bubble = SpeechBubble().scale(0.5).next_to(teacher, RIGHT).shift(3*UP)
      words = Tex(
          "``Mathematics is an important tool...\\\\",
          "in order to understand the nature\\\\",
          "it may be necessary to have\\\\",
          "a deeper understanding of\\\\",
          "mathematical relationships.''").scale(3)
      speech.position_mobject_inside(words)

      self.play(
        Create(speech),
        Write(words),
      )
      self.wait()
      for i in range(3):
          blink_eye(self, mobject = teacher, times = 1, delay = 2.5)
      self.wait(2)
