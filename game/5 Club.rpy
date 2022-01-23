label club:
    if clubunlocked == 0:
        "Unlock this location by getting a friend to invite you."
        jump postworldmap
    if morning == 1:
        "Ahh, the club isn't open yet."
        jump postworldmap
    elif True:
        pass
    play music club
    scene bg club with d
    call clothes from _call_clothes_36
    show mce happy
    with d
    "Bright lights, people dancing everywhere, and here's me all on my own."
    menu cm:
        "Sexual Desire: [sd], Shame: [shame]."
        "Buy some Alcohol" if drunk < 3:
            if pregnancyshowing == 1:
                "I really shouldn't drink while pregnant."
                jump cm
            menu clubbarmenu:
                "Money: [money]. Intoxication Level: [drunk]/4. The effects of alcohol last until morning. Your character won't drink past her limits without peer pressure."
                "Spirit ($10) (+10 Sexual Desire, -10 Shame) (+2 Intoxication)" if drunk <2:
                    if money < 10:
                        "I can't afford it."
                        jump clubbarmenu
                    play sound success
                    if qlightweight:
                        $ sd += 10
                        $ shame -= 10
                        "As a lightweight, you feel twice the effects from the alcohol."
                    $ sd += 10
                    $ shame -= 10
                    $ money -= 10
                    $ drunk += 2
                    "The bartender serves my order and I don't waste any time trying to swallow it's bitter taste down."
                "Cocktail ($5) (+5 Sexual Desire, -5 Shame) (+1 Intoxication)" if True:
                    if money < 5:
                        "I can't afford it."
                        jump clubbarmenu
                    play sound success
                    if qlightweight:
                        $ sd += 5
                        $ shame -= 5
                        "As a lightweight, you feel twice the effects from the alcohol."
                    $ sd += 5
                    $ shame -= 5
                    $ money -= 5
                    $ drunk += 1
                    "The bartender serves my order and I take my time savouring the sweet taste."
                "Back" if True:
                    jump cm
            if drunk == 1:
                "Ahh! A light buzz!"
            elif drunk == 2:
                "Phew... I'm really feeling it."
            elif drunk == 3:
                "Mmm... I'm quite drunk now..."
            jump cm
        "You're too drunk to buy any more alcohol" if drunk > 3:
            jump cm
        "Approach someone (50 Sexual Desire, <50 Shame)" if True:
            if sd < 50 or shame > 50:
                "Approach? I think I'm too nervous for that, maybe a little liquid courage would help."
                jump cm
            jump pickingup
        "Wait for someone to approach (20 Sexual Desire, <80 Shame)" if yokoroute2 == 0:
            if sd < 20 or shame > 80:
                "Wait for someone? I think I'm too nervous for that, maybe a little liquid courage would help."
                jump cm
            jump yokoroute
        "Meet up with [yoko]." if yokoroute2 == 1:
            jump yokoroute
        "Pickpocket Someone (<80 Shame)" if personality == 3 and clubpp == 0:
            if shame > 80:
                "Mmm, probably best if I don't."
                jump cm
            $ clubpp = 1
            $ rand = renpy.random.randint(1,10)
            if rand > 5:
                "I wait for someone to pass, and manage to snatch some money from someone's pocket as they walk past. Completely undetected."
                play sound success
                $ shameloss = 1
                $ moneygain = 20
                call shameloss from _call_shameloss_71
                call moneygain from _call_moneygain_58
                "(+$[fmoney], -[fshame] Shame!)"
            elif True:
                "I wait for someone to pass, but I fail to snatch anything, and end up having to move away and lay low. Woops..."
                play sound success2
                $ shameloss = 1
                call shameloss from _call_shameloss_72
                "(-[fshame] Shame!)"
            jump cm
        "Leave" if True:
            jump worldmap

jump worldmap

