label lonelyfansroute:
    scene bg computer with d
    play music lonelyfans
    if lonelyfans3 == 0 or lonelyfans2 == 0 or lonelyfans1 == 0:
        menu lft1:
            "Sexual Desire: [sd], Shame: [shame]"
            "Upload Casual Clothing set (Free Slot!)" if lonelyfans1 == 0:
                jump lonelyfans1
            "Upload Underwear set (4 Sexual Desire, <98 Shame)" if lonelyfans2 == 0:
                if sd < 4 or shame > 98:
                    "I'm not quite mentally prepared to do it yet. Let's start with something a little more... mellow?"
                    jump lft1
                jump lonelyfans2
            "Upload Feet set?! (8 Sexual Desire, <95 Shame)" if lonelyfans3 == 0:
                if sd < 8 or shame > 95:
                    "I suppose feet would be a logical step if I'm keeping my clothes on, but I'm not comfortable with the idea of doing it quite yet."
                    jump lft1
                jump lonelyfans3
            "Tier 2 unlocked after all pictures taken" if True:
                jump lft1
            "View your previous pictures" if True:
                jump lonelyfansgallery
            "Back" if True:
                jump computermenu
    elif lonelyfans4 == 0 or lonelyfans5 == 0 or lonelyfans6 == 0:
        menu lft2:
            "Sexual Desire: [sd], Shame: [shame]"
            "Upload Sexy Underwear set (12 Sexual Desire, <90 Shame)" if lonelyfans4 == 0:
                if sd < 12 or shame > 90:
                    "I'm not ready to go that far yet."
                    jump lft2
                jump lonelyfans4
            "Upload Braless (15 Sexual Desire, <85 Shame)" if lonelyfans5 == 0:
                if sd < 15 or shame > 85:
                    "I'm not ready to go that far yet."
                    jump lft2
                jump lonelyfans5
            "Upload Nude set (20 Sexual Desire, <80 Shame)" if lonelyfans6 == 0:
                if sd < 20 or shame > 80:
                    "I'm not ready to go that far yet."
                    jump lft2
                jump lonelyfans6
            "Tier 3 unlocked after all pictures taken" if True:
                jump lft2
            "View your previous pictures" if True:
                jump lonelyfansgallery
            "Back" if True:
                jump computermenu
    elif lonelyfans7 == 0 or lonelyfans8 == 0 or lonelyfans9 == 0:
        menu lft3:
            "Sexual Desire: [sd], Shame: [shame]"
            "Nude Ass Focus Set (25 Sexual Desire, <75 Shame)" if lonelyfans7 == 0:
                if sd < 25 or shame > 75:
                    "I'm not ready to go that far yet."
                    jump lft3
                $ lonelyfans7 = 1
                jump lonelyfans7
            "Pussy Focus Set (30 Sexual Desire, <70 Shame)" if lonelyfans8 == 0:
                if sd < 30 or shame > 70:
                    "I'm not ready to go that far yet."
                    jump lft3
                $ lonelyfans8 = 1
                jump lonelyfans8
            "Masturbating Set (35 Sexual Desire, <65 Shame)" if lonelyfans9 == 0:
                if sd < 35 or shame > 65:
                    "I'm not ready to go that far yet."
                    jump lft3
                $ lonelyfans9 = 1
                jump lonelyfans9
            "View your previous pictures" if True:
                jump lonelyfansgallery
            "Back" if True:
                jump computermenu
    elif lonelyfans10 == 0 or lonelyfans11 == 0 or lonelyfans12 == 0:
        menu lft4:
            "Sexual Desire: [sd], Shame: [shame]"
            "Vibe Set (Vibrator, 38 Sexual Desire and <62 Shame)" if lonelyfans10 == 0:
                if sd < 38 or shame > 62:
                    "I'm not ready to go that far yet."
                    jump lft4
                if vibrator == 0:
                    "I don't have a vibrator, I can buy one at the shopping centre."
                    jump lft4
                $ lonelyfans10 = 1
                jump lonelyfans10
            "Camisole Set (Camisole, 40 Sexual Desire and <60 Shame)" if lonelyfans11 == 0:
                if sd < 40 or shame > 60:
                    "I'm not ready to go that far yet."
                    jump lft4
                if cami == 0:
                    "I don't have a camisole, I can buy one at the shopping centre."
                    jump lft4
                $ lonelyfans11 = 1
                jump lonelyfans11
            "Face Reveal Set (42 Sexual Desire and <58 Shame)" if lonelyfans12 == 0:
                if sd < 40 or shame > 60:
                    "I'm not ready to go that far yet."
                    jump lft4
                $ lonelyfans12 = 1
                jump lonelyfans12
            "View your previous pictures" if True:
                jump lonelyfansgallery
            "Back" if True:
                jump computermenu
    elif lonelyfans13 == 0 or lonelyfans14 == 0 or lonelyfans15 == 0:
        menu lft5:
            "Sexual Desire: [sd], Shame: [shame]"
            "Masturbation Video (45 Sexual Desire and <55 Shame)" if lonelyfans13 == 0:
                if sd < 45 or shame > 55:
                    "I'm not ready to go that far yet."
                    jump lft5
                $ lonelyfans13 = 1
                jump lonelyfans13
            "Dildo Set (Dildo, 48 Sexual Desire and <52 Shame)" if lonelyfans14 == 0:
                if sd < 48 or shame > 52:
                    "I'm not ready to go that yet."
                    jump lft5
                if dildo == 0:
                    "I don't have a dildo, I can buy one at the shopping centre."
                    jump lft5
                $ lonelyfans14 = 1
                jump lonelyfans14
            "Bunny Suit Set (Bunny Suit, 50 Sexual Desire and <50 Shame)" if lonelyfans15 == 0:
                if sd < 50 or shame > 50:
                    "I'm not ready to go that far yet."
                    jump lft5
                if bs == 0:
                    "I don't have a bunny suit, I can buy one at the shopping centre."
                    jump lft5
                $ lonelyfans15 = 1
                jump lonelyfans15
            "View your previous pictures" if True:
                jump lonelyfansgallery
            "Back" if True:
                jump computermenu
    elif lonelyfans16 == 0 or lonelyfans17 == 0 or lonelyfans18 == 0:
        menu lft6:
            "Sexual Desire: [sd], Shame: [shame]"
            "Cat Lingerie (Cat Lingerie, 55 Sexual Desire, <45 Shame)" if lonelyfans16 == 0:
                if sd < 55 or shame > 45:
                    "I'm not ready to go that far yet."
                    jump lft6
                if cgl == 0:
                    "I don't have any cat lingerie, I can buy some at the shopping centre."
                    jump lft6
                $ lonelyfans16 = 1
                jump lonelyfans16
            "Butt Plug (Butt Plug, 60 Sexual Desire, <40 Shame)" if lonelyfans17 == 0:
                if sd < 60 or shame > 40:
                    "I'm not ready to go that far yet."
                    jump lft6
                if plug == 0:
                    "I don't have a butt plug, I can buy one at the shopping centre."
                    jump lft6
                $ lonelyfans17 = 1
                jump lonelyfans17
            "Blowjob Set (65 Sexual Desire, <35 Shame)" if lonelyfans18 == 0:
                if sd < 65 or shame > 35:
                    "I'm not ready to go that far yet."
                    jump lft6
                $ lonelyfans18 = 1
                jump lonelyfans18
            "View your previous pictures" if True:
                jump lonelyfansgallery
            "Back" if True:
                jump computermenu
    elif lonelyfans19 == 0 or lonelyfans20 == 0 or lonelyfans21 == 0:
        menu lft7:
            "Sexual Desire: [sd], Shame: [shame]"
            "Sex Set (70 Sexual Desire, <30 Shame)" if lonelyfans19 == 0:
                if sd < 70 or shame > 30:
                    "I'm not ready to go that far yet."
                    jump lft7
                $ lonelyfans19 = 1
                jump lonelyfans19
            "Anal Set (75 Sexual Desire, <25 Shame)" if lonelyfans20 == 0:
                if sd < 75 or shame > 25:
                    "I'm not ready to go that far yet."
                    jump lft7
                $ lonelyfans20 = 1
                jump lonelyfans20
            "Double Penetration Set (80 Sexual Desire, <20 Shame)" if lonelyfans21 == 0:
                if sd < 80 or shame > 20:
                    "I'm not ready to go that far yet."
                    jump lft7
                $ lonelyfans21 = 1
                jump lonelyfans21
            "View your previous pictures" if True:
                jump lonelyfansgallery
            "Back" if True:
                jump computermenu
    elif True:
        menu lft8:
            "Sexual Desire: [sd], Shame: [shame]"
            "Fuck a Fan (+$$$) (100 Sexual Desire, 0 Shame)" if True:
                jump lonelyfans22
            "Upload Random Photoset (+$$)" if True:
                jump lonelyfans23
            "View your previous pictures" if True:
                jump lonelyfansgallery
            "Back" if True:
                jump computermenu
