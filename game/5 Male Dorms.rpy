label maledorms:
    if boyfriend == 0 and maledormsunlocked == 0:
        "Unlock this location by having >50 Sexual Desire and <50 Shame."
        if sd >= 50 and shame <= 50:
            menu:
                "Unlock?"
                "Unlock" if True:
                    jump maledormsunlock
                "Back" if True:
                    pass
        jump postworldmap
    if morning == 1:
        scene bg maledorms
    elif True:
        scene bg maledormsnight
    call clothes from _call_clothes_35
    show mce happy
    with d
    "There's not a lot for me to do here, but..."
    menu mdm1:
        "Sexual Desire: [sd], Shame: [shame]"
        "Visit Boyfriend" if boyfriend == 1:
            if morning == 1:
                scene bg bedroomday
            elif True:
                scene bg bedroomnight
            call clothes from _call_clothes_87
            show mce happy
            show crushb:
                xpos 1200
            show crushe happy:
                xpos 1200
            with d
            if nude == 1:
                crush "W-Wow, [mc], you're uhm... n-naked!"
            elif lewdoutfit == 1:
                crush "O-Ohh, you came here dressed like that? Is it for the reason I think it is?"
            elif True:
                crush "Hey, [mc], thanks for coming."
            menu:
                "Sexual Desire: [sd], Affection for [crush]: [ca]"
                "Play Games." if True:
                    show crushe laughing:
                        xpos 1200
                    with d
                    "We spend a few hours playing Smash together until I return home to eat dinner."
                    "You felt a little closer to your [crush] after spending some time with him."
                    $ ca += 1
                    play sound success
                    "(+1 [crush] Affection)"
                "Study" if True:
                    show mce laughing
                    show crushb:
                        xpos 1200
                    show crushe happy:
                        xpos 1200
                    with d
                    "We spend a few hours studying together until I return home to eat dinner."
                    "You felt a little closer to your [crush] after spending some time with him."
                    $ ca += 1
                    $ smarts += 1
                    play sound success
                    "(+1 [crush] Affection, +[fsmarts] Smarts)"
                "Act Flirtacious. (5 Sexual Desire, 1 [crush] Affection)" if True:
                    if sd < 5 or ca < 1:
                        "It's still a little early for that kind of behaviour. I need to build some rapport first."
                        jump crushmenu1
                    $ sdgain = 1
                    call sdgain from _call_sdgain_160
                    $ ca += 1
                    show crushb:
                        xpos 1200
                    show crushe horny:
                        xpos 1200
                    with d
                    "I spend a few hours acting interested and flirty with my crush. He seems to reciprocate!"
                    "You felt a little closer to your crush after spending some time with him."
                    play sound success
                    "(+[fsd] Sexual Desire, +1 [crush] Affection)"
                "Seduce (15 Sexual Desire, 2 [crush] Affection)" if True:
                    if sd < 15 or ca < 2:
                        "I'm not quite ready for that, and I don't think he'd be either."
                        jump crushmenu1
                    show mce horny
                    show crushe horny
                    with d
                    "What are we going to do on the bed, [crush]?"
                    menu csm2:
                        "Sexual Desire: [sd], [crush] Affection: [ca]"
                        "Make-Out Session (15 Sexual Desire, 2 [crush] Affection)" if True:
                            if sd < 15 or ca < 2:
                                "I'm not quite ready for that, and I don't think he'd be either."
                                jump csm2
                            scene bg bed with d
                            "My crush and I spend about an hour making out and some conversation inbetween."
                            "At times, I can feel his erection against my hips."
                            "And when he rubs my body, sometimes he'd get extra frisky as he teasingly grazes around my waist and hips."
                            "It turns me on so much."
                            play sound success
                            $ sdgain = 1
                            call sdgain from _call_sdgain_161
                            $ ca += 1
                            "(+[fsd] Sexual Desire, +1 Crush Affection)"
                            jump postworktrans
                        "Blowjob (25 Sexual Desire, 3 [crush] Affection)" if True:
                            if sd < 25 or ca < 3:
                                "I'm not quite ready for that, and I don't think he'd be either."
                                jump csm2
                            play music action
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
                            "My [crush] lays back and I soon have his erection in my hands. Curiously, I wrap my lips around the tip and swirl my toungue around the glans."
                            mc "Mmphh... Sho biiigg..."
                            "I take a hand and begin to jerk it up and down, mixing that with my tongue is sure to make him feel good."
                            "Then I slip my spare hand between my legs and slide my pantyhose down so I can rub my damp panties."
                            mc "Ooohhh... That's good... *Slurp, lick*"
                            "Speeding up, I keep up my handjob and tongue motions until I can feel his cock swell up."
                            play sound cum
                            show lyingblowjob 2 with cum
                            play sound cum
                            show lyingblowjob 2 with cum
                            "His entire body visibly tenses for a moment before a surge of hot cum erupts into my mouth."
                            play sound cum
                            show lyingblowjob 2 with cum
                            play sound cum
                            show lyingblowjob 2 with cum
                            "Several loads hit the back of my throat which I graciously swallow."
                            "It didn't taste great, but damn was it arousing; my pussy is soaked."
                            "I spend the next few moments lazily cleaning his cock with my tongue before it becomes fully unerect."
                            play sound success
                            $ sdgain = 1
                            call sdgain from _call_sdgain_162
                            $ blowjobs += 1
                            $ ca += 2
                            "(+[fsd] Sexual Desire, +2 Crush Affection)"
                            "We spend the rest of about an hour chatting before he returns to the male dorms."
                            jump postworktrans
                        "Vaginal Sex (40 Sexual Desire, 4 [crush] Affection)" if True:
                            if sd < 40 or ca < 4:
                                "I'm not quite ready for that, and I don't think he'd be either."
                                jump csm2
                            $ condomon = 0
                            $ crushsex = 1
                            if pregnancyshowing == 0:
                                $ condomon = 1
                                "Wear a condom?"
                                menu crushsexmenu2:
                                    "Your Crush has some condoms, so don't worry about your own stash!"
                                    "Yup!" if True:
                                        $ condomon = 1
                                    "Nah." if True:
                                        if boyfriend == 1:
                                            $ condomon = 0
                                            $ crushunsafesex = 1
                                        elif True:
                                            "Your [crush] refuses. Maybe if the circumstances were right he'd change his mind."
                                            jump crushsexmenu2
                            play music action
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
                            if condomon == 1:
                                "My [crush] puts on a condom and I coo in anticipation as he taps the tip of his cock against my wet pussy."
                            elif True:
                                "My [crush] kneels behind me and I coo in anticipation as he taps the tip of his cock against my wet pussy."
                            "On my knees, I thrust my butt against him and beckon for him to take me."
                            "As he pushes the tip inside me, he pushes forward and slides deeper into my soaking wet insides."
                            play ambience sex
                            play sound cum
                            show doggystylesex 2
                            with d
                            if virgin == 0:
                                "And just like that, my [crush] takes my virginity!"
                            mc "Ahhh, your cock feels so good..."
                            "He begins thrusting back and forth, slowly sliding his cock almost all the way out before sinking back in."
                            "These deep thrusts drive me wild as they grind against sensitive erogenous zones deep inside of me."
                            mc "Haaahh, mmmmpphhh... Right there, keep going!"
                            "Making me feel even better, he starts to thrust faster while reaching down to rub my clit."
                            "The pleasure overwhelmed me, turning my mind blank as my body trembled towards a potent orgasm."
                            mc "Ahhh, it's so good! I-I'm gonna, aahhh... Ahhhh!"
                            "I tightly grip the bedsheets as I climax, my pussy tightening around my [crush]'s throbbing cock."
                            "And he only speeds up, motivated by my climax, he pushes towards his own."
                            play sound cum
                            if condomon == 1:
                                show doggystylesex 2 with cum
                            elif True:
                                show doggystylesex 3 with cum
                            play sound cum
                            play sound cum
                            if condomon == 1:
                                show doggystylesex 2 with cum
                            elif True:
                                show doggystylesex 3 with cum
                            if condomon == 1:
                                "His tight cock explodes a hot load which accumulates in the tip condom as he ravishes me"
                            elif True:
                                "His tight cock explodes a hot load deep into my pussy as he ravishes me"
                            play sound cum
                            if condomon == 1:
                                show doggystylesex 2 with cum
                            elif True:
                                show doggystylesex 3 with cum
                            play sound cum
                            play sound cum
                            if condomon == 1:
                                show doggystylesex 2 with cum
                            elif True:
                                show doggystylesex 3 with cum
                            "I bounce my butt against his hips, and both of us fuck in rhythm together as we indulge the last moments of our euphoric orgasms."
                            play sound cum
                            if condomon == 1:
                                show doggystylesex 1 with d
                                "Ahhh... As he pulls out, I let out a satisfied sigh."
                            elif True:
                                show doggystylesex 4 with d
                                "Ahhh... As he pulls out, several droplets of cum seep out my well-fucked pussy and drip down my pelvis and thighs."
                            if condomon == 1:
                                "Thanks to the condom, I don't need to worry about getting pregnant."
                            elif True:
                                call pregnancyroll from _call_pregnancyroll_21
                            scene bg black with d
                            stop ambience
                            "My [crush] and I spend the rest of our time snuggling and having some post-sex discussion."
                            if virgin == 0:
                                "For my first time, that wasn't bad at all! I really liked being able to share such a special moment with my [crush]."
                                $ virgin = 1
                            play sound success
                            $ status += 1
                            $ sdgain = 1
                            call sdgain from _call_sdgain_163
                            $ ca += 2
                            $ vaginalsexes += 1
                            "(+[fsd] Sexual Desire, +2 Crush Affection)"
                            jump postworktrans
                        "Anal Sex (40 Sexual Desire, 4 [crush] Affection)" if qanalqueen == 1:
                            if sd < 40 or ca < 4:
                                "I'm not quite ready for that, and I don't think he'd be either."
                                jump csm2
                            "(Anal Queen) Your high desire for anal has convinced your crush to partake!"
                            jump crushanalsex2
                        "Anal Sex (50 Sexual Desire, 5 [crush] Affection)" if qanalqueen == 0:
                            if sd < 50 or ca < 5:
                                "I'm not quite ready for that, and I don't think he'd be either."
                                jump csm2
                            label crushanalsex2:
                                pass
                            play music action
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
                            "I coo in anticipation as my [crush] taps the tip of his cock against my wet pussy. He slides it up and down, collecting a generous amount of my wetness before he presses the tip against my butt."
                            "On my knees, I thrust my butt against him and beckon for him to take me."
                            "As he pushes the tip inside me, he pushes forward and slides deeper into my tight pucker."
                            play sound cum
                            show doggystylesex a2
                            with d
                            mc "Ahhh, your cock feels so good..."
                            "He pushes deeper, going gently as to let me slowly adjust to his thick girth."
                            play ambience sex
                            "Once I've eased up, he begins thrusting back and forth, slowly sliding his cock almost all the way out before sinking back in."
                            "These deep thrusts drive me wild as they grind deep inside of me."
                            mc "Haaahh, mmmmpphhh... It feels pretty good, ahhh keep going!"
                            "Making me feel even better, he starts to thrust faster while reaching down to rub my clit, and that extra stimulation really helps push me over the edge."
                            "The sensations begin to overwhelm me. My mind blanks, and my body shivers as my orgasm begins to swell up."
                            mc "Ahhh, it's really going to make me come! I-I'm gonna, aahhh... Ahhhh!"
                            "I bite my lip and grip the bedsheets as I come, my ass squeezing around my [crush]'s throbbing cock needily."
                            "And he only speeds up, motivated by my climax, he pushes towards his own."
                            play sound cum
                            show doggystylesex a3 with cum
                            play sound cum
                            show doggystylesex a3 with cum
                            "His thick cock shoots several hot loads deep into my ass as he pounds me"
                            play sound cum
                            show doggystylesex a3 with cum
                            play sound cum
                            show doggystylesex a3 with cum
                            "I bounce my butt against his hips, both of us lustfully making love as we make the most of our blissful orgasms."
                            play sound cum
                            show doggystylesex a4 with d
                            "Ahhh... As he pulls out, several droplets of cum seep out my well-fucked ass and drip down my pelvis and thighs."
                            scene bg black with d
                            stop ambience
                            "My [crush] and I spend the rest of our time snuggling and having some post-sex discussion."
                            play sound success
                            $ status += 1
                            $ sdgain = 1
                            call sdgain from _call_sdgain_164
                            $ ca += 2
                            $ analsexes += 1
                            "(+[fsd] Sexual Desire, +2 Crush Affection)"
                            jump postworktrans
                        "Nothing?" if True:
                            "I chicken out, and we just decide to chat instead. It's still a cheerful conversation. I'm glad he's so understanding."
                            jump postworktrans
                "Ask him to be your boyfriend. (5 [crush] Affection)" if boyfriend == 0:
                    if ca < 5:
                        "I think he'd decline if I asked so early."
                        jump crushmenu1
                    "(By upgrading your crush to your boyfriend, you can now spend Fridays with him as well as Mondays.)"
                    "(There may also be other hidden aspects to this relationship that you'll have to discover yourself.)"
                    "Finally I shoot my shot!"
                    mc "Crush! Will you please be my boyfriend?"
                    "..."
                    if pregnancyshowing == 1:
                        "While he is somewhat cautious of my pregnancy..."
                    play sound success
                    "He said yes! It's official! I have a boyfriend!"
                    $ crush = "Boyfriend"
                    $ boyfriend = 1
                    scene bg black with d
                    "We use the opportunity to go somewhere nice together, we have lunch at a nearby restaurant before returning to our dorms."
                    jump postworktrans
                "Break up with him (Permanent)" if boyfriend == 1:
                    scene bg black with d
                    $ boyfriend = 0
                    "Although I feel bad, I feel like this would be for the best..."
                    "The breakup is a little difficult, but we both take it quite well in the moment before returning to our respective dorms for a little cry."
                    $ crush = "Friend"
                    "We'll still be friends though, of course!"
                    jump postworktrans
            jump postworktrans
        "Prostitution Options (50 Sexual Desire, <50 Shame)" if True:
            if sd < 50 or shame > 50:
                "I'm not whoring myself out."
                jump mdm1
            "I think it'll be easy to find someone interested."
            $ money1 = 40
            $ money2 = 80
            $ money3 = 90
            call moneycalculate from _call_moneycalculate_1
            menu:
                "Sexual Desire: [sd], Shame: [shame]"
                "Offer a Blowjob for $[fmoney1]" if True:
                    stop music
                    scene bg black with d
                    "I find a target and soon bring him home..."
                    label maledormblowjob:
                        pass
                    $ mdbj = 1
                    play music action
                    play sound equip
                    scene bg bedroomnight with d
                    call clothesnude from _call_clothesnude_53
                    show mce laughing
                    with d
                    mc "Just seat on the bed, and I'll blow your mind..."
                    "Shamelessly, I kneel down before my customer as he takes out his half-erection."
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
                    show povblowjob 2 with cum
                    play sound cum
                    show povblowjob 2 with cum
                    "Mmphh, yesss! His cock unloads several hot jets of cum straight into the back of my mouth."
                    play sound cum
                    show povblowjob 2 with cum
                    play sound cum
                    show povblowjob 2 with cum
                    "Load after load, I struggle to swallow it all. Some of it seeps outwards, dripping on my chin and face."
                    stop ambience
                    "I finish up the job, and he withdraws his rapidly shrinking cock."
                    $ blowjobs += 1
                    $ sdgain = 1
                    $ shameloss = 1
                    call sdgain from _call_sdgain_165
                    call shameloss from _call_shameloss_117
                    play sound success
                    "(+[fsd] Sexual Desire, -[fshame] Shame.)"
                    scene bg bedroomnight with d
                    call clothesnude from _call_clothesnude_54
                    show mce horny
                    with d
                    mc "I hope you enjoyed my service!"
                    $ moneygain = 40
                    call moneygain from _call_moneygain_76
                    play sound success
                    "(+$[fmoney])"
                    scene bg black with d
                    "My customer leaves, returning to the male dorms."
                    jump postworktrans
                "Offer Vaginal for $[fmoney2] (75 Sexual Desire, <25 Shame)" if True:
                    if sd < 75 or shame > 25:
                        "I don't think I'm quite ready to do that with a stranger yet."
                        jump mdm1
                    stop music
                    $ mdsex = 1
                    scene bg black with d
                    "I find a target and soon bring him home..."
                    play music action
                    play sound equip
                    scene bg bedroomnight with d
                    call clothesnude from _call_clothesnude_55
                    show mce laughing
                    with d
                    mc "Mmphh, I can't wait for you to ravage my pussy..."
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
                    show sittingsex v2
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
                    show sittingsex v2
                    "I tightly grip the bedsheets as I climax, my pussy tightening around my partner's throbbing cock."
                    "And he only speeds up, motivated by my climax, he pushes towards his own."
                    play sound cum
                    show sittingsex v3 with cum
                    play sound cum
                    show sittingsex v3 with cum
                    "His tight cock explodes a hot load deep into my pussy as he ravishes me"
                    play sound cum
                    show sittingsex v3 with cum
                    play sound cum
                    show sittingsex v3 with cum
                    "I roll my hips back and forth needily as we both fuck in rhythm together, indulging the last moments of our euphoric orgasms."
                    play sound cum
                    show sittingsex 4 with d
                    stop ambience fadeout 3.0
                    "Ahhh... As he pulls out, several droplets of cum seep out my well-fucked pussy and drip down my pelvis and thighs."
                    if condomon == 1 and pregnancyshowing == 0:
                        "But thanks to the condom, I don't need to worry about getting pregnant."
                    elif True:
                        call pregnancyroll from _call_pregnancyroll_22
                    scene bg bedroomnight with d
                    call clothesnude from _call_clothesnude_56
                    show mce horny
                    with d
                    mc "I hope you enjoyed my service!"
                    scene bg black with d
                    $ sdgain = 1
                    call sdgain from _call_sdgain_166
                    $ shameloss = 1
                    call shameloss from _call_shameloss_118
                    "(+[fsd] Sexual Desire, -[fshame] Shame)"
                    if qsecretlydepraved == 1:
                        "The enjoyment of a depraved act causes you to gain an additional [fsd] sexual desire!"
                        call sdgain from _call_sdgain_167
                    $ status += 1
                    $ vaginalsexes += 1
                    $ moneygain = 80
                    call moneygain from _call_moneygain_77
                    play sound success
                    "(+$[fmoney])"
                    scene bg black with d
                    "My customer leaves, returning to the male dorms."
                    jump postworktrans
                "Offer Anal for $[fmoney3] (85 Sexual Desire, <20 Shame)" if qanalqueen == 0:
                    if sd < 85 or shame > 20:
                        "I don't think I'm quite ready to do that with a stranger yet."
                        jump mdm1
                    label dormanalprostitution:
                        pass
                    stop music
                    $ mdsex = 1
                    scene bg black with d
                    "I find a target and soon bring him home..."
                    play music action
                    play sound equip
                    scene bg bedroomnight with d
                    call clothesnude from _call_clothesnude_57
                    show mce laughing
                    with d
                    mc "I have some lube in my bedside draw, think you can apply it for me?"
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
                    "I get into position with confidence, lifting my leg to expose both my dripping wet pussy and my tight ass."
                    "As the customer watches, he strokes his cock to erection. He takes some lube and gently applies it to my pucker."
                    mc "Mmphh, I'm ready for that fat cock now... Hehe."
                    "With my butt held high, I teasingly wiggle it while and spreading my cheeks."
                    play sound cum
                    play ambience sex fadein 2.0
                    show sittingsex a2 with d
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
                    show sittingsex a2
                    with cum
                    "As my pussy contracts, my ass clenches too, squeezing around my customer's tense cock as I climax."
                    "And as my ass squeezees and milks his cock, he only speeds up. Motivated by my climax, he pushes towards his own."
                    play sound cum
                    show sittingsex a3 with cum
                    play sound cum
                    show sittingsex a3 with cum
                    "His tight cock explodes a hot load deep into my ass as he ravishes me"
                    play sound cum
                    show sittingsex a3 with cum
                    play sound cum
                    show sittingsex a3 with cum
                    "I roll my hips back and forth needily as we both fuck in rhythm together, indulging the last moments of our euphoric orgasms."
                    play sound cum
                    show sittingsex 4 with d
                    stop ambience fadeout 3.0
                    "Ahhh... As he pulls out, several droplets of cum seep out my well-fucked butt and drip down."
                    scene bg black with d
                    scene bg bedroomnight with d
                    call clothesnude from _call_clothesnude_58
                    show mce horny
                    with d
                    mc "Mmm, that was so good! Do you want to clean up in the shower with me? I have an ensuite!"
                    scene bg black with d
                    "After an unknown amount of time, my customer leaves."
                    play sound success
                    $ sdgain = 1
                    call sdgain from _call_sdgain_168
                    $ shameloss = 1
                    call shameloss from _call_shameloss_119
                    "(+[fsd] Sexual Desire, -[fshame] Shame)"
                    if qsecretlydepraved == 1:
                        "The enjoyment of a depraved act causes you to gain an additional [fsd] sexual desire!"
                        call sdgain from _call_sdgain_169
                    $ moneygain = 90
                    call moneygain from _call_moneygain_78
                    play sound success
                    "(+$[fmoney])"
                    $ status += 1
                    $ analsexes += 1
                    jump postworktrans
                "Offer Anal for $[fmoney3] (75 Sexual Desire, <25 Shame)" if qanalqueen == 1:
                    jump dormanalprostitution
                "Back" if True:
                    jump mdm1
        "Leave" if True:
            jump worldmap

init:
    $ mdsex = 0
    $ mdbj = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