label pickingup:
    "There are quite a lot of men around, I think it'd be quite easy to get someone's attention."
    if yokoroute2 == 1 and yokoroute2ee == 0:
        $ yokoroute2ee = 1
        "Just as a cute guy sits next to me, and I'm about to hit him up for a conversation - "
        play music toko
        show yokob:
            xpos 1200
        show yokoo clothes:
            xpos 1200
        show yokoe laughing:
            xpos 1200
        with d
        yoko "Oh my gosh, hiii!"
        jump yokoroute4
    menu:
        "Take a man home" if True:
            "Okay, so I'll bring a man home, but what am I going to do with him?"
            menu:
                "Blowjob" if True:
                    $ clubbj = 1
                    stop music
                    scene bg black with d
                    "I find a target and soon bring him home..."
                    play music action
                    play sound equip
                    scene bg bedroomnight with d
                    call clothesnude from _call_clothesnude_34
                    show mce laughing
                    with d
                    mc "Just seat on the bed, and I'll blow your mind..."
                    "Shamelessly, I kneel down before my new lover as he takes out his half-erection."
                    scene bg bedsex
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
                    play ambience oral1 fadein 3.0
                    "Taking his cock in my hand, I guide it to my mouth and passionately take it deeper."
                    "Mmpphh, there's just something so primal and sexy about doing something naughty with a guy you just met."
                    "I begin by bringing my mouth level to its tip and accepting it into my mouth, swirling my tongue around the edge of the glans for a high pleasure start."
                    "Meanwhile my hands begin to naturally caress the cock, my left jacking it off while my right delicately massages the balls."
                    "I move slowly, drawing out the process as I try to tease him as much as possible. My goal is to coax as much cum out of him in one orgasm as possible."
                    mc "Mmphh, mmm... *Lick, slurp*"
                    "Occasionally flicking my tongue across the sensitive tip of the erection, I focus on where he reacts the most favourably."
                    "When his cock throbs in response to my movements, I know I'm doing something right."
                    "My thighs brush together, and I shiver with desire. I'm getting so aroused by this."
                    "I can't help but get more passionate, my handjob speeds up as the desire to have my mouth filled up with hot cum grows."
                    "I purse my lips around the glans and guide it back and forth in a fucking motion, sucking and licking with each movement."
                    "These motions are most similar to vaginal sex, this should make him cum in no time. And the tense throbbing in his cock confirms my thoughts."
                    "Using the last of my stamina I go all out to bring my partner to climax. I fuck his cock with my mouth deeply, while jacking him off intensely."
                    play sound cum
                    show blowjob3 2 with cum
                    play sound cum
                    show blowjob3 2 with cum
                    "Mmphh, yesss! His cock unloads several hot jets of cum straight into the back of my mouth."
                    play sound cum
                    show blowjob3 2 with cum
                    play sound cum
                    show blowjob3 2 with cum
                    "Load after load, I struggle to swallow it all. Some of it seeps outwards, dripping on my chin and face."
                    stop ambience
                    "I finish up the job, and he withdraws his rapidly shrinking cock."
                    $ blowjobs += 1
                    $ sdgain = 1
                    $ shameloss = 1
                    call sdgain from _call_sdgain_107
                    call shameloss from _call_shameloss_73
                    play sound success
                    "(+[fsd] Sexual Desire, -[fshame] Shame.)"
                    scene bg bedroomnight with d
                    call clothesnude from _call_clothesnude_35
                    show mce horny
                    with d
                    mc "It's definitely your turn to go down on me now."
                    scene bg black with d
                    "After an unknown amount of time, my partner leaves, returning to the male dorms."
                    jump postworktrans
                "Vaginal (60 Sexual Desire)" if True:
                    if sd < 60:
                        "I don't think I'm quite ready to sleep with a stranger yet."
                        jump pickingup
                    $ clubsex = 1
                    stop music
                    scene bg black with d
                    "I find a target and soon bring him home..."
                    play music action
                    play sound equip
                    scene bg bedroomnight with d
                    call clothesnude from _call_clothesnude_36
                    show mce laughing
                    with d
                    mc "Mmphh, I can't wait for you to ravage my pussy..."
                    label clubvaginalsex:
                        pass
                    show sidewayssexb
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
                    "Shamelessly, I lay down on my side and spread my legs before my new partner as he takes out his half-erection."
                    $ condomon = 0
                    if condoms > 0 and pregnancyshowing == 0:
                        menu:
                            "Use a condom? Condoms: [condoms]. [fertilityrate]."
                            "Yeah." if True:
                                $ condomon = 1
                                $ condoms -= 1
                            "Fuck the rules! (Without protection!)" if True:
                                $ condomon = 0
                    "I beckon for him to take me. My lustful pussy is on full display, sheening slightly from a wetness."
                    "As he pushes the tip inside me, he pushes forward and slides deeper into my soaking wet insides."
                    play sound cum
                    show sidewayssex v2
                    with d
                    if virgin == 0:
                        "And just like that, the stranger I brought home takes my virginity."
                        $ virgin = 1
                    mc "Ahhh, you're quite big! Go steady at first."
                    play ambience sex fadein 3.0
                    "He begins thrusting back and forth, slowly sliding his cock almost all the way out before sinking back in."
                    "Although I'm so aroused, he's able to speed up a lot, and it doesn't take long until he's pounding me deeply, shaking my entire body against the bed."
                    "These deep thrusts drive me wild as they grind against sensitive erogenous zones deep inside of me."
                    "The pleasure slowly builds over the course of a minute before it starts to really overwhelm me."
                    "And just to start making me feel even better, he starts to thrust faster while reaching down to rub my clit."
                    "My mind turns blank as my body trembles towards a potent orgasm."
                    mc "Ahhh, it's so good! I-I'm gonna, aahhh... Ahhhh!"
                    play sound cum
                    show sidewayssex v2
                    "I tightly grip the bedsheets as I climax, my pussy tightening around my partner's throbbing cock."
                    "And he only speeds up, motivated by my climax, he pushes towards his own."
                    play sound cum
                    show sidewayssex v3 with cum
                    play sound cum
                    show sidewayssex v3 with cum
                    "His tight cock explodes a hot load deep into my pussy as he ravishes me"
                    play sound cum
                    show sidewayssex v3 with cum
                    play sound cum
                    show sidewayssex v3 with cum
                    "I roll my hips back and forth needily as we both fuck in rhythm together, indulging the last moments of our euphoric orgasms."
                    play sound cum
                    show sidewayssex 4 with d
                    stop ambience fadeout 3.0
                    "Ahhh... As he pulls out, several droplets of cum seep out my well-fucked pussy and drip down my pelvis and thighs."
                    if condomon == 1 and pregnancyshowing == 0:
                        "But thanks to the condom, I don't need to worry about getting pregnant."
                    elif True:
                        call pregnancyroll from _call_pregnancyroll_11
                    scene bg bedroomnight with d
                    call clothesnude from _call_clothesnude_37
                    show mce horny
                    with d
                    mc "Haah, let's cuddle for five minutes, then go again?"
                    scene bg black with d
                    $ sdgain = 1
                    call sdgain from _call_sdgain_108
                    $ shameloss = 1
                    call shameloss from _call_shameloss_74
                    "(+[fsd] Sexual Desire, -[fshame] Shame)"
                    $ status += 1
                    $ vaginalsexes += 1
                    "After an unknown amount of time, my partner leaves, returning to the male dorms."
                    jump postworktrans
                "Anal (70 Sexual Desire)" if qanalqueen == 0:
                    if sd < 70:
                        "I don't think I'm quite ready to do that with a stranger yet."
                        jump pickingup
                    label clubanal:
                        pass
                    $ clubsex = 1
                    stop music
                    scene bg black with d
                    "I find a target and soon bring him home..."
                    play music action
                    play sound equip
                    scene bg bedroomnight with d
                    call clothesnude from _call_clothesnude_38
                    show mce laughing
                    with d
                    mc "I have some lube in my bedside draw, think you can apply it for me?"
                    show sidewayssexb
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
                    "I get into position with confidence, lifting my leg to expose both my dripping wet pussy and my tight ass."
                    "As my partner watches, he strokes his cock to erection. He takes some lube and gently applies it to my pucker."
                    mc "Mmphh, I'm ready for that fat cock now... Hehe."
                    "With my butt held high, I teasingly wiggle it while and spreading my cheeks."
                    play sound cum
                    play ambience sex fadein 2.0
                    show sidewayssex a2 with d
                    "He taps the tip of his cock against my anus a few times before lining it up properly and pushing in deep."
                    "It takes a while for my ass to adjust, but the lubrication and some relaxation enable me to take it with ease."
                    "Not only that, but it starts to feel good!"
                    "Once I'm ready, he begins slowly sliding his cock almost all the way out before sinking back in."
                    mc "Ohhh, yeaahh... Ahhh, you're really filling me up!"
                    "He starts to thrust faster while reaching down and rubbing my clit with his thumb."
                    mc "Aahhh, mmmpphhmmm... That's really good, yeah!"
                    "I love the way it grinds against all the sensitive spots deep inside. And in this position, it feels tighter and totally amazing for me."
                    "And all these combined sensations are enough to bring about my orgasm rather quickly, causing my entire body to tremble."
                    mc "Ahhh, it's so good! I-I'm gonna, aahhh... Ahhhh!"
                    play sound cum
                    show sidewayssex a2
                    with cum
                    "As my pussy contracts, my ass clenches too, squeezing around my partner's tense cock as I climax."
                    "And as my ass squeezees and milks his cock, he only speeds up. Motivated by my climax, he pushes towards his own."
                    play sound cum
                    show sidewayssex a3 with cum
                    play sound cum
                    show sidewayssex a3 with cum
                    "His tight cock explodes a hot load deep into my ass as he ravishes me"
                    play sound cum
                    show sidewayssex a3 with cum
                    play sound cum
                    show sidewayssex a3 with cum
                    "I roll my hips back and forth needily as we both fuck in rhythm together, indulging the last moments of our euphoric orgasms."
                    play sound cum
                    show sidewayssex 4 with d
                    stop ambience fadeout 3.0
                    "Ahhh... As he pulls out, several droplets of cum seep out my well-fucked butt and drip down."
                    scene bg black with d
                    scene bg bedroomnight with d
                    call clothesnude from _call_clothesnude_39
                    show mce horny
                    with d
                    mc "Mmm, that was so good! Do you want to clean up in the shower with me? I have an ensuite!"
                    scene bg black with d
                    "After an unknown amount of time, my partner leaves, returning to the male dorms."
                    play sound success
                    $ sdgain = 1
                    call sdgain from _call_sdgain_109
                    $ shameloss = 1
                    call shameloss from _call_shameloss_75
                    "(+[fsd] Sexual Desire, -[fshame] Shame)"
                    $ status += 1
                    $ analsexes += 1
                    jump postworktrans
                "Anal (60 Sexual Desire)" if qanalqueen == 1:
                    if sd < 60:
                        "I don't think I'm quite ready to sleep with a stranger yet."
                        jump pickingup
                    jump clubanal
                "Back" if True:
                    jump pickingup
        "Prostitution Options" if True:
            "Sure, I could take anyone I want, but getting paid? Now that's something not just anyone can do."
            $ money1 = 40
            $ money2 = 80
            $ money3 = 90
            call moneycalculate from _call_moneycalculate_12
            menu:
                "Offer a Blowjob for $[fmoney1]" if True:
                    $ clubbj = 1
                    stop music
                    scene bg black with d
                    "I find a target and soon bring him home..."
                    play music action
                    play sound equip
                    scene bg bedroomnight with d
                    call clothesnude from _call_clothesnude_40
                    show mce laughing
                    with d
                    mc "Just seat on the bed, and I'll blow your mind..."
                    "Shamelessly, I kneel down before my customer as he takes out his half-erection."
                    scene bg bedsex
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
                    play ambience oral1 fadein 3.0
                    "Taking his cock in my hand, I guide it to my mouth and passionately take it deeper."
                    "Mmpphh, there's just something so depraved and arousing about fucking someone you just met for money."
                    "I begin by bringing my mouth level to its tip and accepting it into my mouth, swirling my tongue around the edge of the glans for a high pleasure start."
                    mc "Haahh, so biiig, mmmphh... *Lick*"
                    "I move quickly, wanting to pleasure him as much as possible. My goal is to coax him to cum fairly quickly."
                    "My hands begin to naturally caress the cock, my left jacking it off while my right delicately massages the balls."
                    "My thighs brush together, and I shiver with desire. I'm getting so aroused by this."
                    mc "Mmphh, mmm... *Lick, slurp*"
                    "Occasionally flicking my tongue across the sensitive tip of the erection, I focus on where he reacts the most favourably."
                    "When his cock throbs in response to my movements, I know I'm doing something right."
                    "I can't help but get more passionate, my handjob speeds up as the desire to have my mouth filled up with hot cum grows."
                    "I purse my lips around the glans and guide it back and forth in a fucking motion, sucking and licking with each movement."
                    "These motions are most similar to vaginal sex, this should make him cum in no time. And the tense throbbing in his cock confirms my thoughts."
                    "Using the last of my stamina I go all out to bring my customer to climax. I fuck his cock with my mouth deeply, while jacking him off intensely."
                    play sound cum
                    show blowjob3 2 with cum
                    play sound cum
                    show blowjob3 2 with cum
                    "Mmphh, yesss! His cock unloads several hot jets of cum straight into the back of my mouth."
                    play sound cum
                    show blowjob3 2 with cum
                    play sound cum
                    show blowjob3 2 with cum
                    "Load after load, I struggle to swallow it all. Some of it seeps outwards, dripping on my chin and face."
                    stop ambience
                    "I finish up the job, and he withdraws his rapidly shrinking cock."
                    $ blowjobs += 1
                    $ sdgain = 1
                    $ shameloss = 1
                    call sdgain from _call_sdgain_110
                    call shameloss from _call_shameloss_76
                    play sound success
                    "(+[fsd] Sexual Desire, -[fshame] Shame.)"
                    scene bg bedroomnight with d
                    call clothesnude from _call_clothesnude_41
                    show mce horny
                    with d
                    mc "I hope you enjoyed my service!"
                    $ moneygain = 40
                    call moneygain from _call_moneygain_59
                    play sound success
                    "(+$[fmoney])"
                    scene bg black with d
                    "My customer leaves, returning to the male dorms."
                    jump postworktrans
                "Offer Vaginal for $[fmoney2] (75 Sexual Desire, <25 Shame)" if True:
                    if sd < 75 or shame > 25:
                        "I don't think I'm quite ready to do that with a stranger yet."
                        jump pickingup
                    $ clubsex = 1
                    stop music
                    scene bg black with d
                    "I find a target and soon bring him home..."
                    play music action
                    play sound equip
                    scene bg bedroomnight with d
                    call clothesnude from _call_clothesnude_42
                    show mce laughing
                    with d
                    mc "Mmphh, I can't wait for you to ravage my pussy..."
                    show sidewayssexb
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
                    "Shamelessly, I lay down on my side and spread my legs before my customer as he takes out his half-erection."
                    $ condomon = 0
                    if condoms > 0 and pregnancyshowing == 0:
                        menu:
                            "Use a condom? Condoms: [condoms]. [fertilityrate]."
                            "Yeah." if True:
                                $ condomon = 1
                                $ condoms -= 1
                            "Fuck the rules! (Without protection!)" if True:
                                $ condomon = 0
                    "I beckon for him to take me. My lustful pussy is on full display, sheening slightly from a wetness."
                    "As he pushes the tip inside me, he pushes forward and slides deeper into my soaking wet insides."
                    play sound cum
                    show sidewayssex v2
                    with d
                    if virgin == 0:
                        "And just like that, the stranger I brought home takes my virginity."
                        $ virgin = 1
                    mc "Ahhh, you're quite big! Go steady at first."
                    play ambience sex fadein 3.0
                    "He begins thrusting back and forth, slowly sliding his cock almost all the way out before sinking back in."
                    "Although I'm so aroused, he's able to speed up a lot, and it doesn't take long until he's pounding me deeply, shaking my entire body against the bed."
                    "These deep thrusts fill me with pleasure as they grind against sensitive erogenous zones deep inside of me."
                    "The pleasure slowly builds over the course of a minute before it starts to really overwhelm me."
                    "And even though he's a customer, he reaches down and begins rub my clit, driving me wild."
                    "My mind turns blank as my body trembled towards a full-body orgasm."
                    mc "Ahhh, it's so good! I-I'm gonna, aahhh... Ahhhh!"
                    play sound cum
                    show sidewayssex v2
                    "I tightly grip the bedsheets as I climax, my pussy tightening around my partner's throbbing cock."
                    "And he only speeds up, motivated by my climax, he pushes towards his own."
                    play sound cum
                    show sidewayssex v3 with cum
                    play sound cum
                    show sidewayssex v3 with cum
                    "His tight cock explodes a hot load deep into my pussy as he ravishes me"
                    play sound cum
                    show sidewayssex v3 with cum
                    play sound cum
                    show sidewayssex v3 with cum
                    "I roll my hips back and forth needily as we both fuck in rhythm together, indulging the last moments of our euphoric orgasms."
                    play sound cum
                    show sidewayssex 4 with d
                    stop ambience fadeout 3.0
                    "Ahhh... As he pulls out, several droplets of cum seep out my well-fucked pussy and drip down my pelvis and thighs."
                    if condomon == 1 and pregnancyshowing == 0:
                        "But thanks to the condom, I don't need to worry about getting pregnant."
                    elif True:
                        call pregnancyroll from _call_pregnancyroll_12
                    scene bg bedroomnight with d
                    call clothesnude from _call_clothesnude_43
                    show mce horny
                    with d
                    mc "I hope you enjoyed my service!"
                    scene bg black with d
                    $ sdgain = 1
                    call sdgain from _call_sdgain_111
                    $ shameloss = 1
                    call shameloss from _call_shameloss_77
                    "(+[fsd] Sexual Desire, -[fshame] Shame)"
                    if qsecretlydepraved == 1:
                        "The enjoyment of a depraved act causes you to gain an additional [fsd] sexual desire!"
                        call sdgain from _call_sdgain_112
                    $ status += 1
                    $ vaginalsexes += 1
                    $ moneygain = 80
                    call moneygain from _call_moneygain_60
                    play sound success
                    "(+$[fmoney])"
                    scene bg black with d
                    "My customer leaves, returning to the male dorms."
                    jump postworktrans
                "Offer Anal for $[fmoney3] (85 Sexual Desire, <20 Shame)" if qanalqueen == 0:
                    if sd < 85 or shame > 20:
                        "I don't think I'm quite ready to do that with a stranger yet."
                        jump pickingup
                    label dormsanalprostitution:
                        pass
                    $ clubsex = 1
                    stop music
                    scene bg black with d
                    "I find a target and soon bring him home..."
                    play music action
                    play sound equip
                    scene bg bedroomnight with d
                    call clothesnude from _call_clothesnude_44
                    show mce laughing
                    with d
                    mc "I have some lube in my bedside draw, think you can apply it for me?"
                    show sidewayssexb
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
                    "I get into position with confidence, lifting my leg to expose both my dripping wet pussy and my tight ass."
                    "As the customer watches, he strokes his cock to erection. He takes some lube and gently applies it to my pucker."
                    mc "Mmphh, I'm ready for that fat cock now... Hehe."
                    "With my butt held high, I teasingly wiggle it while and spreading my cheeks."
                    play sound cum
                    play ambience sex fadein 2.0
                    show sidewayssex a2 with d
                    "He taps the tip of his cock against my anus a few times before lining it up properly and pushing in deep."
                    "It takes a while for my ass to adjust, but the lubrication and some relaxation enable me to take it with ease."
                    "Not only that, but it starts to feel good!"
                    "Once I'm ready, he begins slowly sliding his cock almost all the way out before sinking back in."
                    mc "Ohhh, yeaahh... Ahhh, you're really filling me up!"
                    "He starts to thrust faster while reaching down and rubbing my clit with his thumb."
                    mc "Aahhh, mmmpphhmmm... That's really good, yeah!"
                    "I love the way it grinds against all the sensitive spots deep inside. And in this position, it feels tighter and totally amazing for me."
                    "And all these combined sensations are enough to bring about my orgasm rather quickly, causing my entire body to tremble."
                    mc "Ahhh, it's so good! I-I'm gonna, aahhh... Ahhhh!"
                    play sound cum
                    show sidewayssex a2
                    with cum
                    "As my pussy contracts, my ass clenches too, squeezing around my customer's tense cock as I climax."
                    "And as my ass squeezees and milks his cock, he only speeds up. Motivated by my climax, he pushes towards his own."
                    play sound cum
                    show sidewayssex a3 with cum
                    play sound cum
                    show sidewayssex a3 with cum
                    "His tight cock explodes a hot load deep into my ass as he ravishes me"
                    play sound cum
                    show sidewayssex a3 with cum
                    play sound cum
                    show sidewayssex a3 with cum
                    "I roll my hips back and forth needily as we both fuck in rhythm together, indulging the last moments of our euphoric orgasms."
                    play sound cum
                    show sidewayssex 4 with d
                    stop ambience fadeout 3.0
                    "Ahhh... As he pulls out, several droplets of cum seep out my well-fucked butt and drip down."
                    scene bg black with d
                    scene bg bedroomnight with d
                    call clothesnude from _call_clothesnude_45
                    show mce horny
                    with d
                    mc "Mmm, that was so good! Do you want to clean up in the shower with me? I have an ensuite!"
                    scene bg black with d
                    "After an unknown amount of time, my customer leaves."
                    play sound success
                    $ sdgain = 1
                    call sdgain from _call_sdgain_113
                    $ shameloss = 1
                    call shameloss from _call_shameloss_78
                    "(+[fsd] Sexual Desire, -[fshame] Shame)"
                    if qsecretlydepraved == 1:
                        "The enjoyment of a depraved act causes you to gain an additional [fsd] sexual desire!"
                        call sdgain from _call_sdgain_114
                    $ moneygain = 90
                    call moneygain from _call_moneygain_61
                    play sound success
                    "(+$[fmoney])"
                    $ status += 1
                    $ analsexes += 1
                    jump postworktrans
                "Offer Anal for $[fmoney3] (75 Sexual Desire, <25 Shame)" if qanalqueen == 1:
                    jump dormsanalprostitution
                "Back" if True:
                    jump pickingup
        "Back" if True:
            jump cm