label lonelyfans24:
    pass
label lonelyfans23:
    scene bg bedroomnight with d
    play sound equip
    call clothesnude from _call_clothesnude_12
    show mce happy
    with d
    "Time for some lewd pictures, hmm..."
    $ rand = renpy.random.randint(1,5)
    if rand == 1:
        show lonelyfansb mirror
        show lonelyfans11a
        if pregnancyshowing == 1:
            show lonelyfans11ap
        if hair == 1:
            show lonelyfans11h black
        if hair == 2:
            show lonelyfans11h blonde
        if piercingson == 1:
            show lonelyfans11piercings
        with d
        ""
    elif rand == 2:
        show lonelyfansb mirror
        if pregnancyshowing == 1:
            show lonelyfans 13p
        elif True:
            show lonelyfans 13
        if hair == 1:
            show lonelyfans13h black
        if hair == 2:
            show lonelyfans13h blonde
        if piercingson == 1:
            show lonelyfans13piercings
        with d
        ""
    elif rand == 3:
        show lonelyfansb mirror
        if pregnancyshowing == 1:
            show lonelyfans 14p
        elif True:
            show lonelyfans 14
        if hair == 1:
            show lonelyfans14h black
        if hair == 2:
            show lonelyfans14h blonde
        if piercingson == 1:
            show lonelyfans14piercings

        with d
        ""
    elif rand == 4:
        show lonelyfansb mirror
        show lonelyfans 17
        with d
        ""
    elif rand == 5:
        scene lonelyfansb mirror
        show frombehindb
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
    "How about this?"
    play sound camera
    show lonelyfansb mirror with cum
    "Perfect!"
    "Checking my post's analytics..."
    $ photosets += 1
    $ moneygain = fol/11 - 2
    $ analsexes += 1
    $ status += 1
    call moneygain from _call_moneygain_70
    $ sdgain = 1
    call sdgain from _call_sdgain_143
    $ shameloss = 1
    call shameloss from _call_shameloss_106
    $ folgain = fol/10 + 1
    call folgain from _call_folgain_20
    play sound success
    "(+$[fmoney], +[ffol] Followers)"
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    jump postworktrans
label lonelyfans22:
    scene bg bedroomnight with d
    call clothescasual from _call_clothescasual_1
    show mce happy
    with d
    "I've been putting this off for a while now, but..."
    "For a large sum of money, I'll be willing to fuck a fan."
    "How much money can I get away with doing this? Just how much money is a fan willing to pay?"
    $ fold2 = fol/2
    "For now, I'll start the bid at [fold2], hehe..."
    show mce horny with d
    "Everyone that pays that much will be put into a raffle, and one winner will be drawn. Only the winner will get charged."
    "Then, I will privately meet with that individual."
    "The high price will easily allow me to get any train, but I won't go outside the country. Not too much of a concern since most fans speak the same language as me."
    "Wow, though... I know I'm not against sleeping around, but this feels quite special indeed."
    "Ohh, and I should make a set out of this! Wait, is that too far? What would my fans think? Oh fuck it, they're the ones having the opportunity to fuck me!"
    "If I show them what they could have got, if I show them what they missed, they'll bid even more aggressively next time."
    play music rest
    scene bg black with d
    "Later, after the bid."
    show bg bus with d
    call clothesclub from _call_clothesclub
    show mce happy
    with d
    "Just taking the bus to meet with the lucky winner!"
    "I'm even wearing my nicest lingerie."
    "He seems like a fairly decent guy too, just lonely."
    scene bg black with d
    play music action
    "Somewhere, in a stranger's house, far away from home..."
    scene bg house3 with d
    show frombehindb
    if tan == 1:
        show frombehindbtan
    if hair == 1:
        show frombehindh black
    if hair == 2:
        show frombehindh blonde
    show frombehind 1
    with d
    mc "Aahhh, Look how wet I am!"
    unknown "I can't beleive it's really you! In person! This is such a crazy experience."
    unknown "I've been waiting all day! I've even saved up some cum for it by not fapping."
    mc "Weeeellll... In that case, I guess I should use a condom, but..."
    $ condomon =  0
    if condoms == 0:
        mc "I don't have any, so whatever! Haha."
    if pregnancyshowing == 0:
        if condoms > 0:
            menu:
                "Condoms: [condoms]. [fertilityrate]."
                "Use a condom?" if True:
                    $ condoms -= 1
                    $ condomon = 1
                "Nah!" if True:
                    $ condomon =  0
    mc "Alright, I'm ready big boy! Put it in!"
    play sound cum
    show frombehind v2 with d
    "While presenting my ass, my new partner scurries between my legs. He positions his cock at my pussy, and slowly pushes forward, easily sinking inside."
    mc "Mmphhh, aaahhh... Not bad!"
    "My entire body shivers with pleasure, and I let escape a little moan to tease my partner."
    play ambience sex fadein 2.0
    play sound2 foreplay1 fadein 2.0
    "He starts to move his hips, his cock comfortably sliding back and forth inside me as I squeeze against his shaft. I'm so wet that as he pulls out, his cock is coated in a sheen of that wetness."
    unknown "Aahhh, incredible! T-Thank you, thank you!"
    mc "Hehe, get to it, lover-boy!"
    "Beginning to rock his hips, his hips enthusiastically slap against my butt creating a satisfying thwap sound which resounds with my moans."
    unknown "Aahh, your pussy feels amazing!"
    "I bite my lip and purposely tighten around his shaft. I can feel him swell up in response. This is driving me absolutely wild."
    "I can barely contain myself as my back arches and my body trembles. I was on the precipice of a full-body orgasm."
    "And then this twerp just had to go and start rubbing my clit!"
    mc "F-F.... F-Fuck!"
    "My moans are reduced to adorable squeaks as my hips buckle, and a strong orgasm consumes me. I think I even squirted a little."
    play sound cum
    show frombehind v3 with cum
    "Not too long after his cock tenses up as he begins to ejaculate inside me, cumming countless loads deep inside."
    play sound cum
    show frombehind v3 with cum
    stop ambience fadeout 3.0
    stop sound2 fadeout 3.0
    mc "Mmphh, yeaaaahhh, fill me up!"
    if condomon == 0:
        call pregnancyroll from _call_pregnancyroll_16
    "We pound out the remaining ecstasy, making sure to draw every drop of pleasure out of the act that we can."
    play sound cum
    show frombehind 4
    "And then, he pulls out, causing copious amounts of cum to ooze out of my pussy. Even I'm surprised by just how much there is."
    mc "Well... Let's take some pictures, shall we? Hehe..."
    unknown "Ohh, yes! I'll show everyone exactly what I did!"
    play sound camera
    show frombehind 4 with cum
    "He's going to brag about this for the rest of his life, I can tell."
    stop music fadeout 3.0
    scene bg black with d
    "Much later, at home."
    scene bg bedroomnight with d
    play sound equip
    call clothescasual from _call_clothescasual_2
    show mce horny
    with d
    $ photosets += 1
    $ vaginalsexes += 1
    $ status +=1
    $ moneygain = fold2
    call moneygain from _call_moneygain_71
    $ sdgain = 1
    call sdgain from _call_sdgain_144
    $ shameloss = 1
    call shameloss from _call_shameloss_107
    $ folgain = 70
    call folgain from _call_folgain_21
    play sound success
    "(+$[fmoney], +[ffol] Followers)"
    show mce laughing with sshake
    "F-Fuck, so much money... Heh, hahaha..."
    if persistent.lfscare == False:
        $ persistent.lfscare = True
        show red:
            alpha 0.1
        show mce laughing with sshake
        "Ahahahahaha."
        show red:
            alpha 0.2
        show mce laughing with sshake
        "Ahahahahaha."
        show red:
            alpha 0.3
        show mce laughing with sshake
        "Ahahahahaha."
        show red:
            alpha 0.4
        show mce laughing with sshake
        "And all I had to do was sell my soul."
    elif True:
        show mce neutral with d
        mc "There's no going back now."
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    if qsecretlydepraved == 1:
        call sdgain from _call_sdgain_180
        "(Secretly Depraved) And since you enjoyed the depraved act! (+1 Sexual Desire!)"
    jump postworktrans
