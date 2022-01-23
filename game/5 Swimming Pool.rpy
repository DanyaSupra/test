label pool:
    $ tinamet = 1
    play music girls
    scene bg pool with d
    if swimmingpoolintro == 0:
        $ swimmingpoolintro = 1
        call clothes from _call_clothes_23
        show mce happy
        with d
        "Ahh, what a gorgeous pool! And thanks to a partnership with the university, I can swim here for free, whenever I want!"
        "Bloody better be able to too! I pay $18,000 a year for this!"
        if swimsuit == 0:
            "Oh crap, I don't have a swimsuit! I better go to the shops later and buy a good one that can last for a few years."
        elif clothes == 11:
            "But I'm all ready in my swimsuit!"
        elif True:
            "I'll just need to head into the changing rooms to put my swimsuit on."
        unknown "Ahoy, classmate! Lovely day for a dip!"
        "Oh? It's..."
        scene bg pool
        show tinacloseup
        with d
        python:
            tina = renpy.input("Name the Mollusk Girl. Leave blank for the default name 'Tina'.")
            tina = tina.strip()
            if not tina:
                tina = "Tina"
        scene bg pool
        call clothes from _call_clothes_24
        show mce happy
        show tinao bikini:
            xpos 1200
        show tinae happy:
            xpos 1200
        with d
        mc "Ahh, [tina]! How's it going?"
        "A student from my class, not one I'm super close with yet, but as a gastropod girl she stands out like crazy."
        "Ahh, she's kinda hot in her swimsuit too."
        tina "Yeahh, I'm the lifeguard here! Not bad, eh?"
        mc "Oohh, I'm not very good at swimming. I have the 'floating' part down though, hahah!"
        show tinae laughing with d
        tina "Haha, good one!"
        tina "It's actually pretty quiet here, so I actually spend a lot of time training and relaxing rather than lifeguarding. I could show you a thing or two."
        mc "I'd appreciate that!"
        show tinae horny with d
        tina "Hehe, it's like a date, then!"
        hide tinab
        hide tinae
        hide tinao
        with d
        if swimsuit == 0:
            "Ooohh, I really need to get a swimsuit now!"
            jump worldmap
    elif swimsuit == 0:
        call clothes from _call_clothes_25
        show mce happy
        with d
        "While I can gawk at [tina]'s abs while I'm here, I really ought to buy a swimsuit before I go in the water."
        jump worldmap
    elif True:
        call clothesbeach from _call_clothesbeach_15
        show mce happy
        with d
        "I'm all ready to get wet!"
        menu pm1:
            "Hang out with [tina]" if True:
                jump tinaroute
            "Swim on your own" if True:
                jump soloswim
            "Back" if True:
                jump worldmap

jump worldmap

label tinaroute:
    if tinaroute1 == 0:
        jump tinaroute1
    elif tinaroute2 == 0:
        jump tinaroute2
    elif True:
        jump tinaroute3