label yokoroute:
    $ yokomet = 1
    if yokoroute1 == 0:
        jump yokoroute1
    elif yokoroute2 == 0:
        jump yokoroute2
    elif True:
        jump yokoroute3
label yokoroute1:
    $ yokoroute1 = 1
    mc "I'll wait at the bar, and keep myself open to anyone that wants to come and talk."
    "Unsurprisingly, it doesn't take long for someone to start chatting to me. The real surprise is who it is!"
    play music toko
    show yokob:
        xpos 1200
    show yokoo clothes:
        xpos 1200
    show yokoe happy:
        xpos 1200
    "A girl with rather unkempt messy hair, and while she's obviously at least my age, she's dressed in cutesy clothes."
    python:
        yoko = renpy.input("Name the Yandere Girl. Leave blank for the default name 'Yoko'.")
        yoko = yoko.strip()
        if not yoko:
            yoko = "Yoko"
    show yokoe horny with d
    yoko "Oh my gosh, you're so cuuute!"
    "Well, she's certainly not holding anything back."
    if nude == 1 or lewdoutfit == 1:
        yoko "And I looove how you're dressed, it's so naughty!"
    elif True:
        yoko "And I looove your outfit! So sexy!"
    show mce horny with d
    mc "Thank you! You look far cuter than I do, though!"
    show yokoe laughing with d
    yoko "Ohh, you really mean it? No way! I'm not nearly as beautiful as you."
    yoko "Oh, let me buy you a dri- wait, you are gay, riight? No, it doesn't matter! Buying you a drink anyway!"
    menu:
        "Uhh, sure! (+5 Sexual Desire, -5 Shame)" if pregnancyshowing == 0:
            $ sd += 5
            $ shame -= 5
            if qlightweight == 1:
                $ sd += 5
                $ shame -= 5
            $ drunk += 1
            show yokoe happy with d
            yoko "A cocktail for me and the beautiful lady, please!"
            play sound success
            "(+1 Intoxication Level)"
            if qlightweight == 1:
                "(Lightweight) Since you're a lightweight, you feel double the effects!"
            $ yokoaffection += 1
        "Something non-alcoholic?" if True:
            show yokoe happy with d
            yoko "N'aww, oookay! I'm already suuuper drunk though, so I hope I don't annoy you!"
    show mce happy with d
    "She's intense, but I can't say I dislike it!"
    "I think it's clear she just has a bubbily personality, and the courage from the alcohol is making her a little over the top."
    show yokoe horny with d
    yoko "Here you go!"
    mc "Thank you, you really didn't have to."
    show yokoe laughing with d
    yoko "Well, I operate by a 'stroke the cat' philosophy!"
    yoko "Whenever I see a cat on the side of the road, I make sure to stop and appreciate it, give it some love."
    mc "Ohh yeah? Am I the cat?"
    show yokoe happy with d
    yoko "Do you want to be? I can make you purr, if you'd like."
    menu yr1:
        "I'd like that a lot! (20 Sexual Desire)" if True:
            if sd < 20:
                "I can't say that... I don't want to lead her on."
                jump yr1
            $ yokoaffection += 1
        "Maybe if I got to know you a little better." if True:
            pass
    yoko "Mmm... I like you! What's your name?"
    mc "I'm [mc], what about you?"
    show yokoe horny with d
    yoko "I'm [yoko]! You must be a student, right?"
    mc "Yup! What about you?"
    show yokoe laughing with d
    yoko "Hohh my gosh, a student for hero academy! How inspiring..."
    mc "It's not all that impressive."
    show yokoe happy with d
    yoko "But it can be, you can be!"
    yoko "What are your thoughts on the commercialization and corportization of hero society and jobs?"
    mc "Ahh- that's quite an intense line of discussion over a drink! I haven't really thought much about it..."
    yoko "I bet you're one of the good ones, though! You do it just to help people."
    mc "Uhhh..."
    "I'm only in it for the money though... I probably shouldn't tell her that."
    mc "Yeah, I want to save lives and help people."
    show yokoe neutral with d
    yoko "Haahhh... Even someone like me?"
    mc "Of course!"
    show yokoe happy with d
    yoko "I'd love for you to save my life, [mc]! *Giggles*"
    show mce laughing with d
    mc "Haha, what is that supposed to mean?"
    yoko "Mmm, I don't know!"
    show mce happy with d
    "She downs the rest of her drink and ponders."
    show yokoe horny with d
    yoko "I reaaally wanna invite you back to my place, but I uhh..."
    "Hmm, me and this girl? What would that be like?"
    "She scratches her messy hair before brushing her fingers through her bangs."
    "Ahh, she really is adorable... Maybe a girlfriend candidate?"
    $ sdgain = 1
    call sdgain from _call_sdgain_115
    play sound success
    "(+[fsd] Sexual Desire)"
    yoko "Can I have your number...?"
    menu:
        "Give her your number." if True:
            $ yokoaffection += 1
            $ yokohasnumber = 1
            show yokoe laughing with d
            yoko "Ahh, thank you so much!"
        "Politely decline" if True:
            $ yokoaffection -= 1
            show yokoe sad with d
            yoko "O-Oh... R-Right! Okay... Here, take mine, just in case."
            "She hands me a pre-prepared slip of paper with her number on it. The relatively fresh ink stands out, implying she wrote this just before she came up to me."
    yoko "I'd stay a little longer, but... I'm getting so sleepy, and I definitely drank too much. I hope I see you around, [mc]!"
    mc "Okay! I'll be leaving soon too. Goodbye, [yoko]!"
    hide yokob
    hide yokoo
    hide yokoe
    with d
    "Mmm... What an interesting character. She seemed so genuinely interested in me, that's quite unusual, but also rather refreshing. I'd like to sit down in a quieter environment and get to know her a little better sometime."
    "Guess I'll finish my drink and go home too."
    jump postworktrans