label lonelyfans21:
    scene bg bedroomnight with d
    play sound equip
    call clothescasual from _call_clothescasual_3
    show mce happy
    with d
    "Hmm... Double penetration..."
    "I can't really ask my last partner for that. I feel like it'd be too weird to do it with him."
    "So, I need two new people..."
    show mce neutral with d
    "Eugh, where am I going to find two people?"
    show mce laughing with d
    "Wait! Those guys from the swimclub... Perfect."
    scene bg black with d
    "Later..."
    play music action
    play sound equip
    scene bg bedroomnight with d
    call clothesunderwear from _call_clothesunderwear
    show mce horny
    show student1:
        xpos 0
    show student2:
        xpos 1200
    with d
    "I drop several articles of clothing to the floor, one by one to the absolute awe of the onlookers."
    mc "Alright boys, any pictures you take, you get to keep! So why not take more than enough, and save your favourites later?"
    stua "What a deal!"
    stub "I'll take the camera, let's start!"
    play sound camera
    call clothesnude from _call_clothesnude_13
    with d
    stub "D-Damn... You're extremely sexy."
    "My loins are burning with desire, especially at the compliments. These guys aren't that different from my fans, maybe they even {i}are{/i} my fans."
    mc "You're not nervous, are you?"
    show student2:
        linear 1.0 xpos 1000
    play sound fondle
    "I take the second student's hand and place it on my breast, encouraging him to touch and caress me."
    show student1:
        linear 1.0 xpos 200
    play sound fondle
    "The other student takes the hint and begins to feel me up from behind too."
    mc "Well, boys, I'm wet and ready, so let's get to the main event."
    scene bg black with d
    play sound equip
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
    with d
    "Getting onto the bed, I readily expose my lustfully wet pussy."
    mc "Well... I have more than enough holes to accomodate you."
    mc "Don't be shy, now."
    $ condomon =  0
    if pregnancyshowing == 0:
        if condoms > 0:
            menu:
                "Condoms: [condoms]. [fertilityrate]."
                "Use a condom?" if True:
                    $ condoms -= 1
                    $ condomon = 1
                "Nah!" if True:
                    $ condomon =  0
    "The two boys hurriedly get undressed and position themselves in a way to tag-team me vaginally and anally."
    play sound cum
    show fmmthreesome 2
    with d
    if virgin == 0:
        $ virgin = 1
        call virgin from _call_virgin_8
        "What a crazy way to lose my virginity! I'm so glad I saved my first time for such a wild, memorable experience."
    play ambience doublepenetration
    play sound2 foreplay2
    "They both clumsily roll their hips back and forth, fucking me slowly as I adjust to the girth."
    "And damn, I really need to adjust to the girth! It's intense, but it's delightful. It's like I'm experiencing the best of both worlds."
    mc "Don't forget, ahhh, to take some pictures!"
    stub "R-Right."
    play sound camera
    show fmmthreesomeb with cum
    "The guy doing my vaginally takes a picture straight on, thankfully obscuring the other student and catching me at what is hopefully a picturesque angle."
    "The pleasure builds tremendously, spiralling me closer to an orgasm, faster than I could have ever imagined."
    play sound camera
    show fmmthreesomeb with cum
    "The two guys use me almost like a toy as they experiment and push themselves."
    mc "Ohh, you two are so fucking good! Keep it up!"
    "There's nothing but bliss and ecstasy until the two guys find a pace that enables them to push towards their orgasm."
    "Going back and forth in intervals, my pussy is filled, and them my ass, faster and faster..."
    play sound cum
    show fmmthreesome 3 with cum
    play sound cum
    show fmmthreesome 3 with cum
    "Until they both erupt in a glorious crescendo of euphoria as they simultaneously stuff both my holes full of hot cum."
    play sound cum
    show fmmthreesome 3 with cum
    play sound cum
    show fmmthreesome 3 with cum
    stop ambience fadeout 3.0
    stop sound2 fadeout 1.0
    "Another few blasts of cum are enough to make me come again, as the guys fuck until they go sensitive."
    play sound cum
    show fmmthreesome 4 with d
    "They both pull out, creating a messy mixture of cum and my juices."
    if condomon == 1:
        "Thanks to the condom, I don't need to worry about getting pregnant."
    elif True:
        call pregnancyroll from _call_pregnancyroll_17
    "We all take a moment to cooldown and catch our breath..."
    scene bg bedroomday
    call clothesnude from _call_clothesnude_14
    show mce happy
    show student1:
        xpos 0
    show student2:
        xpos 1200
    with d
    scene bg black with d
    "Later on..."
    scene bg bedroomnight with d
    play sound equip
    call clothescasual from _call_clothescasual_4
    show mce horny
    with d
    "Checking my statistics... W-Woah! The post blew up!"
    "'Remember when this was just a cute girl taking pictures in underwear'?"
    "'Haha, she become such a slut'."
    "'Who were those guys? BF? Fans?'"
    "'Look how far this whore went just to earn some money, what a world'."
    "Even the slightly harsh comments only excited me further."
    "So many people care about me, so many people are thinking about me."
    "This could be my career for the rest of my life, and I could retire early!"
    "I'm unstoppable!"
    $ photosets += 1
    $ moneygain = 200
    $ analsexes += 1
    $ status += 1
    call moneygain from _call_moneygain_72
    $ sdgain = 1
    call sdgain from _call_sdgain_146
    $ shameloss = 1
    call shameloss from _call_shameloss_108
    $ folgain = 250
    call folgain from _call_folgain_22
    play sound success
    "(+$[fmoney], +[ffol] Followers)"
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    jump postworktrans
    scene bg black with d
