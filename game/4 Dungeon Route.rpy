label dungeon:
    if dungeonunlocked == 0:
        "Unlock this location by having >50 Sexual Desire"
        if sd >= 50:
            menu:
                "Unlock?"
                "Unlock" if True:
                    jump dungeonunlock
                "Back" if True:
                    pass
        jump postworldmap
    elif True:
        if dungeonintro == 0:
            jump dungeonintro
        elif True:
            play music dungeon
            jump dungeonaltstart
label dungeonintro:
    $ dungeonintro = 1
    stop ambience fadeout 3.0
    stop music fadeout 3.0
    call clothes from _call_clothes_82
    show mce neutral
    with d
    "Is this the right place? Next to a music store, in the alleyway of a retail district, sits a lone dilapidated door. The address is indeed correct."
    "I send [mika] a text, she quickly replies ‘come in’, and a buzz indicates the door is now open."
    "Opening the door, an immediate staircase to a basement level is revealed, signifying that this is the lower floor to the music store this building belongs to."
    scene bg dungeon
    call clothes from _call_clothes_83
    show mce happy
    with d
    "Despite the dilapidated exterior, the interior is a contrast between cold, stone walls, and warm, thoughtful décor."
    "This is more than just a dungeon, it’s evident that this is also where [mika] lives."
    play music dungeon
    show mikab:
        xpos 1200
    show mikao dom:
        xpos 1200
    show mikae happy:
        xpos 1200
    with d
    mika "Hiya! How’s it hanging?"
    show mce horny with d
    mc "Oh my god."
    show mikae horny with d
    mika "Perfect timing! We were just about to start a rope workshop. Want to be my bunny?"
    "I look around the room and there are about three others, oddly enough, with one of them being a girl, we actually outnumber the two men. That’s a surprise for sure."
    show mce happy with d
    mc "Shouldn’t I get an introduction, or something?"
    show mikae laughing with d
    mika "Don’t sweat it, we can introduce you after you’ve been tied up!"
    if nude == 0:
        show mikae horny with d
        mika "That being said, what we’re about to do is best enjoyed in the nude."
    elif lewdoutfit == 1:
        show mikae horny with d
        mika "Looking sexy, by the way, but I think for this next trick you’d do best completely nude. I wouldn’t want the ropes damaging your clothes."
        show mce neutral with d
        mc "What about my skin?"
        mika "Haha, a little bit of damage is part of the fun."
    elif True:
        show mikae horny with d
        mika "I’d ask you to get undressed, but you came completely nude. You’re far more extreme than I anticipated!"
        show mce laughing with d
        mc "Heyy, you’re not so subtle either with your getup!"
    show mce happy with d
    show mikae laughing with d
    mika "Bunnies, undress!"
    "Without another word, the other girl in the room giggles as she slips off her clothing, exposing her completely in front of everyone else."
    show mikae horny with d
    mika "You can handle this much, right? I handpicked you because I knew you could!"
    "Gulp, I guess she’s not wrong!"
    menu:
        "Join In" if nude == 1:
            pass
        "Undress (50 Sexual Desire, <60 Shame)" if nude == 0:
            if sd < 50 or shame > 60:
                "In front of all these people? I'm too embarrassed!"
            "I shrug playfully and begin to undress."
        "Chicken Out!" if True:
            show mce neutral with d
            mc "Sorry, this is all a bit much, and sudden for me! Can I just sit this one out, and maybe watch?"
            show mikae happy with d
            mika "Of course, I understand. We won’t make you do anything you’re uncomfortable with."
            scene bg dungeon with d
            "The other bunny happily takes my place, and I get a chance to watch and learn more about the dungeon."
            "With a better understanding of what to expect, I’m slightly more open to joining in next time."
            play sound success
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_156
            call shameloss from _call_shameloss_114
            "(+[fsd] Sexual Desire, -[fsd] Shame)"
            jump postworktrans
    jump dungeonshibari1