label tinaroute1:
    "Come to think of it, where is she?"
    "I know the pool is empty, but shouldn't she be on lifeguard duty right now?"
    "Hmm, maybe she's in one of these changing huts. Unlike the changing rooms, they're just a quick place for individuals."
    "I take a peek at the one behind her usual guard post, and..."
    play music action
    show tinavoyeur1b
    show tinavoyeur1 1
    with d
    "O-Oh my gosh!"
    tina "Stick it in, stick it in!"
    "She's in there with someone else!"
    menu tr1m1:
        "Keep watching! (25 Sexual Desire, <75 Shame)" if True:
            if sd < 25 or shame > 75:
                "I shouldn't!"
                jump tr1m1
            $ tinaroute1 = 1
            label tinadoggy:
                pass
            "I continue peeking from behind the curtain, and I see a guy get behind [tina]."
            "He surveys every inch of her cute, pink body while biting his lip and preparing his cock."
            play sound cum
            show tinavoyeur1 2 with d
            tina "Aahhh, yesss!"
            "As the thick cock pushes deep inside, a look of satisfaction spreads across [tina]'s face."
            play ambience sex fadein 3.0
            "With one hand on her ass, she spreads her butt as she takes the cock like a pornstar."
            "Her partner grinds back and forth, really spreading her lips as they tightly grip around the shaft. It's an incredible sight."
            "He starts thrusting quickly, and [tina]'s pussy reacts by squeezing so tightly it slows him down."
            tina "Unnphh, so huuuge! Ahhhnn!"
            "Her sopping wet pussy does slowly spread after a while, allowing the man to really pummel her insides."
            "Just watching is starting to make me feel hot and wet between my legs. I can't believe I'm really seeing something like this."
            "As moans leak from [tina]'s mouth with each thrust, it would seem she's getting closer by the second."
            "With my eyes keenly watching the connection between [tina]'s and her partner's sexes, I can't help but slip my hand under my bikini. I make sure no one can see me as I begin to rub my pussy."
            tina "Aaahhh, ooohhh, I'm almost there!"
            "Her cheeks flush red as she begins to lustfully sway her hips."
            "The man groans as his cock swells up, and [tina]'s orgasming pussy clenches around his cock."
            play sound cum
            show tinavoyeur1 3 with cum
            "Finally! An eruption of hot cum seeps from their point of connection. The duet of orgasms causes [tina] to moan even louder, her pussy squeezing tighter."
            play sound cum
            show tinavoyeur1 3 with cum
            "An extreme amount of cum drips and splats everywhere it can as the two continue fucking for an extended amount of time."
            "I hadn't even realized I was rubbing my pussy quite fast, I was even close to my own orgasm, but... I don't think I'll be able to finish."
            show tinavoyeur1 4 with d
            stop ambience
            "As predicted, they begin to finish up, as the male pulls his thick cock out of [tina]'s pussy."
            tina "Aahhh, that was perfect... Same thing next time? Hehe."
            "Now would be a good time to slip away undetected."
            if trr == 1:
                jump tr3mp
            scene bg pool
            call clothesbeach from _call_clothesbeach_16
            show mce happy
            with d
            "Phew, that was kinda hot..."
            play sound success
            $ sdgain = 1
            $ shameloss = 1
            $ masturbations += 1
            $ voyeurisms += 1
            call sdgain from _call_sdgain_91
            call shameloss from _call_shameloss_32
            "(+[fsd] Sexual Desire, -[fshame] Shame)"
            scene bg black with d
            "Thirty minutes later..."
            scene bg pool
            call clothesbeach from _call_clothesbeach_17
            show mce happy
            with d
            "Ahh, the water feels good on my skin. I'd built up quite a sweat masturbating, heh."
            show tinao bikini:
                xpos 1200
            show tinae happy:
                xpos 1200
            with d
            tina "Leaving already?"
            mc "Yeah, I've got some work to catch up on at home."
            show tinae horny with d
            tina "Heh, maybe you should join in next time."
            show mce neutral with d
            mc "Huh?!"
            show mce horny with d
            "How embarrassing for her to have seen me watching!"
            hide tinab
            hide tinae
            hide tinao
            with d
            "She giggles to herself and leaves me with a wink."
            "I'm glad she doesn't seem to mind."
        "Stop watching!" if True:
            if personality == 2 and shame < 75 and sd > 25:
                "(Always Horny) I can't stop watching! It's good juicy!"
                jump tr1m1
            scene bg pool
            call clothesbeach from _call_clothesbeach_18
            show mce happy
            with d
            "I can't watch that! It's a total breach in trust."
            "Phew, that was kinda hot though..."
            play sound success
            $ sdgain = 1
            call sdgain from _call_sdgain_92
            "(+[fsd] Sexual Desire)"
    jump postworktrans