label lonelyfans20:
    scene bg bedroomnight with d
    play sound equip
    call clothesnude from _call_clothesnude_15
    show mce happy
    with d
    "Time for some butt stuff! I've been wearing my plug for a while as preparation."
    "I take out my phone and call the last guy I had take photos of me, I think it'll be easier if I just turn that into a friendship with benefits situation for now."
    "The benefits? Lots of money for me, hehehe."
    play music action fadein 3.0
    scene bg black with d
    show bg bedsex
    show buttupb
    if tan == 1:
        show buttupb tan
    if hair == 1:
        show buttuph black
    if hair == 2:
        show buttuph blonde
    show buttup 1
    with d
    mc "Is this a good pose? Take a few more."
    play sound camera
    show bg bedsex with cum
    mc "Good boy... I think I'll let you fuck me like this, how about it? I have some lube in my bedside."
    play sound2 foreplay1 fadein 2.0
    play ambience sex fadein 3.0
    play sound cum
    show buttup a2 with d
    "Fully lubricated, he presses his tip against my pucker, sinks inside and begins thrusting."
    mc "That's tiiight! Haaahh, in the best way possible..."
    play sound camera
    show bg bedsex with cum
    mc "Yesss! Take pictures of my slutty butt!"
    play sound camera
    show bg bedsex with cum
    mc "Mmmpphhh... Perfect..."
    "An underrated aspect of taking these photosets is that it makes the sex a lot more stimulating for me."
    "It's so arousing knowing people online are going to be seeing me doing something so lewd."
    play sound cum
    show buttup a3 with cum
    "With an explosive orgasm, my butt is filled up with cum."
    play sound cum
    show buttup a3 with cum
    mc "Aahh, yeaahh! I'm coming too!"
    play sound cum
    show buttup 4 with d
    "He pulls out, leaving a messy trial of cum behind, which he happily takes a few photos of."
    play sound camera
    show bg bedsex with cum
    stop ambience fadeout 1.0
    stop sound2 fadeout 1.0
    mc "Mm... I could get used to this..."
    "My partner agrees as we move to go shower together."
    scene bg black with d
    "Later on..."
    scene bg bedroomnight with d
    play sound equip
    call clothescasual from _call_clothescasual_5
    show mce happy
    with d
    "Checking my statistics, lots of people are fans of the anal set! Even some that aren't usually fans of anal say they're enjoying this one."
    scene bg bedsex
    show buttupb
    if tan == 1:
        show buttupb tan
    if hair == 1:
        show buttuph black
    if hair == 2:
        show buttuph blonde
    show buttup 4
    with d
    "I think I picked the perfect pose for it, as I catch even myself admiring the picture for a few moments."
    $ photosets += 1
    $ moneygain = 130
    $ analsexes += 1
    $ status += 1
    call moneygain from _call_moneygain_73
    $ sdgain = 1
    call sdgain from _call_sdgain_147
    $ shameloss = 1
    call shameloss from _call_shameloss_109
    $ folgain = 105
    call folgain from _call_folgain_23
    play sound success
    "(+$[fmoney], +[ffol] Followers)"
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    jump postworktrans
label lonelyfans19:
    scene bg bedroomnight with d
    play sound equip
    call clothesnude from _call_clothesnude_16
    show mce happy
    with d
    "Okay... Next set..."
    "Damn, it's not easy procuring a guy every time I want to make a set..."
    "If only I had someone to do this regularly with."
    "Ah, what if... What if I were to get one of my fans to..."
    "Paid for the sex, paid for the sets, it's perfect."
    "I'll need to figure out the best way to do that, but for now, I think I'll..."
    menu:
        "Use your [crush]" if True:
            $ genericvariable = 1
            "That's right, I can use my sweet!"
            "And maybe in the future if we do hypothetically get together, he'll be more comfortable doing that kind of thing."
        "Use a semi-close friend from bar" if True:
            $ genericvariable = 2
            "One of those guys I drink with occasionally... Yeah, I could see that working."
        "Use a one-night stand from the club" if True:
            $ genericvariable = 3
            "Certainly makes it easier that way. It's a little degenrate but..."
            if qsecretlydepraved == 1:
                "(Secretly Depraved) That just makes it even hotter for me"
                $ sdgain = 1
                call sdgain from _call_sdgain_148
                "(+1 Sexual Desire!)"
    play music action fadein 3.0
    scene bg black with d
    show lonelyfansb mirror
    show frombehindb
    if tan == 1:
        show frombehindbtan
    if hair == 1:
        show frombehindh black
    if hair == 2:
        show frombehindh blonde
    show frombehind v2
    with d
    play sound2 foreplay1 fadein 2.0
    play ambience sex fadein 3.0
    "Pushing his cock deep inside my wet, tight pussy, we begin to pound each other like rabbits."
    call virgin from _call_virgin_9
    mc "Aahhaahh, yesss!"
    mc "Take a picture, take a picture!"
    play sound camera
    show lonelyfansb mirror with cum
    "From his above perspective, he takes a variety of shots as requested."
    "Hard to blame him, since he's keeping every picture too, he wants to make sure he gets my best angle from every angle!"
    "Perfect for me."
    play sound cum
    show frombehind v3 with cum
    "Ohh, aahhh! T-The money shot!"
    play sound cum
    show frombehind v3 with cum
    "Although I'm wearing a condom, it still messily splurts and drips out creating a perfect shot for the photoset."
    show frombehind 4 with d
    stop sound2 fadeout 1.0
    stop ambience fadeout 1.0
    mc "Take as many pics as you'd like, sexy!"
    play sound camera
    show lonelyfansb mirror with cum
    play sound camera
    show lonelyfansb mirror with cum
    mc "Hehehe!"
    scene bg black with d
    "Later on..."
    scene bg bedroomnight with d
    play sound equip
    call clothescasual from _call_clothescasual_6
    show mce happy
    with d
    "Checking my statistics, we're back on track! Making more money, and more followers than ever."
    "In fact, we're at a peak!"
    $ photosets += 1
    $ moneygain = 120
    $ vaginalsexes += 1
    $ status += 1
    call moneygain from _call_moneygain_74
    $ sdgain = 1
    call sdgain from _call_sdgain_149
    $ shameloss = 1
    call shameloss from _call_shameloss_110
    $ folgain = 100
    call folgain from _call_folgain_24
    play sound success
    "(+$[fmoney], +[ffol] Followers)"
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    jump postworktrans
label lonelyfans18:
    scene bg bedroomnight with d
    play sound equip
    call clothesnude from _call_clothesnude_17
    show mce neutral
    with d
    "Hmm... Just as I thought... My money and follower count has been stagnating recently."
    "My last two sets haven't gotten more any more attention than usual! I can't believe it! They were excellent sets..."
    show mce angry with d
    "Hmph... I was worried this would happen."
    "I blew my load, showed my pussy and face too early, and now I have nothing else special to draw people in..."
    "What do I need to do? Am I not pretty enough? Why are my posts not as popular as some of these other girls? I mean she has the same amount of followers, why is she getting more likes? She's not even as pretty as me!"
    "Grr... I don't get it at all!"
    show mce neutral with d
    "Ahh! This one's selling gifs of her having sex... And it's so popular!"
    "Hmm... Yeah, that's the natural direction to take this. Especially in the future when I'm living with my partner/future husband."
    "I won't make the same mistake, though. I'll drag this 'sexcapade' out and start with just a blowjob!"
    "Oh- Wait... I don't... have anyone here to do that with..."
    show mce horny with d
    "Unless..."
    menu:
        "Use your [crush]" if True:
            $ genericvariable = 1
            "That's right, I can use my sweet!"
            "And maybe in the future if we do hypothetically get together, he'll be more comfortable doing that kind of thing."
        "Use a semi-close friend from bar" if True:
            $ genericvariable = 2
            "One of those guys I drink with occasionally... Yeah, I could see that working."
        "Use a one-night stand from the club" if True:
            $ genericvariable = 3
            "Certainly makes it easier that way. It's a little degenrate but..."
            if qsecretlydepraved == 1:
                "(Secretly Depraved) That just makes it even hotter for me"
                $ sdgain = 1
                call sdgain from _call_sdgain_125
                "(+1 Sexual Desire!)"
    "It's not like I have to tell them the truth. In fact, I can use their overtuned male sexuality against them by offerring to happily take photos under the illusion that it's for them, and they can keep it."
    "Heheh, delightfully devilish, [mc]..."
    scene bg black with d
    "A little while later... I have succesfully invited my partner to my room."
    scene bg bedroomnight with d
    play sound equip
    call clothesnude from _call_clothesnude_18
    show mce neutral
    with d
    if genericvariable == 1:
        show crush:
            xpos 1200
        with d
        "It wasn't hard getting [crush] to come here again, I just invited him to hang out, and then as usual I did 'my moves' on him."
    elif genericvariable == 2:
        show student2:
            xpos 1200
        with d
        "After some chatting, I did manage to pull someone from the bar. I certainly hope I don't get a reptuation."
    elif True:
        show student4:
            xpos 1200
        with d
        "Picking someone up from the club is almost a little too easily sometimes. Although maybe I'm just getting dangerously confident and competent at this."
    show lonelyfansb mirror
    show lonelyfans 18
    if hair == 1:
        show lonelyfans18h black
    if hair == 2:
        show lonelyfans18h blonde
    if piercingson == 1:
        show lonelyfans18piercings
    with d
    play ambience oral1 fadein 3.0
    "I wrap my lips around his cock and get to work, offering MY phone to him so he can take pictures."
    "Naturally, I promise to send them all back to him so he can admire them. He doesn't even deny the request, if anything he's esctatic to have some wank material for later."
    "Honestly it doesn't seem so bad to have something to commemorate the event when you want to remember it later."
    "But for me..."
    play sound camera
    show lonelyfansb mirror with cum
    "*Snap, snap* I'm going to be making absolute bank from this!"
    play sound cum
    show lonelyfansb mirror with cum
    play sound cum
    show lonelyfansb mirror with cum
    "I encourage him to take his time as I get many angles. I manage to get a photo of the money shot! Perfect!"
    stop ambience fadeout 1.0
    "And when all is said and done, he leaves and I upload the images online."
    "All according to plan... The unexpected sexual set blows up, and my posts breaks my like record as it goes semi-viral."
    "Phew... So... Time to plan what I do next."
    $ photosets += 1
    $ moneygain = 110
    $ blowjobs += 1
    call moneygain from _call_moneygain_65
    $ sdgain = 1
    call sdgain from _call_sdgain_126
    $ shameloss = 1
    call shameloss from _call_shameloss_88
    $ folgain = 95
    call folgain from _call_folgain_17
    play sound success
    "(+$[fmoney], +[ffol] Followers)"
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    jump postworktrans
label lonelyfans17:
    scene bg bedroomnight with d
    play sound equip
    call clothesnude from _call_clothesnude_19
    show mce happy
    "I take my fancy, jewelled buttplug out of my bedside drawer."
    "It came in a fancy cushioned box that I keep it in, as if it were an expensive ring."
    "Bending over in front of my mirror, I press the cool tip to my butt and try to push it inside."
    if cgl == 1:
        "It's a little larger than the tail of the cat lingerie, but I still manage to get it in juuust right!"
    show lonelyfansb mirror
    show lonelyfans 17
    with d
    "It's perfect, and it feels amazing! Mmphhh, I can't help but imagine how tight and amazing it'd be to get fucked with this in."
    "Spreading my butt in front of the mirror, I also can't help but admire how cute my butt is with the shining jewel in place of my tight pucker."
    "Not bad! I didn't get understand the appeal of buttplugs until right this second, I think."
    "Wow, I can't believe I'm admiring my own butt right now. I know I'm proud of my butt, but let's quell the ego a bit, heh."
    play sound camera
    show lonelyfansb mirror with cum
    "*Snap, snap* From several angles, spread, unspread and even laying down. I show off my buttplug in its glory."
    "This is becoming quite an awesome job! I can buy cute sex toys, earn a profit from them, and then I can keep and use the toy for my own enjoyment."
    "Then, I upload my image set and wait for the comments, likes and love to flood in."
    "It doesn't even take a minute now, I can refresh and someone will have already liked my post."
    "I've also been getting a lot better and confident at taking photos. The lightning and quality has improved so much since my first sets."
    "With a wistful sigh, I put my legs up, and relax for the evening, safe in the knowledge that things are going so well."
    "Oh! My buttplug is still inserted! *Giggle*"
    $ photosets += 1
    $ moneygain = 90
    call moneygain from _call_moneygain_66
    $ sdgain = 1
    call sdgain from _call_sdgain_127
    $ shameloss = 1
    call shameloss from _call_shameloss_89
    $ folgain = 80
    call folgain from _call_folgain_18
    play sound success
    "(+$[fmoney], +[ffol] Followers)"
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    jump postworktrans
label lonelyfans16:
    scene bg bedroomnight with d
    play sound equip
    call clothescatlingerie from _call_clothescatlingerie_1
    show mce happy
    "Ahh, time to get some use out of this expensive lingerie. Fingers crossed that I recoup some costs."
    "Not to mention, I finally get to show off and look super cute to all my fans!"
    show lonelyfansb mirror
    show lonelyfans 16
    if pregnancyshowing == 1:
        show lonelyfans 16p
    if hair == 1:
        show lonelyfans16h black
    if hair == 2:
        show lonelyfans16h blonde
    with d
    "Easing the tail into my butt, it sinks in with a pop!"
    "Ohh, the plug feels weird! In a good way, though. It's cold too! Hehe..."
    "Mmmm, I'm so hot and horny already. It's like my body heats up in a pavlovian response every time I prepare to take a photoset."
    "I position my cat panties in such a way to show off my pussy, and also my tail buttplug a little."
    "I keep the bra on to show off my photogenic cleavage in the boob window."
    "Even with my breasts contained, that doesn't stop my erect nipples from poking through."
    play sound camera
    show lonelyfansb mirror with cum
    "*Snap, snap* Hehe, I'm getting the tingles in my loins."
    "I can't wait to masturbate to my follower's comments tonight. The orgasms are always a little stronger that way."
    "For the caption, I put: 'Come and make the kitty purr?', that'll rile them up."
    "I spend the next hour lazing around and masturbating in my cat lingerie as the money and followers roll in!"
    "I'm unstoppable."
    $ photosets += 1
    $ masturbations += 1
    $ moneygain = 90
    call moneygain from _call_moneygain_67
    $ sdgain = 1
    call sdgain from _call_sdgain_128
    $ shameloss = 1
    call shameloss from _call_shameloss_90
    $ folgain = 80
    call folgain from _call_folgain_19
    play sound success
    "(+$[fmoney], +[ffol] Followers)"
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    jump postworktrans
label lonelyfans15:
    scene bg bedroomnight with d
    play sound equip
    call clothesbunnysuit from _call_clothesbunnysuit_11
    show mce happy
    "Hehe, I can't wait to show this thing off!"
    "It even has a hole in the tights for easy access. I'm guessing this is usually used so you don't have to remove the entire outfit to pee, or... to fuck!"
    "But I have other ideas..."
    show lonelyfansb mirror
    show lonelyfans15
    if pregnancyshowing == 1:
        show lonelyfans15p
    if hair == 1:
        show lonelyfans15h black
    if hair == 2:
        show lonelyfans15h blonde
    if piercingson == 1:
        show lonelyfans15piercings
    with d
    "Hoho, they're gonna like this one!"
    "I've always been fond of wearing tights, they're comfy, and the fishnet pattern eccentuates my curvy thighs."
    "And the suit does a very poor job of containing my perky nipples, already erect due to my arousal."
    "Parting the soft fabric of the leotard, I expose my dripping, wet pussy and..."
    play sound camera
    show lonelyfansb mirror with cum
    "*Snap, snap* Pictures, more pictures of my pussy!"
    "My followers can't get enough, they love my pussy, and I looove them loving my pussy."
    "For the description of this picture, I put 'Can you cum inside my pussy?'"
    "I'd say it's official. I have an exhibitionist fetish now, at least when I show off online."
    "I can't help but get super aroused as I read all the comments."
    "'Hoooly fucking fuck! Best tits ever in existence!'"
    "'Daaayum, that pussy is phat!!'"
    "While I may be losing a few brain cells reading them, they're certainly ego boosters! Hahaaaa!"
    $ photosets += 1
    $ moneygain = 90
    call moneygain from _call_moneygain
    $ sdgain = 1
    call sdgain from _call_sdgain_24
    $ shameloss = 1
    call shameloss from _call_shameloss_12
    $ folgain = 80
    call folgain from _call_folgain
    play sound success
    "(+$[fmoney], +[ffol] Followers)"
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    jump postworktrans
label lonelyfans14:
    scene bg bedroomnight with d
    play sound equip
    call clothesnude from _call_clothesnude_20
    show mce happy
    "I bought this expensive, but amazing dildo, and hopefully I'll be able to recoup this expense!"
    "Hmm, I wonder if it's tax deductable too?"
    show lonelyfansb mirror
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
    play ambience sex fadein 3.0
    "*Schlick*! The dildo easily sinks into my soppy, wet pussy. Mmphh, I love how much it fills me."
    "It really is a great dildo too. I'm glad I decided to get something a little more pricy than not."
    "Mmphh, I fuck myself with the dildo for a few moments before I realize I forgot to take pictures."
    "Woops! I got a little carried away, I guess I'm just that horny, hehe."
    play sound camera
    show lonelyfansb mirror with cum
    "Taking a full set of pictures of me using the dildo, I then take the opportunity to finish myself off."
    "Pounding my pussy with the purple cock, I easily bring myself to orgasm with the thoughts of all my fans masturbating to my body."
    play sound cum
    show lonelyfansb mirror with cum
    stop ambience fadeout 1.0
    "Haaahhh... Soooo goood..."
    $ photosets += 1
    $ moneygain = 80
    call moneygain from _call_moneygain_1
    $ sdgain = 1
    call sdgain from _call_sdgain_25
    $ shameloss = 1
    call shameloss from _call_shameloss_13
    $ folgain = 70
    call folgain from _call_folgain_1
    play sound success
    "(+$[fmoney], +[ffol] Followers)"
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    jump postworktrans
label lonelyfans13:
    scene bg bedroomnight with d
    play sound equip
    call clothesnude from _call_clothesnude_21
    show mce happy
    with d
    "I had this idea last time of doing a video, and I've been thinking about what kind of video to do."
    "Having a look online, a lot of girls would do fairly mundane things, such as simply moving around while their genitals are on display. That was a little boring!"
    "Although, I did enjoy the occasional titty drop, and one thing that caught my eye was, of course, people masturbating!"
    show lonelyfansb mirror
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
    play ambience sex fadein 3.0
    "So, while I take my time thinking of something creative, I'll do a video of me masturbating."
    "Hoooh, my clit is already swollen. I'd probably have done this tonight anyway knowing me."
    "Ohh, and the viewers will be able to hear me moan. Voice reveal? Heheh."
    "I turn on my phone, standing it up on my bedside table, and begin recording."
    "Wasting no time, I quickly bring my finger to my swollen, aroused pussy."
    "Mmphh... I feel far more sensitive than usual. Just rubbing my clit feels so much better."
    "Rather than blue-ball my paying viewers with a 10 second clip, I'm going to go for the full orgasm."
    "That way they'll hopefully they'll be able to enjoy this as much as I am."
    "And, ahhh... I can just imagine them rubbing their cocks while watching me. Mmphh..."
    play sound cum
    show lonelyfansb mirror with cum
    "Oh god, I'm gonna come! Ahhaaahhhhh..."
    "Masturbating on camera for the first time ever gave me a blissful orgasm. I imagine you could even see my pussy contract on video."
    "Phewww... T-That was so amazing I ended up laying back and doing nothing for another 30 seconds. I'll have to crop that out."
    stop ambience fadeout 3.0
    $ photosets += 1
    $ moneygain = 70
    call moneygain from _call_moneygain_2
    $ sdgain = 1
    call sdgain from _call_sdgain_26
    $ shameloss = 1
    call shameloss from _call_shameloss_14
    $ folgain = 60
    call folgain from _call_folgain_2
    play sound success
    "(+$[fmoney], +[ffol] Followers)"
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    jump postworktrans
label lonelyfans12:
    scene bg bedroomnight with d
    play sound equip
    call clothesnude from _call_clothesnude_22
    show mce happy
    with d
    "Well, I've been putting this off for a while."
    "To be honest, I've been ready to reveal my face for a while, but it's one of those things that didn't entirely seem necessary to me."
    "That is, until I realized one small problem this potential career will have for me."
    show lonelyfansb mirror
    show lonelyfans12
    if pregnancyshowing == 1:
        show lonelyfans12p
    if hair == 1:
        show lonelyfans12h black
    if hair == 2:
        show lonelyfans12h blonde
    if piercingson == 1:
        show lonelyfans12piercings
    with d
    "There are some poses I'd never be able to do without showing my face."
    "If I'm going to take this selling lewd photo sets job as seriously as I want to, I can't have any limitations."
    if chatfaproute1 == 1:
        "And I've already shown my face on ChatFap, so this isn't a huge leap."
    elif True:
        "Additionally, if I want to do videos or streams, it'd be ridiculous to hide my face the entire time."
    "So, here I am! Just me, plain and simple!"
    play sound camera
    show lonelyfansb mirror with cum
    "*Snap, snap* There we go!"
    "I think establishing myself as a person will help in my journey in becoming the top LonelyFans creator too."
    "I'm no longer this faceless entity that could be anyone or anything."
    "I'm now the cute girl next door!"
    "And as the comments, money and followers come in... Wow, this is huge!"
    $ photosets += 1
    $ moneygain = 80
    call moneygain from _call_moneygain_3
    play sound success
    $ folgain = 100
    call folgain from _call_folgain_3
    "(+$[fmoney], +[ffol] Followers!)"
    "Did showing my face really excite them so much?"
    "It was only something small to me, but to them it seems like a big event! Like when I showed my pussy for the first time."
    "I love this, I love it so much!"
    $ sdgain = 1
    call sdgain from _call_sdgain_27
    $ shameloss = 1
    call shameloss from _call_shameloss_15
    play sound success
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    jump postworktrans
label lonelyfans11:
    scene bg bedroomnight with d
    play sound equip
    call clothescamisole from _call_clothescamisole
    show mce happy
    with d
    "Ahh, my cute camisole! I'm exciting to show this off, I feel so sexy while I'm wearing it."
    "It's only a shame I can't do something more than just show it off to my fans."
    show lonelyfansb mirror
    show lonelyfans11a
    if pregnancyshowing == 1:
        show lonelyfans11ap
    if hair == 1:
        show lonelyfans11h black
    if hair == 2:
        show lonelyfans11h blonde
    if piercingson == 1:
        show lonelyfans11piercings
    with d
    "Lowering the angle of my camera, I make sure to capture the 'good stuff', and a bit of under boob can be appreciated too!"
    "Ohh, and these lingerie panties are slightly see through, especially when I'm wet."
    "And ohhh god, is my pussy wet."
    "I don't know how it happens so fast. Taking pictures of myself gets me so hot and bothered."
    play sound camera
    show lonelyfansb mirror with cum
    "I take a few pictures, but..."
    "I'm not quite satisfied yet."
    play sound equip
    scene lonelyfansb mirror
    show lonelyfans11b
    if pregnancyshowing == 1:
        show lonelyfans11bp
    if hair == 1:
        show lonelyfans11h black
    if hair == 2:
        show lonelyfans11h blonde
    if piercingson == 1:
        show lonelyfans11piercings
    with d
    "There!"
    "Mmphhh, so wet.... Let's take some more pictures."
    play sound camera
    show lonelyfansb mirror with cum
    "Haaahhh... Now this is going to be a nice set."
    "I'm glad I can enjoy this as much as I do."
    "For me, I can just use it to spice up my nightly masturbatory sessions, so I'll never burn out, hehe."
    "Okay, let's upload this, take a masturbreak and see how the set performs."
    "..."
    $ moneygain = 65
    call moneygain from _call_moneygain_4
    play sound success
    "I end up receiving $[fmoney]! Along with even more followers and praise."
    "This platform really is like a snowball."
    "Will I ever stop growing? I hope not!"
    "Top 1%%, I'm coming for you!"
    $ photosets += 1
    $ sdgain = 1
    call sdgain from _call_sdgain_28
    $ shameloss = 1
    call shameloss from _call_shameloss_16
    $ folgain = 55
    call folgain from _call_folgain_4
    play sound success
    "(+[fsd] Sexual Desire, -[fshame] Shame, +[ffol] Followers)"
    jump postworktrans
