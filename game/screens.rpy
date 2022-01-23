init offset = -1





label splashscreen:
    scene black
    pause 0.5
    show expression "splash1" with dissolve
    pause 1.5
    show expression "splash2" with dissolve
    pause 3.0
    return





style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)









screen trueendscreen():
    tag menu

    imagemap:
        if persistent.dateready == 1:
            ground "te screendate"
        else:
            ground "te screen"
        hover "te screen hover"
        hotspot (26, 18, 392, 335) clicked Jump("tewardrobe")
        hotspot (32, 362, 375, 330) clicked Jump("temusicchoice")
        hotspot (1476, 14, 384, 328) clicked Jump ("techat")
        hotspot (1469, 351, 426, 330) clicked Jump ("tebed")
        hotspot (1500, 640, 400, 400) clicked Jump ("tedates")
        hotspot (375, 941, 137, 95) action Start()
        hotspot (560, 925, 189, 116) action ShowMenu("load")
        hotspot (769, 928, 314, 113) action ShowMenu("preferences")
        hotspot (1096, 928, 224, 109) action ShowMenu("about")
        hotspot (1324, 925, 148, 107) clicked Jump("tequit")

    text "{size=+3}{b}[persistent.affection]{/b}":
        xpos 300
        ypos 770
    text "{size=+3}{b}[persistent.virgin2]{/b}":
        xpos 300
        ypos 820


label worldmap:
    if morning == 1:
        play ambience ambienceday fadein 3.0
        play music daytime
        scene bg street with d
    elif True:
        play ambience ambiencenight fadein 3.0
        play music rest
        scene bg street with d
    label postworldmap:
        pass
    $ rand2 = renpy.random.randint(1,100)
    if clothes == 13:
        pass
    elif peppersprayon == 1:
        pass
    elif dailygrope == 1:
        pass
    elif rand2 >= 50 and lewdoutfit == 1 or nude == 1 or rand2 >= 95:
        $ dailygrope = 1
        $ groped += 1
        if gropeevent == 0:
            $ gropeevent = 1
            show buttgropeb:
                xalign 0.5 yalign 0.5
            if tan == 1:
                show buttgropebtan:
                    xalign 0.5 yalign 0.5
            if pregnancyshowing == 1:
                show buttgropebp:
                    xalign 0.5 yalign 0.5
                if tan == 1:
                    show buttgropebtanp:
                        xalign 0.5 yalign 0.5
            if nude == 1:
                pass
            elif clothes == 5:
                show buttgropeo bunny:
                    xalign 0.5 yalign 0.5
                if pregnancyshowing == 1:
                    show buttgropeo bunnyp:
                        xalign 0.5 yalign 0.5
            elif clothes == 10:
                show buttgropeo bar:
                    xalign 0.5 yalign 0.5
            elif clothes == 4:
                show buttgropeo catlingerie:
                    xalign 0.5 yalign 0.5
            elif clothes == 6:
                show buttgropeo camisole:
                    xalign 0.5 yalign 0.5
                if pregnancyshowing == 1:
                    show buttgropeo camisolep:
                        xalign 0.5 yalign 0.5
            elif clothes == 7:
                show buttgropeo underwear:
                    xalign 0.5 yalign 0.5
            elif clothes == 11:
                show buttgropeo bikini:
                    xalign 0.5 yalign 0.5
            elif True:
                show buttgropeo formal:
                    xalign 0.5 yalign 0.5
                if pregnancyshowing == 1:
                    show buttgropeo formalp:
                        xalign 0.5 yalign 0.5
            with d
            "While you were walking out around the city..."
            play sound fondle
            show buttgrope grope:
                xalign 0.5 yalign 0.5
            with d
            "You feel a stranger grope your butt!"
            hide buttgrope with d
        elif True:
            $ gropeevent = 0
            show boobgropeb:
                xalign 0.5 yalign 0.5
            if tan == 1:
                show boobgropebtan:
                    xalign 0.5 yalign 0.5
            if piercingson == 1:
                show boobgropebpiercings:
                    xalign 0.5 yalign 0.5
            if nude == 1:
                pass
            elif clothes == 5:
                show boobgropeo bunny:
                    xalign 0.5 yalign 0.5
            elif clothes == 10:
                show boobgropeo bar:
                    xalign 0.5 yalign 0.5
            elif clothes == 4:
                show boobgropeo catlingerie:
                    xalign 0.5 yalign 0.5
            elif clothes == 6:
                show boobgropeo camisole:
                    xalign 0.5 yalign 0.5
            elif clothes == 7:
                show boobgropeo underwear:
                    xalign 0.5 yalign 0.5
            elif clothes == 11:
                show boobgropeo swimsuit:
                    xalign 0.5 yalign 0.5
            elif True:
                show boobgropeo formal:
                    xalign 0.5 yalign 0.5
            with d
            "While you were walking out around the city..."
            play sound fondle
            show boobgrope grope with d:
                xalign 0.5 yalign 0.5
            "You feel a stranger grope your breasts!"
            hide boobgrope with d
        if sd < 50:
            "H-Hey! How horrible!"
        elif sd < 100 and rand2 >= 8 and lewdoutfit == 1:
            "Just because I'm dressed like this, doesn't mean you can just grope me!"
        elif sd < 100 and rand2 >= 5:
            "H-Hey! Don't touch me like that!"
        elif sd > 100 and rand2 >= 8:
            "Mmphh, if you touch me like that..."
        elif sd > 100 and rand2 >= 5:
            "Haahhhh, I'm getting wet..."
        play sound success
        $ sd += 5
        "(+5 Temporary Sexual Desire today!)"
        scene bg street with d
