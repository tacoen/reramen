screen input_dialog(prompt,default_value='None',size=(380,150)):

    add ramu.ezfile2(pt.overlays)

    modal True
    zorder 200
    layer "dialog_layer"
    style_prefix "dialog"

    frame:
        ymaximum size[1]
        xsize size[0]+style['dialog_frame'].right_padding+style['dialog_frame'].left_padding
        textbutton ico('close') style 'dialog_closebutton' action Return(default_value)
        
        vbox:
            xalign 0.0
            yalign .5
            spacing 0
            xsize size[0]
            label _(prompt):
                style "dialog_prompt"
                xalign 0.0
            
            null height 8
            input default default_value:
                xminimum size[0]
                
            add ramu.hline((size[0],1),"#666")

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