label lonelyfans10:
    "I best put this vibrator to good use! I mean it's basically an investment, right?"
    scene bg bedroomnight with d
    play sound equip
    call clothesnude from _call_clothesnude_23
    show mce happy
    with d
    "What's the harm? I already did a masturbation set. Let's throw a vibrator into the mix too."
    "It's not that different, but a steady supply of pictures will keep my growing fanbase happy."
    show lonelyfansb mirror
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
    "I press the vibrator into my pussy and turn it onto a low setting as I get my phone ready for a picture."
    play sound camera
    show lonelyfansb mirror with cum
    "I don't just think I'm becoming desensitised to this, I think I'm really enjoying it."
    "Even as I take these pictures pragmatically and upload them online, there's not a doubt in my mind that I'm going to finish myself off with an orgasm afterwards."
    "I mean, is it that easy? Just broadcast my nightly masturbation session, and then have tons of admiring fans donating a sustainable living?"
    "I'd say every girl should try this! But I wouldn't want the competition, hehe..."
    "Gosh... I wonder what past me would think if she'd hear me think like this."
    "I guess I really have become an e-girl through and through."
    "Am I proud?"
    "After an hour, I check the analytics of my picture."
    play sound success
    $ moneygain = 60
    call moneygain from _call_moneygain_5
    "(+$[fmoney])"
    "Yeah... I'm proud."
    play sound success
    $ photosets += 1
    $ sdgain = 1
    call sdgain from _call_sdgain_29
    $ shameloss = 1
    call shameloss from _call_shameloss_17

    $ folgain = 50
    call folgain from _call_folgain_5
    play sound success
    "(+[fsd] Sexual Desire, -[fshame] Shame, +[ffol] Followers)"
    jump postworktrans
