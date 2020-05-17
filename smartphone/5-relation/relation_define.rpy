init -20 python:

    smphone.register('relation',
        dir = ramu.getdir(),
        active=True,
        order=9,
    )


# #init python:

# #    mcph.update_app({
 # #       'title': 'Relations',
  # #      'hcolor': '#222',
   # # })

# init -1 python:

    # smp.index_update(
        # title='Relations',
        # hcolor='#92A',
        # order=1,
        # bgr="#ffd"
    # )

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



