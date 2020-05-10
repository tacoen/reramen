screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign pt.dialogue_text_xalign
            xpos pt.dialogue_xpos
            xsize pt.dialogue_width
            ypos pt.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"


style input_prompt:
    xalign pt.dialogue_text_xalign
    color "#111"

style input:
    xalign pt.dialogue_text_xalign
    xmaximum pt.dialogue_width