label yokoroute2:
    $ yokoroute2 = 1
    mc "I'll wait at the bar, and keep myself open to anyone that wants to come and talk."
    "It doesn't take long for someone to start chatting to me. The real surprise is who it is!"
    "This girl, again! I'm not sure if it's high odds or low odds to run into her in this specific bar, but it's always good to see a recognizable face."
    play music toko
    show yokob:
        xpos 1200
    show yokoo clothes:
        xpos 1200
    show yokoe happy:
        xpos 1200
    with d
    yoko "Oh my god, is that… you! [mc]! I'm so happy to see you again! Hehe."
    show mce laughing with d
    mc "[yoko]! How’ve you been?"
    show yokoe laughing with d
    yoko "Oh, I'm feeling terrific! The sun has been shining brighter than usual!"
    show mce happy2 with d
    mc "That's wonderful to hear! Let me buy you a drink this time."
    show yokoe horny with d
    yoko "Haahhh, y-you’re going to buy me a drink?! Aahh, are you trying to pick me up? I’d love to drink something you’ve bought for me!"
    show mce happy with d
    mc "Uhm, ahaha, we'll see about that. What would you like?"
    yoko "I'd like Sex on the Beach! Ohh, you meant to drink?"
    bartender "What can I get you two lovely lasses?"
    if pregnancyshowing == 1:
        mc "One Sex on the Beach cocktail, and one cola please."
    elif True:
        mc "Two Sex on the Beach cocktails please."
    show yokoe neutral with d
    yoko "Wait that wasn’t-… N-Nevermind."
    if pregnancyshowing == 0:
        "With a drink of alcohol, you’ve gotten slightly drunk! (+5 Sexual Desire, -5 Shame)"
        $ sd += 5
        $ shame -= 5
        $ drunk += 1
        if qlightweight == 1:
            "And since you’re a lightweight you feel the effect twice as much. (+5 Sexual Desire, -5 Shame)"
            $ sd += 5
            $ shame -= 5
    "Yoko and I get a better opportunity to chat more."
    "She's even more nervous than last time, but that's probably because she's less drunk."
    show yokoe laughing with d
    yoko "Soo, I can't believe I ran into someone as beautiful as you again! (That being you!) What are you here for?"
    menu:
        "Just here for a good time" if True:
            show yokoe horny with d
            yoko "A-A good time? I see…"
            yoko "I might be in the business of that!"
        "Here for some guy-love" if True:
            show yokoe sad with d
            yoko "Figures…"
            yoko "Ohh, but maybe I could convince you!"
        "Here for some girl-love" if True:
            show yokoe horny with d
            yoko "Ohh, me too, and you’re just my type!"
        "I came hoping to see you again" if True:
            show yokoe horny with d
            yoko "W-What, really? I mean, me too! That’s why I’m here…"
    show mce horny with d
    mc "Oh yeah? Hehe, maybe you should tell me more."
    "She bites her lip and grins."
    show yokoe laughing with d
    yoko "I could tell you, but only if you invite me to your place..."
    "She's really cute, and a few subtle red flags aside, I wouldn't mind getting closer with her at all."
    menu yr2m:
        "Invite her back for some fun (40 Sexual Desire)" if True:
            if sd < 40:
                "A little too early for me, I think"
                jump yr2m
            "Hmm… Sounds like it could be a lot of fun. Where’s the harm in experimenting a little while I’m at college?"
            show mce laughing with d
            mc "Okay, I’ll bite, I’ll invite you back to my place."
            show yokoe horny with d
            yoko "Oh yesss, I hope you bite during the act too! If you don’t, I might, hehe."
            jump yokosex
        "Politely decline" if True:
            show yokoe neutral with d
            yoko "Aa-aahh… M-Maybe next time?"
            show mce neutral with d
            mc "Mm…? Yeah, maybe. I'll send you a text if I ever want to hang out, you can too."
            yoko "I’m sorry if I was pushy…"
            mc "Lighten up a bit, I’m not even the cutest girl in the room!"
            "Yoko glumly nods and whispers something under her breath. "
            yoko "Thanks for the drink, [mc]. I’ll get out your hair now."
            hide toko with d
            mc "Bye Yoko, have a nice night!"
            "I finish my drink and it’s a mostly uneventful evening other than that. There was a moment where a guy flirted with me, but I wasn’t really in the mood after just rejecting Yoko."
            "It’s kinda weird though, I feel like someone was watching me. It definitely wasn’t Yoko, though, I saw her leave and never saw her again."
            jump postworktrans