label tinaroute2:
    "[tina] disappeared again… And I think I know exactly where she is, because I saw her chatting with the same guy from before!"
    "The changing hut behind her guard post catches my eye again, it’s closed tight."
    menu tr2m:
        "Go and peek! (30 Sexual Desire, <70 Shame)" if True:
            if sd < 30 or shame > 70:
                "Watching someone have sex? It's too shameless."
                jump tr2m
            $ tinaroute2 = 1
            label tinafrontal:
                pass
            play music action
            "She knew I was watching last time, and seemed to be okay with it. There’s no harm in a peek, right?"
            show tinavoyeur2b
            show tinavoyeur2 1
            with d
            tina "Mmmphhh, I’m always so wet around you."
            "There she is- ahh, this is such a lewd position! I can see everything!"
            play sound cum
            show tinavoyeur2 2
            with d
            "The same man as before peels back her shear thong and starts to teasingly rub her clit. I can feel my own tingle just by watching."
            "No part of [tina] goes untouched, as the man fully indulges in every detail and pleasure of [tina]’s fine ass. God, I wish that was me."
            "And then with his thick cock, he starts to tap it on her tight ass, preparing to take the next step."
            menu:
                "I see him press his cock against her pussy. (Vaginal)" if True:
                    $ hole = "pussy"
                    play sound cum
                    show tinavoyeur2 v3
                    with d
                "I see him press his cock against her anus. (Anal)" if True:
                    $ hole = "ass"
                    play sound cum
                    show tinavoyeur2 a3
                    with d
            play sound2 foreplay1 fadein 3.0
            tina "Yeesss, aahhh!"
            "A satisfied look spreads across [tina]’s face as the thick cock pushes deep inside of her [hole]."
            play ambience sex fadein 3.0
            "The man begins to thrust his hips back and forth, each full thrust creating a satisfying thwap as his hips connect with her pink, bubble butt."
            "The tightness of her [hole] around his member is intense, I can’t keep my eyes off it."
            "Her [hole] squeezes rhythmically, almost purposely, and so tightly that it causes the man’s thrusting to briefly slow down as they almost play a game of sexual tug of war."
            tina "Mmphh, you handle me pretty well, big boy, ahah, aahhh…"
            "I wonder if she gets off on having sex in such a daring location? And am I getting off on just watching this like a voyeur? What a complicated situation."
            "[tina]’s [hole] slowly begins to yield, spreading more and allowing the man to pound at a faster pace."
            "This is even lewder than last time, and I have a much better view. I grow tempted to rub my pussy again as I watch, barely resisting the urge due to the risk of being seen by some of the swimmers."
            tina "Mphh, I’m close!"
            "She lustfully grinds her hips back and forth, ineffective from her position maybe, but her entire body milks the man’s cock for every drop of pleasure possible as she reaches for her orgasm."
            tina "Aahhh, keep going! I’m gonna- aahh, gonna come!"
            "Her [hole] contracts as she orgasms, tightening and clenching around his cock, pushing him over the edge too."
            play sound cum
            if hole == "ass":
                show tinavoyeur2 a4 with cum
            elif True:
                show tinavoyeur2 v4 with cum
            "The result is a pair of simultaneous orgasms as [tina] takes the complete creampie with any protection, hot cum pouring deep inside her."
            play sound cum
            if hole == "ass":
                show tinavoyeur2 a4 with cum
            elif True:
                show tinavoyeur2 v4 with cum
            stop ambience fadeout 3.0
            stop sound2 fadeout 3.0
            "The two continue to fuck throughout the entire climax, causing the cum to bubble and splatter at their point of connection."
            play sound cum
            show tinavoyeur2 5 with d
            "It isn’t until they both grow weary and sensitive that he pulls out with several more loads of cum splattering hre thighs, breasts and even hair."
            tina "Mmpphh, look at all this mess you made… "
            tina "I don't think I'll ever be able to get enough."
            "I think that’s my que to disappear!"
            if trr == 1:
                jump tr3mp
            scene bg pool
            call clothesbeach from _call_clothesbeach_19
            show mce horny
            with d
            "Slipping away, I get back into the pool before they leave, I even make an effort to not make eye contact as [tina] and her secret lover leave the hut."
            show tinao bikini:
                xpos 1200
            show tinae happy:
                xpos 1200
            with d
            "That doesn’t stop a giggling [tina] from approaching me and sitting beside the pool, her legs swinging back and forth."
            tina "Sooo, what do you think? He’s cute, isn’t he?"
            menu:
                "He’s okay, I guess." if True:
                    show mce laughing
                    show tinae laughing
                    with d
                    tina "Hehe, so you were watching again."
                    mc "Uh, oh!"
                "Not my type!" if True:
                    show mce laughing
                    show tinae laughing
                    with d
                    tina "Awwhh, really? The sex is gooood, you shouldn’t knock it."
                    "It did look very good…"
                "What do you mean? (Innocent whistling)" if True:
                    show mce laughing
                    show tinae laughing
                    with d
                    tina "Hahaha, no need to be so coy, I already said you’d be welcome to join us."
            show mce neutral
            show tinae horny
            with d
            tina "How about next time you just… knock and ask to come in?"
            show mce happy2 with d
            mc "How often exactly are you fucking this guy in the changing hut?!"
            show tinae happy with d
            tina "We’re both swimmers, so it’s just convenient to do it during my break!"
            show mce laughing with d
            mc "Every day? [tina]!"
            show tinae neutral with d
            tina "Heeyy, keep your voice down, hahah. It’s fun, trust me!"
            show mce horny with d
            if sd >= 80:
                mc "I don’t need to trust you there; I already know it’s fun. If I catch you again, I’ll definitely join in!"
            elif True:
                mc "I’ll think about it…"
            play sound success
            $ sdgain = 1
            $ shameloss = 1
            $ voyeurisms += 1
            call sdgain from _call_sdgain_140
            call shameloss from _call_shameloss_103
            "(+[fsd] Sexual Desire, -[fshame] Shame)"
            jump postworktrans
        "Just wait for her to finish" if True:
            jump pm1