label dungeonaltstart:
    if dungeonroute2 == 1 and dungeonroute3 == 0:
        jump dungeonsuspended
    scene bg dungeon
    call clothes from _call_clothes_84
    show mce happy
    show mikab:
        xpos 1200
    show mikao dom:
        xpos 1200
    show mikae happy:
        xpos 1200
    with d
    mika "Hiya, [mc]! Shall we get kinky?"
    menu dasm:
        "Sexual Desire: [sd], Shame: [shame]."
        "Nude Shibari (50 Sexual Desire, <60 Shame)" if True:
            if sd < 50 or shame > 60:
                "I probably shouldn't get too involved, I'm too shy for that."
                jump dasm
            jump dungeonshibari1
        "Shibari Sex (70 Sexual Desire, <30 Shame)" if dungeonroute1 == 1:
            if sd < 70 or shame > 30:
                "I probably shouldn't get too involved, I'm too shy for that."
                jump dasm
            jump dungeonshibari2
        "Suspended Bunny" if dungeonroute3 == 1:
            jump dungeonsuspended
        "Back" if True:
            jump worldmap
label dungeonshibari1:
    stop ambience
    $ dungeonroute1 = 1
    scene bg dungeon
    play sound equip
    call clothesnude from _call_clothesnude_49
    show mce horny
    show mikab:
        xpos 1200
    show mikao dom:
        xpos 1200
    show mikae happy:
        xpos 1200
    with d
    mika "It’ll be just you and me… The other bunny will be well looked after by the boys here, feel free to watch."
    mc "Okay, where do you want me?"
    show mikae horny with d
    mika "Lie down here, and legs up!"
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
    "Getting into position, with a mixture of humour and embarrassment, I lift my legs up and expose my pussy to the room. Not unlike the other bunny as she begins to get tied up."
    "I’m next, as [mika] quickly ties my thighs to my shins, and then my arms, and then my breasts, and even my pelvis!"
    play sound equip
    show shibari 2 with d
    "Expertly, I’m completely tied up within minutes, and unable to move an inch."
    show shibari 3 with d
    mc "Hehehe, this is pretty hot."
    mika "Look here, your pussy is all wet…"
    show shibari 2 with d
    "I shiver slightly as [mika] playfully pushes the rope against my clit."
    mika "Are you enjoying the show?"
    "It’s impossible to say I hadn’t notice, as my eyes were transfixed on the other bunny getting spit roasted in the corner."
    mika "That could be you, what do you think about that?"
    "[mika] whispers her words, all whilst teasing my clit more and more through the rope."
    show shibari 3 with d
    mc "Mmphh… It doesn’t seem so bad…"
    "I wiggle, growing hot and bothered as my pussy gets wet and drippy."
    mika "Looks like they’re finishing. Why don’t I untie you and let you go chat with them?"
    show shibari 2 with d
    mc "Haahh, okay…"
    scene bg dungeon
    play sound equip
    call clothes from _call_clothes_85
    show mce horny
    show mikab:
        xpos 1200
    show mikao dom:
        xpos 1200
    show mikae happy:
        xpos 1200
    with d
    if nude == 0:
        "Finally untying me, I redress."
    elif True:
        "Finally untied, I stand back up, still completely nude."
    show mikae laughing
    show mce laughing
    with d
    "I spend some time chatting with the others, and getting to know them better. It’s a nice club, and I'm eager to see what kind of trouble I can get up to in here."
    "Or maybe, get up to soon…"
    hide mikae
    hide mikab
    hide mikao
    with d
    play sound success
    $ sdgain = 1
    $ shameloss = 1
    call sdgain from _call_sdgain_157
    call shameloss from _call_shameloss_115
    "(+[fsd] Sexual Desire, -[fsd] Shame)"
    show student5 with d:
        xpos 1200
    "Feeling hot and horny, I recognize an opportunity to flirt with one of the men, as they mention that they need to walk back home the same direction as me."
    menu genm1:
        "Seduce and Fuck (70 Sexual Desire, <30 Shame)" if True:
            if sd < 70 or shame > 30:
                "I'm horny, but I'm not so needy that I'd have sex with a stranger."
                jump genm1
            "Mmphh, I’m too horny not to… Okay, I’m going to do it!"
            stop music fadeout 1.0
            scene bg black with d
            "A little bit of seduction later..."
            play music action
            jump clubvaginalsex
        "Go Home Alone" if True:
            if personality == 2 and sd > 80 and shame < 20:
                "(Always Horny) I'm too horny not to!"
            "I’m horny, but I can deal that with myself."
            jump postworktrans

