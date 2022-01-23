













define config.name = _("My Tuition Academia")





define gui.show_name = True




define config.version = "0.9.0"





define gui.about = _p("""Art, Coding and Writing:
TwistedScarlett60

All music is royalty free.
However, considering the subject of my game, please don't hesistate to message me if I'm using your content and you're not comfortable associating with it.

Sex Theme - Laffey - Exhale ft. Dillan Witherow

Club Theme - Sewerslvt - untitled unfinished 2

Day Theme - Living Room - Circle of Trust

Intro Theme - away - Frozen Snow

LonelyFans Theme - Sewerslvt - Slipknxt Remix

Massage Theme - Softy - Felt the Same

Evening Theme - Slo Loris x Stehlow - Aftercastle

Toko's Theme - Sewerslvt - Pandora's Box

Lesbian Theme - Dontcry & Nokiaa - Unwritten

Misc 1 - Sewerslvt - Private Life

Dungeon - Kevin MacLeod - Unwritten Return

Ending - Sewerslvt - mutant standard

True Ending - Sewerslvt - Restlessness

Sound Effects from https://www.zapsplat.com

""")






define build.name = "MyTuitionAcademia"







init:
    define config.has_sound = True
    define config.has_music = True
    define config.default_music_volume = 0.5
    define config.default_sfx_volume = 0.8
    define config.default_voice_volume = 0.6
init python:
    renpy.music.register_channel("ambience", mixer="sfx", loop=True, stop_on_mute=True, tight=False, buffer_queue=True)
init python:
    renpy.music.register_channel("sound2", mixer="voice", loop=True, stop_on_mute=True, tight=False, buffer_queue=True)























define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = dissolve




define config.end_game_transition = dissolve
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 0





default preferences.afm_time = 15
















define config.save_directory = "MyTuitionAcademia-1623248860"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)



    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.webp', 'archive')





    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