label tinaroute3:
    show tinao bikini:
        xpos 1200
    show tinae happy:
        xpos 1200
    with d
    tina "Heyy, me and my man were thinking about going into the changing huts for a quickie in five minutes."
    tina "I’m not gonna ask if you want to come, I’ll simply tell you that and leave the information to stew, haha."
    hide tinab
    hide tinae
    hide tinao
    show mce neutral
    with d
    mc "H-Hey-"
    mc "Ahh, she already left…"
    show mce horny with d
    "I guess I’ll…"
    menu tr3m:
        "Voyeur 1 (Doggystyle)" if True:
            $ trr = 1
            play music action
            scene tinavoyeur1b
            show tinavoyeur1 1
            with d
            jump tinadoggy
        "Voyeur 2 (Frontal Vaginal/Anal)" if True:
            play music action
            $ trr = 1
            jump tinafrontal
        "Threesome (80 Sexual Desire)" if True:
            if sd < 80:
                "I'm not comfortable doing that, yet."
                jump tr3m
            jump tinaroute4
        "Back" if True:
            jump pm1
    label tr3mp:
        play sound success
        $ sdgain = 1
        $ shameloss = 1
        $ voyeurisms += 1
        call sdgain from _call_sdgain_141
        call shameloss from _call_shameloss_104
        "(+[fsd] Sexual Desire, -[fshame] Shame)"
    jump postworktrans
