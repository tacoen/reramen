init -10 python:

    inventory_ui =  ramen_object(
        enable = False,
        size=(464,480),
        align=(0.9,0.5)
    )
    
    ramen.res =[False,False,False,None,""]
    
    ramen.labeloc={}
    ramen.labeloc['storage']=['ramen_test']
    ramen.labeloc['microwave']=['mc_kitchen']
    ramen.labeloc['pawn'] = ['pawn_shop']

    def inventory_resnotify():
        msg = []
        res= ramen.res
        
        if res[0]:
            msg.append( str(res[3][0]) +" = "+ str(res[3][1]) )
        
        if res[1]:
            msg.append( "- "+ res[4] )
        else:
            msg.append( res[4] )

#        if res[2]:
#            msg.append( res[4] + " depleted" )
            
        notify_ico("\n".join(msg),'logo-python')
    
    def labeloc(what):
        try:
            if ramen.last_label in ramen.labeloc[what]:
                return True
            else:
                return False
        except:
            return False
    
screen inventory_ui(inventory,size=(464,480),align=(0.9,0.3)):

    $ size = inventory_ui.size
    $ align = inventory_ui.align
    
    default item = None
    
    use modal('inventory_ui', \
        Showtitle=True, title = inventory.id, closebutton=True,size=size,align=align ):
        style_prefix "modal"

        if item is None:
            use inventory_grid(inventory, size, align)
        else:
            use inventory_detail( inventory, item, size, align)

screen inventory_hbox(what,value):
    
    hbox xfill True:
        style_prefix 'inventory_detail'
        text str(what) color "#666" min_width 120
        text str(value) xalign 1.0
        
screen inventory_detail(inventory,item,size,align):

    python:
        i = inventory.item(item)
        ramen.inventory_pid = [inventory, i.id]
 
    hbox:
        vbox xsize size[0]-148 :
            
            hbox:
                textbutton ico('arrow-left') style 'ramen_icon':
                    text_size 20 text_color "#333" text_hover_color "#111"
                    action SetScreenVariable('item',None)

                vbox:
                    spacing 8
                    if i.name is not None:
                        text i.name
            
                    if not i.desc == "":
                        text i.desc
                
                    if i.count > 1:
                        use inventory_hbox('Count',i.count)
                        
                    if i.require is not None:
                        use inventory_hbox('Require',i.require)

                    if i.tradable and labeloc('pawn'):
                        use inventory_hbox('Sell Price',i.price)

                    if i.effect:
                        null height 6
                        add ramu.hline(((size[0]-148-24),1),"#ccc")
                        text 'Effect' bold True size 18 color "#ccc"
                
                        for e in effect:
                            use inventory_hbox(e.title(),i.effect[e])
            
        vbox xsize 140 yfill True ysize size[1]-64:
            style_prefix "inventory_action"            
        
            add i.icon xalign 0.5
            
            vbox yalign 1.0 xalign 0.5:
                spacing 8
                $ action_text = i.require 
            
                if labeloc('store'):
                    textbutton "Store"  action Null
            
                if i.tradable and labeloc('pawn'):

                    textbutton "Sell" action [ 
                        Function(inventory.sell,item_id=i.id,use_ramen=True),
                        Function(inventory_resnotify),
                        SetScreenVariable('item',None)
                    ]

                if i.eatable:
                    $ action_text = "Consume"
                else:
                    $ action_text = "Use"

                if i.require is not None:
                    if labeloc(i.require):
                        $ action_text = i.require 
                    else:
                        $ action_text = False

                if action_text:
                    
                    textbutton action_text action [ 
                        Function(inventory.use,item_id=i.id,use_ramen=True),
                        Function(inventory_resnotify),
                        SetScreenVariable('item',None)
                    ]
                
                null height 8
                
                textbutton "Drop" action [ 
                    Confirm("Drop "+i.name+" ?", [ Function(inventory.drop,item_id=i.id) ], None, True),
                    SetScreenVariable('item',None)
                    ]



   
screen inventory_grid(inventory,size,align):

    python:
        max = 16
        vp_height = size[1]-40
        vp_width = size[0]-24
        cols = int( math.floor(vp_width/110) )
        rows = int(max/cols)
            
    vpgrid id "inventory_vp":
        cols cols
        rows rows
        spacing 5
        draggable True
        mousewheel True
        ysize vp_height
        xsize vp_width
       
        for item in sorted(inventory()):

            $ i = inventory.item(item)
            
            imagebutton action SetScreenVariable('item',item):
                idle i.icon
                hover Composite ((100,100),(0,0),Solid(pt.accent_color),(0,0),i.icon)

    vbar value YScrollValue("inventory_vp"):
        ysize vp_width-8


style inventory_detail_text:
    size 20
    color "#999"
    
style inventory_detail_label_text:
    color "#666"

style inventory_action_button is button:
    background rui.button_frame("#369",Borders(1,1,1,1),False)
    hover_background rui.button_frame("#58B",Borders(1,1,1,1),False)
    selected_background rui.button_frame("#58B",Borders(1,1,1,1),True)
    xsize 100
    xalign 0.5
    
style inventory_action_button_text is ramen_gui:
    color "#eee"
    hover_color "#fff"
    xalign 0.5
    size 18
