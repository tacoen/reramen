init -100 python:

    # For phone calls
    
    def phone_in(npc_id, type='label', what=None):

        renpy.sound.play(
           plugin('phone')['dir']+'/audio/phone-ring.mp3',
           channel='sound',
           loop=3,
           fadeout=1,
           fadein=0)

        npc_name = npc_get(npc_id,'name')
        npc_phonenum = npc_get(npc_id,'phonenum')
        color = "#113"
        
        prefix = "{icon=phone-incoming} Incoming call \n"+npc_name+" ("+npc_phonenum+")\n\n"
           
        res = renpy.call_screen('confirm',\
            message="{color="+color+"}"+prefix+"Answer The Call?{/color}",\
            yes_action=Return(True),
            no_action=Return(False),\
            timeout=26)

        if res: 
            renpy.sound.stop()
            result = side_talk(npc_id,type,what)
        else:
            renpy.sound.stop()
            narrator('You ignore the call')
            
        return result

    def phone_out(npc_id, type='label', what=None):
    
        npc_name = npc_get(npc_id,'name')
        npc_phonenum = npc_get(npc_id,'phonenum')

        renpy.show(
            "side "+npc_id+" outcall",
            [ramen_lb],
            zorder=99,
            layer='above_screens'
            )
                
        phone_dialing("Calling: " + npc_name \
            + " (" + npc_phonenum + ")...\n" \
            + ("Ring... {w=2.5}" * ramu.random_int(3, 6)) \
            + "Ring..."
        )    

        result = side_talk(npc_id,type,what)
        
        if not result:
            narrator(npc_name + "didn't answer your call.")
    

    def side_talk(npc_id, type='label', what=None, side='oncall', transform=ramen_lb):
    
        renpy.hide(npc_id)
        
        renpy.show(
            'side '+ npc_id + ' '+side.lower(),
            at_list=[transform],
            zorder=99,
            layer='above_screens'
        )
        
        if type == 'json':
            pass
        else:
        
            if renpy.has_label(npc_id + '_' + what):
                renpy.call_in_new_context(npc_id + '_' + what)
                return True
            else:
                if renpy.has_label(what):
                    renpy.call_in_new_context(what)
                    return True
                    
        return False

    def ramen_phone_cb_dialing(event, interact=False, **kwargs):
        """Provide callback function for `phone_dialing`."""
        if event == "show_done":
            ramu.sfx('phone-dial',plugin('phone')['dir']+"/audio")
        elif event == "end":
            renpy.sound.stop()

    def ramen_phone_cb_hangup(event, interact=False, **kwargs):
        """Provide callback function for `phone_hangup`."""
        if event == "show_done":
            ramu.sfx('phone-close',plugin('phone')['dir']+"/audio")
        elif event == "end":
            renpy.sound.stop()

init offset=-1

define phone_dialing = Character(None,callback=ramen_phone_cb_dialing)
define phone_hangup = Character(None,callback=ramen_phone_cb_hangup)