label tinaroute4:
    $ tinaroute4 = 1
    show mce laughing with d
    "Alright, fuck it! I’ll take her offer and join her!"
    scene bg hut
    "I step into the changing hut and already find a very naked [tina] strutting her stuff."
    call clothesbeach from _call_clothesbeach_20
    show mce happy
    show tinao bikini:
        xpos 1200
    show tinae happy:
        xpos 1200
    show student4:
        xpos 50
    with d
    tina "Oohh, look at that, Thad, I told you we’d have a guest!"
    thad "Hey, you [tina]'s friend?"
    mc "H-Hello! I’m [mc], and I guess I’m here to join you, ehehe."
    tina "Strip ‘er!"
    play sound equip
    hide mco
    show mce horny
    show tinao bikini:
        linear 1.0 xpos 1100
    show tinae horny:
        linear 1.0 xpos 1100
    show student4:
        linear 1.0 xpos 150
    with d
    "The guy I watched [tina] have sex with twice before pulls my bikini top off in one smooth move, while [tina] goes for the bottoms."
    mc "Eep, you’re tag-teaming me!"
    tina "That’s the plan, haha…"
    scene bg black with d
    "…"
    play music action
    play sound2 foreplay1
    show tinathreesomeb
    if tan == 1:
        show tinathreesomebtan
    if hair == 1:
        show tinathreesomeh black
    if hair == 2:
        show tinathreesomeh blonde
    show tinathreesome 1
    with d
    "*Spread, squish*"
    tina "Mmphh, such a pretty, pink pussy! What do you think, Thad?"
    thad "I’d say her ass is good enough to rival yours, [tina]!"
    tina "Ohoh, those are fighting words! Buuut, you miiight be right…"
    mc "S-Such a lewd pose… *Pant*"
    "I look back expectantly as the man jacks his cock to full erection. [tina] doesn’t just spread and toy with my pussy, but also wiggles my butt enthusiastically."
    $ condomon = 0
    if condoms > 0 and pregnancyshowing == 0:
        tina "Wanna use a condom? I think it feels better without, personally!"
        menu:
            "Use a condom? Condoms: [condoms]. [fertilityrate]."
            "Yeah." if True:
                $ condomon = 1
                $ condoms -= 1
            "Fuck the rules! (Without protection!)" if True:
                $ condomon = 0
    play sound cum
    show tinathreesome 2 with d
    "With his cock ready to go, Thad positions it at my pussy and slowly pushes forward. Easily sinking inside, my lips grip and squeeze around every inch of the shaft."
    call virgin from _call_virgin_7
    mc "Aaahhh, aahhh…"
    "My whole body reacts with a shiver of pleasure, culminating in a loud moan that escapes my mouth. I quickly realize that I shouldn’t be moaning when only a thin cloth separates me and the swimming pool, and quickly close my mouth."
    tina "Oohh, such cuuute moans! And you took such a large cock so easily, mm…"
    play ambience sex fadein 2.0
    "[tina] bites her lip as she watches the man and I fuck. My hips move too, as the cock comfortably slides back and forth in my pussy."
    "I’m already so wet, there’s something about this situation that’s really getting me off!"
    "Is it that I’m being watched? Is it the thrill of getting caught? Is it the culmination of watching these two fuck like rabbits and finally getting to join in?"
    "I don’t know, but my pussy is absolutely throbbing with pleasure and desire."
    "We both speed up slightly, me rocking my hips while Thad pistons his hips into me. Every time our bodies meet there’s a satisfying thwap sound along with my stifled moans."
    "This cock feels astounding in my pussy right now, it’s overwhelming my senses."
    "It won’t take me long to cum at all, I might even come once or twice before he finishes inside."
    "And that’s around the time [tina] starts toying with my clit in addition to her spreading. This drives me absolutely wild, my back arching and my entire body trembling."
    "This is every bit as good as I imagined, letting both a girl and guy toy with me to their heart’s content!"
    "His thick cock begins to swell up as my mind and body are overwhelmed with orgasmic euphoria."
    play sound cum
    show tinathreesome 3 with cum
    "With my pussy rhythmically contracting around the cock, I manage to milk him for all he’s worth as he unloads inside me."
    play sound cum
    show tinathreesome 3 with cum
    "My vision turns white and my muscles grow tense as I reach the peak of my climax. The pleasure is indescribable."
    stop ambience fadeout 2.0
    stop sound2 fadeout 2.0
    tina "Damn, stud! Leave some for me, mmm…."
    play sound cum
    show tinathreesome 4 with d
    "Pulling out, copious amounts of cum oozes from my pussy, he must have really enjoyed it."
    mc "Phew… So much…"
    mc "Well… Time to team-up on [tina]? Hehe…"
    call pregnancyroll from _call_pregnancyroll_10
    $ status += 2
    $ vaginalsexes += 1
    $ groupsexes += 1
    play sound success
    $ sdgain = 1
    $ shameloss = 1
    call sdgain from _call_sdgain_142
    call shameloss from _call_shameloss_105
    "(+[fsd] Sexual Desire, -[fshame] Shame!)"
    scene bg pool with d
    "After ten more minutes of fooling around in the hut, I finish off by swimming a little."
    jump postworktrans
