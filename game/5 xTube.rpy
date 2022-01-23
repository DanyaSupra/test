
label gallery:
    scene bg black
    show xtubeborder
    with d

    menu gallerymenu:
        "Porn!" if True:
            if susumet == 0 and yomomet == 0 and tinamet == 0:
                "Hmm, looks like there isn't anything here yet, I should check back later!"
            label gpm1:
                hide xtubee with d
            menu:
                "Money: [money]"
                "[susu] Tan + Butt from Below ($10)" if xtube1 == 0 and susumet == 1:
                    if money < 10:
                        "Awwhh, I can't afford it!"
                        jump gpm1
                    $ xtube1 = 1
                    "Ohh, let's see what we've got here..."
                    show xtube 1
                    hide xtubeborder
                    show xtubeborder
                    with d
                    play sound success
                    $ sdgain = 1
                    call sdgain from _call_sdgain_43
                    "Lewd! (+[fsd] Sexual Desire)"
                    $ money -= 10
                    "Maybe I should just... slip my panties down for a moment, hehe."
                    ""
                    jump gpm1
                "[susu] Tan + Butt from Below (Bought)" if xtube1 == 1:
                    show xtube 1
                    hide xtubeborder
                    show xtubeborder
                    with d
                    ""
                    jump gpm1
                "[susu] Squatting Butt ($15)" if xtube2 == 0 and susumet == 1:
                    if money < 15:
                        "Awwhh, I can't afford it!"
                        jump gpm1
                    $ xtube2 = 1
                    "Ohh, let's see what we've got here..."
                    show xtube 2
                    show xtubee 2a
                    hide xtubeborder
                    show xtubeborder
                    with d
                    play sound success
                    $ sdgain = 1
                    call sdgain from _call_sdgain_41
                    "Ahh, sexy! (+[fsd] Sexual Desire)"
                    hide xtubee with d
                    "There's even another version!"
                    $ money -= 15
                    "Without even thinking, I start idly rubbing my panties."
                    "Eek! What am I doing? This is one of my closest friends!"
                    ""
                    jump gpm1
                "[susu] Squatting Butt (Bought)" if xtube2 == 1:
                    show xtube 2
                    show xtubee 2a with d
                    hide xtubeborder
                    show xtubeborder
                    with d
                    ""
                    hide xtubee with d
                    ""
                    jump gpm1
                "[susu] Lifeguard ($20)" if xtube3 == 0 and susumet == 1:
                    if money < 20:
                        "Awwhh, I can't afford it!"
                        jump gpm1
                    $ xtube3 = 1
                    "Ohh, let's see what we've got here..."
                    show xtube 3
                    show xtubee 3a
                    hide xtubeborder
                    show xtubeborder
                    with d
                    play sound success
                    $ sdgain = 1
                    call sdgain from _call_sdgain_44
                    "Ohhh, very nice! (+[fsd] Sexual Desire)"
                    hide xtubee with d
                    "Yeahh, take those clothes off..."
                    show xtubee 3b
                    hide xtubeborder
                    show xtubeborder
                    with d
                    "Ahh! Nice lingerie!"
                    call sdgain from _call_sdgain_45
                    $ money -= 20
                    ""
                    jump gpm1
                "[susu] Lifeguard (Bought)" if xtube3 == 1:
                    show xtube 3
                    show xtubee 3a with d
                    hide xtubeborder
                    show xtubeborder
                    with d
                    ""
                    show xtubee 3b with d
                    ""
                    hide xtubee with d
                    ""
                    jump gpm1
                "[yomo] Bathing ($25)" if xtube4 == 0 and yomomet == 1:
                    if money < 25:
                        "Awwhh, I can't afford it!"
                        jump gpm1
                    $ xtube4 = 1
                    "Ahh, [yomo]! I can't believe the most gifted girl in my class is on a website like this."
                    show xtube 4
                    show xtubee 4a
                    hide xtubeborder
                    show xtubeborder
                    with d
                    play sound success
                    $ sdgain = 1
                    call sdgain from _call_sdgain_46
                    "My goodness, she's beautiful. (+[fsd] Sexual Desire)"
                    hide xtubee with d
                    "Eek! She went all the way!"
                    show xtubee 4b
                    hide xtubeborder
                    show xtubeborder
                    with d
                    "Ahh, I just realized! With her hero costume already being so revealing, of course she doesn't mind doing something like this."
                    play sound success
                    $ shameloss = 1
                    call shameloss from _call_shameloss_26
                    "Maybe I should be more open too! (-[fshame] Shame)"
                    $ money -= 25
                    ""
                    jump gpm1
                "[yomo] Bathing (Bought)" if xtube4 == 1:
                    show xtube 4
                    show xtubee 4a
                    hide xtubeborder
                    show xtubeborder
                    with d
                    ""
                    show xtubee 4b with d
                    ""
                    hide xtubee with d
                    ""
                    jump gpm1
                "[tina] From Below ($25)" if xtube5 == 0 and tinamet == 1:
                    if money < 25:
                        "Awwhh, I can't afford it!"
                        jump gpm1
                    $ xtube5 = 1
                    "Funnily enough, I already knew [tina] was a swimsuit model."
                    show xtube 5
                    show xtubee 5b
                    hide xtubeborder
                    show xtubeborder
                    with d
                    play sound success
                    $ sdgain = 1
                    call sdgain from _call_sdgain_47
                    "Hehe, she looks as good as I imagined (+[fsd] Sexual Desire)"
                    hide xtubee with d
                    "W-Wait! She's completely naked! I didn't know she did this kind of modelling."
                    show xtubee 5a
                    hide xtubeborder
                    show xtubeborder
                    with d
                    play sound success
                    $ shameloss = 1
                    call shameloss from _call_shameloss_27
                    "Well, when you have a body like that, why not use it to your advantage? (-[fshame] Shame)"
                    $ money -= 25
                    jump gpm1
                "[tina] From Below (Bought)" if xtube5 == 1:
                    show xtube 5
                    show xtubee 5b with d
                    hide xtubeborder
                    show xtubeborder
                    with d
                    ""
                    show xtubee 5a with d
                    ""
                    hide xtubee with d
                    ""
                    jump gpm1
                "[yoko] Pinup ($50)" if xtube6 == 0 and yokomet == 1:
                    if money < 50:
                        "Awwhh, I can't afford it!"
                        jump gpm1
                    $ xtube6 = 1
                    "Hmm? Is that the girl I met at the bar?"
                    show xtube 6
                    hide xtubeborder
                    show xtubeborder
                    with d
                    play sound success
                    "Heh, it's hard to tell from this angle. I think I'd still tap it!"
                    show xtubee 6a
                    hide xtubeborder
                    show xtubeborder
                    with d
                    "Wow, where can I get myself a set of lingerie like that?"
                    show xtubee 6b
                    hide xtubeborder
                    show xtubeborder
                    with d
                    "Eek! She's fuckin'!"
                    "Well, might as well enjoy myself after paying that much."
                    $ sdgain = 2
                    call sdgain from _call_sdgain_48
                    "I slip off my panties and masturbate to the video. (+[fsd] Sexual Desire)"
                    $ masturbations += 1
                    $ money -= 50
                    jump gpm1
                "[yoko] Pinup (Bought)" if xtube6 == 1:
                    show xtube 6
                    hide xtubeborder
                    show xtubeborder
                    with d
                    ""
                    show xtubee 6a
                    hide xtubeborder
                    show xtubeborder
                    with d
                    ""
                    show xtubee 6b
                    hide xtubeborder
                    show xtubeborder
                    with d
                    ""
                    jump gpm1
                "Back" if True:
                    jump gallery
            jump gallery
        "CG Gallery" if True:

            jump cggallery
        "Back" if True:

            jump computer
    menu xtubep1:
        "Masturbation ($10)" if True:
            ""
        "Flashing ($30)" if True:
            ""
        "Groping ($75)" if True:
            ""
        "Blowjob ($40)" if True:
            ""
        "Legs-Up Sex ($60)" if True:
            ""
        "Missionary Sex ($60)" if True:
            ""
        "Doggystyle Sex ($60)" if True:
            ""
        "Page 2 ->" if True:
            jump xtubep2
        "Other Girls ->" if True:
            ""
        "Back" if True:
            jump computermenu
    menu xtubep2:
        "Double Penetration Threesome ($100)" if True:
            ""
        "<- Page 1" if True:
            jump xtubep1
        "Other Girls ->" if True:
            ""
        "Back" if True:
            jump computermenu

