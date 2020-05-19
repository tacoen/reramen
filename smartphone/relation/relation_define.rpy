init -20 python:

    smphone.register('relation',
        dir = ramu.getdir(),
        active=True,
        order=9,
        stat = {
            'relation':'#c22',
            'trust':'#fc3',
            'like':'#93C',
            }
    )

    style['smphone_bar']=Style('bar')
    style['smphone_bar'].ysize= 10
        
    for s in smphone.apps()['relation']['stat'].keys(): 
        color = smphone.apps()['relation']['stat'][s]
        style['smphone_bar_'+s]=Style('smphone_bar')
        style['smphone_bar_'+s].thumb = color
        style['smphone_bar_'+s].base_bar = Color(color).tint(0.4)
        style['smphone_bar_'+s].left_bar = color
        
        
screen smphone_apps_relation(var,page):

    python:
        app = ramu.makeobj( smphone.apps()['relation'] )
        app.width = style['smphone_default_vbox'].xmaximum
        app.bar_width = style['smphone_default_vbox'].xmaximum -(2*8)-96-8
        app.minibar_width = style['smphone_default_vbox'].xmaximum -(2*8)-96-8
    
    
    use smphone_viewport(app.title,app.hcolor):

        vbox:
            spacing 16
            style_prefix "smphone_default"
            for p in mc.rel:
                
                hbox:
                    spacing 8
                    add im.Scale( ramu.npc(p,'profile_pic'),96,96 )
                    
                    vbox:
                        spacing 8
                        
                        text ramu.npc(p,'name')+ " " + ramu.npc(p,'lastname')
                        
                        for s in sorted(app.stat.keys()):
                            python:
                                try: val = mc.rel[p][s]
                                except: val = 0
                                
                            vbox:
                                text s.title() size 14
                                bar range 20 value val style 'smphone_bar_'+s xsize app.minibar_width
                            



# screen smp_app_relationme():

    # python:
        # try: rbc.smp_who
        # except: rbc.smp_who = None
    
    # if rbc.smp_who is None:
        # vbox:
            # for who in sorted(mc.rel.keys()):
                # use smp_app_relationme_glance(who)          
    # else:
        # vbox:
            # use smp_app_relationme_details(rbc.smp_who)

# screen smp_app_relationme_glance(who):

    # python:
        # ppic = ramu.get_profilepic(who,(32,32))
        # sta = mc.rel[who]
        # inf = globals()[who]
        
    # hbox yalign 0.5 xfill True:
        # imagebutton action SetVariable('rbc.smp_who',who):
            # idle ppic
        # null width 8
        # textbutton inf.name text_color "#000" text_size 20 action SetVariable('rbc.smp_who',who) xsize style['smp']['area']['display'].xminimum-80-40
        # hbox yalign 0.5 xalign 1.0 xsize 80:
            # text str(sta['relation'])+"/"+str(mc.limit['relation'][1]) color "#369" text_align 1.0 size 16
        
    # null height 16

# screen smp_app_relationme_details(who):

    # python:
        # ppic = ramu.get_profilepic(who,(96,96))
        # sta = mc.rel[who]
        # inf = globals()[who]

    # use smp_backbutton('rbc.smp_who', inf.callname)
        
    # text inf.name+" "+inf.lastname color "#000"
    
    # null height 16
            
    # hbox:
        # add ppic yoffset 8
        # null width 16
        # vbox:
            # for s in sorted(sta.keys()):
                # use hc_hbar(smp, s, sta[s], style['smp']['area']['pbars'], "#000")
                # null height 4
            # null height 16