label worldmap2:
    if yokohasnumber == 1 and yokoroute2 == 0 and yokocalled == 0:
        play sound ringtone
        $ yokocalled = 1
        "Hmm? I seem to be getting a call."
        play ambience foreplay2
        "Huh...?"
        mc "Hello?"
        "What is this?"
        mc "Hellloooo?"
        "Someone must have pocket dialled me..."
        stop ambience
    call screen worldmap with d
screen worldmap():
    imagemap:
        if morning == 1:
            ground "world map morning"
        else:
            ground "world map afternoon"
        hover "world map hover"
        hotspot (1476, 212, 177, 162) clicked Jump("maptobedroom")
        hotspot (1309, 109, 154, 159) clicked Jump("college")
        hotspot (288, 80, 172, 173) clicked Jump("tutor")
        hotspot (510, 511, 177, 175) clicked Jump("shops")
        hotspot (1555, 721, 174, 167) clicked Jump("massage")
        hotspot (1179, 266, 177, 171) clicked Jump("bar")
        hotspot (424, 310, 184, 159) clicked Jump("studio")
        hotspot (668, 906, 147, 138) clicked Jump("beach")
        hotspot (878, 71, 153, 146) clicked Jump("pool")
        hotspot (807, 414, 161, 160) clicked Jump("club")
        hotspot (854, 727, 156, 144) clicked Jump("stripclub")
        hotspot (1155, 47, 141, 139) clicked Jump("maledorms")
        hotspot (1181, 833, 174, 166) clicked Jump("hospital")
        hotspot (110, 430, 180, 180) clicked Jump("park")
        hotspot (1677, 922, 149, 145) clicked Jump("dungeon")
        hotspot (631, 105, 157, 139) clicked Jump("bank")
        hotspot (1677, 47, 300, 300) clicked Jump("todolist")

    add "wmtodo"
    if boyfriend == 1 or maledormsunlocked == 1:
        add "wmmaledorms"
    if pregnant == 1 and pregnancyterm > 9 or pregnancies >= 1:
        add "wmhospital"
    if parkunlocked == 1:
        add "wmpark"
    if massageparlourunlocked == 1:
        add "wmmassageparlour"
    if clubunlocked == 1:
        add "wmclub"
    if stripclubunlocked == 1:
        add "wmstripclub"
    if studiounlocked == 1:
        add "wmstudio"
    if dungeonunlocked == 1:
        add "wmdungeon"
    if bankunlocked == 1:
        add "wmbank"
    if morning == 1:
        text "{size=+3}{b}Morning {/b}":
            xpos 1700
            ypos 15
    else:
        text "{size=+3}{b}Afternoon {/b}":
            xpos 1700
            ypos 15
    if event == 0:
        text "{size=+3}Su -":
            xpos 165
            ypos 15
    elif event == 1:
        text "{size=+3}Mo -":
            xpos 165
            ypos 15
    elif event == 2:
        text "{size=+3}Tu -":
            xpos 165
            ypos 15
    elif event == 3:
        text "{size=+3}We -":
            xpos 165
            ypos 15
    elif event == 4:
        text "{size=+3}Th -":
            xpos 165
            ypos 15
    elif event == 5:
        text "{size=+3}Fr -":
            xpos 165
            ypos 15
    elif event == 6:
        text "{size=+3}Sa -":
            xpos 165
            ypos 15
    elif event == 7:
        text "{size=+3}Su -":
            xpos 165
            ypos 15
    text "{size=+3} Day [days]":
        xpos 240
        ypos 15
    text "{size=+3}$[money]":
        xpos 620
        ypos 15

