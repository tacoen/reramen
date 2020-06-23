init -20 python:

    smphone.register('news',
                     active=True,
                     title='SHNews',
                     order=1,
                     hcolor='#393'
                     )

    paper = object()
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
            paper.ads = ramu.random_files('sanhila/syndicate/'+'ads' )

        if not int(paper.sh) == int(ramen.time.hour):
            paper.news=[]
            for i in range(0, 8):
                paper.news.append(
                    ramu.random_of(wv.news_subject)+' ' +
                    ramu.random_of(wv.news_noun)+' '+
                    ramu.random_of(wv.news_object)
                )

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
