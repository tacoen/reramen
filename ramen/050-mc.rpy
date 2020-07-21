init -50 python:

    mcpersonality = ramen_persistent('mcpersonality')
    mcpersonality.comment ={}
    mcpersonality.comment['mumble'] = ['I am mumbling', 'Hmm....']

    ramen.doing_solo = True
    ramen.solo_item = None
    ramen.solo_goto = None
    ramen.solo_inv = 'storage'

    class ramen_mcfunction():

        """
        ramen_mcfunction is a set of renpy/python script. It's require manything,
        so it has to be set in higher init number.

        ### Require this object/parameter to be set earlier:
        * mcp = ramen_npc('mcp')
        * mc pose/sprite anim
        * mc.stats
        """

        def pay(self, value, sfx=True):
            if mc.money['cash'] > value:
                mc.money['cash'] -=  value
            if sfx:
                ramu.sfx('money-pay')
            return mc.money['cash']

        def gain(self, value, sfx=True):
            mc.money['cash'] += value
            if sfx:
                ramu.sfx('beep')
                renpy.show_screen('hud_cash', notif=True)
            return mc.money['cash']

        def bankgain(self, value, sfx=True):
            mc.money['bank'] +=  value
            if sfx:
                ramu.sfx('tone1')
            return mc.money['bank']

        def bankpay(self, value, sfx=True):
            if mc.money['bank'] >  value:
                mc.money['bank'] -= value
            if sfx:
                ramu.sfx('tone0')
            return mc.money['bank']

        def score(self, value, sfx=True):
            ramu.sfx('score')
            renpy.show_screen('hud_score', notif=True)
            mc.score['point'] += value

            #renpy.block_rollback()
            #return mc.score['point']

        def withdrawn(self, ammount):
            if mc.money['bank'] >= ammount:
                mc.money['bank'] -= ammount
                mc.money['cash'] += ammount
                return True
            else:
                return False

        def deposite(self, ammount):
            if mc.money['cash'] >= ammount:
                mc.money['bank'] += ammount
                mc.money['cash'] -= ammount
                return True
            else:
                return False

        def stat(self,which,value=1):
            mc.stat[which] = ramu.limits(mc.stat[which]+value)
            return mc.stat[which]

        def trait(self, which, value=1):
            mc.skill[which] = ramu.limits(mc.skill[which]+value)
            return mc.skill[which]

            
        def mumble(self, topic='mumble'):
            thought(self.commenting(topic))

        def commenting(self, label):

            try:
                return ramu.random_of(mcpersonality.comment[label]).capitalize()
            except BaseException:
                return 'How randomize is random was.'

        def skill_preferer(self, what=None):

            order=sorted(mc.skill.items(), key=lambda x: x[1], reverse=True)
            if len(order[0][0]) <= 3:
                return order[0][0].upper()
            else:
                return order[0][0].title()

        def doing(self, **kwargs):

            try:
                kwargs['cost']
            except BaseException:
                kwargs['cost']={'energy': 1}

            try:
                kwargs['time_adv']
            except BaseException:
                kwargs['time_adv']=1

            try:
                kwargs['pause']
            except BaseException:
                kwargs['pause']=1

            try:
                kwargs['action_text']
            except BaseException:
                kwargs['action_text']=1

            try:
                kwargs['max']
            except BaseException:
                kwargs['max']=None

            try:
                kwargs['adv']
            except BaseException:
                kwargs['adv']=False

            try:
                kwargs['reverse']
            except BaseException:
                kwargs['reverse']=False

            key = kwargs['cost'].keys()[0]

            if kwargs['max'] is None:
                measure = mc.stat[key]
            else:
                measure = kwargs['max']

                if kwargs['adv']:

                    if 20-mc.stat[key] > measure:
                        measure = 20-mc.stat[key]

                else:
                    if mc.stat[key] < measure:
                        measure = mc.stat[key]

            lapse = 0

            ramen.doing_solo = True

            renpy.hide_screen('smphone_ui')
            hud.active = False

            renpy.show_screen('hud_stats', stats=kwargs['cost'].keys() )
            renpy.show_screen('solo_stopbutton', text=kwargs['action_text'])

            while measure > 0:

                if not ramen.doing_solo:
                    break

                lapse += 1
                measure -= 1

                wotime=ramentime.adv(kwargs['time_adv'])

                renpy.pause(kwargs['pause'], True)

                for k in kwargs['cost'].keys():
                    mcf.stat(k, -kwargs['cost'][k])

            renpy.hide_screen('hud_stats')
            renpy.hide_screen('solo_stopbutton')

            hud.active = True

            return lapse

        def pc_writing(self, transform=None):

            if transform is None:
                transform = [basic_anim]

            renpy.show('mcp pc_writing', at_list=transform)

            lapse = self.doing(
                cost={'energy': 1, 'hygiene': 0.25, 'vital': 0.25 },
                time_adv=1,
                pause=3,
                action_text=[
                    'Creating Narration...',
                    'Constructing Mysteries...',
                    'Framing...',
                    'Building plot...',
                    'Developing Character...',
                    'Put some comedy...']
                )

            book = mc.bookcraft_current
            book_title = mc.bookcraft[book]['title']

            anatomy = list(mc.bookcraft[book]['anatomy'])

            anatomy[0] += round(lapse * (float(mc.skill['writing']) /20), 1)
            anatomy[1] += round(lapse * (float(mc.stat['libido']) /20), 1)
            anatomy[2] += round(lapse * (float(mc.stat['intel']) /20), 1)
            anatomy[3] += round(lapse * (float(mc.stat['luck']) /20), 1)

            total = sum(anatomy)

            mc.skill['writing'] += total/6
            mc.bookcraft[book]['anatomy']=tuple(anatomy)

            renpy.hide('mcp')

            if lapse >0:
                rascr.notify(book_title +" - Progress: "+ str(total) + " %", 'arrow-up-left')
            else:
                self.mumble('hungry')

            hud.active = True
            sysnote('')

        def pc_working(self, hour, trait, transform=None):

            if transform is None:
                transform = [basic_anim]

            renpy.show('mcp pc_working', at_list=transform)

            lapse = self.doing(
                cost={'energy': 1, 'hygiene': 0.25, 'vital': 0.25 },
                max=hour,
                time_adv=1,
                pause=3,
                action_text=['Commenting...', 'Debuging...', 'Create Function...', 'Build Query...']
                )

            sum = lapse * 30
            mc.money['bank'] += sum

            sum = str(sum)
            ramu.trait( trait.lower(), lapse * float(0.25) )

            ramen.pc_job={}
            ramen.pc_job_select={}

            renpy.hide('mcp')

            if lapse>0:
                rascr.notify('You gain '+ sum+' $ at Your Bank Account.')
            else:
                self.mumble('hungry')

            hud.active = True
            sysnote('')

        def shower(self, pose='shower', transform=None):

            if transform is None:
                transform = [basic_anim]

            renpy.show('mcp '+pose, at_list=transform)

            lapse = self.doing(
                cost={'hygiene': -1},
                time_adv=0.1,
                adv=True,
                pause=1,
                action_text='Showering...'
                )

            renpy.hide('mcp')

            if mc.stat['hygiene']>19:
                rascr.notify('You gain your hygiene back.', 'arrow-up-left')
            else:
                rascr.notify('You feel refreshed.', 'arrow-up-left')

            sysnote('')

        def eat(self, pose='home_eat', item=None, inventory_id='storage', transform=None):
            # not working as expected

            renpy.hide_screen('smphone_ui')
            hud.active = False

            if transform is None:
                transform = [basic_anim]

            renpy.show_screen('hud_stats', stats=item.effect.keys() )
            renpy.show('mcp '+pose, at_list=transform)

            key = item.effect.keys()
            duration = item.effect[key[0]]

            for n in range(0, duration):

                renpy.pause(1)
                ramentime.adv(0.05)

            inv_resnotify

            renpy.hide('mcp')
            renpy.hide('hud_stats')

            hud.active = True

        def sleep(self, pose='sleep0', hours=None, transform=None):
            """
            ``` python
                mcf.sleep(False,'sleep0')
            ```
            * Napping with 'sleep0' pose/attr (usually a sprite anim)
            """

            if hours is None:
                max = pe.limit[1] - mc.stat['vital']
            else:
                max = hours

            if transform is None:
                transform = [basic_anim]

            renpy.show('mcp '+pose, at_list=transform)

            renpy.show('dim2')

            lapse = self.doing(
                cost={'vital': -1, 'hygiene': 0.1},
                max=max,
                adv=True,
                time_adv=0.75,
                pause=2,
                action_text=['Zzz... zZz...', 'zZz... zzZ...', 'zzZ... Zzz...', 'Zzz... zzZ...']
                )

            renpy.hide('dim2')
            renpy.hide('mcp')

            if mc.stat['vital']>18:
                rascr.notify('You gain your vitality back.', 'arrow-up-left')
            elif mc.stat['vital']<18 and mc.stat['vital']<10:
                rascr.notify('You gain some vitality back.', 'arrow-up-left')
            else:
                rascr.notify('You feel refreshed.', 'arrow-up-left')

            sysnote('')

    mcf = ramen_mcfunction()

    solo = mcf

screen solo_stopbutton(text=["Working..."]):

    python:
        tx=[]
        if not isinstance(text, type([])):
            tx.append(text)
        else:
            tx = text

    frame background "#0006" xalign 0.5 yalign 0.85 xsize config.screen_width/4*3 ysize 120:
        padding(10, 10, 10, 10)
        hbox:
            vbox xsize(config.screen_width/4*3 )-220 ysize 100:
                text ramu.random_of(tx) color "#fff" yalign 0.5 xalign 0.0
            vbox xsize 200 ysize 100:
                textbutton 'Stop' style 'stop_button' xalign 1.0 yalign 0.5:
                    action[
                        SetVariable('ramen.doing_solo', False),
                        Hide('solo_stopbutton')
                        ]