label yokoroute3:
    "While waiting at the bar, I feel like sending a text to [yoko]. With a quick message, I get a reply in less than a minute!"
    "’I’ll be right there! Gimmie 5 min! xxx’"
    "Lo and behold, she arrives in 5 minutes."
    play music toko
    show yokob:
        xpos 1200
    show yokoo clothes:
        xpos 1200
    show yokoe happy:
        xpos 1200
    yoko "Eee, it’s so nice to see you!"
    "We spend a while drinking, dancing, and catching up with our recent day-to-day."
    "After that, I…"
    menu yr3m:
        "Invite her back to my place (40 Sexual Desire)" if True:
            if sd < 40:
                "A little too early for me, I think"
                jump yr3m
            jump yokosex
        "Thank her for a good time and go home" if True:
            jump postworktrans
label yokoroute4:
    "An unexpected surprise, but a pleasant one!"
    "Just how do we keep running into each other like this?"
    show mce happy2 with d
    mc "Heyy, [yoko], I didn't see you there! How's it going?"
    show yokoe happy with d
    yoko "Ehh, hehe, it's really good now. Are you okay? You're all alone again."
    show mce happy with d
    mc "Ohh, uhmm... Sometimes I just come to the club by myself."
    show yokoe neutral with d
    yoko "R-Really? Like... To bring men back, or...?"
    show mce neutral with d
    "Awwhhh, she's jealous..."
    "... That could be bad."
    mc "I'm just here to drink and make friends."
    show yokoe sad with d
    yoko "Aahhh, I think I get it... It's a little dangerous, though... I wouldn't want something bad to happen to you."
    show mce happy with d
    mc "Aren't you here alone too?"
    yoko "Not anymore now I'm with my friend, [mc]! We're more than friends, r-right?"
    menu:
        "We're just friends." if True:
            yoko "Ohh, I see... Too early..."
        "Maybe... with benefits?" if True:
            "She grins and coos."
            yoko "My, my... We should go through each and every benefit one by one."
        "Uhm... besties?" if True:
            yoko "Hehe, besties! I like that!"
        "Time will tell what we'll become." if True:
            yoko "Aahh, how beautifully poetic... This is why I like you, [mc]!"
    "I have to say, [yoko] seems to be getting pretty attached."
    "Still, she cools down a little, we order a few drinks and dance a little. I guess I can forget about my previous plan of taking a man home..."
    "After that, I…"
    menu yr4m:
        "Invite her back to my place (40 Sexual Desire)" if True:
            if sd < 40:
                "A little too early for me, I think"
                jump yr4m
            jump yokosex
        "Thank her for a good time and go home" if True:
            jump postworktrans
