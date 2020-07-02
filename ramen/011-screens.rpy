init -11 python:

    class ramen_screentools:

        def overlay(self, imgs):
            """
            add overlays image to layer 'master'

            ``` python
                rascr.overlay([
                    [rstreet.overlay['vadd'],(0.0,0.0),(120,220)],
                    [rstreet.overlay['car'],(0.0,1.0),(20,20)],
                    ['flat/overlay/car.webp',(0.0,1.0),(60,620)],

                ])
            ```

            """

            renpy.show_screen('scene_overlay', imgs=imgs)

        def story_skiper(self, label, text='Skip'):
            renpy.show_screen('story_skipbutton', text=text, label=label)

        def notify(self, msg, icon='alert', sfx='beep2', sec=5.0):
            """
            Notify with icon and sound

            ``` python:
                $ notify_icon('You see notification with icon','logo-ramen',5.0,'ring')
                $ renpy.notify("You see renpy default notification.")
            ```

            """

            if not isinstance(msg, (str, unicode, int)):
                msgs = "\n".join(msg)
            else:
                msgs = str(msg)

            if sfx is not None:
                ramu.sfx(sfx)

            renpy.show_screen('notify_ico', message=msgs, icon=icon, sec=sec)

        def hide(self, whats):
            for w in whats:
                renpy.hide(w)
                renpy.hide_screen(w)

    rascr = ramen_screentools()
