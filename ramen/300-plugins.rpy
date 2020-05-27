init -299 python:

    pp = ramen_persistent('extend')

    pp.plugins = {}
    pp.episodes = {}
    pp.asset = {}

    def plugin(what,type='plugins'):
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
                kwargs['url']
            except BaseException:
                kwargs['url'] = None

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

            if not type in ['plugins','episodes','asset']:
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
            if plugin(p).build:
                type = plugin(p).type
                build.archive(type+'_'+ramu.safestr(p), "all")
                build.classify('game/'+plugin(p).dir+'**', type+'_'+ramu.safestr(p) )

init -1 python:

    if not pp.episodes.keys() != []:
        ramen.episode_menu = True
    else:
        ramen.episode_menu = False

screen ramen_episodes_menu():

    tag menu

    use game_menu(_("Episodes")):

        vpgrid:
            cols 2
            yinitial 0.0
            spacing 24
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True            

            style_prefix 'episodes'
            
            
            for p in pp.episodes:
            
                python:
                    e = plugin(p,'episodes') 
                    sty = True
                    if renpy.loadable(e.dir+'thumb.png'):
                        thumb = im.Scale(e.dir+'thumb.png',200,112)
                    else:
                        thumb = Composite((200,112), (0,0),Solid('#456'), (8,8),Text(e.title.title()))
                    if renpy.has_label(e.label):
                        action = Jump(e.label)
                    else:
                        action = Null
                        sty = False
                    
                button xsize 465:
                    if sty:
                        action action
                    has hbox
                    add thumb
                    null width 24
                    vbox:
                        spacing 2
                        text e.title.title()
                        text e.desc size 16


    