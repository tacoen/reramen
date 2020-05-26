
# must at last init

init python:

    build.classify('**.rpy', None)
    build.classify('wiki/**', None)
    
    build.documentation('*.md')

    if not ramen.dev:
    
        build.archive('ramen-framework-'+config.version, "all")
        build.classify('game/ramen/**', 'ramen-framework-'+config.version )

        # exclude all developer script from the packages
        #build.classify('game/developer-option.*', None)
        build.classify('game/plugins/dev/**', None)
    
    if 'ramen_plugins_build' in dir():
        ramen_plugins_build()
        
        