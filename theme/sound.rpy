init -200 python:

    # Uncomment the following line to set an audio file that will be played while
    # the player is at the main menu. This file will continue playing into the
    # game, until it is stopped or another file is played.

    ## Sounds and music ######################################################

    snd = ramu.ezfind_sound("main_music")

    if snd is not None:
        config.main_menu_music = snd

    snd = ramu.ezfind_sound("sample/sound")
    
    if snd is not None:
        config.sample_sound= snd

    snd = ramu.ezfind_sound("sample/voice")
    
    if snd is not None:
        config.sample_voice=snd

    config.has_sound = True
    config.has_music = True
    config.has_voice = True
