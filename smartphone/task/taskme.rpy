init -20 python:

    smphone.register('task',
        active=True,
        title = 'My Task',
        order=7,
    )

    mc.task = {}
    mc.task[ramu.uid()]=['test this',False]
    mc.task[ramu.uid()]=['do some test',True]
    
screen smphone_apps_task(var,page):
        
    python:
        app = ramu.makeobj( smphone.apps()['task'] )
        app.width = style['smphone_default_vbox'].xmaximum
        
    use smphone_viewport(app.title,app.hcolor):
        
        vbox:
            style_prefix "smphone_default"
            spacing 8
        
            for t in mc.task:
                
                hbox:
                    spacing 8
                    vbox xsize 32:
                        if mc.task[t][1]:
                            text "{icon=circle-check}" size 18 color "#393" yoffset 2
                            $ tcolor = "#999"
                        else:
                            text "{icon=circle}" size 18 color "#666" yoffset 2
                            $ tcolor = "#000"
                    vbox:
                        text mc.task[t][0].title() color tcolor