label yokosex:
    scene bg bedroomnight with d
    "Chatting, flirting, and giggling on the way back to my dorm, [yoko] and I find ourselves getting closer."
    "Until we finally reach my room, and hit the bed."
    menu ysm:
        "Cunnilingus" if True:
            scene bg bedsex
            show yokoroute2b
            show yokoroute2 1
            with d
            yoko "I can’t believe I pulled a hero student, so naughty!"
            mc "What's so surprising about that? You're not secretly 40, riiight?"
            yoko "Hehehe, I'm only 23, don't be a meanie! I just like the idea of some 'hero' between my legs, hehehe..."
            yoko "Now let’s see you put that sassy tongue to some good use! Hehe…"
            "Completely undressed, I get the opportunity to marvel at her fine body. It’s even toned and clearly very active, although she never said she was a student."
            "I wonder what her power is? Oh well, let’s focus on the sex."
            "I slowly lower myself and make an effort to pleasure her as much as possible. My cunnilingus is amateur if anything, but as a girl I have a certain advantage of knowing how to pleasure her."
            play sound2 foreplay1 fadein 3.0
            play ambience oral1 fadein 3.0
            show yokoroute2 2 with d
            "Swirling my tongue around her clit immediately, she already starts to feel the pleasure as her breathing turns ragged, and a few cute gasps escape her lips."
            yoko "Mmphh, good girl… That’s the spot…"
            "She’s abnormally wet and aroused, as if this is more than just a fling, but something that truly gets her going. Some fetish being tapped into, perhaps. Regardless, it’s clear that she’s burning with desire."
            "As my tongue flicks around her clit, she gradually begins to grind back and forth, pressing herself against my face."
            yoko "Mmphh, that’s perfect… Keep going just like that!"
            "I keep lapping her sweet spot while her grinding gradually becomes more needy and vigorous. Her gasps from earlier have become complete passionate moans that would make my dormitory neighbours jealous."
            yoko "Aaahh, aaaahhhh… I-I’m gonna, c-cum!"
            play sound cum
            show yokoroute2 2 with cum
            "While cumming, she wriggles intensely, and I have to hold her butt in place while I tactfully suck and lick her clit to the best of my ability."
            "Her toes curl and her back arches as she reaches the peak of her bliss, and as she gradually comes to a halt, she crumples back down the bed. Her legs seemingly weak as she catches her breath."
            stop sound2 fadeout 2.0
            yoko "*Pant, pant* T-That was so good…"
            show yokoroute2 1
            with d
            "I sit up , my face covered in wetness. [yoko] giggles and pats me down with a tissue."
            mc "Hehe, thank you. That wasn't so bad."
            mc "Now it’s your turn, if you impress me I might consider making this a regular thing."
            "I tease her, and it seems to work as [yoko] bites her lip."
            yoko "I like the sound of that…"
            scene bg bedsex with d
            "Yoko and I make love for almost an entire hour afterwards, indulging in many orgasms until we both fall asleep, cuddled in the nude together."
            "It seems this was more than just a one time thing, [yoko] and I managed to connect today."
            "I don’t know whether it’ll become anything more than just sex, but I’d be open to doing this again, many more times…"
            jump postworktrans
        "Sixty-Nine" if True:
            jump yp69
        "Futa" if yokosex2 == 1:
            jump ypfuta
        "Selfcest" if yokosex3 == 1:
            jump ypsc


