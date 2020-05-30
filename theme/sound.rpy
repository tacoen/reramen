init -200 python:

    # Uncomment the following line to set an audio file that will be played while
    # the player is at the main menu. This file will continue playing into the
    # game, until it is stopped or another file is played.

    ## Sounds and music ######################################################

    config.main_menu_music = ramu.ezfind("main_music",'sound')
    config.sample_sound= ramu.ezfind("sample/sound",'sound')
    config.sample_voice=ramu.ezfind("sample/voice",'sound')

    config.has_sound = True
    config.has_music = True
    config.has_voice = True
