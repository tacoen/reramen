image dim = Solid('#000c')

init -2 python:

    quotes=[
        'Just like this town, everything as it was.',
        'I mumble like this. Sometimes is a loop.',
        'This place bring back some memories.',
        'Just like old times, a new me everyday.',
        'San Hila, this town remains gray for me,{w=1}\nall the times.',
        'I Wonder where are the people.',
        'Sometimes life is holding-on.\n{w=1}Sometimes let it go.',
        'Why '+ ramu.random_of(paper.subject) +" keep poping in my head?"
    ]

    class solo():
        """
        Solo is a set of renpy/python script. It's require manything,
        so it has to be set in higher init number.

        ### Require this object/parameter to be set earlier:
        * mcp = ramen_npc('mcp')
        * mc pose/sprite anim
        * mc.stats
        """

        def quote(self):

            thought(ramu.random_of(quotes))

        def sleep(self, full=True, pose='sleep0',):
            """
            ``` python
                solo().sleep(False,'sleep0')
            ```
            * Napping with 'sleep0' pose/attr (usually a sprite anim)
            """

            renpy.hide_screen('smphone_ui')
            hud.active = False

            if full:
                max = pe.limit[1]-mc.stat['vital']
            else:
                max = 3

            renpy.show_screen('hud_stats', stats=['vital'])
            renpy.show('mcp '+pose)

            if full:
                renpy.show('dim')

            for i in range(0, max):
                renpy.pause(1, True)
                wotime=ramentime.adv(0.5)
                mc.stat['vital'] += 1
            renpy.hide('dim')
            renpy.pause(1, True)
            renpy.hide('mcp')

            hud.active = True

            if full:
                notify_ico('You gain your vitality back.', 'arrow-up-left')

            renpy.hide_screen('hud_stats')