label cggallery:
    label cgm:
        scene bg bedsex
    menu:
        "LonelyFans Route" if True:
            if lonelyfans21 == 0:
                "Complete the LonelyFans route to access this gallery."
                jump cgm
            elif True:
                menu cglfg1:
                    "1 - Casual Clothes set" if lonelyfans1 == 1:
                        show lonelyfansb mirror
                        show lonelyfans 1
                        if hair == 1:
                            show lonelyfans1h black
                        if hair == 2:
                            show lonelyfans1h blonde

                        with d
                        ""
                        scene bg bed with d
                    "2 - Underwear set" if lonelyfans2 == 1:
                        show lonelyfansb mirror
                        show lonelyfans 2
                        if tan == 1:
                            show lonelyfans2tan
                        with d
                        ""
                    "3 - Feet Set" if lonelyfans3 == 1:
                        scene lonelyfansb mirror
                        show lonelyfans 3a
                        with d
                        ""
                        scene lonelyfansb mirror
                        show lonelyfans 3b
                        if hair == 1:
                            show lonelyfans3h black
                        if hair == 2:
                            show lonelyfans3h blonde
                        if piercingson == 1:
                            show lonelyfans3piercings
                        with d
                        ""
                        scene lonelyfansb mirror
                        show lonelyfans 3b
                        if hair == 1:
                            show lonelyfans3h black
                        if hair == 2:
                            show lonelyfans3h blonde
                        if piercingson == 1:
                            show lonelyfans3piercings
                        show lonelyfans3c
                        with d
                        ""
                    "4 - Sexy Underwear Set" if lonelyfans4 == 1:
                        scene lonelyfansb mirror
                        show lonelyfans 4
                        if hair == 1:
                            show lonelyfans4h black
                        if hair == 2:
                            show lonelyfans4h blonde
                        with d
                        ""
                    "5 - Braless Set" if lonelyfans5 == 1:
                        scene lonelyfansb mirror
                        show lonelyfans5
                        if pregnancyshowing == 1:
                            show lonelyfans5p
                        if hair == 1:
                            show lonelyfans5h black
                        if hair == 2:
                            show lonelyfans5h blonde
                        if piercingson == 1:
                            show lonelyfans5piercings
                        with d
                        ""
                    "6 - Nude Set" if lonelyfans6 == 1:
                        scene lonelyfansb mirror
                        if pregnancyshowing == 1:
                            show lonelyfans6p
                        elif True:
                            show lonelyfans6
                        if hair == 1:
                            show lonelyfans6h black
                        if hair == 2:
                            show lonelyfans6h blonde
                        if piercingson == 1:
                            show lonelyfans6piercings
                        with d
                        ""
                    "7 - Ass Focus Set" if lonelyfans7 == 1:
                        scene lonelyfansb mirror
                        show lonelyfans7
                        if pregnancyshowing == 1:
                            show lonelyfans7p
                        if hair == 1:
                            show lonelyfans7h black
                        if hair == 2:
                            show lonelyfans7h blonde
                        if piercingson == 1:
                            show lonelyfans7piercings
                        with d
                        ""
                    "8 - Pussy Focus Set" if lonelyfans8 == 1:
                        scene lonelyfansb mirror
                        show lonelyfans8
                        if pregnancyshowing == 1:
                            show lonelyfans8p
                        if hair == 1:
                            show lonelyfans8h black
                        if hair == 2:
                            show lonelyfans8h blonde
                        if piercingson == 1:
                            show lonelyfans8piercings
                        with d
                        ""
                    "9 - Masturbating Set" if lonelyfans9 == 1:
                        scene lonelyfansb mirror
                        if pregnancyshowing == 1:
                            show lonelyfans9p
                        elif True:
                            show lonelyfans9
                        if hair == 1:
                            show lonelyfans9h black
                        if hair == 2:
                            show lonelyfans9h blonde
                        if piercingson == 1:
                            show lonelyfans9piercings
                        with d
                        ""
                    "Next Page ->" if True:
                        jump cglfg2
                    "Back" if True:
                        jump cgm
                jump cglfg1
                menu cglfg2:
                    "10 - Vibrator Set" if lonelyfans10 == 1:
                        scene lonelyfansb mirror
                        show lonelyfans10
                        if pregnancyshowing == 1:
                            show lonelyfans10p
                        if hair == 1:
                            show lonelyfans10h black
                        if hair == 2:
                            show lonelyfans10h blonde
                        if piercingson == 1:
                            show lonelyfans10piercings
                        with d
                        ""
                    "11 - Camisole Set" if lonelyfans11 == 1:
                        scene lonelyfansb mirror
                        if pregnancyshowing == 1:
                            show lonelyfans11ap
                        elif True:
                            show lonelyfans11a
                        ""
                        if pregnancyshowing == 1:
                            show lonelyfans11bp
                        elif True:
                            show lonelyfans11b
                        if hair == 1:
                            show lonelyfans11h black
                        if hair == 2:
                            show lonelyfans11h blonde
                        if piercingson == 1:
                            show lonelyfans11piercings
                        with d
                        ""
                    "12 - Face Reveal Set" if lonelyfans12 == 1:
                        scene lonelyfansb mirror
                        if pregnancyshowing == 1:
                            show lonelyfans12p
                        elif True:
                            show lonelyfans12
                        if hair == 1:
                            show lonelyfans12h black
                        if hair == 2:
                            show lonelyfans12h blonde
                        if piercingson == 1:
                            show lonelyfans12piercings
                        with d
                        ""
                    "13 - Masturbation Video" if lonelyfans13 == 1:
                        scene lonelyfansb mirror
                        show lonelyfans 13
                        if pregnancyshowing == 1:
                            show lonelyfans 13p
                        if hair == 1:
                            show lonelyfans13h black
                        if hair == 2:
                            show lonelyfans13h blonde
                        if piercingson == 1:
                            show lonelyfans13piercings
                        with d
                        ""
                    "14 - Dildo Set" if lonelyfans14 == 1:
                        scene lonelyfansb mirror
                        show lonelyfans 14
                        if pregnancyshowing == 1:
                            show lonelyfans 14p
                        if hair == 1:
                            show lonelyfans14h black
                        if hair == 2:
                            show lonelyfans14h blonde
                        if piercingson == 1:
                            show lonelyfans14piercings
                        with d

                        ""
                    "15 - Bunny Suit Set" if lonelyfans15 == 1:
                        scene lonelyfansb mirror
                        if pregnancyshowing == 1:
                            show lonelyfans15p
                        elif True:
                            show lonelyfans15
                        if hair == 1:
                            show lonelyfans15h black
                        if hair == 2:
                            show lonelyfans15h blonde
                        if piercingson == 1:
                            show lonelyfans15piercings
                        with d
                        ""
                    "16 - Cat Girl Lingerie Set" if lonelyfans16 == 1:
                        scene lonelyfansb mirror
                        if pregnancyshowing == 1:
                            show lonelyfans 16p
                        elif True:
                            show lonelyfans 16
                        if hair == 1:
                            show lonelyfans16h black
                        if hair == 2:
                            show lonelyfans16h blonde
                        with d
                        ""
                    "17 - Buttplug Set" if lonelyfans17 == 1:
                        scene lonelyfansb mirror
                        show lonelyfans 17
                        with d
                        ""
                    "18 - Blowjob Set" if lonelyfans18 == 1:
                        scene lonelyfansb mirror
                        show lonelyfans 18
                        if hair == 1:
                            show lonelyfans18h black
                        if hair == 2:
                            show lonelyfans18h blonde
                        if piercingson == 1:
                            show lonelyfans18piercings
                        with d
                        ""
                    "Previous Page <-" if True:
                        jump cglfg1
                    "Next Page ->" if True:
                        jump cglfg3
                    "Back" if True:
                        jump cgm
                jump cglfg2
                menu cglfg3:
                    "19 - Sex Set" if lonelyfans19 == 1:
                        scene lonelyfansb mirror
                        show frombehindb
                        if tan == 1:
                            show frombehindbtan
                        if hair == 1:
                            show frombehindh black
                        if hair == 2:
                            show frombehindh blonde
                        show frombehind 1
                        with d
                        ""
                        show frombehind v2
                        with d
                        ""
                        show frombehind v3
                        with d
                        ""
                        show frombehind 4
                        with d
                        ""
                    "20 - Anal Set" if lonelyfans20 == 1:
                        scene bg bedsex
                        show buttupb
                        if tan == 1:
                            show buttupb tan
                        if hair == 1:
                            show buttuph black
                        if hair == 2:
                            show buttuph blonde
                        show buttup 1
                        with d
                        ""
                        show buttup a2
                        with d
                        ""
                        show buttup a3
                        with d
                        ""
                        show buttup 4
                        with d
                        ""
                    "21 - Double Penetration Set" if lonelyfans21 == 1:
                        scene fmmthreesomeb
                        if pregnancyshowing == 1:
                            show fmmthreesomea pregnant
                        if tan == 1:
                            show fmmthreesomebtan
                            if pregnancyshowing == 1:
                                show fmmthreesomebtanp
                        if hair == 1:
                            show fmmthreesomeh black
                        if hair == 2:
                            show fmmthreesomeh blonde
                        if piercingson == 1:
                            show fmmthreesomepiercings
                        show fmmthreesome 1
                        with d
                        ""
                        show fmmthreesome 2
                        with d
                        ""
                        show fmmthreesome 3
                        with d
                        ""
                        show fmmthreesome 4
                        with d
                        ""
                    "Previous Page <-" if True:
                        jump cglfg2
                    "Back" if True:
                        jump cgm
                jump cglfg3
        "ChatFap Route" if True:
            if chatfaproute5 == 0:
                "Complete the LonelyFans route to access this gallery."
                jump cgm
            elif True:
                menu cfp1:
                    "Masturbation" if True:
                        scene masturbationb
                        if tan == 1:
                            show masturbationbtan
                            if pregnancyshowing == 1:
                                show masturbationbtanp
                        if hair == 1:
                            show masturbationh black
                        if hair == 2:
                            show masturbationh blonde
                        if piercingson == 1:
                            show masturbationpiercings

                        if pregnancyshowing == 1:
                            show masturbatione pregnant
                        show masturbation 1c
                        show chatfapborder
                        with d
                        ""
                        play sound cum
                        show masturbation 1c with cum
                        ""
                        scene masturbation2b
                        if tan == 1:
                            show masturbation2btan
                            if pregnancyshowing == 1:
                                show masturbation2btanp
                        if hair == 1:
                            show masturbation2h black
                        if hair == 2:
                            show masturbation2h blonde
                        if piercingson == 1:
                            show masturbation2piercings
                        show masturbation2e 1
                        if pregnancyshowing == 1:
                            show masturbation2 underwearp
                        elif True:
                            show masturbation2 underwear
                        show chatfapborder
                        with d
                        ""
                        scene masturbationb
                        if tan == 1:
                            show masturbationbtan
                            if pregnancyshowing == 1:
                                show masturbationbtanp
                        if hair == 1:
                            show masturbationh black
                        if hair == 2:
                            show masturbationh blonde
                        if piercingson == 1:
                            show masturbationpiercings
                        show masturbation 1b
                        if pregnancyshowing == 1:
                            show masturbatione pregnant
                        show chatfapborder
                        with d
                        ""
                    "Vibrator" if True:
                        scene masturbation2b
                        if tan == 1:
                            show masturbation2btan
                            if pregnancyshowing == 1:
                                show masturbation2btanp
                        if hair == 1:
                            show masturbation2h black
                        if hair == 2:
                            show masturbation2h blonde
                        if piercingson == 1:
                            show masturbation2piercings
                        show masturbation2e 1
                        show masturbation2 vibe
                        if pregnancyshowing == 1:
                            show masturbation2p
                        show chatfapborder
                        with d
                        ""
                        play sound cum
                        show masturbation2e 2
                        show masturbation2 vibe with vpunch
                        ""
                    "Dildo" if True:

                        scene masturbation2b
                        if tan == 1:
                            show masturbation2btan
                            if pregnancyshowing == 1:
                                show masturbation2btanp
                        if hair == 1:
                            show masturbation2h black
                        if hair == 2:
                            show masturbation2h blonde
                        if piercingson == 1:
                            show masturbation2piercings
                        show masturbation2e 1
                        show masturbation2 dildo
                        if tan == 1:
                            show masturbation2 dildotan
                        if pregnancyshowing == 1:
                            show masturbation2p
                        show chatfapborder
                        with d
                        ""
                        play sound cum
                        show masturbation2e 2 with cum
                        ""
                    "Camisole" if True:
                        scene bg bedsex
                        show camoutfitsb
                        if tan == 1:
                            show camoutfitsb tan
                            if pregnancyshowing == 1:
                                show camoutfitsb tanp
                        elif True:
                            if pregnancyshowing == 1:
                                show camoutfitse2 pregnant
                        if hair == 1:
                            show camoutfitsh black
                        if hair == 2:
                            show camoutfitsh blonde
                        if piercingson == 1:
                            show camoutfitspiercings
                        show camoutfits 1
                        if pregnancyshowing == 1:
                            show camoutfitse camisolep
                        elif True:
                            show camoutfitse camisole
                        show chatfapborder
                        with d
                        ""
                        show camoutfitsvibe with d
                        ""
                        show camoutfits 2 with cum
                        play sound cum
                        ""
                    "Bunny Suit" if True:
                        scene bg bedsex
                        show camoutfitsb
                        if tan == 1:
                            show camoutfitsb tan
                            if pregnancyshowing == 1:
                                show camoutfitsb tanp
                        elif True:
                            if pregnancyshowing == 1:
                                show camoutfitse2 pregnant
                        if hair == 1:
                            show camoutfitsh black
                        if hair == 2:
                            show camoutfitsh blonde
                        if piercingson == 1:
                            show camoutfitspiercings
                        show camoutfits 1
                        if pregnancyshowing == 1:
                            show camoutfitse bunnysuitp
                        elif True:
                            show camoutfitse bunnysuit
                        show chatfapborder
                        with d
                        ""
                        show camoutfitsvibe with d
                        ""
                        show camoutfits 2 with cum
                        play sound cum
                        ""
                    "Cat Lingerie" if True:
                        scene bg bedsex
                        show camoutfitsb
                        if tan == 1:
                            show camoutfitsb tan
                            if pregnancyshowing == 1:
                                show camoutfitsb tanp
                        elif True:
                            if pregnancyshowing == 1:
                                show camoutfitse2 pregnant
                        if hair == 1:
                            show camoutfitsh black
                        if hair == 2:
                            show camoutfitsh blonde
                        if piercingson == 1:
                            show camoutfitspiercings
                        show camoutfits 1
                        if pregnancyshowing == 1:
                            show camoutfitse catgirlp
                        elif True:
                            show camoutfitse catgirl
                        show chatfapborder
                        with d
                        ""
                        play sound cum
                        show camoutfitsvibe with d
                        ""
                    "Back" if True:
                        jump cgm
                jump cfp1
        "Bar Route" if True:
            if barroute <= 0:
                "Complete the LonelyFans route to access this gallery."
                jump cgm
            elif True:
                menu cgbm:
                    "Bar Uniform Undressing" if True:
                        scene bg bar
                        call clothesbar from _call_clothesbar
                        show mce horny
                        with d
                        ""
                        call clothesbar2 from _call_clothesbar2
                        with d
                        "No Panties"
                        call clothesbar3 from _call_clothesbar3
                        with d
                        "Shirtless"
                    "Upskirt" if True:
                        scene bg bar
                        show bar2a
                        with d
                        ""
                    "Gloryhole BJ" if True:
                        scene gloryholebjb
                        if tan == 1:
                            show gloryholebjbtan
                        if hair == 1:
                            show gloryholebjh black
                        if hair == 2:
                            show gloryholebjh blonde
                        if piercingson == 1:
                            show gloryholebjpiercings
                        show gloryholebj 1
                        with d
                        ""
                        play sound cum
                        show gloryholebj 2 with cum
                        ""
                    "Gloryhole Sex" if True:
                        show gloryholesexb
                        if tan == 1:
                            show gloryholesexbtan
                        if piercingson == 1:
                            show gloryholesexpiercings
                        if hair == 1:
                            show gloryholesexh black
                        if hair == 2:
                            show gloryholesexh blonde
                        if pregnancyshowing == 1:
                            show gloryholesexe pregnant
                            if tan == 1:
                                show gloryholesexe tanpregnant
                        with d
                        ""
                        play sound cum
                        show gloryholesex cum with cum
                        ""
                    "Threesome" if True:
                        scene fmmthreesomeb
                        if pregnancyshowing == 1:
                            show fmmthreesomea pregnant
                        if tan == 1:
                            show fmmthreesomebtan
                            if pregnancyshowing == 1:
                                show fmmthreesomebtanp
                        if hair == 1:
                            show fmmthreesomeh black
                        if hair == 2:
                            show fmmthreesomeh blonde
                        if piercingson == 1:
                            show fmmthreesomepiercings
                        show fmmthreesome 1
                        if pregnancyshowing == 1:
                            show fmmthreesomea pregnant
                        with d
                        ""
                        play sound cum
                        show fmmthreesome 2
                        with d
                        ""
                        play sound cum
                        show fmmthreesome 3 with cum
                        ""
                    "Back" if True:
                        jump cgm
                jump cgbm
        "Boyfriend Route" if True:
            if ca < 10:
                "Reach ten crush affection to access this gallery. You currently have [ca]."
                jump cgm
            elif True:
                menu cgbfm:
                    "Blowjob" if True:
                        scene bg bed with d
                        show lyingblowjobb
                        if tan == 1:
                            show lyingblowjobb tan
                        if piercingson == 1:
                            show lyingblowjobpiercings
                        if hair == 1:
                            show lyingblowjobh black
                        if hair == 2:
                            show lyingblowjobh blonde
                        show lyingblowjob 1
                        if pregnancyshowing == 1:
                            show lyingblowjobe milk
                        with d
                        ""
                        play sound cum
                        show lyingblowjob 2 with cum
                        ""
                    "Vaginal" if True:
                        scene doggystylesexb
                        if pregnancyshowing == 1:
                            show doggystylesexe pregnant
                        if tan == 1:
                            show doggystylesexbtan
                            if pregnancyshowing == 1:
                                show doggystylesexbtanp
                        if hair == 1:
                            show doggystylesexh black
                        if hair == 2:
                            show doggystylesexh blonde
                        if piercingson == 1:
                            show doggystylesexpiercings
                        show doggystylesex 1
                        with d
                        ""
                        play sound cum
                        show doggystylesex 2
                        with d
                        ""
                        play sound cum
                        show doggystylesex 3 with cum
                    "Anal" if True:
                        scene doggystylesexb
                        if pregnancyshowing == 1:
                            show doggystylesexe pregnant
                        if tan == 1:
                            show doggystylesexbtan
                            if pregnancyshowing == 1:
                                show doggystylesexbtanp
                        if hair == 1:
                            show doggystylesexh black
                        if hair == 2:
                            show doggystylesexh blonde
                        if piercingson == 1:
                            show doggystylesexpiercings
                        show doggystylesex 1
                        with d
                        ""
                        play sound cum
                        show doggystylesex a2
                        with d
                        ""
                        play sound cum
                        show doggystylesex a3 with cum
                        ""
                    "Back" if True:
                        jump cgm
                jump cgbfm
        "Massage Parlour Route" if True:
            if massageroute4 == 0:
                "Complete the massage route to access this gallery"
            elif True:
                menu cgmprm:
                    "Bunny Vaginal" if True:
                        show bunnyspreadingassb
                        show bunnyspreadingass 1
                        with d
                        ""
                        play sound cum
                        show bunnyspreadingass 2
                        with d
                        ""
                        play sound cum
                        show bunnyspreadingass 3 with cum
                        ""
                    "Bunny Anal" if True:
                        scene bg massage with d
                        show bunnystandingbendingb
                        show bunnystandingbending 1
                        with d
                        ""
                        play sound cum
                        show bunnystandingbending a2
                        with d
                        ""
                        play sound cum
                        show bunnystandingbending a3 with cum
                        ""
                    "Blowjob Service" if True:
                        scene bg massage
                        show lyingblowjobb
                        show lyingblowjob 1
                        if pregnancyshowing == 1:
                            show lyingblowjobe milk
                        with d
                        ""
                        play sound cum
                        show lyingblowjob 2 with cum
                        ""
                    "Missionary Service" if True:
                        scene missionarysexb
                        if pregnancyshowing == 1:
                            show missionarysexa pregnant1
                        if tan == 1:
                            show missionarysexbtan
                            if pregnancyshowing == 1:
                                show missionarysexbtanp
                        if hair == 1:
                            show missionarysexh black
                        if hair == 2:
                            show missionarysexh blonde
                        if piercingson == 1:
                            show missionarysexpiercings
                        show missionarysex 1
                        with d
                        ""
                        play sound cum
                        show missionarysex 2
                        with d
                        ""
                        play sound cum
                        show missionarysex 3
                        if pregnancyshowing == 1 and tan == 0:
                            show missionarysexa pregnant2
                        with cum
                        ""
                        play sound cum
                        show missionarysex 4 with cum
                        ""
                        play sound cum
                        show missionarysex 5 with d
                        ""
                    "Anal Service" if True:
                        scene bg massage
                        show legs-upsexb
                        if tan == 1:
                            show legs-upsexbtan
                        if hair == 1:
                            show legs-upsexh black
                        if hair == 2:
                            show legs-upsexh blonde
                        show legs-upsex 1
                        with d
                        ""
                        play sound cum
                        show legs-upsex a2 with d
                        ""
                        play sound cum
                        show legs-upsex a2
                        with cum
                        ""
                        play sound cum
                        show legs-upsex a3 with cum
                        ""
                        play sound cum
                        show legs-upsex 4 with d
                        ""
                    "Back" if True:
                        jump cgm
                jump cgmprm
        "Prostitution Route" if True:
            if sd < 100:
                "Get a sexual desire of 100 to access this gallery"
            elif True:
                menu cgpm:
                    "Club Blowjob" if True:
                        scene blowjob3b
                        if tan == 1:
                            show blowjob3b tan
                        if hair == 1:
                            show blowjob3h black
                        if hair == 2:
                            show blowjob3h blonde
                        if piercingson == 1:
                            show blowjob3piercings
                        show blowjob3 1
                        with d
                        ""
                        play sound cum
                        show blowjob3 2 with cum
                        play sound cum
                        show blowjob3 2 with cum
                        ""
                    "Club Vaginal" if True:
                        scene sidewayssexb
                        if pregnancyshowing == 1:
                            show sidewayssexe pregnant
                        if tan == 1:
                            show sidewayssexbtan
                            if pregnancyshowing == 1:
                                show sidewayssexbtanp
                        if hair == 1:
                            show sidewayssexh black
                        if hair == 2:
                            show sidewayssexh blonde
                        if piercingson == 1:
                            show sidewayssexpiercings
                        show sidewayssex 1
                        with d
                        ""
                        play sound cum
                        show sidewayssex v2
                        with d
                        ""
                        play sound cum
                        show sidewayssex v3 with cum
                        ""
                    "Club Anal" if True:
                        scene sidewayssexb
                        if pregnancyshowing == 1:
                            show sidewayssexe pregnant
                        if tan == 1:
                            show sidewayssexbtan
                            if pregnancyshowing == 1:
                                show sidewayssexbtanp
                        if hair == 1:
                            show sidewayssexh black
                        if hair == 2:
                            show sidewayssexh blonde
                        if piercingson == 1:
                            show sidewayssexpiercings
                        show sidewayssex 1
                        show sidewayssex 1
                        if pregnancyshowing == 1:
                            show sidewayssexe pregnant
                        with d
                        ""
                        play sound cum
                        show sidewayssex a2 with d
                        ""
                        play sound cum
                        show sidewayssex a3 with cum
                        ""
                    "Male Dorms Blowjob" if True:
                        scene bg bedsex
                        show povblowjobb
                        if tan == 1:
                            show povblowjobbtan
                        if piercingson == 1:
                            show povblowjobpiercings
                        if hair == 1:
                            show povblowjobh black
                        if hair == 2:
                            show povblowjobh blonde
                        show povblowjob 1
                        with d
                        ""
                        play sound cum
                        show povblowjob 2 with cum
                        ""
                    "Male Dorms Vaginal" if True:
                        scene bg bedsex
                        show sittingsexb
                        if pregnancyshowing == 1:
                            show sittingsexe p1
                        if tan == 1:
                            show sittingsexbtan
                            if pregnancyshowing == 1:
                                show sittingsexbtanp
                        if hair == 1:
                            show sittingsexh black
                        if hair == 2:
                            show sittingsexh blonde
                        if piercingson == 1:
                            show sittingsexpiercings
                        show sittingsex 1
                        with d
                        ""
                        play sound cum
                        show sittingsex v2
                        with d
                        ""
                        play sound cum
                        show sittingsex v3 with cum
                        ""
                        play sound cum
                        show sittingsex 4 with d
                        ""
                    "Male Dorms Anal" if True:
                        scene bg bedsex
                        show sittingsexb
                        if pregnancyshowing == 1:
                            show sittingsexe p1
                        if tan == 1:
                            show sittingsexbtan
                            if pregnancyshowing == 1:
                                show sittingsexbtanp
                        if hair == 1:
                            show sittingsexh black
                        if hair == 2:
                            show sittingsexh blonde
                        if piercingson == 1:
                            show sittingsexpiercings
                        show sittingsex 1
                        with d
                        ""
                        play sound cum
                        show sittingsex a2 with d
                        ""
                        play sound cum
                        show sittingsex a3 with cum
                        ""
                        play sound cum
                        show sittingsex 4 with d
                        ""
                    "Back" if True:
                        jump cgm
                jump cgpm
        "Studio Route" if True:
            if studioroute4 == 0:
                "Complete the Studio Route to access this gallery"
            elif True:
                menu cgsm:
                    "Nude/Masturbation Shoot" if True:
                        scene bg thecouch
                        show lyingb
                        if pregnancyshowing == 1:
                            show lyinge pregnant
                        if tan == 1:
                            show lyingbtan
                            if pregnancyshowing == 1:
                                show lyingbtanp
                        if hair == 1:
                            show lyingh black
                        if hair == 2:
                            show lyingh blonde
                        if piercingson == 1:
                            show lyingpiercings
                        show lying 1
                        with d
                        ""
                        scene bg black
                        show bg thecouch
                        show masturbation3b
                        if pregnancyshowing == 1:
                            show masturbation3e pregnant
                        if tan == 1:
                            show masturbation3btan
                            if pregnancyshowing == 1:
                                show masturbation3btanp
                        if hair == 1:
                            show masturbation3h black
                        if hair == 2:
                            show masturbation3h blonde
                        if piercingson == 1:
                            show masturbation3piercings
                        with d
                        ""
                        scene bg black
                        show bg thecouch
                        show doggy2b
                        if pregnancyshowing == 1:
                            show doggy2e pregnant
                        if tan == 1:
                            show doggy2tan
                            if pregnancyshowing == 1:
                                show doggy2tanp
                        if hair == 1:
                            show doggy2h black
                        if hair == 2:
                            show doggy2h blonde
                        if piercingson == 1:
                            show doggy2piercings
                        show doggy2 1
                        with d
                        ""
                    "Paizuri" if True:
                        scene bg thecouch
                        show paizurib
                        if tan == 1:
                            show paizuribtan
                        if hair == 1:
                            show paizurih black
                        if hair == 2:
                            show paizurih blonde
                        if piercingson == 1:
                            show paizuripiercings
                        show paizuri 1
                        ""
                        show paizuri 2 with d
                        ""
                        play sound cum
                        show paizuri 3 with cum
                        ""
                    "Butt-Up Vaginal" if True:
                        scene bg thecouch
                        show buttupb
                        if tan == 1:
                            show buttupb tan
                        if hair == 1:
                            show buttuph black
                        if hair == 2:
                            show buttuph blonde
                        show buttup 1
                        with d
                        ""
                        play sound cum
                        show buttup v2 with d
                        ""
                        play sound cum
                        show buttup v3 with cum
                        ""
                        play sound cum
                        show buttup 4 with d
                    "Jacko Sex" if True:
                        scene jackob
                        if tan == 1:
                            show jackobtan
                        if pregnancyshowing == 1:
                            show jackoe pregnant
                            if tan == 1:
                                show jackoe tanpregnant
                        if hair == 1:
                            show jackoh black
                        if hair == 2:
                            show jackoh blonde
                        show jacko 1
                        with d
                        ""
                        play sound cum
                        show jacko 2 with d
                        ""
                        play sound cum
                        show jacko 3 with cum
                        ""
                        play sound cum
                        show jacko 4 with d
                        ""
                    "Standing Double Penetration" if True:
                        show standingdpb
                        if tan == 1:
                            show standingdpbtan
                        if pregnancyshowing == 1:
                            show standingdpe pregnant
                            if tan == 1:
                                show standingdpe tanpregnant
                        if hair == 1:
                            show standingdph black
                        if hair == 2:
                            show standingdph blonde
                        if piercingson == 1:
                            show standingdppiercings
                        show standingdp 1
                        ""
                        play sound cum
                        show standingdp 2 with cum
                        ""
                    "Back" if True:
                        jump cgm
                jump cgsm
        "Swimming Pool Route" if True:
            if tinaroute2 == 0:
                "Complete [tina]'s route to access this gallery."
            elif True:
                menu:
                    "Changing Room Sex" if True:
                        scene bg changingrooms with d
                        play music action
                        show masturbation3b
                        if pregnancyshowing == 1:
                            show masturbation3e pregnant
                        if tan == 1:
                            show masturbation3btan
                            if pregnancyshowing == 1:
                                show masturbation3btanp
                        if hair == 1:
                            show masturbation3h black
                        if hair == 2:
                            show masturbation3h blonde
                        if piercingson == 1:
                            show masturbation3piercings
                        with d
                        ""
                        play sound cum
                        show masturbation3 2 with d
                        ""
                        show masturbation3face 2
                        if tan == 1:
                            show masturbation3face 2tan
                        with d
                        play sound cum
                        show masturbation3 3 with cum
                        ""
                    "[tina] Voyeur Doggystyle" if True:
                        show tinavoyeur1b
                        show tinavoyeur1 1
                        with d
                        ""
                        play sound cum
                        show tinavoyeur1 2 with d
                        ""
                        play sound cum
                        show tinavoyeur1 3 with cum
                        ""
                        show tinavoyeur1 4 with d
                        ""
                    "[tina] Voyeur Full-Frontal (Vaginal to Anal)" if True:
                        show tinavoyeur2b
                        show tinavoyeur2 1
                        with d
                        ""
                        play sound cum
                        show tinavoyeur2 2
                        with d
                        ""
                        play sound cum
                        show tinavoyeur2 v3
                        with d
                        ""
                        play sound cum
                        show tinavoyeur2 v4 with cum
                        ""
                        show tinavoyeur2 5 with d
                        ""
                        play sound cum
                        show tinavoyeur2 a3 with d
                        ""
                        play sound cum
                        show tinavoyeur2 a4 with cum
                        ""
                        show tinavoyeur2 5 with d
                        ""
                    "[tina] Threesome" if True:
                        show tinathreesomeb
                        if tan == 1:
                            show tinathreesomebtan
                        if hair == 1:
                            show tinathreesomeh black
                        if hair == 2:
                            show tinathreesomeh blonde
                        show tinathreesome 1
                        with d
                        ""
                        show tinathreesome 2 with d
                        ""
                        play sound cum
                        show tinathreesome 3 with cum
                        ""
                        play sound cum
                        show tinathreesome 4 with d
                        ""
                    "Back" if True:
                        jump cgm
        "Strip Club Route" if True:
            if stripclubwork4 == 0 or twilightdance3 == 0:
                "Complete the Strip Club's route, and buy the full dance from Twilight to access this gallery."
            elif True:
                menu cgscm:
                    "Bunnysuit Paizuri" if True:
                        scene bg booth
                        show paizurib
                        if tan == 1:
                            show paizuribtan
                        if hair == 1:
                            show paizurih black
                        if hair == 2:
                            show paizurih blonde
                        if piercingson == 1:
                            show paizuripiercings
                        show paizurie bunny
                        show paizuri 1
                        with d
                        ""
                        show paizuri 1b with d
                        ""
                        show paizuri 2 with d
                        ""
                        play sound cum
                        show paizuri 3 with cum
                        ""
                    "Bunnysuit Doggystyle" if True:
                        scene bg booth
                        show doggy2b
                        if tan == 1:
                            show doggy2tan
                            if pregnancyshowing == 1:
                                show doggy2tanp
                        if hair == 1:
                            show doggy2h black
                        if hair == 2:
                            show doggy2h blonde
                        show doggy2bunny
                        if pregnancyshowing == 1:
                            show doggy2e bunnypregnant
                        if piercingson == 1:
                            show doggy2piercings
                        show doggy2 1
                        with d
                        ""
                        play sound cum
                        show doggy2 2
                        ""
                        play sound cum
                        show doggy2 3 with cum
                        ""
                    "Bunnysuit Standing DP" if True:
                        show standingdpb
                        if tan == 1:
                            show standingdpbtan
                        if pregnancyshowing == 1:
                            show standingdpe pregnant
                            if tan == 1:
                                show standingdpe tanpregnant
                        if hair == 1:
                            show standingdph black
                        if hair == 2:
                            show standingdph blonde
                        if piercingson == 1:
                            show standingdppiercings
                        if pregnancyshowing == 1:
                            show standingdpe bunnypregnant
                        elif True:
                            show standingdpe bunny
                        show standingdp 1
                        with d
                        ""
                        play sound cum
                        show standingdp 2 with cum
                        ""
                    "Bunnysuit Anal Bukkake Gangbang" if True:
                        show analbukkakeb
                        if tan == 1:
                            show analbukkakebtan
                            if pregnancyshowing == 1:
                                show analbukkakebtanp
                        if piercingson == 1:
                            show analbukkakepiercings
                        if hair == 1:
                            show analbukkakeh black
                        if hair == 2:
                            show analbukkakeh blonde
                        if pregnancyshowing == 0:
                            show analbukkakee bunny
                        elif True:
                            show analbukkakee bunnypregnant
                        show analbukkake 1
                        with d
                        ""
                        play sound cum
                        show analbukkake 2 with d
                        ""
                        show analbukkake 3 with d
                        ""
                        show analbukkake 4 with d
                        ""
                        play sound cum
                        show analbukkake 5 with cum
                        ""
                        play sound cum
                        show analbukkake 6 with cum
                        ""
                        play sound cum
                        show analbukkake 7 with d
                        ""
                    "Full Twilight Dance" if True:
                        show twilightdance 1 with d
                        ""
                        show twilightdance 2 with d
                        ""
                        show twilightcunnilingus 1 with d
                        ""
                        show twilightcunnilingus 2 with d
                        ""
                    "Back" if True:
                        jump cgm
                jump cgscm
        "Lewd Sounds On/Off" if True:
            if xtubesounds == 0:
                $ xtubesounds = 1
                play ambience sex fadein 2.0
                play sound2 foreplay1 fadein 2.0
            elif True:
                $ xtubesounds = 0
                stop ambience
                stop sound2
        "Sex Music On/Off" if True:
            if xtubemusic == 0:
                $ xtubemusic = 1
                play music action
            elif True:
                $ xtubemusic = 0
                stop music
        "Page 2 ->" if True:
            jump cgm2
        "Back" if True:
            jump computermenu
    jump cgm
    label cgm2:
        scene bg bedsex
        menu:
            "[yoko] Route" if True:
                if yokoroute2 == 0:
                    "Complete [yoko]'s route to access this gallery"
                elif True:
                    menu cgym:
                        "Cunnilingus" if True:
                            scene bg bedsex
                            show yokoroute2b
                            show yokoroute2 1
                            with d
                            ""
                            show yokoroute2 2 with d
                            ""
                        "Sixty-Nine" if True:
                            scene bg bedsex
                            show yoko69b
                            if tan == 1:
                                show yoko69btan
                            if hair == 1:
                                show yoko69h black
                            if hair == 2:
                                show yoko69h blonde
                            show yoko69 1
                            with d
                            ""
                            show yoko69 2
                            with d
                            ""
                        "Futa" if True:
                            scene bg bedsex
                            show yokofutab
                            if tan == 1:
                                show yokofutabtan
                            if hair == 1:
                                show yokofutah black
                            if hair == 2:
                                show yokofutah blonde
                            show yokofuta 1
                            with d
                            ""
                            play sound cum
                            show yokofuta 2 with d
                            ""
                            show yokofuta 3 with d
                            ""
                            play sound cum
                            show yokofuta 4 with cum
                            ""
                            show yokofuta 5 with d
                            ""
                        "Selfcest" if True:
                            scene bg bedsex
                            show yokoselfcestb
                            if tan == 1:
                                show yokoselfcestbtan
                            if pregnancyshowing == 1:
                                show yokoselfcestbp
                                if tan == 1:
                                    show yokoselfcestbtanp
                            if hair == 1:
                                show yokoselfcesth black
                            if hair == 2:
                                show yokoselfcesth blonde
                            show yokoselfcest 1
                            with d
                            ""
                            show yokoselfcest 2
                            with d
                            ""
                        "Back" if True:
                            jump cgm2
                    jump cgym
            "Beach Route" if True:
                if susuroute4 == 0:
                    "Complete [susu]'s route to access this gallery"
                elif True:
                    menu cgbrm:
                        "Sunbathing Makeout to Vaginal to Anal" if True:
                            call sunbathingart from _call_sunbathingart_5
                            ""
                            show malemakeout
                            if hair == 1:
                                show malemakeouth black
                            elif hair == 2:
                                show malemakeouth blonde
                            with d
                            ""
                            show malemakeout2 with d
                            ""
                            scene bg black
                            call sunbathingart from _call_sunbathingart_6
                            hide beach1e
                            hide beachtanunderwearp
                            ""
                            play sound cum
                            show beach1 v3 with d
                            ""
                            play sound cum
                            show beach1 v4 with cum
                            ""
                            play sound cum
                            show beach1 5 with d
                            ""
                            show beach1 a3 with d
                            ""
                            play sound cum
                            show beach1 a4 with cum
                            ""
                            play sound cum
                            show beach1 5 with d
                            ""
                        "Beach Bar Vaginal to Anal" if True:
                            scene standingsexb
                            if tan == 1:
                                show standingsexbtan
                                if pregnancyshowing == 1:
                                    show standingsexbtanp
                            if hair == 1:
                                show standingsexh black
                            if hair == 2:
                                show standingsexh blonde
                            show standingsexswimsuit
                            if pregnancyshowing == 1:
                                show standingsexe pregnant
                                if tan == 1:
                                    show standingsexe pregnanttan
                            show standingsex 1
                            with d
                            ""
                            play sound equip
                            hide standingsexswimsuit with d
                            ""
                            play sound cum
                            show standingsex v2 with d
                            ""
                            show standingsex v3 with d
                            ""
                            play sound cum
                            show standingsex v4 with cum
                            ""
                            show standingsex v5 with cum
                            ""
                            play sound cum
                            show standingsex a2 with d
                            ""
                            show standingsex a3 with d
                            ""
                            play sound cum
                            show standingsex a4 with cum
                            ""
                            play sound cum
                            show standingsex a5 with cum
                            ""
                        "[susu] Makeout" if True:
                            play sound equip
                            scene bg house2
                            show yomomakeout1
                            with d
                            play sound2 foreplay1
                            ""
                            show yomomakeout2
                            with d
                            ""
                        "[susu] 69 + Sex Variant" if True:
                            show yuri69b
                            if pregnancyshowing == 1:
                                show yuri69e pregnant
                            if tan == 1:
                                show yuri69btan
                                if pregnancyshowing == 1:
                                    show yuri69btanp
                            if hair == 1:
                                show yuri69h black
                            if hair == 2:
                                show yuri69h blonde
                            show yuri69susu
                            with d
                            ""
                            play sound cum
                            show yuri69orgasm with cum
                            ""
                            play sound cum
                            show yuri69 1 with cum
                            ""
                            play sound cum
                            show yuri69 2 with cum
                            ""
                            play sound cum
                            show yuri69 3 with cum
                            ""
                        "[susu] Threesome" if True:
                            scene ffmthreesomeb
                            if tan == 1:
                                show ffmthreesomebtan
                            if hair == 1:
                                show ffmthreesomeh black
                            if hair == 2:
                                show ffmthreesomeh blonde
                            show ffmthreesome 1
                            with d
                            ""
                            play sound cum
                            show ffmthreesome 2 with cum
                            ""
                            play sound cum
                            show ffmthreesome 3 with cum
                            ""
                            show ffmthreesome 4 with d
                            ""
                        "Back" if True:
                            jump cgm2
                    jump cgbrm
            "Tutor Route" if True:
                if yomotutor4 == 0:
                    "Complete [yomo]'s route to access this gallery"
                elif True:
                    menu cgtrm:
                        "Tutor Seduction Blowjob" if True:
                            show povblowjobb
                            if tan == 1:
                                show povblowjobbtan
                            if piercingson == 1:
                                show povblowjobpiercings
                            if hair == 1:
                                show povblowjobh black
                            if hair == 2:
                                show povblowjobh blonde
                            show povblowjob 1
                            with d
                            ""
                            play sound cum
                            show povblowjob 2 with cum
                            ""
                        "[yomo] Makeout" if True:
                            play sound equip
                            scene bg house1
                            show yomomakeout1
                            with d
                            ""
                            show yomomakeout2
                            with d
                            ""
                        "[yomo] 69" if True:
                            show yuri69b
                            if pregnancyshowing == 1:
                                show yuri69e pregnant
                            if tan == 1:
                                show yuri69btan
                                if pregnancyshowing == 1:
                                    show yuri69btanp
                            if hair == 1:
                                show yuri69h black
                            if hair == 2:
                                show yuri69h blonde
                            show yuri69yomo
                            with d
                            ""
                            play sound cum
                            show yuri69orgasm with cum
                            ""
                        "[yomo] Fingering" if True:
                            scene yomofingeringb
                            if pregnancyshowing == 1:
                                show yomofingeringe pregnant
                            if tan == 1:
                                show yomofingeringbtan
                                if pregnancyshowing == 1:
                                    show yomofingeringbtanp
                            if hair == 1:
                                show yomofingeringh black
                            if hair == 2:
                                show yomofingeringh blonde
                            if piercingson == 1:
                                show yomofingeringpiercings
                            show yomofingering 1
                            with d
                            ""
                            show yomofingering 2
                            with d
                            ""
                            show yomofingering 3
                            with d
                            ""
                        "Back" if True:
                            jump cgm2
                    jump cgtrm
            "Exhibitionist Route" if True:
                if sd < 120:
                    "Reach a sexual desire of 120 to access this gallery"
                elif True:
                    menu:
                        "Public Sex" if True:
                            scene bg sky
                            show chikanb
                            if tan == 1:
                                show chikanbtan
                            if hair == 1:
                                show chikanh black
                            if hair == 2:
                                show chikanh blonde
                            show chikan park1
                            with d
                            ""
                            play sound fondle
                            show chikan park2
                            with d
                            ""
                            play sound spank
                            show chikan park3 with cum
                            ""
                            play sound cum
                            show chikan park4 with d
                            ""
                            play sound cum
                            show chikan park5 with cum
                            ""
                            play sound cum
                            show chikan park6 with d
                            ""
                        "Public Gangbang" if True:
                            scene parkgangbangb
                            if tan == 1:
                                show parkgangbangbtan
                            if pregnancyshowing == 1:
                                show parkgangbangbp
                                if tan == 1:
                                    show parkgangbangbtanp
                            if piercingson == 1:
                                show parkgangbangbpiercings
                            if hair == 1:
                                show parkgangbangh black
                            if hair == 2:
                                show parkgangbangh blonde
                            with d
                            ""
                            play sound cum
                            show parkgangbang 1 with d
                            ""
                            play sound cum
                            show parkgangbang 2 with cum
                            ""
                            play sound cum
                            show parkgangbang 3 with d
                            ""
                        "Back" if True:
                            jump cgm2
            "Dungeon Route" if True:
                if dungeonroute3 == 0:
                    "Complete the Dungeon Route to access this gallery."
                elif True:
                    menu cgmdu:
                        "Shibari (Strap-On, then Penis)" if True:
                            scene shibarib
                            if tan == 1:
                                show shibaribtan
                            if hair == 1:
                                show shibarih black
                            if hair == 2:
                                show shibarih blonde
                            if piercingson == 1:
                                show shibaribpiercings
                            show shibari 1
                            with d
                            ""
                            show shibari 2 with d
                            ""
                            play sound equip
                            show shibari 4 with d
                            ""
                            show shibari 5s with d
                            ""
                            show shibari 6s with d
                            ""
                            show shibari 7 with d
                            ""
                            show shibari 5 with d
                            ""
                            show shibari 6 with d
                            ""
                            show shibari 7 with d
                            ""
                        "Suspended (Pick and Choose)" if True:
                            scene bg black with d
                            show suspendedb
                            if tan == 1:
                                show suspendedbtan
                            if hair == 1:
                                show suspendedh black
                            if hair == 2:
                                show suspendedh blonde
                            if piercingson == 1:
                                show suspendedpiercings
                            show suspended 1
                            with d
                            ""
                            $ dungeonpunishments = 0
                            $ dblindfold = 0
                            $ dgag = 0
                            $ dspanking = 0
                            $ dwhipping = 0
                            menu dungeonpcg:
                                "Pick Punishments"
                                "Blindfold" if dblindfold == 0:
                                    play sound equip
                                    show suspendedblindfold with d
                                    $ dblindfold = 1
                                    $ dungeonpunishments += 1
                                    jump dungeonpcg
                                "Gag" if dgag == 0:
                                    play sound equip
                                    show suspendedgag
                                    if tan == 1:
                                        show suspendedgag tan
                                    with d
                                    $ dgag = 1
                                    $ dungeonpunishments += 1
                                    jump dungeonpcg
                                "Nipple Piercings" if piercingson == 0:
                                    $ piercingson == 1
                                    $ dungeonpunishments += 1
                                    jump dungeonpcg
                                "Spanking" if dspanking == 0:
                                    play sound spank
                                    show suspendedspanked with d
                                    $ dspanking = 1
                                    $ dungeonpunishments += 1
                                    jump dungeonpcg
                                "Whipping" if dspanking == 1 and dwhipping == 0:
                                    play sound whip
                                    show suspendedspanked 2 with d
                                    $ dwhipping = 1
                                    $ dungeonpunishments += 1
                                    jump dungeonpcg
                                "Done Picking" if True:
                                    pass
                            ""
                            menu dungeonp2cg:
                                "Pick Penetration"
                                "Oral" if True:
                                    hide suspendedgag
                                    show suspended 2
                                    play sound cum
                                    show suspendedoral
                                    if tan == 1:
                                        show suspendedoral tan
                                    ""
                                    play sound cum
                                    show suspendedoral 2
                                    if tan == 1:
                                        show suspendedoral 2tan
                                    with cum
                                    ""
                                    show suspendedoral 3 with d
                                    ""
                                "Vaginal" if True:
                                    show suspended 2
                                    play sound cum
                                    show suspendedvaginal with d
                                    ""
                                    play sound cum
                                    show suspendedvaginal 2 with cum
                                    ""
                                    show suspendedvaginal 3 with d
                                    ""
                                "Spitroast!" if True:
                                    hide suspendedgag
                                    show suspended 2
                                    play sound cum
                                    show suspendedoral
                                    if tan == 1:
                                        show suspendedoral tan
                                    show suspendedvaginal
                                    with d
                                    ""
                                    play sound cum
                                    show suspendedoral 2
                                    if tan == 1:
                                        show suspendedoral 2tan
                                    show suspendedvaginal 2
                                    with cum
                                    ""
                                    show suspendedoral 3
                                    show suspendedvaginal 3
                                    with d
                                    ""
                        "Back" if True:
                            jump cgm2
                    jump cgmdu
            "Bank Route" if True:
                if bankhj and banksex == 0:
                    "Reach 4%% interest to unlock this gallery."
                    jump cgm2
                menu:
                    "Bank Handjob" if True:
                        scene bankerhjb
                        if pregnancyshowing == 1:
                            show bankerhjbp
                        if tan == 1:
                            show bankerhjbtan
                            if pregnancyshowing == 1:
                                show bankerhjbtanp
                        if piercingson == 1:
                            show bankerhjpiercings
                        if hair == 1:
                            show bankerhjh black
                        if hair == 2:
                            show bankerhjh blonde
                        show bankerhj 1
                        with d
                        ""
                        play sound cum
                        show bankerhj 2 with cum
                        ""
                    "Bank Sex" if True:
                        show bankersexb
                        if pregnancyshowing == 1:
                            show bankersexbp
                        if tan == 1:
                            show bankersexbtan
                            if pregnancyshowing == 1:
                                show bankersexbtanp
                        if hair == 1:
                            show bankersexh black
                        if hair == 2:
                            show bankersexh blonde
                        if piercingson == 1:
                            show bankersexpiercings
                        show bankersex 1
                        with d
                        ""
                        play sound cum
                        show bankersex 2 with d
                        ""
                        play sound cum
                        show bankersex 3 with cum
                        ""
                        play sound cum
                        show bankersex 4 with d
                        ""
                jump cgm2
            "Random Events" if True:
                if sd < 100:
                    "Reach a sexual desire of 100 to access this gallery"
                elif True:
                    menu cgrem:
                        "Public Flashing" if True:
                            scene bg street
                            "I remove my blazer, and then..."
                            show flashing
                            if pregnancyshowing == 1:
                                show flashing p
                            if tan == 1:
                                show flashingtan
                                if pregnancyshowing == 1:
                                    show flashingtanp
                            if piercingson == 1:
                                show flashingpiercings
                            if hair == 1:
                                show flashingh black
                            if hair == 2:
                                show flashingh blonde
                            with d
                            ""
                        "Double Penetration" if True:
                            scene fmmthreesomeb
                            if pregnancyshowing == 1:
                                show fmmthreesomea pregnant
                            if tan == 1:
                                show fmmthreesomebtan
                                if pregnancyshowing == 1:
                                    show fmmthreesomebtanp
                            if hair == 1:
                                show fmmthreesomeh black
                            if hair == 2:
                                show fmmthreesomeh blonde
                            if piercingson == 1:
                                show fmmthreesomepiercings
                            show fmmthreesome 1
                            with d
                            ""
                            play sound cum
                            show fmmthreesome 2
                            with d
                            ""
                            play sound cum
                            show fmmthreesome 3 with cum
                            ""
                        "Bus Chikan" if True:
                            scene bg bus with d
                            show student1:
                                xpos 950
                            call clothesformal from _call_clothesformal_29
                            show mce neutral
                            with d
                            ""
                            scene chikanbus
                            show chikanb
                            if tan == 1:
                                show chikanbtan
                            if hair == 1:
                                show chikanh black
                            if hair == 2:
                                show chikanh blonde
                            show chikan 1
                            with d
                            ""
                            show chikan 2
                            with d
                            ""
                            play sound rip
                            show chikan 3 with d
                            ""
                            play sound cum
                            show chikan 4 with d
                            ""
                            play sound cum
                            show chikan 5 with cum
                            ""
                            play sound cum
                            show chikan 6 with d
                            ""
                        "Club Bathroom Blowjob" if True:
                            show bg toiletstall with d
                            show povblowjobb
                            if tan == 1:
                                show povblowjobbtan
                            if piercingson == 1:
                                show povblowjobpiercings
                            if hair == 1:
                                show povblowjobh black
                            if hair == 2:
                                show povblowjobh blonde
                            show povblowjob 1
                            with d
                            ""
                            play sound cum
                            show povblowjob 2 with cum
                            ""
                        "[susu] Threesome" if True:
                            scene bg bed
                            show ffmthreesomeb
                            if tan == 1:
                                show ffmthreesomebtan
                            if hair == 1:
                                show ffmthreesomeh black
                            if hair == 2:
                                show ffmthreesomeh blonde
                            show ffmthreesome 1
                            with d
                            ""
                            play sound cum
                            show ffmthreesome 2
                            with d
                            ""
                            play sound cum
                            show ffmthreesome 3 with cum
                            ""
                        "Classroom Blackmail Blowjob" if True:
                            scene classroombjb
                            if tan == 1:
                                show classroombjbtan
                            if hair == 1:
                                show classroombjh black
                            if hair == 2:
                                show classroombjh blonde
                            if piercingson == 1:
                                show classroombjpiercings
                            show classroombj 1
                            with d
                            ""
                            show classroombj 2 with d
                            ""
                            play sound cum
                            show classroombj 3 with cum
                            ""
                        "Classroom Blackmail Sex" if True:
                            scene classroomsexb
                            if tan == 1:
                                show classroomsexbtan
                            if pregnancyshowing == 1:
                                show classroomsexbp
                                if tan == 1:
                                    show classroomsexbtanp
                            if hair == 1:
                                show classroomsexh black
                            if hair == 2:
                                show classroomsexh blonde
                            if piercingson == 1:
                                show classroomsexpiercings
                            show classroomsex 1
                            show classroomsexo uniform1
                            with d
                            ""
                            show classroomsex 1b with d
                            ""
                            play sound equip
                            show classroomsexo uniform2 with d
                            ""
                            show classroomsex 1b with d
                            ""
                            show classroomsex 2 with d
                            ""
                            play sound cum
                            show classroomsex 3 with cum
                            ""
                            play sound cum
                            show classroomsex 4 with d
                            ""
                        "Onsen Double Handjob" if True:
                            scene onsenbjb
                            if tan == 1:
                                show onsenbjbtan
                            if pregnancyshowing == 1:
                                show onsenbjbp
                                if tan == 1:
                                    show onsenbjbtanp
                            if hair == 1:
                                show onsenbjh black
                            if hair == 2:
                                show onsenbjh blonde
                            if piercingson == 1:
                                show onsenbjpiercings
                            show onsenbj 1
                            with d
                            ""
                            play sound cum
                            show onsenbj 2 with cum
                            ""
                        "Onsen Sex (Vaginal, then Anal)" if True:
                            scene onsensexb
                            if tan == 1:
                                show onsensexbtan
                            if pregnancyshowing == 1:
                                show onsensexbp
                                if tan == 1:
                                    show onsensexbtanp
                            if hair == 1:
                                show onsensexh black
                            if hair == 2:
                                show onsensexh blonde
                            show onsensex 1b
                            with d
                            ""
                            show onsensex v2 with d
                            ""
                            show onsensex v3 with cum
                            ""
                            show onsensex 4 with d
                            ""
                            show onsensex a2 with d
                            ""
                            show onsensex a3 with cum
                            ""
                            show onsensex 4 with d
                            ""
                        "Tentacles Standing" if True:
                            play sound whip
                            scene tentaclesstandingsexb
                            if tan == 1:
                                show tentaclesstandingsexbtan
                            if pregnancyshowing == 1:
                                show tentaclesstandingsex1p
                                show tentaclesstandingsexbp
                                if tan == 1:
                                    show tentaclesstandingsexbtanp
                            if hair == 1:
                                show tentaclesstandingsexh black
                            if hair == 2:
                                show tentaclesstandingsexh blonde
                            if piercingson == 1:
                                show tentaclesstandingsexpiercings
                            show tentaclesstandingsex 1
                            show tentaclesstandingsex1clip
                            show mrslime:
                                xpos 50 ypos 100
                            with hpunch
                            ""
                            hide tentaclesstandingsex1clip
                            show tentaclesstandingsex 2
                            ""
                            play sound cum
                            show tentaclesstandingsex 3
                            ""
                            play sound cum
                            show tentaclesstandingsex 4 with cum
                            ""
                            play sound cum
                            show tentaclesstandingsex 5 with d
                            ""
                            play sound equip
                            show tentaclesstandingsex 6
                            show tentaclesstandingsex1p
                            with d
                            ""
                        "Tentacles Double Penetration" if True:
                            scene tentaclesdpsexb
                            if tan == 1:
                                show tentaclesdpsexbtan
                            if pregnancyshowing == 1:
                                show tentaclesdpsexbp
                                if tan == 1:
                                    show tentaclesdpsexbtanp
                            if hair == 1:
                                show tentaclesdpsexh black
                            if hair == 2:
                                show tentaclesdpsexh blonde
                            if piercingson == 1:
                                show tentaclesdpsexpiercings
                            show tentaclesdpsex 1
                            with d
                            ""
                            play sound cum
                            show tentaclesdpsex 2 with d
                            ""
                            play sound cum
                            show tentaclesdpsexmilking 1
                            show tentaclesdpsex 2b
                            with d
                            ""
                            play sound cum
                            show tentaclesdpsex 2
                            show tentaclesdpsexmilking 2
                            with cum
                            ""
                            play sound cum
                            show tentaclesdpsex 3 with cum
                            ""
                            play sound cum
                            hide tentaclesdpsexmilking
                            show tentaclesdpsex 4
                            show tentaclesdpsexmilk
                            with d
                            ""
                        "Back" if True:
                            jump cgm2
                    jump cgrem
            "Endings" if True:
                menu cgem:
                    "View endings to see the CG here."
                    "Loyal Girlfriend Ending" if lge == 1:
                        scene loyalgfendb
                        if tan == 1:
                            show loyalgfendbtan
                        if hair == 1:
                            show loyalgfendh black
                        if hair == 2:
                            show loyalgfendh blonde
                        if piercingson == 1:
                            show loyalgfendpiercings
                        show loyalgfend 1
                        with d
                        ""
                        show loyalgfend 2
                        with d
                        ""
                        show loyalgfend 3
                        with d
                        ""
                        show loyalgfend 4
                        with d
                        ""
                    "Cheating Girlfriend Ending" if lge == 1:
                        show ntrendb
                        if tan == 1:
                            show ntrendbtan
                        if hair == 1:
                            show ntrendh black
                        if hair == 2:
                            show ntrendh blonde
                        if piercingson == 1:
                            show ntrendpiercings
                        show ntrend 1
                        with d
                        ""
                        show ntrend 2
                        with d
                        ""
                        show ntrend 3
                        with d
                        ""
                        show ntrend 4
                        with d
                        ""
                    "[yomo]'s Girlfriend Ending" if yge == 1:
                        show yomoendingb
                        if pregnancyshowing == 1:
                            show yomoendingbp
                        if tan == 1:
                            show yomoendingbtan
                            if pregnancyshowing == 1:
                                show yomoendingbtanp
                        if hair == 1:
                            show yomoendingh black
                        if hair == 2:
                            show yomoendingh blonde
                        if piercingson == 1:
                            show yomoendingpiercings
                        show yomoending 1
                        with d
                        ""
                        show yomoending 2
                        with d
                        ""
                        show yomoending 3
                        with d
                        ""
                    "Dominatrix Ending" if de == 1:
                        menu:
                            "Choose a Sex Partner"
                            "Female" if True:
                                show dominatrixendb
                                if tan == 1:
                                    show dominatrixendbtan
                                if hair == 1:
                                    show dominatrixendh black
                                if hair == 2:
                                    show dominatrixendh blonde
                                if piercingson == 1:
                                    show dominatrixendpiercings
                                show dominatrixendcollar
                                show dominatrixenddom 1
                                show dominatrixend f1
                                with d
                                ""
                                show dominatrixenddom 2 with d
                                ""
                                show dominatrixend f2 with d
                                ""
                                show dominatrixend f3 with d
                                ""
                            "Male" if True:
                                show dominatrixendb
                                if tan == 1:
                                    show dominatrixendbtan
                                if hair == 1:
                                    show dominatrixendh black
                                if hair == 2:
                                    show dominatrixendh blonde
                                if piercingson == 1:
                                    show dominatrixendpiercings
                                show dominatrixendcollar
                                show dominatrixenddom 1
                                show dominatrixend 1
                                with d
                                ""
                                show dominatrixenddom 2
                                with d
                                ""
                                play sound cum
                                show dominatrixend v2 with d
                                ""
                                play sound cum
                                show dominatrixend v3 with cum
                                ""
                    "Yandere Ending" if yye == 1:
                        scene bg bedsex
                        show yokoselfcestb
                        if tan == 1:
                            show yokoselfcestbtan
                        if pregnancyshowing == 1:
                            show yokoselfcestbp
                            if tan == 1:
                                show yokoselfcestbtanp
                        if hair == 1:
                            show yokoselfcesth black
                        if hair == 2:
                            show yokoselfcesth blonde
                        show yokoselfcest alt1
                        with d
                        ""
                        play sound cum
                        show yokoselfcest alt2 with cum
                        ""
                        play sound cum
                        show yokoselfcest alt3 with d
                        ""
                    "E-Girl Empress Ending" if ege == 1:
                        scene bg bedsex
                        show camoutfitsb
                        show camoutfitse catgirl
                        show camoutfitsh pink
                        show camoutfits 1
                        show chatfapborder
                        with d
                        ""
                        show egirlempressendb
                        show egirlempressend 1
                        with d
                        ""
                        show egirlempressend 2
                        with d
                        ""
                        show egirlempressend 3
                        with d
                        ""
                        show egirlempressend 4
                        with d
                        ""
                        show egirlempressend 5
                        with d
                        ""
                        show egirlempressend 6
                        with d
                        ""
                        show egirlempressend 7
                        with d
                        ""
                        show egirlempressend 8
                        with d
                        ""
                    "Professional Masseuse" if mpe == 1:
                        scene bg massage
                        show massageparlourthreesomeb
                        if tan == 1:
                            show massageparlourthreesomebtan
                        if hair == 1:
                            show massageparlourthreesomeh black
                        if hair == 2:
                            show massageparlourthreesomeh blonde
                        show massageparlourthreesome 1
                        with d
                        ""
                        show massageparlourthreesome 2 with d
                        ""
                        show massageparlourthreesome 3 with d
                        ""
                        show massageparlourthreesome 4 with d
                        ""
                    "Drug Addict Ending" if dae == 1:
                        scene addictendb
                        show addictend 1
                        with d
                        ""
                        show addictend 2
                        with d
                        ""
                        show addictend 3
                        with d
                        ""
                        show addictend 4
                        with d
                        ""
                    "Sex Addict Ending" if sae == 1:
                        show sexaddictendingb
                        if tan == 1:
                            show sexaddictendingbtan
                        if hair == 1:
                            show sexaddictendingh black
                        if hair == 2:
                            show sexaddictendingh blonde
                        if piercingson == 1:
                            show sexaddictendingpiercings
                        show sexaddictending 1
                        with d
                        ""
                        play sound cum
                        show sexaddictending 2 with cum
                        ""
                    "Prostitute Ending" if pe == 1:
                        scene prostituteendb
                        if tan == 1:
                            show prostituteendbtan
                        if hair == 1:
                            show prostituteendh black
                        if hair == 2:
                            show prostituteendh blonde
                        if piercingson == 1:
                            show prostituteendpiercings
                        show prostituteend 1
                        show prostituteendjar 1
                        with d
                        ""
                        scene holeb
                        show holetina
                        with d
                        ""
                        play sound cum
                        show hole cum with cum
                        ""
                        play sound2 foreplay1
                        play ambience sex
                        scene prostituteendb
                        if tan == 1:
                            show prostituteendbtan
                        if hair == 1:
                            show prostituteendh black
                        if hair == 2:
                            show prostituteendh blonde
                        if piercingson == 1:
                            show prostituteendpiercings
                        show prostituteendjar 2
                        show prostituteend 2
                        if tan == 1:
                            show prostituteendclip 1
                        show prostituteendborder
                        with d
                        ""
                        play sound cum
                        if tan == 1:
                            show prostituteendclip 2
                        show prostituteend 3 with cum
                        ""
                        play sound cum
                        if tan == 1:
                            show prostituteendclip 3
                        show prostituteend 4 with d
                        ""
                    "Slime Girl" if sge == 1:
                        show tinathreesomeb
                        if tan == 1:
                            show tinathreesomebtan
                        if hair == 1:
                            show tinathreesomeh black
                        if hair == 2:
                            show tinathreesomeh blonde
                        show tinathreesomeslime
                        show tinathreesome 1
                        show tinathreesomepinkeyes
                        with d
                        ""
                        hide tinathreesomepinkeyes
                        show tinathreesome 2b
                        with d
                        ""
                        play sound cum
                        show tinathreesome 3b with cum
                        ""
                        play sound cum
                        show tinathreesome 4
                        show tinathreesomepinkeyes
                        with d
                        ""
                    "Back" if True:
                        jump cgm2
                jump cgem
            "Lewd Sounds On/Off" if True:
                if xtubesounds == 0:
                    $ xtubesounds = 1
                    play ambience sex fadein 2.0
                    play sound2 foreplay1 fadein 2.0
                elif True:
                    $ xtubesounds = 0
                    stop ambience
                    stop sound2
            "Sex Music On/Off" if True:
                if xtubemusic == 0:
                    $ xtubemusic = 1
                    play music action
                elif True:
                    $ xtubemusic = 0
                    stop music
            "<- Page 1" if True:
                jump cgm
            "Back" if True:
                jump computermenu
    jump cgm2