label lonelyfans1:
    scene bg bedroomnight with d
    call clothescasual from _call_clothescasual_7
    show mce happy
    with d
    "Okay, hm... I suppose if I'm going to be uploading pictures here, it's only sensible to have some casual pictures of myself."
    "Will people even be willing to pay for that? It's hard to say."
    show lonelyfansb mirror
    show lonelyfans 1
    if hair == 1:
        show lonelyfans1h black
    if hair == 2:
        show lonelyfans1h blonde
    with d
    "Taking out my smartphone, I position myself infront of the mirror and take some very casual shots with my face obscured."
    "Now... If I set my camera here, and put it on a timer... There!"
    play sound camera
    "*Snap, snap*"
    "With a few basic shots, I assume that might be enough? I think I'll just pick the best few."
    "I upload them online, and post them onto my LonelyFans page."
    "It's not much, but it did bump my profile up to the top of 'latest uploads', so I received a few profile hits."
    call sdgain from _call_sdgain_31
    call shameloss from _call_shameloss_2
    $ folgain = 2
    call folgain from _call_folgain_6
    "And hey, someone did end up buying to check the pictures!"
    $ moneygain = 5
    call moneygain from _call_moneygain_6
    play sound success
    "(+$[fmoney], +[ffol] Followers!)"
    "Ohh, and they left a comment..."
    "'Damn! Sexy body! When are we going to see more?'"
    "..."
    "I've never had anyone say anything quite like that to me before."
    "How on earth do I reply to that?"
    menu:
        "Reply 'I'm not like that!'" if True:
            "I get another reply... 'Another model too scared to do anything interesting. No one wants to pay for softcore porn."
            "Eek... Maybe he has a point..."
        "Reply 'I'll upload some lewd photos soon!'" if True:
            "I get another reply... 'Nice! Can't wait to see your breasts!'"
            "My breasts, hm? Sheesh..."
        "Reply 'Thanks for purchasing! What kind of things would you like to see more of?" if True:
            "I get another reply... 'I wanna see you bent over spreading your pussy and ass!"
            "Wha?! That's way too lewd!"
        "Don't reply..." if True:
            "This is a little too weird for me. I'll just let the commenters's imagination stew."
    "I never imagined that it'd be quite like this. Can I really make $72,000 doing this?"
    "Well... I'll probably have to turn the heat up, like the commenter desired."
    play sound success
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    $ photosets += 1
    $ lonelyfans1 = 1
    jump postworktrans
label lonelyfans2:
    scene bg bedroomnight with d
    "*Gulp*... I know I said I'd do this, but now, as I'm finally taking off my clothes, the embarrassing reality is hitting me."
    show lonelyfansb mirror
    show lonelyfans 2
    if tan == 1:
        show lonelyfans2tan
    with d
    "I take out a pair of sexy panties and wiggle my butt infront of the mirror with them on."
    "Even without my face, the entire internet will potentially have access to images of my body in underwear."
    "They may even masturbate to that."
    "Well... That's what these pictures are for, right? People are going to masturbate to them."
    "It feels slightly degrading, but a small dark corner of my mind is aroused by the idea."
    "Okay! I've pepped myself up."
    "I'm going to take a sexy picture of my butt. I'm very proud of my butt, and honestly don't mind if people admire it... anonymously."
    play sound camera
    "*Snap, snap*"
    "I take a lot more pictures compared to before, and as I upload them onto the computer I take my time to pick and choose the best ones for upload."
    "Heyyy, I actually look pretty cute from this angle!"
    "Will someone actually masturbate to this? Phew..."
    "Okay, here we go... *Click* They're uploading!"
    "After uploading, I leave the website for a few hours, then return to see how my post is doing."
    "Ohh, five new followers? That's not bad at all, and two of them paid to see the picture."
    play sound success
    $ moneygain = 10
    call moneygain from _call_moneygain_7
    $ folgain = 5
    call folgain from _call_folgain_7
    "(+$[fmoney], +[ffol] Followers!)"
    "Not bad, not bad at all. I can't believe I got $[fmoney] and all I had to do was take a picture of my butt!"
    "Now I think I'm starting to understand the appeal."
    play sound success
    $ lonelyfans2 = 1
    $ sdgain = 1
    call sdgain from _call_sdgain_30
    $ shameloss = 1
    call shameloss from _call_shameloss_18
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    $ photosets += 1
    jump postworktrans