label soloswim:
    scene bg pool
    "Dipping into the water, a refreshing warmth hits me."
    "Aaahhh... That's nice."
    scene bg black with d
    "Afterwards..."
    scene bg pool with d
    call clothesbeach from _call_clothesbeach_21
    show mce happy
    with d
    show student4 with d:
        xpos 50
    "I noticed this student kept peeking at me, he must see something he likes."
    stu "Uuhhm, uhh, hey! I just wanted to say you're really cute..."
    "Awwhh, he's shy! I guess that'd make me the top for once."
    menu psm1:
        "Sexual Desire: [sd], Shame: [shame]."
        "Tease him. (20 Sexual Desire)" if True:
            if sd < 20:
                "Naahhh, I'm too shy to do that."
                jump psm1
            mc "Awwhh, you're such a cutie... Maybe think about me tonight while you're all alone? Hehe, I'll think about you too."
            stu "*Gulp* I will!"
            "I walk off to the changing rooms, and while I don't look back, I can feel his gaze on my butt as I catwalk away."
            scene bg black with d
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_93
            call shameloss from _call_shameloss_34
            play sound success
            "(+[fsd] Sexual Desire, -[fshame] Shame!)"
        "Flash him. (45 Sexual Desire, <75 Shame)" if True:
            if sd < 45 or shame > 75:
                "Out here? No way!"
                jump psm1
            play sound equip
            show mco swimsuitflash with d
            mc "Ahh, whoops! My bikini just came off!"
            stu "W-Woaahh! Amazing!"
            mc "Teehee, don't tell anyone you saw them! I haven't shown anyone my breasts before."
            "I wink and hurry to the changing rooms while covering myself."
            scene bg black with d
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_94
            call shameloss from _call_shameloss_63
            play sound success
            $ soloswimflash = 1
            "(+[fsd] Sexual Desire, -[fshame] Shame!)"
        "Fuck him in the changing rooms. (80 Sexual Desire, <45 Shame)" if True:
            if sd < 80 or shame > 45:
                "Fucking a stranger just because he thinks I'm cute? I haven't fallen that far, have I?"
                jump psm1
            mc "Heyy, you should come with me if you really think I'm that cute, hehe..."
            "I take him by his hand, and before he can fully process a reaction, he's already coming along with me into the male's changing rooms."
            stu "B-But, this is the male changing rooms!"
            scene bg changingrooms with d
            mc "It's also empty, heh... Here."
            play music action
            show masturbation3b
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
            if pregnancyshowing == 1:
                show masturbation3e pregnant
            with d
            "Slipping off my bikini with extreme ease, my already wet pussy is immediately on display for my shy partner."
            mc "Maybe this'll give you some confidence, hmm?"
            play sound cum
            "*Rub, rub, schlick*"
            "As predicted, arousal displaces any remnants of shyness as he drops his swimming trunks and begins to jack his already throbbing cock off."
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
            show masturbation3 2 with d
            "Pressing his erection against my wet pussy, he gradually slides in causing me to coo."
            if virgin == 0:
                $ virgin = 1
                "Not a bad way to lose my virginity! Although it does feel a tiny bit like a waste."
            mc "Oohhh, you're surprisingly thick! It's really filling me up."
            play ambience sex fadein 3.0
            "My partner groans with pleasure, still too shy to really say anything, but his actions say enough as his hips begin to move."
            "My pussy squeezes and sucks around his large cock, it's such a tight fit that I can really feel every bump and ridge as it moves through me."
            show masturbation3face 2
            if tan == 1:
                show masturbation3face 2tan
            with d
            mc "Mmphhh, you should go faster! Someone could come in any minute."
            "He nods, squeezing my hips for leverage as he pushes all the way in and begins to pound back and forth like a spring."
            hide masturbation3face with d
            mc "Aahhh, yesss! Just like that! Sooo deep..."
            "I moan with delight every time the tip reaches the deeper, sensitive spots within my pussy."
            "The student pumps his waist with all his might as he gazes in awe at my body, taking particular delight in the way my breasts bounce with each thrust."
            show masturbation3face 2
            if tan == 1:
                show masturbation3face 2tan
            with d
            mc "More, I-I'm nearly there! Fuck me hard!"
            "Sweating and panting, he focuses all his effort into his movements. I can't help but grin as the sense of power both arouses and empowers me. This, feels, amazing."
            "And, it's going to make me come, really hard!"
            hide masturbation3face with d
            mc "That's it! Ahhh, yesss! Keep going like that! Ahh, aahh!"
            "My hips unconsciously try to match my lover's thrusts, in almost a synced movement. At the peak of our rutting, my pussy begins to tighten as I climax."
            "And my contracting pussy squeezes and clenches around his throbbing cock, pushing him past his limit as he cries out."
            play sound cum
            show masturbation3 3 with cum
            mc "Ooohhh! Yessshhh... Fill me up..."
            play sound cum
            show masturbation3 3 with cum
            pause 0.2
            play sound cum
            show masturbation3 3 with cum
            stop ambience fadeout 2.0
            "Within an instance, a tremendous amount of cum floods through my pussy with such aggression that a lot of it seeps and splurts out."
            mc "Ahhhaaahh, yessss!"
            "My orgasm continues for a little longer, leaving me in a blissful daze as my body grows numb."
            show masturbation3 4 with d
            "Exhausted, my partner pulls out and staggers back. His body must have not been quite prepared for such a quick, and sudden situation, but I'm the better for it."
            show masturbation3face 2
            if tan == 1:
                show masturbation3face 2tan
            with d
            mc "Haahh, look at this mess you made..."
            stu "*Pant, pant* Haahhh, you're like an angel..."
            mc "I suppose if I were to be a mythological creature, a succubus would be an accurate choice right now."
            "I playfully toy with the cum dripping out of my pussy for a few moments."
            "Then I stand up and slip my bikini on in such a way that it stops the cum from dripping out."
            scene bg changingrooms
            call clothesbeach from _call_clothesbeach_22
            show mce horny
            show student4:
                xpos 50
            with d
            mc "Aahh, whoops! I think I came into the wrong changing rooms."
            stu "Hehe, yeah, 'came' is accurate."
            mc "Heh, see you around campus. Don't be afraid to say hi!"
            "I give him one last wink before I return to the female changing rooms."
            scene bg black with d
            $ sdgain = 1
            $ shameloss = 1
            $ status +=1
            $ vaginalsexes += 1
            $ soloswimfuck = 1
            call sdgain from _call_sdgain_95
            call shameloss from _call_shameloss_64
            play sound success
            "(+[fsd] Sexual Desire, -[fshame] Shame!)"
        "Pass him" if True:
            if personality == 2 and sd > 20:
                "(Always Horny) I should do at least something!"
                jump psm1
            pass
    jump postworktrans

init:
    $ soloswimflash = 0
    $ soloswimfuck = 0
    $ swimmingpoolintro = 0
    $ tinaroute1 = 0
    $ tinaroute2 = 0
    $ tinaroute4 = 0
    $ hole = "pussy"
    $ trr = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