label dungeonshibari2:
    stop ambience
    show mikae horny with d
    mika "For today, I’ll let you choose your partner. Needless to say, whoever you choose is probably going to fuck you!"
    menu:
        "Mika (Vaginal with Strap-On)" if True:
            $ lesbian += 1
            show mikae laughing with d
            mika "Mmh, I won’t hold back. I’ll come at you and fuck you as good and hard as any man."
            show mce horny with d
            mc "Challenge accepted!"
            $ gv = 1
        "Male (Vaginal)" if True:
            show mikae happy with d
            mika "Good choice! Here’s a condom, free on me!"
            $ condoms += 1
            show mce horny with d
            mc "Thank you, Mika. Have fun with the others."
            mika "Oh I will!"
            $ gv = 0
    play music action
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
    "Without shame, I lay down and readily raise my legs in preparation for the rope. My pussy is already noticeably dripping wet, and my partner takes note."
    if gv == 0:
        mp "Ohh, you’re so wet already. I can’t wait to sink my cock into that."
        mc "And I can’t wait for you to pound me."
    elif True:
        mika "Look how wet you are! Well, I’m not too surprised, I’m just as wet and ready too. I’m glad you ended up enjoying this so much."
        mc "Hehe, how could I not? It’s hot!"
    play sound equip
    show shibari 4
    with d
    "Fully tied up, I’m completely unable to move, and my lustful pussy is fully exposed to the open air."
    "I bite my lip, and beckon for my partner to take me, and they’re as eager as I am, as they quickly get into position."
    if gv == 1:
        "[mika] takes out a strap-on, featuring a bullet vibrator on the inside for her pleasure."
    elif True:
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
    if gv == 0:
        show shibari 5 with d
    elif True:
        show shibari 5s with d
    "They start by slipping the tip inside, then they pushing forward, sliding deep into my soaking wet insides."
    if virgin == 0:
        "Losing my virginity here isn’t bad at all! We’re all having a lot of fun."
        $ virgin = 1
    mc "Mmphh, that’s pretty big! But don’t go easy, hehe…"
    if gv == 1:
        mika "You know me well, let’s begin!"
    elif True:
        mp "There’s no way I could hold back with someone as beautiful as you."
    play ambience sex fadein 3.0
    play sound2 foreplay2 fadein 3.0
    "Thrusting back and forth, they pound me quick, and the thrusts go long and hard."
    "My entire body shakes, and squirms in response to the pleasure, but the ropes keep me tightly in place."
    "I can feel burning desire in my loins at the acknowledgement that I can’t move at all, I’m completely at the whim of my partner. They have all the power."
    "The cock goes deep, driving me wild as it hits all the deep sensitive spots, and the pleasure leads me towards a quick orgasm."
    "My mind turns blank, and my body trembles as I feel that euphoric release so soon into the session."
    "I don’t know whether it was the tying, or the environment, but this was one of my fastest orgasms from penetration."
    if gv == 1:
        mika "Well, aren’t you having fun? Hahaha, it feels pretty good for me too! The vibrator is really pressing against my clit, I can usually come after a few minutes."
    elif True:
        mp "Coming already? And I’m not even half-way done with you."
    "Haaahhh, could easily fit another orgasm in by the time they’re done."
    mc "Mmphh, well, you can go all out… I’ll come again anyway, I’m sure."
    "With that said, they speed up a lot, slapping into my ass and causing ripples."
    mc "Aaahhh, mmphhh… That’s it! Keep going…"
    "Almost as if they’re showing off, they also bring a thumb to my clit, and effortlessly hold it there. My non-stop squirming results in my clit constantly rubbing and grinding against the thumb, creating a most exquisite and overwhelming pleasure."
    "I can’t stop moaning, to the point where it’s even a little embarrassing when I realize the others in the room can hear me."
    "But I’m tied up, I can’t do anything, and that makes it so much hotter. I can already feel my second orgasm bubbling to the surface."
    if gv == 1:
        mika "Aaahh, ohhh, I-I’m close…"
        "[mika] is close too, our eyes close tightly as we’re both overwhelmed with the ecstasy of our simultaneous climaxes."
        play sound cum
        show shibari 6s with cum
        "A pump is activated, leading to thick, hot, gooey cum filling up my pussy from the strap-on dildo."
        play sound cum
        show shibari 6s with cum
    elif True:
        "I can feel my partner’s cock swell up and throb inside of me, he must be close too."
        play sound cum
        show shibari 6 with cum
        "And as my pussy clenches and milks him desperately, it doesn’t take long for him to unload several hot, sticky ropes of cum deep inside of me."
        play sound cum
        show shibari 6 with cum
    stop ambience fadeout 3.0
    stop sound2 fadeout 3.0
    "To the best of my ability, I roll my hips back and forth needily to get the most of my second orgasm."
    "Although as the peak of the pleasure fades, I’m eventually left weary and panting. Then, my partner pulls out."
    play sound cum
    show shibari 7 with cum
    if gv == 0:
        "Cum freely drips and seeps from my well-fucked pussy."
    elif True:
        "The fake cum drips freely from my tingly and well-fucked pussy. I couldn’t ask for anything more."
    mc "Mmphh, that was sooo good… Haahhh…"
    "Just as I go to move, the ropes hold me in place again, woops!"
    if gv == 0:
        mp "Haha, here, let me untie you."
    elif True:
        mika "Someone’s eager! Let me untie you first."
    scene bg dungeon
    play sound equip
    call clothesnude from _call_clothesnude_50
    show mce horny
    if gv == 1:
        show mikab:
            xpos 1200
        show mikao dom:
            xpos 1200
        show mikae happy:
            xpos 1200
    with d
    "Phew, my body is aching a little after being fucked like that. But I’d definitely do it again."
    "The rest of my time here is spent like just a group of friends chatting and messing around. It really is a nice club, I should come back again!"
    $ dungeonroute2 = 1
    $ status +=1
    $ vaginalsexes += 1
    play sound success
    "(+[fsd] Sexual Desire, -[fsd] Shame)"
    jump postworktrans