label todolist:
    call screen todo with d
    jump postworldmap

screen todo():
    imagemap:
        ground "todo screen"
        hover "todo screen hover"
        hotspot (1512, 923, 146, 125) clicked Jump("postworldmap")
        if tuition > 0:
            text "{size=-3}$[tuition]/$72000":
                xpos 345
                ypos 67
        else:
            text "{size=-3}Complete":
                xpos 345
                ypos 67
        if eventflash == 0 or event2threesome == 0 or event4complete == 0 or event3complete == 0 or blackmailsex == 0 or mrslime == 0 or onsensex == 0:
            text "{size=-3}Incomplete":
                xpos 389
                ypos 101
        else:
            text "{size=-3}Complete":
                xpos 389
                ypos 101
        if lonelyfans21 == 0:
            text "{size=-3}Incomplete":
                xpos 336
                ypos 287
        else:
            text "{size=-3}Complete":
                xpos 336
                ypos 287
        if chatfaproute6 == 0:
            text "{size=-3}Incomplete":
                xpos 300
                ypos 318
        else:
            text "{size=-3}Complete":
                xpos 300
                ypos 318
        if xtube6 == 0 or xtube5 == 0 or xtube4 == 0 or xtube3 == 0 or xtube2 == 0 or xtube1 == 0:
            text "{size=-3}Incomplete":
                xpos 276
                ypos 348
        else:
            text "{size=-3}Complete":
                xpos 276
                ypos 348
        if barroute <= 5:
            text "{size=-3}Incomplete":
                xpos 268
                ypos 516
        else:
            text "{size=-3}Complete":
                xpos 268
                ypos 516
        if gloryholesex == 0:
            text "{size=-3}Incomplete":
                xpos 329
                ypos 547
        else:
            text "{size=-3}Complete":
                xpos 329
                ypos 547
        if soloswimfuck == 0 or soloswimflash == 0:
            text "{size=-3}Incomplete":
                xpos 329
                ypos 725
        else:
            text "{size=-3}Complete":
                xpos 329
                ypos 725
        if tinaroute4 == 0:
            text "{size=-3}Incomplete":
                xpos 329
                ypos 826
        else:
            text "{size=-3}Complete":
                xpos 329
                ypos 826
        if sbmakeout == 0 or sbsex == 0:
            text "{size=-3}Incomplete":
                xpos 340
                ypos 935
        else:
            text "{size=-3}Complete":
                xpos 340
                ypos 935
        if susuroute4 == 0:
            text "{size=-3}Incomplete":
                xpos 342
                ypos 964
        else:
            text "{size=-3}Complete":
                xpos 342
                ypos 964
        if bbsex == 0:
            text "{size=-3}Incomplete":
                xpos 322
                ypos 994
        else:
            text "{size=-3}Complete":
                xpos 322
                ypos 994
        if massageroute5 == 0:
            text "{size=-3}Incomplete":
                xpos 1010
                ypos 71
        else:
            text "{size=-3}Complete":
                xpos 1010
                ypos 71
        if banksex == 0:
            text "{size=-3}Incomplete":
                xpos 993
                ypos 179
        else:
            text "{size=-3}Complete":
                xpos 993
                ypos 179
        if clubsex == 0 or clubbj == 0:
            text "{size=-3}Incomplete":
                xpos 1017
                ypos 288
        else:
            text "{size=-3}Complete":
                xpos 1017
                ypos 288
        if yokosex4 == 0:
            text "{size=-3}Incomplete":
                xpos 965
                ypos 395
        else:
            text "{size=-3}Complete":
                xpos 965
                ypos 395
        if studioroute5 == 0:
            text "{size=-3}Incomplete":
                xpos 949
                ypos 514
        else:
            text "{size=-3}Complete":
                xpos 949
                ypos 514
        if tutorbj == 0:
            text "{size=-3}Incomplete":
                xpos 1050
                ypos 723
        else:
            text "{size=-3}Complete":
                xpos 1050
                ypos 723
        if yomoroutecomplete == 0:
            text "{size=-3}Incomplete":
                xpos 967
                ypos 830
        else:
            text "{size=-3}Complete":
                xpos 967
                ypos 830
        if supervisorsex == 0:
            text "{size=-3}Incomplete":
                xpos 1005
                ypos 939
        else:
            text "{size=-3}Complete":
                xpos 1005
                ypos 939
        if blackoutsex == 0:
            text "{size=-3}Incomplete":
                xpos 1006
                ypos 968
        else:
            text "{size=-3}Complete":
                xpos 1006
                ypos 968
        if twilightdance3 == 0:
            text "{size=-3}Incomplete":
                xpos 1530
                ypos 74
        else:
            text "{size=-3}Complete":
                xpos 1530
                ypos 74
        if stripclubwork4 == 0:
            text "{size=-3}Incomplete":
                xpos 1658
                ypos 104
        else:
            text "{size=-3}Complete":
                xpos 1658
                ypos 104
        if mdbj == 0 or mdsex == 0:
            text "{size=-3}Incomplete":
                xpos 1637
                ypos 292
        else:
            text "{size=-3}Complete":
                xpos 1637
                ypos 292
        if ca <= 5:
            text "{size=-3}Incomplete":
                xpos 1642
                ypos 394
        else:
            text "{size=-3}Complete":
                xpos 1642
                ypos 394
        if parkroute2 == 0:
            text "{size=-3}Incomplete":
                xpos 1648
                ypos 517
        else:
            text "{size=-3}Complete":
                xpos 1648
                ypos 517
        if dungeonroute3 == 0:
            text "{size=-3}Incomplete":
                xpos 1580
                ypos 619
        else:
            text "{size=-3}Complete":
                xpos 1580
                ypos 619
        text "{size=-3}[endingsseen]/11":
            xpos 1610
            ypos 833

