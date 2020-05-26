init -101 python:

    register_plugins(
        title="phone call",
        version="1.0",
        author="tacoen",
        author_url='https://github.com/tacoen/reramen',
        desc="telephone function",
        build=True
    )

    renpy.add_layer('above_screens', above='screens', menu_clear=True)

    # For phone calls

    class ramen_phonecall():

        def incoming(self, npc_id, what=None, type='label',
                     prefix=False, side='oncall', transform=ramen_lb):
            """

            See: phonecall.talk

            ``` python
            $ phonecall.incoming('rita','chat','json')
            ```
            """

            ramen.backto = ramen.label_last
            ramu.sfx(
                'phone-ring',
                plugin('phonecall').dir,
                loop=3,
                fadeout=1,
                fadein=0)

            npc_name = ramu.npc(npc_id, 'name')
            npc_phonenum = ramu.npc(npc_id, 'phonenum')
            color = "#113"

            prefix = "{icon=phone-incoming} Incoming call \n" + \
                npc_name + " (" + npc_phonenum + ")\n\n"

            res = renpy.call_screen('confirm',
                                    message="{color=" + color + "}" +
                                    prefix + "Answer The Call?{/color}",
                                    yes_action=Return(True),
                                    no_action=Return(False),
                                    timeout=26)

            if res:
                renpy.sound.stop()
                result = self.talk(
                    npc_id,
                    what,
                    type,
                    prefix,
                    side='oncall',
                    transform=ramen_lb)
            else:
                renpy.sound.stop()
                narrator('You ignore the call')

            return result

        def outcoming(self, npc_id, what=None, type='label', prefix=False):
            """

            See: phonecall.talk

            ``` python
            $ phonecall.outcoming('rita','chat')
            ```
            """

            ramen.backto = ramen.label_last

            npc_name = ramu.npc(npc_id, 'name')
            npc_phonenum = ramu.npc(npc_id, 'phonenum')

            renpy.show(
                "side " + npc_id + " outcall",
                [ramen_lb],
                layer='above_screens'
            )

            phone_dialing("Calling: " + npc_name
                          + " (" + npc_phonenum + ")...\n"
                          + ("Ring... {w=2.5}" * ramu.random_int(3, 6))
                          + "Ring..."
                          )

            result = self.talk(
                npc_id,
                what,
                type,
                prefix,
                side='oncall',
                transform=ramen_lb)

            if not result:
                narrator(npc_name + " didn't answer your call.")
                return False
            else:
                return result

        def talk(self, npc_id, what=None, type='label',
                 prefix=False, side='oncall', transform=ramen_lb):
            """

            ``` python
            $ phonecall.talk('rita','chat','json','01','oncall',ramen_lb)
            ```

            ### Keyword arguments:

            | # | Key | Description |
            | --- | --- | --- |
            | 0 | npc_id | npc.id to talk with |
            | 1 | what | json topic / label |
            | 2 | type | json or label |
            | 3 | prefix | topic id / label prefix |
            | 4 | side | side image template |
            | 5 | transform | atl to use by side image |

            See: ramen_util.talk

            """

            renpy.hide(npc_id)
            renpy.show(
                'side ' + npc_id + ' ' + side.lower(),
                at_list=[transform],
                zorder=99,
                layer='above_screens'
            )

            return ramu.talk(npc_id=npc_id, what=what,
                             type=type, prefix=prefix)

        def cb_dialing(self, event, interact=False, **kwargs):
            """Provide callback function for `phone_dialing`."""
            if event == "show_done":
                ramu.sfx('phone-dial', plugin('phonecall').dir)
            elif event == "end":
                renpy.sound.stop()

        def cb_hangup(self, event, interact=False, **kwargs):
            """Provide callback function for `phone_hangup`."""
            if event == "show_done":
                ramu.sfx('phone-close', plugin('phonecall').dir)
            elif event == "end":
                renpy.sound.stop()

    phonecall = ramen_phonecall()

init offset = -1

define phone_dialing = Character(None, callback=phonecall.cb_dialing)
define phone_hangup = Character(None, callback=phonecall.cb_hangup)