label dungeonsuspended:
    if dungeonroute3 == 0:
        stop ambience
        scene bg dungeon
        play sound equip
        call clothes from _call_clothes_86
        show mce horny
        show mikab:
            xpos 1200
        show mikao dom:
            xpos 1200
        show mikae happy:
            xpos 1200
        with d
        mika "I think it’s time you get the proper initiation into the club, [mc]."
        mc "Eh?! I’m not part of the club, yet?"
        show mikae horny with d
        mika "You aaareee, but you’re not really ‘one of us’, yet. There’s still one more thing we like to do before we consider a female member officially part of the club."
        mc "Okay, let me do it, then!"
        mika "Well… Maybe you ought to… Ah, nevermind."
        if nude == 0:
            mika "Undress, bunny."
            mc "Yes, mistress."
            play sound equip
            hide mco
            call clothesnude from _call_clothesnude_51
            with d
        elif True:
            mika "This is the part where I’d ask you to undress, but you’re honestly crazy for walking here naked."
            mc "Thank you, mistress, hehe."
    mika "Okay, everyone. Suspend her."
    if dungeonroute3 == 0:
        show mce neutral with d
        mc "Eh?!"
    mp2 "Yes mistress."
    scene bg black with d
    show suspendedb
    if tan == 1:
        show suspendedbtan
    if pregnancyshowing == 1:
        show suspendedbp
        if tan == 1:
            show suspendedbtanp
    if hair == 1:
        show suspendedh black
    if hair == 2:
        show suspendedh blonde
    if piercingson == 1:
        show suspendedpiercings
    show suspended 1
    with d
    "With some of the most complicated rope tying I’ve seen yet, I’m left fully suspended in the air, my legs and arms hog-tied back."
    "This is an even more oppressive restraint than last time."
    mika "First, your safe word is cucumber, secondly, you may choose your punishments."
    mika "Here are your options:"
    $ dungeonpunishments = 0
    $ dblindfold = 0
    $ dgag = 0
    $ dspanking = 0
    $ dwhipping = 0
    menu dungeonp1:
        "Blindfold" if dblindfold == 0:
            play sound equip
            show suspendedblindfold
            with d
            "With my punishment requested, a soft, fabric blindfold is wrapped around my face, completely obscuring my vision."
            mika "Hehe, that’s one of your most important senses gone."
            $ dblindfold = 1
            $ dungeonpunishments += 1
            jump dungeonp1
        "Gag" if dgag == 0:
            play sound equip
            show suspendedgag
            if tan == 1:
                show suspendedgag tan
            with d
            "With my punishment requested, a leather strap is placed around my cheeks, and a red ball is placed in my mouth."
            "The strap is tightened to such a degree that the ball is locked in place, preventing me from talking, or doing much else with my mouth."
            mika "Go ‘mmphh’ three times fast as your safe word, okay?"
            mc "Mmhm!"
            $ dgag = 1
            $ dungeonpunishments += 1
            jump dungeonp1
        "Nipple Piercings" if piercingson == 0:
            if piercings == 0:
                mika "This is quite a painful punishment, but I assure you that I’m a professional body piercer."
                "With some sharp pain, my nipples are pierced, and after the work a typical bar with two silver balls on each side is left, permanently marking my body."
                $ piercings = 1
            elif True:
                if dgag == 1:
                    mc "Mmphh, mmm!"
                    mika "Uhmm… Hang on, what are you saying?"
                    "Temporarily loosening my gag…"
                mc "My nipples are already pierced, I just don’t have them on right now."
                mika "Aahhh! In that case, let’s just put some bars in."
                if dgag == 1:
                    "My gag is tightened back up."
            $ piercingson = 1
            $ dungeonpunishments += 1
            show suspendedpiercings with d
            jump dungeonp1
        "Spanking" if dspanking == 0:
            play sound equip
            mika "I’ll make these cheeks nice and red."
            play sound spank
            show suspendedspanked with d
            "Sharply, [mika] slaps my ass with her main hand, causing my entire body to shudder with pleasure and pain."
            play sound spank
            "Not holding back, my next cheek is the target of [mika]’s second slap."
            play sound spank
            "For good measure, another two slaps are served on both cheeks, and then a final fifth and sixth to leave my ass red and raw… and my pussy, dripping and wet."
            $ dspanking = 1
            $ dungeonpunishments += 1
            jump dungeonp1
        "Whipping" if dspanking == 1 and dwhipping == 0:
            mika "How daring! We use a riding crop here, so while it will hurt, it won’t be utterly excruciating, hahaha…"
            show suspendedspanked 2 with d
            play sound whip
            "It strikes, hard and fast. I can’t help but moan at each impact."
            play sound whip
            "The pain aches through my body, but now as much as the burning desire and pleasure that builds up with each strike."
            play sound whip
            "The pain fades pretty quickly, only leaving a lasting erotic impression."
            $ dwhipping = 1
            $ dungeonpunishments += 1
            jump dungeonp1
        "Done Picking" if True:
            pass
    if dungeonpunishments >= 4:
        mika "You really are a sucker for punishments, aren’t you? Look how wet you are too, I bet you’d just melt if someone were to…"
        "Mika playfully brushes her riding crop around my pubic mound, causing my entire body to shiver with desire."
        mika "Hehehe, but you’re not done picking yet, there’s another stage…"
    elif dungeonpunishments >= 1:
        mika "Yes, that’s quite enough. You’re perfectly setup, wet and horny for the next stage."
        mika "Oh that’s right, it’s not over yet…"
    elif dungeonpunishments == 0:
        mika "No punishments? That’s okay too. There’s still one more stage that might entice you more."
    mika "You’ve chosen how you’re going to be served, now choose how you’re going to be fucked!"
    play music action
    menu:
        "Oral" if True:
            show suspended 2
            $ gv = 1
            $ blowjobs += 1
            $ status +=1
            mika "Hehe, just oral? It’s not like you’re a virgin. But I can’t complain, it’s your choice."
            "While I’m left suspended in mid-air, one of the male participants comes towards me, my eyes level with his pelvis as he takes his cock out."
            if dblindfold == 0:
                "It’s already half-erect, and honestly a bit of a monster cock even in this state. I’m excited."
            elif True:
                "While I can’t see, I can hear the sounds of him jacking it off in preparation."
            if dgag == 1:
                play sound equip
                hide suspendedgag
                "Removing my gag, it drops to the floor, leaving my mouth ready to be fucked."
            "And now fully erect, he lifts it with his hand and guides it towards my rosy lips."
            play sound cum
            show suspendedoral
            if tan == 1:
                show suspendedoral tan
            "As the tip of his cock presses against my mouth, I gently part my lips and accept it, my tongue lolling on the side as I do my best to take it."
            if blowjobs > 0:
                "Unlike my previous blowjobs, my involvement is a lot less necessary. This’ll be closer to a mouthfuck than anything."
            play sound2 oral1 fadein 2.0
            "And this is only evident by the amount of control he has, and how little control I have. With only my tongue to pleasure him, he is quick to slide deep, almost causing me to gag."
            play ambience sex fadein 3.0
            "And then pulling back, using the friction of my lips against his shaft almost like a pseudo-pussy, he begins to gently thrust back and forth."
            "It’s rough, and difficult to keep up with at first, but that only makes it hotter."
            "I do my best to involve my tongue, especially on his sensitive tip. I love the way it sometimes throbs and swells up in my mouth and I do my best to coax out this feeling."
            "At a gradually increasing pace, I eventually manage to bring him closer and closer. I hadn’t anticipated being able to make him cum like this, so I take pride with each of his groans."
            play sound cum
            show suspendedoral 2
            if tan == 1:
                show suspendedoral 2tan
            with cum
            "And before I know it, I feel something hot hit the back of my throat. Thick, warm loads of cum unloading, almost making me choke as I take it all in."
            play sound cum
            show suspendedoral 2 with cum
            "It’s excessive, and most of all, extremely hot."
            show suspendedoral 3 with d
        "Vaginal" if True:
            show suspended 2
            $ gv = 2
            $ vaginalsexes += 1
            $ status +=1
            mika "I bet your pussy is absolutely begging for a good cock right now. Well, boys, who gets the honour? Rock paper scissors for it?"
            "Damn… I can’t believe they’re actually playing rock paper scissors for my pussy."
            "The winner cheers as they approach my soaking wet behind. My pussy dripping excessively with desire."
            "No need for foreplay as my partner slips a condom on and already begins teasingly poking and prodding at my entrance."
            play sound cum
            show suspendedvaginal with d
            "And as he pushes inside, he easily slides to the deepest reaches of my soaking wet insides."
            play ambience sex
            if dgag == 0:
                mc "Mmmphhh, yeaahhh... That's good..."
                "I couldn't hold back my moans and excitement, especially as he began pumping back and forth."
            elif True:
                mc "Mmphh, mmmm... Mmphhh."
                "My moans were muffled by the gag as he began pumping back and forth."
            "I shiver and pant as his hips sway with increasing fervor, my pussy dripping its shimmering lubricants onto his shaft."
            "Completely unable to move, I can at best squeeze my internal muscles around his cock as he pounds me in a manner that can only be described as rough and primal."
            mc "Aaahhh, mmphhh..."
            "In this moment, suspended in the air, I've fully resigned myself to the carnal, wanting only to indulge in as much pleasure as possible, and without a shred of shame."
            "Admittedly I'm so horny and sensitive right now that it doesn't take long for me to come at all. However, suspended as I am, my pleasure is irrelevant in the face of my partner, who continues fucking me."
            "And my pussy only gets wetter and more sensitive as he keeps up his thrusts. His fingers digging into my ass as he seems to be getting closer."
            if dgag == 0:
                "I squeal in delight as I come again, my mind going completely blank as I drown in pleasure."
            elif True:
                "The gag muffles many moans as my mind going completely blank and I drown in pleasure."
            "My entire body shivers and shakes in orgasmic bliss, and my spasming pussy seems to bring my partner to his limit."
            play sound cum
            show suspendedvaginal 2
            hide suspendedbp
            hide suspendedbtanp
            if pregnancyshowing == 1:
                show suspendedbp
                if tan == 1:
                    show suspendedbtanp
            with cum
            "And in one instant, cum splatters from his cock, spilling into my pussy and overflowing it."
            play sound cum
            show suspendedvaginal 2 with cum
            "My mind is completely filled with a bright, fuzzy feeling of euphoria."
            "He continues to fuck out the rest of his orgasm until the sensitivity sets in."
            show suspendedvaginal 3 with d
        "Spitroast!" if True:
            show suspended 2
            $ gv = 3
            $ blowjobs ==1
            $ vaginalsexes +=1
            $ groupsexes +=1
            $ status +=2
            mika "Now that's what I'm talking about! A real show to watch today."
            "While I’m left suspended in mid-air, one of the male participants comes towards me, my eyes level with his pelvis as he takes his cock out."
            play sound equip
            hide suspendedgag with d
            "On the other side, there's no need for foreplay as my other partner slips a condom on and already begins teasingly poking and prodding at my entrance."
            "Both fully erect, the one infront lifts it with his hand and guides it towards my rosy lips."
            play sound2 blowjob fadein 3.0
            play sound cum
            show suspendedoral
            if tan == 1:
                show suspendedoral tan
            "As the tip of his cock presses against my mouth, I gently part my lips and accept it, my tongue lolling on the side as I do my best to take it."
            play sound cum
            show suspendedvaginal with d
            "And equally I feel the man behind me push inside of my pussy, he easily slides to the deepest reaches of my soaking wet insides."
            play ambience sex fadein 3.0
            "I shiver and pant as their hips begin to sway with increasing fervor, my pussy dripping its shimmering lubricants onto his shaft."
            "The one fucking my mouth uses the friction of my lips against his shaft almost like a pseudo-pussy, he begins to thrust back and forth."
            "It’s rough, and difficult to keep up with at first, but being fucked like this only makes it hotter."
            "I'm so horny and sensitive right now that it doesn't take long for me to come at all. However, suspended as I am, my pleasure is irrelevant in the face of my partners, who continue fucking me."
            "At a gradually increasing pace, I eventually manage to bring them closer and closer. The cock in my mouth swelling while the partner behind me digging his fingers into my ass."
            "And before I know it, I feel something hot hit the back of my throat. Thick, warm loads of cum unloading, almost making me choke as I take it all in."
            play sound cum
            show suspendedoral 2
            if tan == 1:
                show suspendedoral 2tan
            with cum
            "From behind, more cum spills into my pussy, overflowing it."
            play sound cum
            hide suspendedbp
            hide suspendedbtanp
            if pregnancyshowing == 1:
                show suspendedbp
                if tan == 1:
                    show suspendedbtanp
            show suspendedvaginal 2 with cum
            "It’s excessive, and most of all, extremely hot."
            play sound cum
            show suspendedvaginal 2 with cum
            "I come too, leaving my mind filled with a bright, fuzzy feeling of euphoria."
            show suspendedvaginal 3 with d
            show suspendedoral 3 with d
    stop ambience
    stop sound2
    "With all said and done, they grow flaccid and move back. Leaving me well-fucked, and covered in cum."
    "Phew… What an experience, if I wasn’t a little worn out, I’d definitely be horny enough to go again."
    mika "*Clapping* Excellent! That was so hot! You probably didn’t even notice the other Bunny and I having some fun in the back, but it was a remarkably fun show to watch."
    mc "S-Sooo, can I get down? Or at least wipe the cum off me, hahaha."
    play sound success
    $ sdgain = 1
    $ shameloss = 1
    call sdgain from _call_sdgain_158
    call shameloss from _call_shameloss_116
    "(+[fsd] Sexual Desire, -[fsd] Shame)"
    if qsecretlydepraved == 1:
        "The enjoyment of the depraved act causes you to gain an additional [fsd] sexual desire!"
        call sdgain from _call_sdgain_159
    if dungeonroute3 == 0:
        scene bg black with d
        "…"
        scene bg dungeon
        play sound equip
        call clothesnude from _call_clothesnude_52
        show mce horny
        show mikab:
            xpos 1200
        show mikao dom:
            xpos 1200
        show mikae happy:
            xpos 1200
        with d
        "Now officially a member of this quirky, kinky dungeon. I’m always welcome to join Mistress [mika] and her lewd antics."
        $ dungeonroute3 = 1
    jump postworktrans

init:
    $ dungeonroute1 = 0
    $ dungeonroute2 = 0
    $ dungeonroute3 = 0
    $ dblindfold = 0
    $ dgag = 0
    $ dspanking = 0
    $ dwhipping = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