label lonelyfans3:
    scene bg bedroomnight with d
    "Hmm... Feet pics, huh?"
    "I'd always hear people joke about it, but apparently people are willing to pay quite a lot for this stuff, and well..."
    "It's just my feet, I don't even feel nervous about that."
    play sound camera
    scene lonelyfansb mirror
    show lonelyfans 3a
    with cum
    "*Snap, snap.*"
    "That was quick and easy!"
    "Something's not quite right to me though. Do people really masturbate to this alone?"
    "No, I think they'll need something a little more enticing alongside the feet to make things more interesting. Let's see what I can do..."
    "Getting my sexy underwear on, I sit with my feet up in the mirror."
    play sound camera
    scene lonelyfansb mirror
    show lonelyfans 3b
    if hair == 1:
        show lonelyfans3h black
    if hair == 2:
        show lonelyfans3h blonde
    if piercingson == 1:
        show lonelyfans3piercings
    with cum
    "*Snap, snap.*"
    "Lewd! And I don't even mind showing off a cheeky glimpse of my butt, that's not different to what I uploaded before."
    "Let me just edit out the my face first..."
    show lonelyfans3c
    with dissolve
    "Perfect!"
    "Aaaand upload."
    scene bg black with dissolve
    "Feeling just as nervous as last time, I close the website and don't look at it for a while."
    "When I return... I realize I'd make a big mistake."
    play music action fadein 3.0
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
    "Oh no! I accidentally flashed my breast in the bottom right corner!"
    "Eughh... I didn't even notice..."
    "I have to delete this quickly-"
    "Wait... What's this?"
    play sound success
    $ sdgain = 1
    call sdgain from _call_sdgain_32
    $ shameloss = 2
    call shameloss from _call_shameloss_19
    $ moneygain = 20
    call moneygain from _call_moneygain_8
    $ folgain = 10
    call folgain from _call_folgain_8
    "(+[ffol] Followers, +$[fmoney]!)"
    "Woah! It's my biggest picture so far, and by a lot!"
    "I... uhh... I guess I'll leave it up..."
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    "I'm such an idiot... I was so focused on making sure my feet were in focus, and then obscuring my face... Why would I even think about covering up a glimpse of my breast?"
    "And yet..."
    scene bg black with d
    scene bg bed with d
    $ masturbations += 1
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
    show masturbation 1a
    if pregnancyshowing == 1:
        show masturbatione pregnant
    with d
    play ambience sex fadein 3.0
    "I'm so turned on right now!"
    "Mmpphh... All of these people looking at me, and masturbating to my body... What a thrill."
    show masturbation 1b
    with d
    "Ahh, I-I'm gonna come!"
    play sound cum
    show masturbation 1b with cum
    play sound cum
    show masturbation 1b with cum
    stop ambience fadeout 1.0
    $ lonelyfans3 = 1
    $ photosets += 1
    jump postworktrans
label lonelyfans4:
    scene bg bedroomnight with d
    call clothesunderwear from _call_clothesunderwear_1
    show mce neutral
    with d
    "After the debacle that was the accidental breast picture, this next photo set doesn't seem so bad..."
    "Although I admit, I was somewhat nervous about returning to the platform after that."
    "Still, the money is rather exceptional. I'd feel like a fool if I didn't at least take advantage of it."
    "With my sexiest underwear on, I'm prepared to take a faceless photo of myself in it."
    scene lonelyfansb mirror
    show lonelyfans 4
    if pregnancyshowing == 1:
        show lonelyfans 4p
    if hair == 1:
        show lonelyfans4h black
        if pregnancyshowing == 1:
            show lonelyfans4h blackp
    if hair == 2:
        show lonelyfans4h blonde
        if pregnancyshowing == 1:
            show lonelyfans4h blondep
    with d
    "I sit myself infront of the mirror, and take a flattering shot with my face partially obscured. No way anyone would recognize my bangs alone."
    "Heh, my panties got a little wet, I couldn't even help it."
    "What is it exactly that turns me on? The power, the control? Or maybe it's the vulnerability of putting a piece of myself out there in an uncertain world."
    "Perhaps it's the potential 1,000s of horny men that'll be stroking their cocks to my spread legs..."
    "I shake my head, hah, what's wrong with me lately? I'm starting to enjoy this a little too much."
    play sound camera
    show lonelyfans 4
    if pregnancyshowing:
        show lonelyfans 4p
    with cum
    "*Snap, snap, snap*"
    "I upload the photos and peek at my statistics are they rise. Likes flood in, then a few dollars."
    "How could I not love this?"
    play sound success
    $ sdgain = 2
    call sdgain from _call_sdgain_33
    $ shameloss = 2
    call shameloss from _call_shameloss_20
    $ moneygain = 30
    call moneygain from _call_moneygain_9
    $ folgain = 20
    call folgain from _call_folgain_9
    $ lonelyfans4 = 1
    "(+$[fmoney], +[fsd] Sexual Desire, -[fshame] Shame, +[ffol] Followers)"
    $ photosets += 1
    jump postworktrans
label lonelyfans5:
    scene bg bedroomnight with d
    call clothespanties from _call_clothespanties_1
    show mce happy
    with d
    "One thing at a time, I guess! I'll slowly get more comfortable showing my body off."
    "And as I build more confidence, I'll gradually entice people to pay for my content with the promise of seeing even more down the line."
    show mce neutral with d
    "I just hope I'm not moving too fast..."
    show mce laughing with d
    "Ahh, who am I kidding? I've already accidentally shown off my nipple, and at the end of the day, it {i}is{/i} just my breasts."
    show lonelyfansb mirror
    if pregnancyshowing == 1:
        show lonelyfans5p
    elif True:
        show lonelyfans5
    if hair == 1:
        show lonelyfans5h black
    if hair == 2:
        show lonelyfans5h blonde
    if piercingson == 1:
        show lonelyfans5piercings
    with d
    "Sheesh, I can't even take a photo like this without my pussy getting soaked."
    play sound camera
    show lonelyfansb mirror with cum
    "That's not even to mention all the comments I've started to get."
    "'Sit on my face'"
    "'Wow! Amazingly cute!'"
    "'You look like you need a good fucking, gorgeous!'"
    "Yeah... I think I do..."
    "Phew! Is it getting warm in here, or is it just me?"
    $ masturbations += 1
    scene masturbationb
    if pregnancyshowing == 1:
        show masturbatione pregnant
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
    show masturbation 1a

    with d
    play ambience sex fadein 3.0
    "Slipping my panties off, I sink two fingers deep into my wet pussy and imagine myself being plowed."
    "I can't believe how much this is turning me on! I'm actually masturbating to these lewd comments."
    show masturbation 1b with d
    "Ahhh, I'm becoming a complete exhibitionist!"
    play sound cum
    show masturbation 1b with cum
    play sound cum
    show masturbation 1b with cum
    stop ambience fadeout 2.0
    "Ohhh god yes..."
    play sound success
    $ moneygain = 40
    call moneygain from _call_moneygain_10
    $ sdgain = 2
    call sdgain from _call_sdgain_34
    $ shameloss = 2
    call shameloss from _call_shameloss_21
    $ folgain = 25
    call folgain from _call_folgain_10
    $ lonelyfans5 = 1
    "(+$[fmoney], +[fsd] Sexual Desire, -[fshame] Shame, +[ffol] Followers)"
    $ photosets += 1
    jump postworktrans
