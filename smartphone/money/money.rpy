init -20 python:

    smphone.register('money',
        dir = ramu.getdir(),
        title="SH Bank E-Money",
        active=True,
        order=20,
        hcolor='#369'
    )

    ramen.epay = 100

screen smphone_apps_money(var,page):
        
    python:
        app = ramu.makeobj( smphone.apps()['money'] )
        app.width = style['smphone_default_vbox'].xmaximum
        
    use smphone_viewport(app.title,app.hcolor):
        
        style_prefix "smphone_default"
        
        vbox:
            spacing 16

            add ramu.ezfile2(app.dir+"qrcode") xalign 0.5
                
            hbox:
                label 'Bank'
                text "{:07d} $".format(mc.bank) xalign 1.0

            hbox:
                label 'Cash'
                text "{:07d} $".format(mc.money) xalign 1.0

            add ramu.hline((app.width,1),"#999")

            if var is None:
                textbutton "{icon=ico-cash} Scan and Pay" xsize app.width:
                    action [
                        SetScreenVariable('var',ramen.epay),
                    ]
            else:
                if ramen.epay > 0 and mc.bank > ramen.epay:
                    textbutton "{icon=ico-cash} Payment: "+str(ramen.epay)+" $" xsize app.width:
                        action [
                            Function(ramu.pay,m=ramen.epay,src=mc.bank,ret=False),
                            SetVariable('ramen.epay',0),
                            SetScreenVariable('var',None)
                        ]
                else:
                    
                    textbutton "{icon=ico-cash} Got Nothing" xsize app.width:
                        action [
                            SetScreenVariable('var',None)
                        ]
                