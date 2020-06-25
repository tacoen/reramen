init -299 python:

    pp = ramen_persistent('extend')

    pp.plugins = {}
    pp.episodes = {}
    pp.asset = {}

    def Plugin(what, type='plugins'):
        """Load plugins-information"""
        try:
            obj = object()
            if type == 'episodes':
                obj.__dict__ = pp.episodes[what]
            elif type == 'asset':
                obj.__dict__ = pp.asset[what]
            else:
                obj.__dict__ = pp.plugins[what]
            return obj
        except BaseException:
            return False

    class register_plugins(object):
        """
        Ramen plugins can be screen, function, class, or assets.
        Registered plugins can be included into your distributions as archive `.rpa`

        **If you not registered the plugin, it will works just like a normal ren'py scripts.**

        ``` python
        register_plugins(
            title="App Container",
            version="1.0",
            author="tacoen",
            author_url='https://github.com/tacoen/reramen',
            desc="small apps in screen",
            build=True
        )

        ```
        """

        def __new__(self, id=None, type='plugins', *args, **kwargs):

            try:
                kwargs['dir']
            except BaseException:
                kwargs['dir'] = ramu.getdir()

            if id is None:
                id = ramu.safestr(
                    re.sub(
                        r'.+/',
                        '',
                        os.path.dirname(
                            renpy.get_filename_line()[0])))

            try:
                kwargs['version']
            except BaseException:
                kwargs['version'] = '1.0'

            try:
                kwargs['author']
            except BaseException:
                kwargs['author'] = None

            try:
                kwargs['author_url']
            except BaseException:
                kwargs['author_url'] = 'http://'

            try:
                kwargs['title']
            except BaseException:
                kwargs['title'] = id

            try:
                kwargs['prefix']
            except BaseException:
                kwargs['prefix'] = id

            try:
                kwargs['build']
            except BaseException:
                kwargs['build'] = False

            if not type in ['plugins', 'episodes', 'asset']:
                type = 'plugins'

            try:
                kwargs['type']
            except BaseException:
                if type is not None:
                    kwargs['type'] = type

            if kwargs['type'] == 'episodes':

                try:
                    kwargs['label']
                except BaseException:
                    kwargs['label'] = id

            try:
                persistent.ramen['extend'][type]
            except BaseException:
                persistent.ramen['extend'][type]={}

            try:
                persistent.ramen['extend'][type][id]
            except BaseException:
                persistent.ramen['extend'][type][id]={}

            for k in kwargs:
                persistent.ramen['extend'][type][id][k]=kwargs[k]

    def ramen_plugins_build():

        for p in pp.plugins.keys():
            if Plugin(p).build:
                type = Plugin(p).type
                build.archive(type+'_'+ramu.safestr(p), "all")
                build.classify('game/'+Plugin(p).dir+'**', type+'_'+ramu.safestr(p) )

init -1 python:

    if not pp.episodes.keys() != []:
        ramen.episode_menu = True
    else:
        ramen.episode_menu = False

screen ramen_episodes_menu():

    tag menu

    default episode = None

    use game_menu(_("Episodes")):

        if episode is not None:

            use ramen_episodes_detail(episode)

        else:
            text 'me'

            vpgrid:
                cols 2
                yinitial 0.0
                spacing 20
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                side_yfill True

                style_prefix 'episodes'

                for episode in pp.episodes:

                    python:
                        e = Plugin(episode, 'episodes')
                        timg = ramu.ezfind('thumb', 'image', e.dir)
                        if timg is not None:
                            thumb = im.Scale(timg, 200, 110)
                        else:
                            thumb = Composite((200, 110), (0, 0), Solid('#456'),
                                              (0.45, 0.3), Text(ramu.capcap(e.title), size=36, font=pt.font_ui_label))

                    button xsize 465:
                        action SetScreenVariable('episode', episode)
                        has hbox
                        add thumb
                        null width 10
                        vbox:
                            spacing 2
                            label e.title.title()
                            text e.desc size 14

screen ramen_episodes_detail(episode):

    python:

        e = Plugin(episode, 'episodes')

        bimg = ramu.ezfind('banner', 'image', e.dir)

        if bimg is not None:
            banner = Composite((900, 150), (0, 0), im.Scale(bimg, 900, 150),
                               (0, 0), Solid("#0009"),
                               (20, 0.6), Text(e.title.title(), size=32, font=pt.font_ui_label))

        else:
            banner = Composite((900, 150), (0, 0), Solid('#456'),
                               (0, 0), Solid("#0009"),
                               (20, 0.6), Text(e.title.title(), size=32, font=pt.font_ui_label))

    viewport:
        yinitial 0.0
        spacing 24
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True

        has hbox

        textbutton ico('arrow-left') style 'ramen_icon' action SetScreenVariable('episode', None)

        vbox xoffset 10:
            spacing 10

            add banner

            vbox xoffset 20 xsize 840:
                spacing 10

                text e.desc

                if renpy.has_label(e.label):

                    null height 20

                    textbutton _("Start Episodes") style 'menu_start_button':
                        xalign 1.0
                        action Start(e.label)

                null height 20

                add ramu.hline((840, 1), "#666")

                vbox:
                    spacing 5
                    style_prefix 'episode_detail'
                    use hbox_line('Version', e.version)
                    use hbox_line('Author', "{a="+ e.author_url+"}"+ e.author +"{/a}")

                add ramu.hline((840, 1), "#666")

style episode_detail_text:
    size 16
    color "#ccc"
