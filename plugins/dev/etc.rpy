init python:

    def showimg(img=False):
        if img:
            renpy.show_screen('showimg',img=img)
        else:
            renpy.hide_screen('showimg')

screen showimg(img):
    add img xalign 0.5 yalign 0.5
    

screen rdsa_tools_icons():

    vpgrid:
        cols 10
        spacing 16
        
        for i in sorted(persistent.icon.keys()):
            vbox xsize 80 ysize 80:
                text ico(i) style 'ramen_icon_text' color "#fff"  xalign 0.5
                text i color "#ccc" size 12  xalign 0.5
            
                