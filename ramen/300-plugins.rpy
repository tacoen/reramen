init -299 python:

    ramen.plugins = object()

    def plugin(what):
        try:
            return ramen.plugins.__dict__[what]()
        except BaseException:
            return False

    class register_plugins(object):
        """
        
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
        
        def __new__(self, id=None, *args, **kwargs):

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
                kwargs['author_url'] = None

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

            try:
                ramen.plugins.__dict__[id]
            except BaseException:
                ramen.plugins.__dict__[id] = ramen_object()

            for k in kwargs:
                ramen.plugins.__dict__[id]._set(k,kwargs[k])
                

    def ramen_plugins_build():
    
        for p in ramen.plugins.__dict__:
            if plugin(p)['build']:
            
                build.archive('plugin_'+ramu.safestr(p), "all")
                build.classify('game/'+plugin(p)['dir']+'**', 'plugin_'+ramu.safestr(p) )