label yokopostsex:
    label yp69:
        play music action
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
        play sound2 foreplay2 fadein 2.0
        "It started when [yoko] pushed me down and started making out with me."
        "It ended up with her turning around, and replacing her top lips with her bottom ones!"
        "I think my eagerness caught her off guard, as I didn’t skip a beat in making out with her lower lips as I ran my tongue around her clit."
        yoko "Aahh, haaahhh! Someone couldn’t wait to dive in!"
        mc "How could I not when you’re such a delectable morsel? Hehe…"
        "She can barely hold back her moans as my tongue skilfully pleasures her clit over and over."
        "This was supposed to be a sixty-nine, I assume, but she can’t get it together long enough to return the favour."
        yoko "Mmphhh, haaahhh… Such a talent you have there! Mmphh…"
        "Eventually getting it together, Yoko buries her head between my thighs too, her slightly longer, slender tongue servicing my clit to perfection."
        yoko "Mmphh, *lick, lick*… Warm, soft and delicious…"
        "Occasionally I can feel her lips purse around the nub as she sucks, and she isn’t shy about introducing her fingers as she prods and teases with everything she can."
        "We’re both left squirming and moaning with pleasure, and the tension just keeps rising."
        play sound cum
        show yoko69 2 with cum
        "And it looks like I’m the winner of our small competitive cunnilingus, pushing her over the edge with my tongue, she throws her head back and moans loudly, even squirting slightly."
        yoko "Hoohhh, fuuuuck! You’re relentless, [mc]!"
        "The climax as initially very powerful, and the euphoria consumed her for well over half a minute before she managed to return her focus to my own pussy, and finish me off."
        stop sound2 fadeout 1.0
        "My head was in the clouds for a while as I too indulged in a powerful orgasm."
        "And as we were both satisfied, we cuddled lovingly in each other’s company."
        if yokosex2 == 0:
            scene bg bedroomnight
            call clothespjs from _call_clothespjs_6
            show mce happy
            show yokob:
                xpos 1200
            show yokoo bottomless:
                xpos 1200
            show yokoe happy:
                xpos 1200
            with d
            mc "Hey, [yoko], usually people know this before they eat each other out, let alone twice, but what’s your power?"
            show yokoe horny with d
            yoko "Hehe, you didn’t have a problem having a deep conversation with my bottom lips."
            show mce horny with d
            mc "Conversation? That was more of a French kiss, ahah."
            show yokoe laughing with d
            yoko "My power is shapeshifting, and I looove it! I can be anyone, but I need to consume some of their ‘DNA’, if you know what I mean."
            show mce happy with d
            mc "So you’re saying you could shapeshift into me just because you ate me out? That’s a cool power! Kinda crazy to think of the possibilities!"
            show yokoe horny with d
            yoko "Mhm! But that’s not all, I can also modify parts of my own body, all I need to do is partially transform an area of my body."
            yoko "I was thinking about adding a little something extra between my legs."
            show mce horny with d
            mc "O-Oh? Not just a strap-on, I’m presuming!"
            show yokoe laughing with d
            yoko "Nuh-uh! I can give you the full-experience, any experience!"
            show mce happy with d
            mc "That sounds like a lot of fun, maybe we should experiment later."
            mc "So, outside of the bedroom, if you partially transformed your body into a really strong female super hero, you’d be super strong?"
            show yokoe neutral with d
            yoko "Huh?! It’s a bit stronger than that… I wouldn’t want to copy some gross hero anyway… I only want to be cute people."
            show mce neutral with d
            mc "H-Hey, I’m training to be a hero, you know? I’m not gross, I hope!"
            show yokoe happy with d
            yoko "O-Oh, I’m sorry! I wasn’t thinking when I said that."
            mc "You said your power is a bit stronger than just copying their strength? You don’t mean what I think, do you?"
            show yokoe laughing with d
            yoko "Ahehe, I’ve said too much… How about we just play with our powers the next time we’re in bed?"
            mc "Sure, it’s a ‘date’, I think!"
            $ yokosex2 = 1
        play sound success
        $ sdgain = 1
        $ shameloss = 1
        $ status += 1
        $ lesbian += 1
        call sdgain from _call_sdgain_153
        call shameloss from _call_shameloss_111
        "(+[fsd] Sexual Desire, -[fshame] Shame)"
        scene bg black with d
        "Early in the morning, around 7:00am, [yoko] returns home."
        jump morning
    label ypfuta:
        play music action
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
        play sound2 foreplay2 fadein 2.0
        "Laying on-top of me, [yoko] starts by making out, occasionally grinding her hips back and forth which creates some friction as our pussies touch."
        "We’re both really wet, and really ready! Wait, ready for what, though?"
        yoko "Remember how I said I shapeshift? Hehehe… Do you want me to fuck you, [mc]?"
        mc "*Gulp* I’m not against it! Show me what you’ve got."
        yoko "Hehehe… Here we go!"
        $ condomon = 0
        if condoms > 0 and pregnancyshowing == 0:
            menu:
                "Use a condom? Condoms: [condoms]. [fertilityrate]."
                "Yeah." if True:
                    $ condomon = 1
                    $ condoms -= 1
                "Fuck the rules! (Without protection!)" if True:
                    $ condomon = 0
        play sound cum
        show yokofuta 2 with d
        "Rather suddenly, I feel something growing and pressing into my pussy! I’m wet enough that it manages to slip right in as it continues to grow."
        if virgin == 0:
            call virgin from _call_virgin_10
            "And what a way to lose it!"
        mc "E-Eep, it’s like I’m feeling it grow hard inside of me."
        yoko "Ooohh, god… You’re so wet and soft… Mmphh…"
        play sound2 sex fadein 2.0
        show yokofuta 3 with d
        play ambience sex fadein 2.0
        play sound2 foreplay1 fadein 2.0
        "Unable to help herself, [yoko] fervently rocks her hips back and forth, plapping and slapping against my pussy as good as any man."
        mc "Haaahh, aaahhh, d-does it really feel that good?"
        yoko "Mmphh, picture it this way, [mc], imagine you’re 23, you’ve never cum in your entire life, and you’ve just entered the best pussy in the world."
        mc "T-That does sound like it’d- ahh, feel good!"
        "The long hard thrusts drive me wild, sending ripples through my butt as our bodies connect."
        "Now I’ve gotten over the shock of her penis, I simply melt in the pleasure and fuck her back too. My hips rock in response to reach thrust, my pussy tightly squeezing around the throbbing member."
        yoko "Ohh, f-fuck! I-I’m gonna-"
        play sound cum
        show yokofuta 4 with cum
        play sound cum
        show yokofuta 4 with cum
        play sound cum
        show yokofuta 4 with cum
        "With a loud moan, [yoko] suddenly fills my pussy up to the brim with excessive amounts of thick, hot cum."
        play sound cum
        show yokofuta 4 with cum
        play sound cum
        show yokofuta 4 with cum
        play sound cum
        show yokofuta 4 with cum
        stop sound2 fadeout 1.0
        stop ambience fadeout 1.0
        "It really is like she hasn’t cum a single time ever. From the sheer amount of cum, to how quick and sudden her orgasm was, it’s rather overwhelming!"
        show yokofuta 5 with d
        "However, despite the premature ejaculation, [yoko] seems to have another trick up her sleeve…"
        yoko "Mmphh, s-sorry… That was too soon, wasn’t it? Hehe, I couldn’t hold back at all."
        yoko "Let me redo that…"
        play sound cum
        show yokofuta 4 with d
        "[yoko] bites her tongue as I feel her body shifting around above me. Her penis disappears, and then… reappears?"
        yoko "There we go, I’ve reloaded and I’m ready to go again!"
        mc "O-Oh my…"
        play ambience sex fadein 2.0
        play sound2 foreplay1 fadein 2.0
        "For some reason, the thought of [yoko] being the perfect girlfriend briefly swirls in my mind, only to be interrupted by her quickly picking up the pace and fucking me again."
        mc "Aahhh, yes! Keep going, [yoko]!"
        yoko "Anything for you, kitten!"
        "I soon feel her cock throbbing deep inside me again as that intense pleasure returns to me."
        "Damn it feels amazing. Our hips rock into each other, each of us fucking as hard as we can. Our moans echoing from my walls and no doubt alerting my neighbours."
        mc "Aaahhh, k-keep going, just like that!"
        yoko "Y-Yeahh, oh god, yeaahh! Come for me, [mc]!"
        "My orgasm keeps swelling up, growing and growing until the burning passion can’t hold on much longer, and neither can [yoko] and she seems to be on the precipice of yet another quick orgasm."
        play sound cum
        show yokofuta 4 with cum
        play sound cum
        show yokofuta 4 with cum
        "Just as I feel myself going over the edge, I feel [yoko]’s cock throb and swell, as a second massive helping of jism is released into my pussy, bubbling and splashing around with the first load."
        play sound cum
        show yokofuta 4 with cum
        play sound cum
        show yokofuta 4 with cum
        "My vision turns cloudy and my mind fogs up as I’m overwhelmed with an entire feeling of euphoria. The two of us orgasm together, all whilst we fuck each other passionately."
        call pregnancyroll from _call_pregnancyroll_19
        stop ambience fadeout 3.0
        mc "Mmphh, yeessss… aaahh!"
        stop sound2 fadeout 3.0
        show yokofuta 5 with d
        "As Yoko’s additional equipment is shapeshifted away, we’re both left panting and drained."
        yoko "Haaahh, I can barely breath, haahhh… *Pant, pant*"
        mc "You really did go all out… It was really good, thank you…"
        if yokosex3 == 0:
            scene bg bedroomnight
            call clothesnude from _call_clothesnude_46
            show mce happy
            show yokob:
                xpos 1200
            show yokoe horny:
                xpos 1200
            with d
            yoko "H-Hey, you don’t need to thank me… I’m just happy to try this out for the first time."
            mc "Really? That was your first time?"
            yoko "Yeahh, haahh… Well, I don’t get out much. You’re one of my only friends, so I really treasure that."
            mc "I thought a happy, bubbly girl like yourself would be quite popular. Much more than someone a little reserved like me."
            show yokoe happy with d
            yoko "Heh… You don’t think I’m reserved? I’m a shy ball of anxiety and insecurity, I just put on a happy face."
            show mce neutral with d
            mc "R-Really? I’m sorry to hear that."
            show yokoe laughing with d
            yoko "Ohh, it’s okay, you make me happy…"
            show mce happy with d
            mc "Ahh, and I’m glad to hear that!"
            show yokoe neutral with d
            yoko "But… I… Maybe I shouldn’t be doing this… I might be putting you in danger."
            show mce neutral with d
            mc "What do you mean? What’s wrong?"
            show yokoe sad with d
            yoko "It’s the people I hang around with… They hate heroes, in fact, I hate heroes… It was never my intention to get this close with you…"
            yoko "My goal was to find a student and shapeshift into them, so I coul- No, I’m saying way too much…"
            show mce sad with d
            mc "I… I don’t understand?"
            yoko "I’m… with a criminal syndicate, we want to take down hero society…"
            mc "But why? Heroes are necessary to maintain peace in this world of powers."
            yoko "I… haven’t had the best experience with heroes… To tell you the truth, what you’re seeing isn’t my ‘real body’…"
            yoko "My real body was covered in burns and scars after an incident."
            yoko "It all happened so quickly, one moment I was about to finish a colouring book, and the next second was fire and chaos."
            yoko "It was a hero, they had just been knocked into my room during a fight, my parents were crushed in the process."
            yoko "They even made eye contact with me, before simply jumping out of the hole they created, leaving me trapped in a burning building."
            yoko "I barely escaped on my own, and made it to an evacuation centre. But the thing that really stirred my gut was seeing the news coverage."
            yoko "This man, that had killed my parents, and essentially ended my life as I had come to know it, they were celebrated as a hero."
            yoko "Everyone in the evacuation centre was cheering, I just couldn’t understand. I was so angry!"
            yoko "This ‘hero’ was treated like a celebrity. Was he too good to save someone like me?"
            yoko "He didn’t care at all, he’s clearly only interested in the fame and other benefits that come with the job, and I’m so sick of the commodification and corporatization of heroes. It makes me sick seeing them as celebrities, or selling merchandise like tacky keychains and posters."
            yoko "What kind of hero even does that?!"
            "The heartfelt confession leaves [yoko] trembling. I listened to her silently, and I take a few moments more to compose my thoughts into a reply that is more than just sympathy."
            show mce angry with d
            mc "You’re right… He’s no hero, that story disgusts me to the core too."
            show yokoe neutral with d
            yoko "R-Really? You understand even though you’re trying to become a hero?"
            show mce sad with d
            mc "You have to understand that even among heroes, there are good and bad. That’s human nature, you can’t escape that a percentage of the population will always be cruel, and selfish."
            show mce happy with d
            mc "You said that you’re with a criminal syndicate, that wants to tear down hero society? I’d say it’d be a lot more productive to be the positive change you want to see in the world, rather than let the entire world burn."
            mc "Be that positive role model, and maybe save the [yoko]’s of the world that need you."
            show yokoe happy with d
            yoko "Ohh… My former master did imply such a thing… You’re right, I think…"
            show yokoe neutral with d
            yoko "Ever since my master passed, I’m certain the syndicate I’m working with now don’t have my interests at heart. But it’s hard to simply break away from something I’ve always ever known."
            show mce sad with d
            mc "Who was your former master?"
            yoko "You wouldn’t know them, but they took me in and raised me after I was orphaned. They only fanned the flames of hate I had towards celebrity heroes."
            show yokoe happy with d
            yoko "But, they never once scorned anyone who they believed to be a genuine hero. They had nothing but respect for those, and these are the morals I carry with me. The people I’m with… I’m starting to doubt if our views align at all."
            yoko "You, [mc], I believe you could be a true hero…"
            show mce happy with d
            mc "Y-Yeah, maybe… What about you, [yoko]?"
            yoko "Me… a hero?"
            show yokoe laughing with d
            yoko "Heh, hahaha… One step at a time. Let me put some distance between me and the bad crowd I’m in. It shouldn’t be hard, I’m useful to them but they barely trust me since I’m apparently too ‘young and unreliable.’"
            "Grasping [yoko]’s hand, I nod and smile."
            show mce laughing with d
            mc "Good luck, keep me updated, okay?"
            $ yokosex3 = 1
        play sound success
        $ sdgain = 1
        $ shameloss = 1
        $ status += 1
        $ lesbian += 1
        $ vaginalsexes += 1
        call sdgain from _call_sdgain_154
        call shameloss from _call_shameloss_112
        "(+[fsd] Sexual Desire, -[fshame] Shame)"
        scene bg black with d
        "Early in the morning, around 7:00am, [yoko] returns home."
        jump morning
    label ypsc:
        if yokosex4 == 0:
            scene bg bedroomnight
            call clothes from _call_clothes_79
            show mce happy
            show yokob:
                xpos 1200
            show yokoo clothes:
                xpos 1200
            show yokoe happy:
                xpos 1200
            with d
            "Sitting on the bed, we continue chatting, and now we’re in private, [yoko] said she’ll update me on her current situation."
            show yokoe laughing with d
            yoko "Sorry to keep you waiting, I had to make sure we were somewhere without any eyes and ears."
            show mce neutral with d
            mc "*Gulp* S-Spooky!"
            show yokoe happy with d
            yoko "Don’t worry, they daren’t get within a kilometer radius of the campus, hehe. They might act tough, but they really are just rabble."
            yoko "I've got my out, and you don't have to worry about me messing around with people like that anymore."
            show mce happy with d
            mc "That’s a relief, I’m glad you’re not in danger."
            yoko "Heh, I can shapeshift, remember? They’ll never be able to get me."
            mc "By the way, what was it they wanted you to do? Shapeshifting into me, or something?"
            yoko "Oh yeah, check this out."
            scene bg bedroomnight
            call clothes from _call_clothes_80
            show mce neutral
            show yokomcdisguise:
                xpos 1150
            with d
            "Woah, she really does look like me…"
            yoko "They wanted me to disguise as a student so I could map out the campus and its security."
            yoko "But after meeting you… I couldn’t do such a thing, especially when I look like you!"
            show mce happy with d
            mc "Hahaha, I appreciate that, ‘me’."
            yoko "Heyy, I just got an idea…"
            show mce horny with d
            mc "What’s your idea?"
            scene bg black with d
            "..."
        play music action
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
        "How do I get myself into these situations?"
        "Her dripping wet pussy is right in front of my face, and it’s an exact replica of mine. It’s the first time I’ve ever seen it so close and in person."
        yoko "Mmphh, don’t be shy!"
        "It’s glistening wet, so I timidly bring my tongue closer and start to explore."
        play sound2 foreplay1 fadein 3.0
        "On the other side, a more lustful ‘me’ is eagerly lapping at my clit, sending tingles of pleasure through me."
        mc "Mmm, this is pretty weird!"
        yoko "Hm, hang on!"
        "She adjusts her body so her pussy is directly on top of my mouth, preventing me from speaking."
        yoko "That’s better, now get to work licking!"
        mc "Mmphh, mm!"
        show yokoselfcest 2
        with d
        "I close my eyes and slide my tongue up and down against her clit. She’s enjoying this, as with each lick I can hear her cute moans- moans that sound exactly like my voice! This may be enjoying it, but it’s a little weird for me."
        "The more I focus her clit, the more enthusiastic she gets, as she grinds her hips back and forth against my face. The pure passion is infectious as we both shiver in pleasure and become sloppier and more lustful with our movements."
        "As I intensify my licking, she doesn’t hold back as she flicks her tongue rapidly against my clit."
        "It feels fantastic, and the novelty of having a sixty-nine with myself is actually adding to the feeling more than I’d expect."
        yoko "Ohh, that’s good! Keep going, mini-[mc]!"
        mc "H-Heyy, why am I mini? Ahhh, ahh."
        "We kept repeating the same sensational motions, getting slightly faster as our desire grew, and our climaxes approached."
        "Eventually the feeling was so overwhelming that it was hard to focus on licking, our tongue work growing sloppy as our bodies squirmed with pleasure."
        play sound cum
        show yokoselfcest 3
        with cum
        "However, with us both extremely close, we easily reached our climaxes. Our entire bodies are rocked with bliss, and the room was filled with the melodic sounds of orgasmic moans."
        yoko "Aaahh, aahhh, yesshhh! *Lick, lick*"
        mc "Mmphhh, s-so good! Haaahhh…"
        stop sound2 fadeout 2.0
        "As our orgasms faded, my entire body felt relaxed and comfortable. I didn’t feel like moving at all."
        "And neither did [yoko], as she spun around, curled up and cuddled beside me- still very much with my body."
        scene bg bedsex with d
        yoko "So, how did you do?"
        mc "You did good, me, you did good… Hehe…"
        "Unable to resist, I close the gap and make out with her for a while."
        "I could get used to this…"
        if yokosex4 == 0:
            scene bg black with d
            "A bit later..."
            scene bg bedroomnight
            call clothespjs from _call_clothespjs_7
            show mce happy
            show yokob:
                xpos 1200
            show yokoo bottomless:
                xpos 1200
            show yokoe happy:
                xpos 1200
            with d
            yoko "So… I was thinking about becoming a student, maybe?"
            show mce laughing with d
            mc "Ohh, that’d be amazing!"
            yoko "Y-Yeah! Hehe, you really inspired me with what you said last time. About being the ‘change you want to see in the world’."
            yoko "I want to be the hero that my younger self always wanted to look up to."
            show mce happy with d
            mc "I’m so glad to hear that, I have no doubt you’ll be an amazing hero."
            show yokoe laughing with d
            yoko "Sooo, maybe you’ll be the senpai of shapeshifting hero [yoko]! Eeee, how exciting!"
            $ yokosex4 = 1
        play sound success
        $ sdgain = 1
        $ shameloss = 1
        $ status += 1
        $ lesbian += 1
        call sdgain from _call_sdgain_155
        call shameloss from _call_shameloss_113
        "(+[fsd] Sexual Desire, -[fshame] Shame)"
        scene bg black with d
        "Early in the morning, around 7:00am, [yoko] returns home."
        jump morning

init:
    $ yokoaffection = 0
    $ yokohasnumber = 0
    $ yokoroute1 = 0
    $ yokoroute2 = 0
    $ yokoroute3 = 0
    $ yokoroute2ee = 0
    $ yokosex2 = 0
    $ yokosex3 = 0
    $ yokosex4 = 0
    $ clubsex = 0
    $ clubbj = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