label maptobedroom:
    $ dsd = int(sd)
    $ dshame = int(shame)+1
    $ dsmarts = int(smarts)
    if qintrovert == 1:
        $ alonemult = 1.1
    if morning == 1:
        scene bg bedroomday
        jump bedroommorning
    elif True:
        jump prebedroom

screen bedroom():
    imagemap:
        ground "bedroom screen buttons"
        hover "bedroom screen buttons hover"
        hotspot (20, 350, 350, 425) clicked Jump("computer")
        hotspot (1400, 400, 700, 350) clicked Jump ("bed")
        hotspot (700, 680, 650, 450) clicked Jump ("outside")
        hotspot (400, 70, 280, 500) clicked Jump("wardrobe")
        hotspot (700, 70, 325, 500) clicked Jump("inventory")
        hotspot (550, 500, 200, 200) clicked Jump ("status")
        hotspot (1400, 700, 700, 400) clicked Jump ("endings")
        hotspot (1471, 100, 284, 278) clicked Jump("tips")
        hotspot (3, 736, 350, 320) clicked Jump("tebt")
    if endingsunlocked == 0 and morning == 1:
        add "bmendings1"
    if endingsunlocked == 0 and morning == 0:
        add "bmendings2"
    if persistent.trueendstage2 == False and morning == 1:
        add "bs tebuttonday"
    if persistent.trueendstage2 == False and morning == 0:
        add "bs tebuttonnight"
    if event == 0:
        text "{size=+3}Su -":
            xpos 165
            ypos 14
    elif event == 1:
        text "{size=+3}Mo -":
            xpos 165
            ypos 14
    elif event == 2:
        text "{size=+3}Tu -":
            xpos 160
            ypos 14
    elif event == 3:
        text "{size=+3}We -":
            xpos 165
            ypos 14
    elif event == 4:
        text "{size=+3}Th -":
            xpos 165
            ypos 14
    elif event == 5:
        text "{size=+3}Fr -":
            xpos 165
            ypos 14
    elif event == 6:
        text "{size=+3}Sa -":
            xpos 165
            ypos 14
    elif event == 7:
        text "{size=+3}Su -":
            xpos 165
            ypos 14
    text "{size=+3} Day [days]":
        xpos 230
        ypos 14
    text "{size=+5}$[money]":
        xpos 620
        ypos 14
    text "{size=+5}[fol]":
        xpos 1148
        ypos 14
    text "{size=+5}[dsd]":
        xpos 1730
        ypos 14
    text "{size=+2}[dsmarts]":
        xpos 770
        ypos 533
    if shame < 0:
        text "{size=+2}Shameless":
            xpos 770
            ypos 583
    else:
        text "{size=+2}[dshame]%":
            xpos 770
            ypos 583
    if virgin == 0:
        text "{size=+2}Virgin":
            xpos 770
            ypos 632
    elif status == 0:
        text "{size=+2}Virgin":
            xpos 770
            ypos 632
    elif status > 55:
        text "{size=+2}Nymphomaniac":
            xpos 770
            ypos 632
    elif status > 40:
        text "{size=+2}Slut":
            xpos 770
            ypos 632
    elif status > 25:
        text "{size=+2}Liberated":
            xpos 770
            ypos 632
    elif status > 15:
        text "{size=+2}Experienced":
            xpos 770
            ypos 632
    elif status > 6:
        text "{size=+2}Novice":
            xpos 770
            ypos 632
    elif status > 0:
        text "{size=+2}Inexperienced":
            xpos 770
            ypos 632
    if pregnancyshowing == 0:
        if onpill == 0:
            if pregchan == 2:
                text "{size=+2}Safe Day":
                    xpos 770
                    ypos 685
            elif pregchan == 1:
                text "{size=+2}Risky Day":
                    xpos 770
                    ypos 685
            elif pregchan == 0:
                text "{size=+1}Dangerous Day":
                    xpos 770
                    ypos 685
        else:
            text "{size=+2}On Pill":
                xpos 770
                ypos 684
    elif pregnant == 1 and pregnancyshowing == 1:
        text "{size=+2}Knocked Up!":
            xpos 770
            ypos 684
    elif bloated == 1:
        text "{size=+2}Cumflated!":
            xpos 770
            ypos 684