label lonelyfans6:
    scene bg bedroomnight with d
    call clothesnude from _call_clothesnude_24
    show mce happy2
    with d
    "As far as nudity goes, let's start tastefully."
    "I don't need to shove my pussy in the camera the first time."
    show mce laughing with d
    "Ohhh, I have an idea, hehe."
    scene bg bedroomnight with d
    "I put on my shirt and skirt..."
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
    "Now this is more interesting than just appearing nude!"
    "Wow, even I think I look pretty hot in this picture..."
    "I've certainly started feeling a lot better about myself ever since I started this LonelyFans thing."
    "The confident I've gotten with my body, I've noticed it even when I'm walking around in public; I'm proud to be in my own skin."
    play sound camera
    show lonelyfansb mirror with cum
    "There, these photos are perfect for my pussy's debut."
    "I really thought I'd be more nervous about this, and I suppose a part of me is, but..."
    "I'm more excited to see how much money I get, how many likes I get, and what kind of comments I get!"
    "Huh... Is this a good thing? It was inevitable that I'd become desensitised to this, but have I really established if this is the direction I want to go?"
    play sound success
    $ moneygain = 45
    call moneygain from _call_moneygain_11
    "(+$[fmoney])"
    "$[fmoney]... That's the most yet..."
    "If I'm going to make $72,000, I can't let pride get in my way, right? Now let's read some of these comments..."
    $ sdgain = 2
    call sdgain from _call_sdgain_35
    $ shameloss = 2
    call shameloss from _call_shameloss_22

    $ folgain = 30
    call folgain from _call_folgain_11
    $ lonelyfans6 = 1
    play sound success
    "(+[fsd] Sexual Desire, -[fshame] Shame, +[ffol] Followers)"
    $ photosets += 1
    scene bg black with d
    jump postworktrans
label lonelyfans7:
    "LonelyFans picture time! That means it's time to strip, hehe."
    scene bg bedroomnight with d
    play sound equip
    call clothesnude from _call_clothesnude_25
    show mce happy
    with d
    "My fans can't get enough of my nude body, and I have just so many angles I can tease them with..."
    "One thing they didn't see with my last set was my butt."
    "And I looove my butt, I'm so proud of it."
    "So even though this is another step down a path of debauchery, I'm quite eager for this one."
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
    "Butt aside, I am still a little nervous showing off my pussy."
    "Fortunately, this seems to be quite a flattering angle."
    play sound camera
    show lonelyfansb mirror with cum
    "I wonder what people are going to think about this picture? I even managed to fit in some feet for the degenerates! I bet they'll like it!"
    "Uploading the picture, I eagerly anticipate the incoming followers, comments and more."
    "And as predicted, it's a hit!"
    play sound success
    $ moneygain = 50
    call moneygain from _call_moneygain_12
    "(+$[fmoney])"
    "Fantastic! People really love my butt that much, huh? I'm so happy."
    "Well, they can have as many pictures as my butt as they want if that's the case."
    play sound success
    $ sdgain = 1
    call sdgain from _call_sdgain_36
    $ shameloss = 1
    call shameloss from _call_shameloss_23
    $ folgain = 40
    call folgain from _call_folgain_12
    play sound success
    "(+[fsd] Sexual Desire, -[fshame] Shame, +[ffol] Followers)"
    $ photosets += 1
    jump postworktrans
label lonelyfans8:
    "Looks like I'll be removing all my clothes again."
    scene bg bedroomnight with d
    play sound equip
    call clothesnude from _call_clothesnude_26
    show mce happy
    with d
    "Men on the internet sure do love to admire the female form."
    "Whether it's in photos, or maybe even games."
    "I'm starting to come round to the idea too. I don't even think I'm nervous about this anymore."
    "I have had a few comments about my pussy, and I suppose I'm confident and shameless enough now to show it off in a more fuller display."
    "Just, like..."
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
    "That!"
    "My pussy ended up getting really wet, I couldn't help it."
    "Ohh, I know! I'll caption this photo set with that. Hehe, I wonder if it turns them on, knowing that I was turned on."
    play sound camera
    show lonelyfansb mirror with cum
    "I hope I'm not moving too fast in terms of content."
    "After all, I don't actually have any other body parts to show off!"
    "Although the full-frontal pussy picture is the big one."
    "And it doesn't disappoint, comments, money and fans flood in like never before."
    play sound success
    "($[fmoney])"
    "This is crazy. I can't believe I can take erotic photos of myself for $[fmoney]ish a day."
    "And since it's more of a crowd funding thing, that's only going to steadily rise as I gain more followers."
    "Just what kind of gold mine have I stumbled upon?"
    play sound success
    $ sdgain = 1
    call sdgain from _call_sdgain_39
    $ shameloss = 1
    call shameloss from _call_shameloss_24
    $ moneygain = 55
    call moneygain from _call_moneygain_13
    $ folgain = 45
    call folgain from _call_folgain_13
    play sound success
    "(+[fsd] Sexual Desire, -[fshame] Shame, +[ffol] Followers)"
    $ photosets += 1
    jump postworktrans
label lonelyfans9:
    "Alright... Think, [mc], think! What can I do to impress my fans this time?"
    scene bg bedroomnight with d
    play sound equip
    call clothesnude from _call_clothesnude_27
    show mce happy
    with d
    "Ah, isn't it obvious?"
    "I do this almost every night without thinking, and to me it's barely something sexual or embarrassing."
    "I'll simply make this next picture set masturbation themed."
    "Again, I'm barely nervous to do so."
    "I've become so desensitised to the idea of showing my body off for money, that any shred of nervousness is gone and only replaced with arousal and excitement at the returns."
    scene lonelyfansb mirror
    show lonelyfans9
    if pregnancyshowing == 1:
        show lonelyfans9p
    if hair == 1:
        show lonelyfans9h black
    if hair == 2:
        show lonelyfans9h blonde
    if piercingson == 1:
        show lonelyfans9piercings
    with d
    "My pussy is already wet, for example. I have quite a high libido, so that's not too unusual at this time of night."
    "But, still... My fingers sink inside so easily without having to rub my clit at all."
    "This fingering action shot is sure to impress my followers."
    play sound camera
    show lonelyfansb mirror with cum
    play ambience sex
    "Ahh, and I'm so horny, I think I might just finish myself off!"
    "Aaahhh, ohhh... My clit is so swollen!"
    "Everything feels way more sensitive... Does showing my body off like this really turn me on this much?"
    "Mmpphhh... Fuck, I'm coming already!"
    stop ambience fadeout 3.0
    play sound cum
    show lonelyfansb mirror with cum
    "Phew... Ahh, where was I?"
    "Ohh, I haven't uploaded the pictures yet."
    "From here on out, it might benefit me to peek at my competition and see what they're doing."
    if chatfaproute1 == 0:
        "Maybe I could do sex toys, and maybe even a face reveal one day..."
    elif True:
        "Maybe I could do sex toys on here too, and even show my face like I did on ChatFap."
    "Hm... Now that actually makes me feel a little nervous."
    "I guess I almost forgot, the fact I'm hiding my face makes LonelyFans much easier to do."
    "I can take a picture of any part of my body and it doesn't matter if I'm anonymous. Anyone could see this and it wouldn't matter."
    "Ahh, my money is coming in."
    play sound success
    "($[fmoney])"
    "Very nice, we're slowly climbing."
    "In addition to getting more money than last time, I'm getting large double digit increases in followers too."
    "I've got to keep up this upward trajectory. Bigger and better all the time."
    play sound success
    $ sdgain = 1
    call sdgain from _call_sdgain_40
    $ shameloss = 1
    call shameloss from _call_shameloss_25
    $ moneygain = 55
    call moneygain from _call_moneygain_14
    $ folgain = 50
    call folgain from _call_folgain_14
    play sound success
    "(+[fsd] Sexual Desire, -[fshame] Shame, +[ffol] Followers)"
    $ photosets += 1
    jump postworktrans
jump postworktrans

label lonelyfansgallery:
    "Let's check how my old pictures are doing..."
    menu lfg1:
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
            jump lfg2
        "Back" if True:
            jump lonelyfansroute
    jump lfg1
    menu lfg2:
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
            jump lfg1
        "Next Page ->" if True:
            jump lfg3
        "Back" if True:
            jump lonelyfansroute
    jump lfg2
    menu lfg3:
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
            jump lfg2
        "Back" if True:
            jump lonelyfansroute
    jump lfg3

init:
    $ lonelyfans1 = 0
    $ lonelyfans2 = 0
    $ lonelyfans3 = 0
    $ lonelyfans4 = 0
    $ lonelyfans5 = 0
    $ lonelyfans6 = 0
    $ lonelyfans7 = 0
    $ lonelyfans8 = 0
    $ lonelyfans9 = 0
    $ lonelyfans10 = 0
    $ lonelyfans11 = 0
    $ lonelyfans12 = 0
    $ lonelyfans13 = 0
    $ lonelyfans14 = 0
    $ lonelyfans15 = 0
    $ lonelyfans16 = 0
    $ lonelyfans17 = 0
    $ lonelyfans18 = 0
    $ lonelyfans19 = 0
    $ lonelyfans20 = 0
    $ lonelyfans21 = 0
    $ lonelyfans22 = 0
    $ lonelyfans23 = 0
    $ lonelyfans24 = 0
    $ fold2 = 1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
