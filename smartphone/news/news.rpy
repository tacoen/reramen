init -20 python:

    smphone.register('news',
                     active=True,
                     title='SHNews',
                     order=1,
                     hcolor='#393'
                     )

    paper = ramen_persistent('shnews')

    paper.subject=[
        'Hilatech Corporation', 'Milner Minning', 'Alter-Town', 'International Contents',
        'TakeSeven', 'SH-Cola Company', 'Education202', 'ToySystem', 'Sleeve Container',
        'Renren Entertaiment', 'Someholding', 'Oni', 'Bona', 'Cilaka', 'Otani OS',
        'Ignorant Community', 'NeoReligion', 'Uni-chains', 'Picadora', 'Aroby'
    ]

    paper.noun=[
        'pinch a risk on', 'doubt', 'relief', 'support', 'respect', 'signal for better',
        'rise their debts on', 'say nothings at incident of', 'had a great intentions on',
        'say: Big No No to', 'plan to claim', 'ignore', 'demans their rights on',
        'answering question in', 'look for profit at', 'has a keys to',
        'restoring for', 'sing about', 'mark a spot in', 'relaxing people from',
        'gain some profit over', 'build a cause for', 'File a sue to', 'Extracting'
    ]

    paper.object=[
        'Yellow High', 'Blue zone', 'Pino district', 'San Hilla', 'SH Games', 'SixNine Road',
        'Wrongvile', 'Lolo', 'their home', 'Hiest-central', 'San More', 'Quill', 'Pidza',
        'Who-know-you', 'Order 69', 'Ikku Club', 'Town', 'River Enviroment', 'Blue Jackets',
        'HUN Community', 'Women Sports.', 'Girls Fight Competition'
    ]

    paper.sh = 0

screen smphone_apps_news(var, page):

    python:
        app = ramu.makeobj(smphone.apps()['news'])
        app.width = style['smphone_default_vbox'].xmaximum

        try:
            paper.sh
        except BaseException:
            paper.sh =0

        try:
            paper.ads
        except BaseException:
            paper.ads = ramu.random_files( app.dir+'ads' )

        if not int(paper.sh) == int(ramen.time.hour):
            paper.news=[]
            for i in range(0, 8):
                paper.news.append( ramu.random_of(paper.subject)+' '+ramu.random_of(paper.noun)+' '+ramu.random_of(paper.object))

            paper.sh  = ramen.time.hour

            paper.ads = ramu.random_files( app.dir+'ads' )

    use smphone_viewport(app.title, app.hcolor):

        vbox:
            style_prefix "smphone_default"
            spacing 16

            text "HOUR 2 HOUR" bold True

            for n in range(0, len(paper.news)):
                text paper.news[n].title()

            null height 12

            add(paper.ads) xoffset -4

            null height 24