label tips:
    scene bg computer with d
    $ rand = renpy.random.randint(1,10)
    if sd < 30:
        "My main goal right now is to get more experience, so I can open up new opportunities."
        if rand <= 3:
            "I should go work at the student bar. It's easy work and I bet I can get a good pay from tips."
        elif rand > 6:
            "I should take some pictures for LonelyFans. I might have to build up some courage if I want to take particularly risqué images."
        elif True:
            "My college gives grants to students with potential, so I should study, maybe at the Yomo Estate."
    elif sd < 50:
        "I'm growing more comfortable doing lewder things for money. I might be able to convert my sexuality into pure gains $$$."
        if rand <= 3:
            "I might try working at that massage parlour. It seems to pay really well, even if I might have to give a blowjob here and there."
        elif rand > 6:
            "With a bunny suit, I could work at the strip club. That could be a lot of fun."
        elif True:
            "I masturbate every evening, so why not go on my computer do it on ChatFap and earn while I fap? Sounds great to me."
    elif sd < 70:
        "I don't mind sucking a dick or two for some quick cash. It's pretty fun, actually."
        if rand <= 3:
            "I should try working at that studio, it's a little lewd but porn is going to pay more than prostitution."
        if rand > 6:
            "I could visit the club, or the male dorms, and maybe approach a guy myself."
        elif True:
            "I should visit [mika]'s dungeon. I won't get paid, but it'll be a nice break."
    elif sd < 120:
        "Time to see how much money I can get fucking around. The few places I did work at but didn't have enough confidence to sell myself, might have new opportunities for me."
        if rand <= 3 and parkunlocked == 0:
            "I should go out in a lewd outfit. Someone I recognize might see me."
        elif rand <= 3:
            "I should visit [hana] in the park, and see what kind of trouble we can get up to."
        elif rand > 6:
            "I should go back to the Massage Parlour, Strip Club and Studio."
        elif True:
            "Maybe I could try selling myself at the club, male dorms, or even through LonelyFans."
    elif True:
        "I should try and unlock all the endings."
    if rand <= 3:
        "(Need more stats? Try buying stat books from the shops or porn from XTube. These help boost your stats up to 50.)"
    elif rand < 3:
        "(Just short of stats for a choice? Drink some booze for an instant +15! Need even more? Aphrodisiac can be used to give another boost.)"
    elif rand > 6:
        "(Need money? Each point in smarts increases money gained by 0.5%%. You can also use the bank, once unlocked, to gain interest. Late-game LonelyFans and ChatFap can also give huge amounts of money.)"
    $ rand = renpy.random.randint(1,10)
    if morning == 1:
        scene bg bedroomday
    elif True:
        scene bg bedroomnight
    show mc:
        xpos 850
    show pinkbody 0:
        xpos 850
    show mcpiercings blank:
        xpos 850
    show mccatears blank:
        xpos 850
    show mch:
        xpos 850
    show mco:
        xpos 850
    show pinkhair 0:
        xpos 850
    call clothes from _call_clothes_100
    show mce happy:
        xpos 850
    with d
    if morning == 1:
        show bedroom screen border
    call screen bedroom
    with d














screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        xalign 0.0
        yalign 1.05

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"




    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0



init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    yalign 0.05
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos












screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action




define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")







screen quick_menu():


    zorder 100

    if quick_menu:

        vbox:
            style_prefix "quick"

            xalign 0.0
            yalign 1.0


            textbutton _("Save") action ShowMenu('save')
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)


            textbutton _("Back") action Rollback()

            textbutton _("Prefs") action ShowMenu('preferences')




init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")











screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc"):


            textbutton _("Help") action ShowMenu("help")


            textbutton _("Quit") action Quit(confirm=not main_menu)

style gm_nav_button:
    size_group "gm_nav"
style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")








label main_menu:
    if persistent.trueendstage1 == True:
        jump trueending
    elif persistent.trueendstage2 == True:
        jump telaunch
    play music rest
label main_menu2:
    call screen main_menu_screen

screen main_menu_screen():
    tag menu

    if persistent.trueendstage1 == True:
        use main_menu_2
    else:
        use main_menu_1
    imagemap:
        ground "main_menu"
        hover "main_menu_hover"
        hotspot (310, 900, 160, 90) action Start()
        hotspot (575, 900, 170, 90) action ShowMenu("load")
        hotspot (810, 900, 380, 90) action ShowMenu("preferences")
        hotspot (1250, 900, 230, 90) action ShowMenu("about")
        hotspot (1510, 900, 170, 90) action Quit()

screen main_menu_1():
    tag menu
    imagemap:
        ground "main_menu"
        hover "main_menu_hover"
        hotspot (310, 900, 160, 90) action Start()
        hotspot (575, 900, 170, 90) action ShowMenu("load")
        hotspot (810, 900, 380, 90) action ShowMenu("preferences")
        hotspot (1250, 900, 230, 90) action ShowMenu("about")
        hotspot (1510, 900, 170, 90) action Quit()

screen main_menu_2():
    tag menu
    imagemap:
        ground "main_menu2"
        hover "main_menu_hover2"
        hotspot (310, 900, 160, 90) action Start()
        hotspot (575, 900, 170, 90) action ShowMenu("load")
        hotspot (810, 900, 380, 90) action ShowMenu("preferences")
        hotspot (1250, 900, 230, 90) action ShowMenu("about")
        hotspot (1510, 900, 170, 90) action Quit()





















style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")











screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45









screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size











screen save():
    tag menu


    use file_slots(_("Save"))


screen load():
    tag menu


    use file_slots(_("Load"))

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):
        fixed:



            order_reverse True


            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

screen load2():
    tag menu

    add "mc":
        xpos 100
    use file_slots(_("Load"))

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")









screen preferences():
    tag menu


    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))




            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675










screen history():




    predict False tag menu

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")




define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5








screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 45

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 150

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 9

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"









screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







style pref_vbox:
    variant "medium"
    xsize 675



screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
