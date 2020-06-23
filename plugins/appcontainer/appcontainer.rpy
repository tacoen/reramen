init -290 python:

    register_plugins(
        title="App Container",
        version="1.0",
        author="tacoen",
        author_url='https://github.com/tacoen/reramen',
        desc="small apps in screen",
        build=True
    )

    ramen.active_apps = {}

    class ramen_apps(ramen_extendable):

        def init(self, id=None, *args, **kwargs):
            self.__dict__['apps'] = ramen_persistent(self.id)
            try:
                ramen.active_apps[self.id]
            except BaseException:
                ramen.active_apps[self.id] = []

        def channel(self,what=None,**kwargs):

            if what is None:
                what = os.path.basename(
                    renpy.get_filename_line()[0]).replace(
                    '.rpy', '')

            what = what.lower().strip()

            try:
                kwargs['dir']
            except BaseException:
                kwargs['dir'] = ramu.getdir()

            try:
                kwargs['icon']
            except BaseException:
                icon = ramu.ezfile(ramu.getdir() + what)
                if icon is None:
                    icon = ramu.ezfile( ramu.getdir() + "icon", Color("#999") )
                kwargs['icon'] = icon

            try:
                kwargs['order'] = "{:03d}".format(kwargs['order'])
            except BaseException:
                kwargs['order'] = ramu.uid()

            try:
                kwargs['hcolor']
            except BaseException:
                kwargs['hcolor'] = ramu.random_color(0, 168)

            try:
                kwargs['title']
            except BaseException:
                kwargs['title'] = what.title()
                
            files = ramu.files( kwargs['dir'], None, pe.ext_img )
            
            gal={}
            
            for f in sorted(files):
                
                if 'icon.' in f:
                    continue
                    
                fn = ramu.file_info(f)
                try: gal[fn.path]
                except: gal[fn.path] = []
                gal[fn.path].append(f)
            
            kwargs['gallery'] = gal
            
            self.apps._set(what, kwargs)        
        
        def register(self, what=None, **kwargs):

            if what is None:
                what = os.path.basename(
                    renpy.get_filename_line()[0]).replace(
                    '.rpy', '')

            what = what.lower().strip()

            try:
                kwargs['dir']
            except BaseException:
                kwargs['dir'] = ramu.getdir()

            try:
                kwargs['icon']
            except BaseException:
                icon = ramu.ezfile(ramu.getdir() + what)
                if icon is None:
                    icon = ramu.ezfile( ramu.getdir() + "icon", Color("#999") )
                kwargs['icon'] = icon

            try:
                kwargs['order'] = "{:03d}".format(kwargs['order'])
            except BaseException:
                kwargs['order'] = ramu.uid()

            try:
                kwargs['hcolor']
            except BaseException:
                kwargs['hcolor'] = ramu.random_color(0, 168)

            try:
                if kwargs['active']:
                    ramen.active_apps[self.id].append(
                        kwargs['order'] + ":" + what)
                    ramen.active_apps[self.id] = list(
                        ramen.active_apps[self.id])
            except BaseException:
                kwargs['active'] = False

            try:
                kwargs['title']
            except BaseException:
                kwargs['title'] = what.title()

            try:
                kwargs['start']
            except BaseException:
                kwargs['start'] = self.id + "_apps_" + what

            self.apps._set(what, kwargs)

        def activated(self, what, state=True):
            if state:
                ramen.active_apps[self.id].append(kwargs['order'] + ":" + what)
                ramen.active_apps[self.id] = list(ramen.active_apps[self.id])
            else:
                try:
                    ramen.active_apps[self.id].pop(what)
                except BaseException:
                    pass

        def get(self, what, attr=None):
            if attr is None:
                return self.apps()[what]
            else:
                try:
                    self.apps()[what][attr]
                except BaseException:
                    return None