label cheatgallery:
    label cheatm:
        scene bg bedsex
    menu:
        "Cheats Gallery Page 1"
        "LonelyFans Route" if True:
            menu cheatlfg1:
                "1 - Casual Clothes set" if True:
                    show lonelyfansb mirror
                    show lonelyfans 1
                    if hair == 1:
                        show lonelyfans1h black
                    if hair == 2:
                        show lonelyfans1h blonde

                    with d
                    ""
                    scene bg bed with d
                "2 - Underwear set" if True:
                    show lonelyfansb mirror
                    show lonelyfans 2
                    if tan == 1:
                        show lonelyfans2tan
                    with d
                    ""
                "3 - Feet Set" if True:
                    scene lonelyfansb mirror
                    show lonelyfans 3a
                    with d
                    ""
                    scene lonelyfansb mirror
                    show lonelyfans 3b
                    if hair == 1:
                        show lonelyfans3h black
                    if hair == 2:
                        show lonelyfans3h blonde
                    if piercingson == 1:
                        show lonelyfans3piercings
                    with d
                    ""
                    scene lonelyfansb mirror
                    show lonelyfans 3b
                    if hair == 1:
                        show lonelyfans3h black
                    if hair == 2:
                        show lonelyfans3h blonde
                    if piercingson == 1:
                        show lonelyfans3piercings
                    show lonelyfans3c
                    with d
                    ""
                "4 - Sexy Underwear Set" if True:
                    scene lonelyfansb mirror
                    show lonelyfans 4
                    if hair == 1:
                        show lonelyfans4h black
                    if hair == 2:
                        show lonelyfans4h blonde
                    with d
                    ""
                "5 - Braless Set" if True:
                    scene lonelyfansb mirror
                    show lonelyfans5
                    if pregnancyshowing == 1:
                        show lonelyfans5p
                    if hair == 1:
                        show lonelyfans5h black
                    if hair == 2:
                        show lonelyfans5h blonde
                    if piercingson == 1:
                        show lonelyfans5piercings
                    with d
                    ""
                "6 - Nude Set" if True:
                    scene lonelyfansb mirror
                    if pregnancyshowing == 1:
                        show lonelyfans6p
                    elif True:
                        show lonelyfans6
                    if hair == 1:
                        show lonelyfans6h black
                    if hair == 2:
                        show lonelyfans6h blonde
                    if piercingson == 1:
                        show lonelyfans6piercings
                    with d
                    ""
                "7 - Ass Focus Set" if True:
                    scene lonelyfansb mirror
                    show lonelyfans7
                    if pregnancyshowing == 1:
                        show lonelyfans7p
                    if hair == 1:
                        show lonelyfans7h black
                    if hair == 2:
                        show lonelyfans7h blonde
                    if piercingson == 1:
                        show lonelyfans7piercings
                    with d
                    ""
                "8 - Pussy Focus Set" if True:
                    scene lonelyfansb mirror
                    show lonelyfans8
                    if pregnancyshowing == 1:
                        show lonelyfans8p
                    if hair == 1:
                        show lonelyfans8h black
                    if hair == 2:
                        show lonelyfans8h blonde
                    if piercingson == 1:
                        show lonelyfans8piercings
                    with d
                    ""
                "9 - Masturbating Set" if True:
                    scene lonelyfansb mirror
                    if pregnancyshowing == 1:
                        show lonelyfans9p
                    elif True:
                        show lonelyfans9
                    if hair == 1:
                        show lonelyfans9h black
                    if hair == 2:
                        show lonelyfans9h blonde
                    if piercingson == 1:
                        show lonelyfans9piercings
                    with d
                    ""
                "Next Page ->" if True:
                    jump cheatlfg2
                "Back" if True:
                    jump cheatgallery
            jump cheatlfg1
            menu cheatlfg2:
                "10 - Vibrator Set" if True:
                    scene lonelyfansb mirror
                    show lonelyfans10
                    if pregnancyshowing == 1:
                        show lonelyfans10p
                    if hair == 1:
                        show lonelyfans10h black
                    if hair == 2:
                        show lonelyfans10h blonde
                    if piercingson == 1:
                        show lonelyfans10piercings
                    with d
                    ""
                "11 - Camisole Set" if True:
                    scene lonelyfansb mirror
                    if pregnancyshowing == 1:
                        show lonelyfans11ap
                    elif True:
                        show lonelyfans11a
                    ""
                    if pregnancyshowing == 1:
                        show lonelyfans11bp
                    elif True:
                        show lonelyfans11b
                    if hair == 1:
                        show lonelyfans11h black
                    if hair == 2:
                        show lonelyfans11h blonde
                    if piercingson == 1:
                        show lonelyfans11piercings
                    with d
                    ""
                "12 - Face Reveal Set" if True:
                    scene lonelyfansb mirror
                    if pregnancyshowing == 1:
                        show lonelyfans12p
                    elif True:
                        show lonelyfans12
                    if hair == 1:
                        show lonelyfans12h black
                    if hair == 2:
                        show lonelyfans12h blonde
                    if piercingson == 1:
                        show lonelyfans12piercings
                    with d
                    ""
                "13 - Masturbation Video" if True:
                    scene lonelyfansb mirror
                    show lonelyfans 13
                    if pregnancyshowing == 1:
                        show lonelyfans 13p
                    if hair == 1:
                        show lonelyfans13h black
                    if hair == 2:
                        show lonelyfans13h blonde
                    if piercingson == 1:
                        show lonelyfans13piercings
                    with d
                    ""
                "14 - Dildo Set" if True:
                    scene lonelyfansb mirror
                    show lonelyfans 14
                    if pregnancyshowing == 1:
                        show lonelyfans 14p
                    if hair == 1:
                        show lonelyfans14h black
                    if hair == 2:
                        show lonelyfans14h blonde
                    if piercingson == 1:
                        show lonelyfans14piercings
                    with d

                    ""
                "15 - Bunny Suit Set" if True:
                    scene lonelyfansb mirror
                    if pregnancyshowing == 1:
                        show lonelyfans15p
                    elif True:
                        show lonelyfans15
                    if hair == 1:
                        show lonelyfans15h black
                    if hair == 2:
                        show lonelyfans15h blonde
                    if piercingson == 1:
                        show lonelyfans15piercings
                    with d
                    ""
                "16 - Cat Girl Lingerie Set" if True:
                    scene lonelyfansb mirror
                    if pregnancyshowing == 1:
                        show lonelyfans 16p
                    elif True:
                        show lonelyfans 16
                    if hair == 1:
                        show lonelyfans16h black
                    if hair == 2:
                        show lonelyfans16h blonde
                    with d
                    ""
                "17 - Buttplug Set" if True:
                    scene lonelyfansb mirror
                    show lonelyfans 17
                    with d
                    ""
                "18 - Blowjob Set" if True:
                    scene lonelyfansb mirror
                    show lonelyfans 18
                    if hair == 1:
                        show lonelyfans18h black
                    if hair == 2:
                        show lonelyfans18h blonde
                    if piercingson == 1:
                        show lonelyfans18piercings
                    with d
                    ""
                "Previous Page <-" if True:
                    jump cheatlfg1
                "Next Page ->" if True:
                    jump cheatlfg3
                "Back" if True:
                    jump cheatgallery
            jump cheatlfg2
            menu cheatlfg3:
                "19 - Sex Set" if True:
                    scene lonelyfansb mirror
                    show frombehindb
                    if tan == 1:
                        show frombehindbtan
                    if hair == 1:
                        show frombehindh black
                    if hair == 2:
                        show frombehindh blonde
                    show frombehind 1
                    with d
                    ""
                    show frombehind v2
                    with d
                    ""
                    show frombehind v3
                    with d
                    ""
                    show frombehind 4
                    with d
                    ""
                "20 - Anal Set" if True:
                    scene bg bedsex
                    show buttupb
                    if tan == 1:
                        show buttupb tan
                    if hair == 1:
                        show buttuph black
                    if hair == 2:
                        show buttuph blonde
                    show buttup 1
                    with d
                    ""
                    show buttup a2
                    with d
                    ""
                    show buttup a3
                    with d
                    ""
                    show buttup 4
                    with d
                    ""
                "21 - Double Penetration Set" if True:
                    scene fmmthreesomeb
                    if pregnancyshowing == 1:
                        show fmmthreesomea pregnant
                    if tan == 1:
                        show fmmthreesomebtan
                        if pregnancyshowing == 1:
                            show fmmthreesomebtanp
                    if hair == 1:
                        show fmmthreesomeh black
                    if hair == 2:
                        show fmmthreesomeh blonde
                    if piercingson == 1:
                        show fmmthreesomepiercings
                    show fmmthreesome 1
                    with d
                    ""
                    show fmmthreesome 2
                    with d
                    ""
                    show fmmthreesome 3
                    with d
                    ""
                    show fmmthreesome 4
                    with d
                    ""
                "Previous Page <-" if True:
                    jump cheatlfg2
                "Back" if True:
                    jump cheatgallery
            jump cheatlfg3
        "ChatFap Route" if True:
            menu cheatfp1:
                "Masturbation" if True:
                    scene masturbationb
                    if tan == 1:
                        show masturbationbtan
                        if pregnancyshowing == 1:
                            show masturbationbtanp
                    if hair == 1:
                        show masturbationh black
                    if hair == 2:
                        show masturbationh blonde
                    if piercingson == 1:
                        show masturbationpiercings

                    if pregnancyshowing == 1:
                        show masturbatione pregnant
                    show masturbation 1c
                    show chatfapborder
                    with d
                    ""
                    play sound cum
                    show masturbation 1c with cum
                    ""
                    scene masturbation2b
                    if tan == 1:
                        show masturbation2btan
                        if pregnancyshowing == 1:
                            show masturbation2btanp
                    if hair == 1:
                        show masturbation2h black
                    if hair == 2:
                        show masturbation2h blonde
                    if piercingson == 1:
                        show masturbation2piercings
                    show masturbation2e 1
                    if pregnancyshowing == 1:
                        show masturbation2 underwearp
                    elif True:
                        show masturbation2 underwear
                    show chatfapborder
                    with d
                    ""
                    scene masturbationb
                    if tan == 1:
                        show masturbationbtan
                        if pregnancyshowing == 1:
                            show masturbationbtanp
                    if hair == 1:
                        show masturbationh black
                    if hair == 2:
                        show masturbationh blonde
                    if piercingson == 1:
                        show masturbationpiercings
                    show masturbation 1b
                    if pregnancyshowing == 1:
                        show masturbatione pregnant
                    show chatfapborder
                    with d
                    ""
                "Vibrator" if True:
                    scene masturbation2b
                    if tan == 1:
                        show masturbation2btan
                        if pregnancyshowing == 1:
                            show masturbation2btanp
                    if hair == 1:
                        show masturbation2h black
                    if hair == 2:
                        show masturbation2h blonde
                    if piercingson == 1:
                        show masturbation2piercings
                    show masturbation2e 1
                    show masturbation2 vibe
                    if pregnancyshowing == 1:
                        show masturbation2p
                    show chatfapborder
                    with d
                    ""
                    play sound cum
                    show masturbation2e 2
                    show masturbation2 vibe with vpunch
                    ""
                "Dildo" if True:

                    scene masturbation2b
                    if tan == 1:
                        show masturbation2btan
                        if pregnancyshowing == 1:
                            show masturbation2btanp
                    if hair == 1:
                        show masturbation2h black
                    if hair == 2:
                        show masturbation2h blonde
                    if piercingson == 1:
                        show masturbation2piercings
                    show masturbation2e 1
                    show masturbation2 dildo
                    if tan == 1:
                        show masturbation2 dildotan
                    if pregnancyshowing == 1:
                        show masturbation2p
                    show chatfapborder
                    with d
                    ""
                    play sound cum
                    show masturbation2e 2 with cum
                    ""
                "Camisole" if True:
                    scene bg bedsex
                    show camoutfitsb
                    if tan == 1:
                        show camoutfitsb tan
                        if pregnancyshowing == 1:
                            show camoutfitsb tanp
                    elif True:
                        if pregnancyshowing == 1:
                            show camoutfitse2 pregnant
                    if hair == 1:
                        show camoutfitsh black
                    if hair == 2:
                        show camoutfitsh blonde
                    if piercingson == 1:
                        show camoutfitspiercings
                    show camoutfits 1
                    if pregnancyshowing == 1:
                        show camoutfitse camisolep
                    elif True:
                        show camoutfitse camisole
                    show chatfapborder
                    with d
                    ""
                    show camoutfitsvibe with d
                    ""
                    show camoutfits 2 with cum
                    play sound cum
                    ""
                "Bunny Suit" if True:
                    scene bg bedsex
                    show camoutfitsb
                    if tan == 1:
                        show camoutfitsb tan
                        if pregnancyshowing == 1:
                            show camoutfitsb tanp
                    elif True:
                        if pregnancyshowing == 1:
                            show camoutfitse2 pregnant
                    if hair == 1:
                        show camoutfitsh black
                    if hair == 2:
                        show camoutfitsh blonde
                    if piercingson == 1:
                        show camoutfitspiercings
                    show camoutfits 1
                    if pregnancyshowing == 1:
                        show camoutfitse bunnysuitp
                    elif True:
                        show camoutfitse bunnysuit
                    show chatfapborder
                    with d
                    ""
                    show camoutfitsvibe with d
                    ""
                    show camoutfits 2 with cum
                    play sound cum
                    ""
                "Cat Lingerie" if True:
                    scene bg bedsex
                    show camoutfitsb
                    if tan == 1:
                        show camoutfitsb tan
                        if pregnancyshowing == 1:
                            show camoutfitsb tanp
                    elif True:
                        if pregnancyshowing == 1:
                            show camoutfitse2 pregnant
                    if hair == 1:
                        show camoutfitsh black
                    if hair == 2:
                        show camoutfitsh blonde
                    if piercingson == 1:
                        show camoutfitspiercings
                    show camoutfits 1
                    if pregnancyshowing == 1:
                        show camoutfitse catgirlp
                    elif True:
                        show camoutfitse catgirl
                    show chatfapborder
                    with d
                    ""
                    play sound cum
                    show camoutfitsvibe with d
                    ""
                "Back" if True:
                    jump cheatm
            jump cfp1
        "Bar Route" if True:
            menu cheatbm:
                "Bar Uniform Undressing" if True:
                    scene bg bar
                    call clothesbar from _call_clothesbar_1
                    show mce horny
                    with d
                    ""
                    call clothesbar2 from _call_clothesbar2_1
                    with d
                    "No Panties"
                    call clothesbar3 from _call_clothesbar3_1
                    with d
                    "Shirtless"
                "Upskirt" if True:
                    scene bg bar
                    show bar2a
                    with d
                    ""
                "Gloryhole BJ" if True:
                    scene gloryholebjb
                    if tan == 1:
                        show gloryholebjbtan
                    if hair == 1:
                        show gloryholebjh black
                    if hair == 2:
                        show gloryholebjh blonde
                    if piercingson == 1:
                        show gloryholebjpiercings
                    show gloryholebj 1
                    with d
                    ""
                    play sound cum
                    show gloryholebj 2 with cum
                    ""
                "Gloryhole Sex" if True:
                    show gloryholesexb
                    if tan == 1:
                        show gloryholesexbtan
                    if piercingson == 1:
                        show gloryholesexpiercings
                    if hair == 1:
                        show gloryholesexh black
                    if hair == 2:
                        show gloryholesexh blonde
                    if pregnancyshowing == 1:
                        show gloryholesexe pregnant
                        if tan == 1:
                            show gloryholesexe tanpregnant
                    with d
                    ""
                    play sound cum
                    show gloryholesex cum with cum
                    ""
                "Threesome" if True:
                    scene fmmthreesomeb
                    if pregnancyshowing == 1:
                        show fmmthreesomea pregnant
                    if tan == 1:
                        show fmmthreesomebtan
                        if pregnancyshowing == 1:
                            show fmmthreesomebtanp
                    if hair == 1:
                        show fmmthreesomeh black
                    if hair == 2:
                        show fmmthreesomeh blonde
                    if piercingson == 1:
                        show fmmthreesomepiercings
                    show fmmthreesome 1
                    if pregnancyshowing == 1:
                        show fmmthreesomea pregnant
                    with d
                    ""
                    play sound cum
                    show fmmthreesome 2
                    with d
                    ""
                    play sound cum
                    show fmmthreesome 3 with cum
                    ""
                "Back" if True:
                    jump cheatm
            jump cheatbm
        "Boyfriend Route" if True:
            menu cheatbfm:
                "Blowjob" if True:
                    scene bg bed with d
                    show lyingblowjobb
                    if tan == 1:
                        show lyingblowjobb tan
                    if piercingson == 1:
                        show lyingblowjobpiercings
                    if hair == 1:
                        show lyingblowjobh black
                    if hair == 2:
                        show lyingblowjobh blonde
                    show lyingblowjob 1
                    if pregnancyshowing == 1:
                        show lyingblowjobe milk
                    with d
                    ""
                    play sound cum
                    show lyingblowjob 2 with cum
                    ""
                "Vaginal" if True:
                    scene doggystylesexb
                    if pregnancyshowing == 1:
                        show doggystylesexe pregnant
                    if tan == 1:
                        show doggystylesexbtan
                        if pregnancyshowing == 1:
                            show doggystylesexbtanp
                    if hair == 1:
                        show doggystylesexh black
                    if hair == 2:
                        show doggystylesexh blonde
                    if piercingson == 1:
                        show doggystylesexpiercings
                    show doggystylesex 1
                    with d
                    ""
                    play sound cum
                    show doggystylesex 2
                    with d
                    ""
                    play sound cum
                    show doggystylesex 3 with cum
                "Anal" if True:
                    scene doggystylesexb
                    if pregnancyshowing == 1:
                        show doggystylesexe pregnant
                    if tan == 1:
                        show doggystylesexbtan
                        if pregnancyshowing == 1:
                            show doggystylesexbtanp
                    if hair == 1:
                        show doggystylesexh black
                    if hair == 2:
                        show doggystylesexh blonde
                    if piercingson == 1:
                        show doggystylesexpiercings
                    show doggystylesex 1
                    with d
                    ""
                    play sound cum
                    show doggystylesex a2
                    with d
                    ""
                    play sound cum
                    show doggystylesex a3 with cum
                    ""
                "Back" if True:
                    jump cheatm
            jump cheatbfm
        "Massage Parlour Route" if True:
            menu cheatmprm:
                "Bunny Vaginal" if True:
                    show bunnyspreadingassb
                    show bunnyspreadingass 1
                    with d
                    ""
                    play sound cum
                    show bunnyspreadingass 2
                    with d
                    ""
                    play sound cum
                    show bunnyspreadingass 3 with cum
                    ""
                "Bunny Anal" if True:
                    scene bg massage with d
                    show bunnystandingbendingb
                    show bunnystandingbending 1
                    with d
                    ""
                    play sound cum
                    show bunnystandingbending a2
                    with d
                    ""
                    play sound cum
                    show bunnystandingbending a3 with cum
                    ""
                "Blowjob Service" if True:
                    scene bg massage
                    show lyingblowjobb
                    show lyingblowjob 1
                    if pregnancyshowing == 1:
                        show lyingblowjobe milk
                    with d
                    ""
                    play sound cum
                    show lyingblowjob 2 with cum
                    ""
                "Missionary Service" if True:
                    scene missionarysexb
                    if pregnancyshowing == 1:
                        show missionarysexa pregnant1
                    if tan == 1:
                        show missionarysexbtan
                        if pregnancyshowing == 1:
                            show missionarysexbtanp
                    if hair == 1:
                        show missionarysexh black
                    if hair == 2:
                        show missionarysexh blonde
                    if piercingson == 1:
                        show missionarysexpiercings
                    show missionarysex 1
                    with d
                    ""
                    play sound cum
                    show missionarysex 2
                    with d
                    ""
                    play sound cum
                    show missionarysex 3
                    if pregnancyshowing == 1 and tan == 0:
                        show missionarysexa pregnant2
                    with cum
                    ""
                    play sound cum
                    show missionarysex 4 with cum
                    ""
                    play sound cum
                    show missionarysex 5 with d
                    ""
                "Anal Service" if True:
                    scene bg massage
                    show legs-upsexb
                    if tan == 1:
                        show legs-upsexbtan
                    if hair == 1:
                        show legs-upsexh black
                    if hair == 2:
                        show legs-upsexh blonde
                    show legs-upsex 1
                    with d
                    ""
                    play sound cum
                    show legs-upsex a2 with d
                    ""
                    play sound cum
                    show legs-upsex a2
                    with cum
                    ""
                    play sound cum
                    show legs-upsex a3 with cum
                    ""
                    play sound cum
                    show legs-upsex 4 with d
                    ""
                "Back" if True:
                    jump cheatm
            jump cheatmprm
        "Prostitution Route" if True:
            menu cheatpm:
                "Club Blowjob" if True:
                    scene bg toiletstall
                    show blowjob3b
                    if tan == 1:
                        show blowjob3b tan
                    if hair == 1:
                        show blowjob3h black
                    if hair == 2:
                        show blowjob3h blonde
                    if piercingson == 1:
                        show blowjob3piercings
                    show blowjob3 1
                    with d
                    ""
                    play sound cum
                    show blowjob3 2 with cum
                    play sound cum
                    show blowjob3 2 with cum
                    ""
                "Club Vaginal" if True:
                    scene sidewayssexb
                    if pregnancyshowing == 1:
                        show sidewayssexe pregnant
                    if tan == 1:
                        show sidewayssexbtan
                        if pregnancyshowing == 1:
                            show sidewayssexbtanp
                    if hair == 1:
                        show sidewayssexh black
                    if hair == 2:
                        show sidewayssexh blonde
                    if piercingson == 1:
                        show sidewayssexpiercings
                    show sidewayssex 1
                    with d
                    ""
                    play sound cum
                    show sidewayssex v2
                    with d
                    ""
                    play sound cum
                    show sidewayssex v3 with cum
                    ""
                "Club Anal" if True:
                    scene sidewayssexb
                    if pregnancyshowing == 1:
                        show sidewayssexe pregnant
                    if tan == 1:
                        show sidewayssexbtan
                        if pregnancyshowing == 1:
                            show sidewayssexbtanp
                    if hair == 1:
                        show sidewayssexh black
                    if hair == 2:
                        show sidewayssexh blonde
                    if piercingson == 1:
                        show sidewayssexpiercings
                    show sidewayssex 1
                    show sidewayssex 1
                    if pregnancyshowing == 1:
                        show sidewayssexe pregnant
                    with d
                    ""
                    play sound cum
                    show sidewayssex a2 with d
                    ""
                    play sound cum
                    show sidewayssex a3 with cum
                    ""
                "Male Dorms Blowjob" if True:
                    scene bg bedsex
                    show povblowjobb
                    if tan == 1:
                        show povblowjobbtan
                    if piercingson == 1:
                        show povblowjobpiercings
                    if hair == 1:
                        show povblowjobh black
                    if hair == 2:
                        show povblowjobh blonde
                    show povblowjob 1
                    with d
                    ""
                    play sound cum
                    show povblowjob 2 with cum
                    ""
                "Male Dorms Vaginal" if True:
                    scene bg bedsex
                    show sittingsexb
                    if pregnancyshowing == 1:
                        show sittingsexe p1
                    if tan == 1:
                        show sittingsexbtan
                        if pregnancyshowing == 1:
                            show sittingsexbtanp
                    if hair == 1:
                        show sittingsexh black
                    if hair == 2:
                        show sittingsexh blonde
                    if piercingson == 1:
                        show sittingsexpiercings
                    show sittingsex 1
                    with d
                    ""
                    play sound cum
                    show sittingsex v2
                    with d
                    ""
                    play sound cum
                    show sittingsex v3 with cum
                    ""
                    play sound cum
                    show sittingsex 4 with d
                    ""
                "Male Dorms Anal" if True:
                    scene bg bedsex
                    show sittingsexb
                    if pregnancyshowing == 1:
                        show sittingsexe p1
                    if tan == 1:
                        show sittingsexbtan
                        if pregnancyshowing == 1:
                            show sittingsexbtanp
                    if hair == 1:
                        show sittingsexh black
                    if hair == 2:
                        show sittingsexh blonde
                    if piercingson == 1:
                        show sittingsexpiercings
                    show sittingsex 1
                    with d
                    ""
                    play sound cum
                    show sittingsex a2 with d
                    ""
                    play sound cum
                    show sittingsex a3 with cum
                    ""
                    play sound cum
                    show sittingsex 4 with d
                    ""
                "Back" if True:
                    jump cheatm
            jump cheatpm
        "Studio Route" if True:
            menu cheatsm:
                "Nude/Masturbation Shoot" if True:
                    scene bg thecouch
                    show lyingb
                    if pregnancyshowing == 1:
                        show lyinge pregnant
                    if tan == 1:
                        show lyingbtan
                        if pregnancyshowing == 1:
                            show lyingbtanp
                    if hair == 1:
                        show lyingh black
                    if hair == 2:
                        show lyingh blonde
                    if piercingson == 1:
                        show lyingpiercings
                    show lying 1
                    with d
                    ""
                    scene bg black
                    show bg thecouch
                    show masturbation3b
                    if pregnancyshowing == 1:
                        show masturbation3e pregnant
                    if tan == 1:
                        show masturbation3btan
                        if pregnancyshowing == 1:
                            show masturbation3btanp
                    if hair == 1:
                        show masturbation3h black
                    if hair == 2:
                        show masturbation3h blonde
                    if piercingson == 1:
                        show masturbation3piercings
                    with d
                    ""
                    scene bg black
                    show bg thecouch
                    show doggy2b
                    if pregnancyshowing == 1:
                        show doggy2e pregnant
                    if tan == 1:
                        show doggy2tan
                        if pregnancyshowing == 1:
                            show doggy2tanp
                    if hair == 1:
                        show doggy2h black
                    if hair == 2:
                        show doggy2h blonde
                    if piercingson == 1:
                        show doggy2piercings
                    show doggy2 1
                    with d
                    ""
                "Paizuri" if True:
                    scene bg thecouch
                    show paizurib
                    if tan == 1:
                        show paizuribtan
                    if hair == 1:
                        show paizurih black
                    if hair == 2:
                        show paizurih blonde
                    if piercingson == 1:
                        show paizuripiercings
                    show paizuri 1
                    ""
                    show paizuri 2 with d
                    ""
                    play sound cum
                    show paizuri 3 with cum
                    ""
                "Butt-Up Vaginal" if True:
                    scene bg thecouch
                    show buttupb
                    if tan == 1:
                        show buttupb tan
                    if hair == 1:
                        show buttuph black
                    if hair == 2:
                        show buttuph blonde
                    show buttup 1
                    with d
                    ""
                    play sound cum
                    show buttup v2 with d
                    ""
                    play sound cum
                    show buttup v3 with cum
                    ""
                    play sound cum
                    show buttup 4 with d
                "Jacko Sex" if True:
                    scene jackob
                    if tan == 1:
                        show jackobtan
                    if pregnancyshowing == 1:
                        show jackoe pregnant
                        if tan == 1:
                            show jackoe tanpregnant
                    if hair == 1:
                        show jackoh black
                    if hair == 2:
                        show jackoh blonde
                    show jacko 1
                    with d
                    ""
                    play sound cum
                    show jacko 2 with d
                    ""
                    play sound cum
                    show jacko 3 with cum
                    ""
                    play sound cum
                    show jacko 4 with d
                    ""
                "Standing Double Penetration" if True:
                    show standingdpb
                    if tan == 1:
                        show standingdpbtan
                    if pregnancyshowing == 1:
                        show standingdpe pregnant
                        if tan == 1:
                            show standingdpe tanpregnant
                    if hair == 1:
                        show standingdph black
                    if hair == 2:
                        show standingdph blonde
                    if piercingson == 1:
                        show standingdppiercings
                    show standingdp 1
                    ""
                    play sound cum
                    show standingdp 2 with cum
                    ""
                "Back" if True:
                    jump cheatm
            jump cheatsm
        "Swimming Pool Route" if True:
            menu cheatspm:
                "Changing Room Sex" if True:
                    scene bg changingrooms with d
                    play music action
                    show masturbation3b
                    if pregnancyshowing == 1:
                        show masturbation3e pregnant
                    if tan == 1:
                        show masturbation3btan
                        if pregnancyshowing == 1:
                            show masturbation3btanp
                    if hair == 1:
                        show masturbation3h black
                    if hair == 2:
                        show masturbation3h blonde
                    if piercingson == 1:
                        show masturbation3piercings
                    with d
                    ""
                    play sound cum
                    show masturbation3 2 with d
                    ""
                    show masturbation3face 2
                    if tan == 1:
                        show masturbation3face 2tan
                    with d
                    play sound cum
                    show masturbation3 3 with cum
                    ""
                "[tina] Voyeur Doggystyle" if True:
                    show tinavoyeur1b
                    show tinavoyeur1 1
                    with d
                    ""
                    play sound cum
                    show tinavoyeur1 2 with d
                    ""
                    play sound cum
                    show tinavoyeur1 3 with cum
                    ""
                    show tinavoyeur1 4 with d
                    ""
                "[tina] Voyeur Full-Frontal (Vaginal to Anal)" if True:
                    show tinavoyeur2b
                    show tinavoyeur2 1
                    with d
                    ""
                    play sound cum
                    show tinavoyeur2 2
                    with d
                    ""
                    play sound cum
                    show tinavoyeur2 v3
                    with d
                    ""
                    play sound cum
                    show tinavoyeur2 v4 with cum
                    ""
                    show tinavoyeur2 5 with d
                    ""
                    play sound cum
                    show tinavoyeur2 a3 with d
                    ""
                    play sound cum
                    show tinavoyeur2 a4 with cum
                    ""
                    show tinavoyeur2 5 with d
                    ""
                "[tina] Threesome" if True:
                    show tinathreesomeb
                    if tan == 1:
                        show tinathreesomebtan
                    if hair == 1:
                        show tinathreesomeh black
                    if hair == 2:
                        show tinathreesomeh blonde
                    show tinathreesome 1
                    with d
                    ""
                    show tinathreesome 2 with d
                    ""
                    play sound cum
                    show tinathreesome 3 with cum
                    ""
                    play sound cum
                    show tinathreesome 4 with d
                    ""
                "Back" if True:
                    jump cheatm
            jump cheatspm
        "Strip Club Route" if True:
            menu cheatscm:
                "Bunnysuit Paizuri" if True:
                    scene bg booth
                    show paizurib
                    if tan == 1:
                        show paizuribtan
                    if hair == 1:
                        show paizurih black
                    if hair == 2:
                        show paizurih blonde
                    if piercingson == 1:
                        show paizuripiercings
                    show paizurie bunny
                    show paizuri 1
                    with d
                    ""
                    show paizuri 1b with d
                    ""
                    show paizuri 2 with d
                    ""
                    play sound cum
                    show paizuri 3 with cum
                    ""
                "Bunnysuit Doggystyle" if True:
                    scene bg booth
                    show doggy2b
                    if tan == 1:
                        show doggy2tan
                        if pregnancyshowing == 1:
                            show doggy2tanp
                    if hair == 1:
                        show doggy2h black
                    if hair == 2:
                        show doggy2h blonde
                    show doggy2bunny
                    if pregnancyshowing == 1:
                        show doggy2e bunnypregnant
                    if piercingson == 1:
                        show doggy2piercings
                    show doggy2 1
                    with d
                    ""
                    play sound cum
                    show doggy2 2
                    ""
                    play sound cum
                    show doggy2 3 with cum
                    ""
                "Bunnysuit Standing DP" if True:
                    show standingdpb
                    if tan == 1:
                        show standingdpbtan
                    if pregnancyshowing == 1:
                        show standingdpe pregnant
                        if tan == 1:
                            show standingdpe tanpregnant
                    if hair == 1:
                        show standingdph black
                    if hair == 2:
                        show standingdph blonde
                    if piercingson == 1:
                        show standingdppiercings
                    if pregnancyshowing == 1:
                        show standingdpe bunnypregnant
                    elif True:
                        show standingdpe bunny
                    show standingdp 1
                    with d
                    ""
                    play sound cum
                    show standingdp 2 with cum
                    ""
                "Bunnysuit Anal Bukkake Gangbang" if True:
                    show analbukkakeb
                    if tan == 1:
                        show analbukkakebtan
                        if pregnancyshowing == 1:
                            show analbukkakebtanp
                    if piercingson == 1:
                        show analbukkakepiercings
                    if hair == 1:
                        show analbukkakeh black
                    if hair == 2:
                        show analbukkakeh blonde
                    if pregnancyshowing == 0:
                        show analbukkakee bunny
                    elif True:
                        show analbukkakee bunnypregnant
                    show analbukkake 1
                    with d
                    ""
                    play sound cum
                    show analbukkake 2 with d
                    ""
                    show analbukkake 3 with d
                    ""
                    show analbukkake 4 with d
                    ""
                    play sound cum
                    show analbukkake 5 with cum
                    ""
                    play sound cum
                    show analbukkake 6 with cum
                    ""
                    play sound cum
                    show analbukkake 7 with d
                    ""
                "Full Twilight Dance" if True:
                    show twilightdance 1 with d
                    ""
                    show twilightdance 2 with d
                    ""
                    show twilightcunnilingus 1 with d
                    ""
                    show twilightcunnilingus 2 with d
                    ""
                "Back" if True:
                    jump cheatm
            jump cheatscm
        "Lewd Sounds On/Off" if True:
            if xtubesounds == 0:
                $ xtubesounds = 1
                play ambience sex fadein 2.0
                play sound2 foreplay1 fadein 2.0
            elif True:
                $ xtubesounds = 0
                stop ambience
                stop sound2
        "Sex Music On/Off" if True:
            if xtubemusic == 0:
                $ xtubemusic = 1
                play music action
            elif True:
                $ xtubemusic = 0
                stop music
        "Page 2 ->" if True:
            jump cheatm2
        "Back" if True:
            jump cheatsmenu
    jump cheatm
    label cheatm2:
        scene bg bedsex
        menu:
            "Cheats Gallery Page 2"
            "[yoko] Route" if True:
                menu cheatym:
                    "Cunnilingus" if True:
                        scene bg bedsex
                        show yokoroute2b
                        show yokoroute2 1
                        with d
                        ""
                        show yokoroute2 2 with d
                        ""
                    "Sixty-Nine" if True:
                        scene bg bedsex
                        show yoko69b
                        if tan == 1:
                            show yoko69btan
                        if hair == 1:
                            show yoko69h black
                        if hair == 2:
                            show yoko69h blonde
                        show yoko69 1
                        with d
                        ""
                        show yoko69 2
                        with d
                        ""
                    "Futa" if True:
                        scene bg bedsex
                        show yokofutab
                        if tan == 1:
                            show yokofutabtan
                        if hair == 1:
                            show yokofutah black
                        if hair == 2:
                            show yokofutah blonde
                        show yokofuta 1
                        with d
                        ""
                        play sound cum
                        show yokofuta 2 with d
                        ""
                        show yokofuta 3 with d
                        ""
                        play sound cum
                        show yokofuta 4 with cum
                        ""
                        show yokofuta 5 with d
                        ""
                    "Selfcest" if True:
                        scene bg bedsex
                        show yokoselfcestb
                        if tan == 1:
                            show yokoselfcestbtan
                        if pregnancyshowing == 1:
                            show yokoselfcestbp
                            if tan == 1:
                                show yokoselfcestbtanp
                        if hair == 1:
                            show yokoselfcesth black
                        if hair == 2:
                            show yokoselfcesth blonde
                        show yokoselfcest 1
                        with d
                        ""
                        show yokoselfcest 2
                        with d
                        ""
                    "Back" if True:

                        jump cheatm2
                jump cheatym
            "Beach Route" if True:
                menu cheatbrm:
                    "Sunbathing Makeout to Vaginal to Anal" if True:
                        call sunbathingart from _call_sunbathingart_7
                        ""
                        show malemakeout
                        if hair == 1:
                            show malemakeouth black
                        elif hair == 2:
                            show malemakeouth blonde
                        with d
                        ""
                        show malemakeout2 with d
                        ""
                        scene bg black
                        call sunbathingart from _call_sunbathingart_8
                        hide beach1e
                        hide beachtanunderwearp
                        ""
                        play sound cum
                        show beach1 v3 with d
                        ""
                        play sound cum
                        show beach1 v4 with cum
                        ""
                        play sound cum
                        show beach1 5 with d
                        ""
                        show beach1 a3 with d
                        ""
                        play sound cum
                        show beach1 a4 with cum
                        ""
                        play sound cum
                        show beach1 5 with d
                        ""
                    "Beach Bar Vaginal to Anal" if True:
                        scene standingsexb
                        if tan == 1:
                            show standingsexbtan
                            if pregnancyshowing == 1:
                                show standingsexbtanp
                        if hair == 1:
                            show standingsexh black
                        if hair == 2:
                            show standingsexh blonde
                        show standingsexswimsuit
                        if pregnancyshowing == 1:
                            show standingsexe pregnant
                            if tan == 1:
                                show standingsexe pregnanttan
                        show standingsex 1
                        with d
                        ""
                        play sound equip
                        hide standingsexswimsuit with d
                        ""
                        play sound cum
                        show standingsex v2 with d
                        ""
                        show standingsex v3 with d
                        ""
                        play sound cum
                        show standingsex v4 with cum
                        ""
                        show standingsex v5 with cum
                        ""
                        play sound cum
                        show standingsex a2 with d
                        ""
                        show standingsex a3 with d
                        ""
                        play sound cum
                        show standingsex a4 with cum
                        ""
                        play sound cum
                        show standingsex a5 with cum
                        ""
                    "[susu] Makeout" if True:
                        play sound equip
                        scene bg house2
                        show yomomakeout1
                        with d
                        ""
                        show yomomakeout2
                        with d
                        ""
                    "[susu] 69 + Sex Variant" if True:
                        show yuri69b
                        if pregnancyshowing == 1:
                            show yuri69e pregnant
                        if tan == 1:
                            show yuri69btan
                            if pregnancyshowing == 1:
                                show yuri69btanp
                        if hair == 1:
                            show yuri69h black
                        if hair == 2:
                            show yuri69h blonde
                        show yuri69susu
                        with d
                        ""
                        play sound cum
                        show yuri69orgasm with cum
                        ""
                        play sound cum
                        show yuri69 1 with cum
                        ""
                        play sound cum
                        show yuri69 2 with cum
                        ""
                        play sound cum
                        show yuri69 3 with cum
                        ""
                    "[susu] Threesome" if True:
                        scene ffmthreesomeb
                        if tan == 1:
                            show ffmthreesomebtan
                        if hair == 1:
                            show ffmthreesomeh black
                        if hair == 2:
                            show ffmthreesomeh blonde
                        show ffmthreesome 1
                        with d
                        ""
                        play sound cum
                        show ffmthreesome 2 with cum
                        ""
                        play sound cum
                        show ffmthreesome 3 with cum
                        ""
                        show ffmthreesome 4 with d
                        ""
                    "Back" if True:
                        jump cheatm2
                jump cheatbrm
            "Tutor Route" if True:
                menu cheattrm:
                    "Tutor Seduction Blowjob" if True:
                        show povblowjobb
                        if tan == 1:
                            show povblowjobbtan
                        if piercingson == 1:
                            show povblowjobpiercings
                        if hair == 1:
                            show povblowjobh black
                        if hair == 2:
                            show povblowjobh blonde
                        show povblowjob 1
                        with d
                        ""
                        play sound cum
                        show povblowjob 2 with cum
                        ""
                    "[yomo] Makeout" if True:
                        play sound equip
                        scene bg house1
                        show yomomakeout1
                        with d
                        ""
                        show yomomakeout2
                        with d
                        ""
                    "[yomo] 69" if True:
                        show yuri69b
                        if pregnancyshowing == 1:
                            show yuri69e pregnant
                        if tan == 1:
                            show yuri69btan
                            if pregnancyshowing == 1:
                                show yuri69btanp
                        if hair == 1:
                            show yuri69h black
                        if hair == 2:
                            show yuri69h blonde
                        show yuri69yomo
                        with d
                        ""
                        play sound cum
                        show yuri69orgasm with cum
                        ""
                    "[yomo] Fingering" if True:
                        scene yomofingeringb
                        if pregnancyshowing == 1:
                            show yomofingeringe pregnant
                        if tan == 1:
                            show yomofingeringbtan
                            if pregnancyshowing == 1:
                                show yomofingeringbtanp
                        if hair == 1:
                            show yomofingeringh black
                        if hair == 2:
                            show yomofingeringh blonde
                        if piercingson == 1:
                            show yomofingeringpiercings
                        show yomofingering 1
                        with d
                        ""
                        show yomofingering 2
                        with d
                        ""
                        show yomofingering 3
                        with d
                        ""
                    "Back" if True:
                        jump cheatm2
                jump cheattrm
            "Exhibitionist Route" if True:
                menu cheaterm:
                    "Public Sex" if True:
                        scene bg sky
                        show chikanb
                        if tan == 1:
                            show chikanbtan
                        if hair == 1:
                            show chikanh black
                        if hair == 2:
                            show chikanh blonde
                        show chikan park1
                        with d
                        ""
                        play sound fondle
                        show chikan park2
                        with d
                        ""
                        play sound spank
                        show chikan park3 with cum
                        ""
                        play sound cum
                        show chikan park4 with d
                        ""
                        play sound cum
                        show chikan park5 with cum
                        ""
                        play sound cum
                        show chikan park6 with d
                        ""
                    "Public Gangbang" if True:
                        scene parkgangbangb
                        if tan == 1:
                            show parkgangbangbtan
                        if pregnancyshowing == 1:
                            show parkgangbangbp
                            if tan == 1:
                                show parkgangbangbtanp
                        if piercingson == 1:
                            show parkgangbangbpiercings
                        if hair == 1:
                            show parkgangbangh black
                        if hair == 2:
                            show parkgangbangh blonde
                        with d
                        ""
                        play sound cum
                        show parkgangbang 1 with d
                        ""
                        play sound cum
                        show parkgangbang 2 with cum
                        ""
                        play sound cum
                        show parkgangbang 3 with d
                        ""
                    "Back" if True:
                        jump cheatm2
                jump cheaterm
            "Dungeon Route" if True:
                menu cheatmdu:
                    "Shibari (Strap-On, then Penis)" if True:
                        scene shibarib
                        if tan == 1:
                            show shibaribtan
                        if hair == 1:
                            show shibarih black
                        if hair == 2:
                            show shibarih blonde
                        if piercingson == 1:
                            show shibaribpiercings
                        show shibari 1
                        with d
                        ""
                        show shibari 2 with d
                        ""
                        play sound equip
                        show shibari 4 with d
                        ""
                        show shibari 5s with d
                        ""
                        show shibari 6s with d
                        ""
                        show shibari 7 with d
                        ""
                        show shibari 5 with d
                        ""
                        show shibari 6 with d
                        ""
                        show shibari 7 with d
                        ""
                    "Suspended (Pick and Choose)" if True:
                        scene bg black with d
                        show suspendedb
                        if tan == 1:
                            show suspendedbtan
                        if hair == 1:
                            show suspendedh black
                        if hair == 2:
                            show suspendedh blonde
                        if piercingson == 1:
                            show suspendedpiercings
                        show suspended 1
                        with d
                        ""
                        $ dungeonpunishments = 0
                        $ dblindfold = 0
                        $ dgag = 0
                        $ dspanking = 0
                        $ dwhipping = 0
                        menu dungeonpcheat:
                            "Pick Punishments"
                            "Blindfold" if dblindfold == 0:
                                play sound equip
                                show suspendedblindfold with d
                                $ dblindfold = 1
                                $ dungeonpunishments += 1
                                jump dungeonpcheat
                            "Gag" if dgag == 0:
                                play sound equip
                                show suspendedgag
                                if tan == 1:
                                    show suspendedgag tan
                                with d
                                $ dgag = 1
                                $ dungeonpunishments += 1
                                jump dungeonpcheat
                            "Spanking" if dspanking == 0:
                                play sound spank
                                show suspendedspanked with d
                                $ dspanking = 1
                                $ dungeonpunishments += 1
                                jump dungeonpcheat
                            "Whipping" if dspanking == 1 and dwhipping == 0:
                                play sound whip
                                show suspendedspanked 2 with d
                                $ dwhipping = 1
                                $ dungeonpunishments += 1
                                jump dungeonpcheat
                            "Done Picking" if True:
                                pass
                        ""
                        menu dungeonp2cheat:
                            "Pick Penetration"
                            "Oral" if True:
                                hide suspendedgag
                                show suspended 2
                                play sound cum
                                show suspendedoral
                                if tan == 1:
                                    show suspendedoral tan
                                ""
                                play sound cum
                                show suspendedoral 2
                                if tan == 1:
                                    show suspendedoral 2tan
                                with cum
                                ""
                                show suspendedoral 3 with d
                                ""
                            "Vaginal" if True:
                                show suspended 2
                                play sound cum
                                show suspendedvaginal with d
                                ""
                                play sound cum
                                show suspendedvaginal 2 with cum
                                ""
                                show suspendedvaginal 3 with d
                                ""
                            "Spitroast!" if True:
                                hide suspendedgag
                                show suspended 2
                                play sound cum
                                show suspendedoral
                                if tan == 1:
                                    show suspendedoral tan
                                show suspendedvaginal
                                with d
                                ""
                                play sound cum
                                show suspendedoral 2
                                if tan == 1:
                                    show suspendedoral 2tan
                                show suspendedvaginal 2
                                with cum
                                ""
                                show suspendedoral 3
                                show suspendedvaginal 3
                                with d
                                ""
                    "Back" if True:
                        jump cgm2
                jump cheatmdu
            "Random Events" if True:
                menu cheatrem:
                    "Public Flashing" if True:
                        scene bg street
                        "I remove my blazer, and then..."
                        show flashing
                        if pregnancyshowing == 1:
                            show flashing p
                        if tan == 1:
                            show flashingtan
                            if pregnancyshowing == 1:
                                show flashingtanp
                        if piercingson == 1:
                            show flashingpiercings
                        if hair == 1:
                            show flashingh black
                        if hair == 2:
                            show flashingh blonde
                        with d
                        ""
                    "Double Penetration" if True:
                        scene fmmthreesomeb
                        if pregnancyshowing == 1:
                            show fmmthreesomea pregnant
                        if tan == 1:
                            show fmmthreesomebtan
                            if pregnancyshowing == 1:
                                show fmmthreesomebtanp
                        if hair == 1:
                            show fmmthreesomeh black
                        if hair == 2:
                            show fmmthreesomeh blonde
                        if piercingson == 1:
                            show fmmthreesomepiercings
                        show fmmthreesome 1
                        with d
                        ""
                        play sound cum
                        show fmmthreesome 2
                        with d
                        ""
                        play sound cum
                        show fmmthreesome 3 with cum
                        ""
                    "Bus Chikan" if True:
                        scene bg bus with d
                        show student1:
                            xpos 950
                        call clothesformal from _call_clothesformal_30
                        show mce neutral
                        with d
                        ""
                        scene chikanbus
                        show chikanb
                        if tan == 1:
                            show chikanbtan
                        if hair == 1:
                            show chikanh black
                        if hair == 2:
                            show chikanh blonde
                        show chikan 1
                        with d
                        ""
                        show chikan 2
                        with d
                        ""
                        play sound rip
                        show chikan 3 with d
                        ""
                        play sound cum
                        show chikan 4 with d
                        ""
                        play sound cum
                        show chikan 5 with cum
                        ""
                        play sound cum
                        show chikan 6 with d
                        ""
                    "Club Bathroom Blowjob" if True:
                        show bg toiletstall with d
                        show povblowjobb
                        if tan == 1:
                            show povblowjobbtan
                        if piercingson == 1:
                            show povblowjobpiercings
                        if hair == 1:
                            show povblowjobh black
                        if hair == 2:
                            show povblowjobh blonde
                        show povblowjob 1
                        with d
                        ""
                        play sound cum
                        show povblowjob 2 with cum
                        ""
                    "[susu] Threesome" if True:
                        scene bg bed
                        show ffmthreesomeb
                        if tan == 1:
                            show ffmthreesomebtan
                        if hair == 1:
                            show ffmthreesomeh black
                        if hair == 2:
                            show ffmthreesomeh blonde
                        show ffmthreesome 1
                        with d
                        ""
                        play sound cum
                        show ffmthreesome 2
                        with d
                        ""
                        play sound cum
                        show ffmthreesome 3 with cum
                        ""
                    "Classroom Blackmail Blowjob" if True:
                        scene classroombjb
                        if tan == 1:
                            show classroombjbtan
                        if hair == 1:
                            show classroombjh black
                        if hair == 2:
                            show classroombjh blonde
                        if piercingson == 1:
                            show classroombjpiercings
                        show classroombj 1
                        with d
                        ""
                        show classroombj 2 with d
                        ""
                        play sound cum
                        show classroombj 3 with cum
                        ""
                    "Classroom Blackmail Sex" if True:
                        scene classroomsexb
                        if tan == 1:
                            show classroomsexbtan
                        if pregnancyshowing == 1:
                            show classroomsexbp
                            if tan == 1:
                                show classroomsexbtanp
                        if hair == 1:
                            show classroomsexh black
                        if hair == 2:
                            show classroomsexh blonde
                        if piercingson == 1:
                            show classroomsexpiercings
                        show classroomsex 1
                        show classroomsexo uniform1
                        with d
                        ""
                        show classroomsex 1b with d
                        ""
                        play sound equip
                        show classroomsexo uniform2 with d
                        ""
                        show classroomsex 1b with d
                        ""
                        show classroomsex 2 with d
                        ""
                        play sound cum
                        show classroomsex 3 with cum
                        ""
                        play sound cum
                        show classroomsex 4 with d
                        ""
                    "Onsen Double Handjob" if True:
                        scene onsenbjb
                        if tan == 1:
                            show onsenbjbtan
                        if pregnancyshowing == 1:
                            show onsenbjbp
                            if tan == 1:
                                show onsenbjbtanp
                        if hair == 1:
                            show onsenbjh black
                        if hair == 2:
                            show onsenbjh blonde
                        if piercingson == 1:
                            show onsenbjpiercings
                        show onsenbj 1
                        with d
                        ""
                        play sound cum
                        show onsenbj 2 with cum
                        ""
                    "Onsen Sex (Vaginal, then Anal)" if True:
                        scene onsensexb
                        if tan == 1:
                            show onsensexbtan
                        if pregnancyshowing == 1:
                            show onsensexbp
                            if tan == 1:
                                show onsensexbtanp
                        if hair == 1:
                            show onsensexh black
                        if hair == 2:
                            show onsensexh blonde
                        show onsensex 1b
                        with d
                        ""
                        show onsensex v2 with d
                        ""
                        show onsensex v3 with cum
                        ""
                        show onsensex 4 with d
                        ""
                        show onsensex a2 with d
                        ""
                        show onsensex a3 with cum
                        ""
                        show onsensex 4 with d
                        ""
                    "Tentacles Standing" if True:
                        play sound whip
                        scene tentaclesstandingsexb
                        if tan == 1:
                            show tentaclesstandingsexbtan
                        if pregnancyshowing == 1:
                            show tentaclesstandingsex1p
                            show tentaclesstandingsexbp
                            if tan == 1:
                                show tentaclesstandingsexbtanp
                        if hair == 1:
                            show tentaclesstandingsexh black
                        if hair == 2:
                            show tentaclesstandingsexh blonde
                        if piercingson == 1:
                            show tentaclesstandingsexpiercings
                        show tentaclesstandingsex 1
                        show tentaclesstandingsex1clip
                        show mrslime:
                            xpos 50 ypos 100
                        with hpunch
                        ""
                        hide tentaclesstandingsex1clip
                        show tentaclesstandingsex 2
                        ""
                        play sound cum
                        show tentaclesstandingsex 3
                        ""
                        play sound cum
                        show tentaclesstandingsex 4 with cum
                        ""
                        play sound cum
                        show tentaclesstandingsex 5 with d
                        ""
                        play sound equip
                        show tentaclesstandingsex 6
                        show tentaclesstandingsex1p
                        with d
                        ""
                    "Tentacles Double Penetration" if True:
                        scene tentaclesdpsexb
                        if tan == 1:
                            show tentaclesdpsexbtan
                        if pregnancyshowing == 1:
                            show tentaclesdpsexbp
                            if tan == 1:
                                show tentaclesdpsexbtanp
                        if hair == 1:
                            show tentaclesdpsexh black
                        if hair == 2:
                            show tentaclesdpsexh blonde
                        if piercingson == 1:
                            show tentaclesdpsexpiercings
                        show tentaclesdpsex 1
                        with d
                        ""
                        play sound cum
                        show tentaclesdpsex 2 with d
                        ""
                        play sound cum
                        show tentaclesdpsexmilking 1
                        show tentaclesdpsex 2b
                        with d
                        ""
                        play sound cum
                        show tentaclesdpsex 2
                        show tentaclesdpsexmilking 2
                        with cum
                        ""
                        play sound cum
                        show tentaclesdpsex 3 with cum
                        ""
                        play sound cum
                        hide tentaclesdpsexmilking
                        show tentaclesdpsex 4
                        show tentaclesdpsexmilk
                        with d
                        ""
                    "Back" if True:
                        jump cheatm2
                jump cheatrem
            "Endings" if True:
                menu cheatsmending:
                    "Loyal Girlfriend Ending" if lge == 1:
                        scene loyalgfendb
                        if tan == 1:
                            show loyalgfendbtan
                        if hair == 1:
                            show loyalgfendh black
                        if hair == 2:
                            show loyalgfendh blonde
                        if piercingson == 1:
                            show loyalgfendpiercings
                        show loyalgfend 1
                        with d
                        ""
                        show loyalgfend 2
                        with d
                        ""
                        show loyalgfend 3
                        with d
                        ""
                        show loyalgfend 4
                        with d
                        ""
                    "Cheating Girlfriend Ending" if lge == 1:
                        show ntrendb
                        if tan == 1:
                            show ntrendbtan
                        if hair == 1:
                            show ntrendh black
                        if hair == 2:
                            show ntrendh blonde
                        if piercingson == 1:
                            show ntrendpiercings
                        show ntrend 1
                        with d
                        ""
                        show ntrend 2
                        with d
                        ""
                        show ntrend 3
                        with d
                        ""
                        show ntrend 4
                        with d
                        ""
                    "[yomo]'s Girlfriend Ending" if yge == 1:
                        show yomoendingb
                        if pregnancyshowing == 1:
                            show yomoendingbp
                        if tan == 1:
                            show yomoendingbtan
                            if pregnancyshowing == 1:
                                show yomoendingbtanp
                        if hair == 1:
                            show yomoendingh black
                        if hair == 2:
                            show yomoendingh blonde
                        if piercingson == 1:
                            show yomoendingpiercings
                        show yomoending 1
                        with d
                        ""
                        show yomoending 2
                        with d
                        ""
                        show yomoending 3
                        with d
                        ""
                    "Dominatrix Ending" if de == 1:
                        menu:
                            "Choose a Sex Partner"
                            "Female" if True:
                                show dominatrixendb
                                if tan == 1:
                                    show dominatrixendbtan
                                if hair == 1:
                                    show dominatrixendh black
                                if hair == 2:
                                    show dominatrixendh blonde
                                if piercingson == 1:
                                    show dominatrixendpiercings
                                show dominatrixendcollar
                                show dominatrixenddom 1
                                show dominatrixend f1
                                with d
                                ""
                                show dominatrixenddom 2 with d
                                ""
                                show dominatrixend f2 with d
                                ""
                                show dominatrixend f3 with d
                                ""
                            "Male" if True:
                                show dominatrixendb
                                if tan == 1:
                                    show dominatrixendbtan
                                if hair == 1:
                                    show dominatrixendh black
                                if hair == 2:
                                    show dominatrixendh blonde
                                if piercingson == 1:
                                    show dominatrixendpiercings
                                show dominatrixendcollar
                                show dominatrixenddom 1
                                show dominatrixend 1
                                with d
                                ""
                                show dominatrixenddom 2
                                with d
                                ""
                                play sound cum
                                show dominatrixend v2 with d
                                ""
                                play sound cum
                                show dominatrixend v3 with cum
                                ""
                    "Yandere Ending" if yye == 1:
                        scene bg bedsex
                        show yokoselfcestb
                        if tan == 1:
                            show yokoselfcestbtan
                        if pregnancyshowing == 1:
                            show yokoselfcestbp
                            if tan == 1:
                                show yokoselfcestbtanp
                        if hair == 1:
                            show yokoselfcesth black
                        if hair == 2:
                            show yokoselfcesth blonde
                        show yokoselfcest alt1
                        with d
                        ""
                        play sound cum
                        show yokoselfcest alt2 with cum
                        ""
                        play sound cum
                        show yokoselfcest alt3 with d
                        ""
                    "E-Girl Empress Ending" if ege == 1:
                        scene bg bedsex
                        show camoutfitsb
                        show camoutfitse catgirl
                        show camoutfitsh pink
                        show camoutfits 1
                        show chatfapborder
                        with d
                        ""
                        show egirlempressendb
                        show egirlempressend 1
                        with d
                        ""
                        show egirlempressend 2
                        with d
                        ""
                        show egirlempressend 3
                        with d
                        ""
                        show egirlempressend 4
                        with d
                        ""
                        show egirlempressend 5
                        with d
                        ""
                        show egirlempressend 6
                        with d
                        ""
                        show egirlempressend 7
                        with d
                        ""
                        show egirlempressend 8
                        with d
                        ""
                    "Professional Masseuse" if mpe == 1:
                        scene bg massage
                        show massageparlourthreesomeb
                        if tan == 1:
                            show massageparlourthreesomebtan
                        if hair == 1:
                            show massageparlourthreesomeh black
                        if hair == 2:
                            show massageparlourthreesomeh blonde
                        show massageparlourthreesome 1
                        with d
                        ""
                        show massageparlourthreesome 2 with d
                        ""
                        show massageparlourthreesome 3 with d
                        ""
                        show massageparlourthreesome 4 with d
                        ""
                    "Drug Addict Ending" if dae == 1:
                        scene addictendb
                        show addictend 1
                        with d
                        ""
                        show addictend 2
                        with d
                        ""
                        show addictend 3
                        with d
                        ""
                        show addictend 4
                        with d
                        ""
                    "Sex Addict Ending" if sae == 1:
                        show sexaddictendingb
                        if tan == 1:
                            show sexaddictendingbtan
                        if hair == 1:
                            show sexaddictendingh black
                        if hair == 2:
                            show sexaddictendingh blonde
                        if piercingson == 1:
                            show sexaddictendingpiercings
                        show sexaddictending 1
                        with d
                        ""
                        play sound cum
                        show sexaddictending 2 with cum
                        ""
                    "Prostitute Ending" if pe == 1:
                        scene prostituteendb
                        if tan == 1:
                            show prostituteendbtan
                        if hair == 1:
                            show prostituteendh black
                        if hair == 2:
                            show prostituteendh blonde
                        if piercingson == 1:
                            show prostituteendpiercings
                        show prostituteend 1
                        show prostituteendjar 1
                        with d
                        ""
                        scene holeb
                        show holetina
                        with d
                        ""
                        play sound cum
                        show hole cum with cum
                        ""
                        play sound2 foreplay1
                        play ambience sex
                        scene prostituteendb
                        if tan == 1:
                            show prostituteendbtan
                        if hair == 1:
                            show prostituteendh black
                        if hair == 2:
                            show prostituteendh blonde
                        if piercingson == 1:
                            show prostituteendpiercings
                        show prostituteendjar 2
                        show prostituteend 2
                        if tan == 1:
                            show prostituteendclip 1
                        show prostituteendborder
                        with d
                        ""
                        play sound cum
                        if tan == 1:
                            show prostituteendclip 2
                        show prostituteend 3 with cum
                        ""
                        play sound cum
                        if tan == 1:
                            show prostituteendclip 3
                        show prostituteend 4 with d
                        ""
                    "Slime Girl" if sge == 1:
                        show tinathreesomeb
                        if tan == 1:
                            show tinathreesomebtan
                        if hair == 1:
                            show tinathreesomeh black
                        if hair == 2:
                            show tinathreesomeh blonde
                        show tinathreesomeslime
                        show tinathreesome 1
                        show tinathreesomepinkeyes
                        with d
                        ""
                        hide tinathreesomepinkeyes
                        show tinathreesome 2b
                        with d
                        ""
                        play sound cum
                        show tinathreesome 3b with cum
                        ""
                        play sound cum
                        show tinathreesome 4
                        show tinathreesomepinkeyes
                        with d
                        ""
                    "Back" if True:
                        jump cheatm2
                jump cheatsmending
            "Lewd Sounds On/Off" if True:
                if xtubesounds == 0:
                    $ xtubesounds = 1
                    play ambience sex fadein 2.0
                    play sound2 foreplay1 fadein 2.0
                elif True:
                    $ xtubesounds = 0
                    stop ambience
                    stop sound2
            "Sex Music On/Off" if True:
                if xtubemusic == 0:
                    $ xtubemusic = 1
                    play music action
                elif True:
                    $ xtubemusic = 0
                    stop music
            "<- Page 1" if True:
                jump cheatm
            "Back" if True:
                jump cheatsmenu
    jump cheatm2

init:
    $ xtubesounds = 0
    $ xtubemusic = 0
    $ xtube1 = 0
    $ xtube2 = 0
    $ xtube3 = 0
    $ xtube4 = 0
    $ xtube5 = 0
    $ xtube6 = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
