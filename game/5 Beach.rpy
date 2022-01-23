label beach:
    $ susumet = 1
    play music girls
    play ambience ambiencebeach
    if beachvisited == 0:
        scene bg beach
        call clothes from _call_clothes_16
        show mce happy2
        with d
        "Ahh, the beach!"
        "Holy shit, it's so busy! There's like, no room to even breath here."
        if clothes == 11:
            "Fortunately I'm already in my swimsuit and ready to chill!"
        elif swimsuit == 1:
            "That being said, I do have a swimsuit. So let's get changed and enjoy myself!"
        elif True:
            "Ohh, I should buy a swimsuit from the shops when I have the chance. I bet I'll be coming here a lot over my time at the college."
        unknown "Hoooi!"
        show mce happy with d
        "Ohh? Who's that?"
        show susub:
            xpos 1200
        show susuo swimsuit:
            xpos 1200
        show susue happy:
            xpos 1200
        with d
        "Ohh, it's!"
        python:
            susu = renpy.input("Name the Frog Girl. Leave blank for the default name 'Susu'.")
            susu = susu.strip()
            if not susu:
                susu = "Susu"
        mc "Aahh, [susu]! Your swimsuit is so cute!"
        show susue laughing with d
        susu "Thank youu, [mc]!"
        susu "Come with me, I know a place that's a little quieter just down the bank."
        scene bg black with d
        show bg beachhut
        call clothes from _call_clothes_21
        show mce happy
        show susub:
            xpos 1200
        show susuo swimsuit:
            xpos 1200
        show susue happy:
            xpos 1200
        with d
        susu "This is a quiet hut my family owns, and this part of the beach is private. You're more than welcome to come here whenever you want to get a tan in peace and quiet!"
        show mce happy2 with d
        mc "Thank you so much, [susu]!"
        show susue horny with d
        susu "Ohh, and you're welcome to invite a boy or two, hehe."
        show mce horny with d
        mc "Ahhaah, I'll keep that in mind!"
        susu "I'm at the hut quite often too, somewhere warm and wet is just my element."
        show mce laughing with d
        mc "Pfft, it certainly is."
        susu "I have a few things to do inside, don't hog all the sun!"
        $ beachvisited = 1
        hide susu
        show mce happy
        with d
        if swimsuit == 0:
            "Hmm... I should get a swimsuit so I can hang out at the beach properly."
        elif True:
            jump swimsuitalreadybought
    elif swimsuit == 0:
        scene bg black with d
        show bg beachhut
        call clothes from _call_clothes_22
        show mce happy
        "I should get a swimsuit so I can hang out at the beach properly."
    elif True:
        label swimsuitalreadybought:
            pass
        scene bg black with d
        show bg beachhut
        if nude == 1:
            call clothes from _call_clothes_3
        elif True:
            call clothesbeach from _call_clothesbeach
        show mce happy
        with d
        if nude == 1:
            "Baring all, as if it was a nude beach, I step out and smell the fresh air."
        elif True:
            "With swimsuit prepared, I step out into the beach and smell the fresh air."
        mc "Aahhh, what should I do?"
        menu:
            "Sunbathing" if True:
                jump sunbathing
            "Spend some time with [susu]" if True:
                jump susuroute
            "Go to the beach bar" if True:
                jump beachbar
            "Actually... Let's leave." if True:
                jump worldmap
jump worldmap
label sunbathing:
    "Time to get some sunshine! It’s so peaceful and quiet around this area of the beach too."
    call sunbathingart from _call_sunbathingart
    if nude == 1:
        "I setup a blanket and lay down; I'm completely nude and exposed to all."
    elif True:
        "I setup a blanket and lay down in my swimsuit."
    "Phew, that’s nice…"
    "Hey, wait a minute… Who’s that hunk over there? Complete six-pack and in his swimming trunks."
    "Seems like they’re a little lost. Well, [susu] did say hot guys are welcome anytime."
    menu sunbathningm1:
        "Sexual Desire: [sd], Shame: [shame]."
        "Ignore ‘em" if True:
            if personality == 2 and sd > 35:
                "(Always Horny) But he’s such a hottie! I bet I could have some fun with him…"
                jump sunbathningm1
            show beach1 1b with d
            "Ahh, forget it. I should just relax. I’m gonna lay down and close my eyes."
            scene bg black with d
            "While napping, you have a dream…"
            call dream from _call_dream_1
            $ tantime += 7
            $ tan = 1
            scene beach1b
            call sunbathingart from _call_sunbathingart_1
            "Phew, how long was I out? I even got a tan!"
            play sound success
            "(+7 Days of Tan)"
            jump postworktrans
        "Invite them over! (25 Sexual Desire)" if True:
            if sd < 25:
                "Nahh, that'd be a bit weird."
                jump sunbathningm1
            play music action
    show bg beachhut
    show bg beachhut
    if nude == 1:
        call clothesnude from _call_clothesnude_5
    elif True:
        call clothesbeach from _call_clothesbeach_1
    show mce happy
    show student3:
        xpos 1200
    with d
    mc "Heyyy, cutie! Whatcha looking for?"
    if nude == 1:
        hunk "Crikey, I don't know what I was looking for, but I think I found it!"
        mc "Ahaha, you’re more than welcome to stay around here lookin’ like that."
        hunk "And I'm liable to stay if you look like that, gorgeous! Can I share your towel? I didn’t bring one."
    elif True:
        hunk "Heya, I was just checking out this part of the beach. Haven’t been down here before. These huts all look like private land, though."
        mc "Correct! But you’re more than welcome to stay around here lookin’ like that."
        hunk "Ahaha, excellent. Can I share your towel? I didn’t bring one."
    play sound equip
    call sunbathingart from _call_sunbathingart_2
    mc "You might have to squeeze up behind me, don’t let my big butt bump into you too much."
    hunk "Well now, maybe that big butt could use some help with sun cream."
    mc "Hehe, I’ve already beaten you to the punch. But, maaayybbee…"
    menu sunbathingm2:
        "Sexual Desire: [sd], Shame: [shame]."
        "Just chat and flirt." if True:
            mc "Nahh, just kidding! Are you a student too, then?"
            hunk "Oh yeah, I’m actually a second year, what about you?"
            scene bg black with d
            "..."
            "I chatted with the sexy hunk for almost an hour before we parted ways. It was a lot of fun!"
            play sound success
            $ sdgain = 1
            call sdgain from _call_sdgain_183
            "(+[fsd] Sexual Desire)"
            jump postworktrans
        "Public Makeout (30 Sexual Desire, 85 Shame)" if True:
            if sd < 30 or shame > 85:
                "Making out with a stranger on a public beach? That's kinda weird."
                jump sunbathingm2
            mc "Maybe you can pickup where you’d leave off applying sun cream? Hehe."
            hunk "Oh yeah? I think I’d start right here…"
            play sound2 foreplay1
            show malemakeout
            if hair == 1:
                show malemakeouth black
            elif hair == 2:
                show malemakeouth blonde
            with d
            "He pulls me into a kiss, and I fully reciprocate turning it into a French kiss."
            "We savour each other’s lips like a delicacy."
            "Eventually our tongues enter the mix as they dance around with each other."
            if nude == 1:
                "Around that time, I can feel his large, strong hand glide over my tummy, approaching my ass."
            elif True:
                "Around that time, I can feel his large, strong hand glide over my tummy, approaching my bottom bikini."
            menu bpmom:
                "Let him finger your pussy (40 Sexual Desire)" if True:
                    if sd < 40:
                        "I can't let him do that, we're in public!"
                        jump bpmom
                    play ambience sex fadein 1.0
                    show malemakeout2 with d
                    if nude == 1:
                        "I spread my legs open as to welcome his hand, which slips between them and begins to fingering my dripping wet pussy.."
                    elif True:
                        "I spread my legs open as to welcome his hand, which slips under my bikini and begins to fingering my dripping wet pussy.."
                    "It’s really sensitive right now. Getting fingered out here in the open, where anyone could see, is extremely exciting!"
                    "I feel like… If he keeps going, I’ll have a tiny orgasm! Haahh… Mmphhh"
                    play sound cum
                    show malemakeout2 with cum
                    "Unable to hold back a few moans into the kiss, he does successfully manage to get me off, phew..."
                    $ sbmakeout = 1
                "Hold his hand" if True:
                    "To distract him slightly, I clasp his hand, interlocking his fingers so he won’t be able to rub my pussy."
                    "It’s still an affectionate move, and the kiss is only fuelled with more passion as a result."
            stop ambience fadeout 3.0
            stop sound2 fadeout 2.0
            $ kisses += 1
            scene bg black with d
            play sound equip
            call sunbathingart from _call_sunbathingart_3
            "Finishing up, I redress."
            "And we end up chatting for almost an hour before we parted ways. It was a lot of fun!"
            scene bg black with d
            play sound success
            $ publicdisplays += 1
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_129
            call shameloss from _call_shameloss_91
            "(+[fsd] Sexual Desire, -[fshame] Shame)"
            jump postworktrans
        "Public Vaginal? (65 Sexual Desire, 40 Shame)" if True:
            if sd < 65 or shame > 40:
                "Fucking a stranger on a public beach? That's kinda weird."
                jump sunbathingm2

            "Am I really going to have sex with a stranger out in the open?"
            "Hell yes I am."
            show beach1 1b with d
            if nude == 1:
                mc "Mmphh, you know, I did apply sun cream to my butt, but I never went under my bikini… I think I might need some extra protection."
            elif True:
                mc "Mmphh, you know, I did apply sun cream to my butt, but that was a while ago… I think I might need another layer."
            mc "Ohh, but I left my sun cream inside too! Do you have any special cream of your own to help me?"
            hunk "Aren’t you cheeky? If you’re that desperate for it, just come out and say it, then."
            show beach1 1 with d
            mc "Hehe, I’m just super horny! You can take me right here."
            hunk "Cheeky, and daring too. Alright, I’ll come up from behind you, so if anyone walks past from the front, it won’t be obvious that we’re fucking."
            mc "Mmm, good thinking, sexy. They’ll just think I’m sunbathing nude, hehe."
            play sound equip
            scene beach1b
            if tan == 1:
                show beachtan
            if pregnancyshowing == 1:
                show beach1e pregnant
                if tan == 1:
                    show beachtanp
            if hair == 1:
                show beachh black
            elif hair == 2:
                show beachh blonde
            show beach1 1
            if nude == 1:
                pass
            elif True:
                "I drop my bikini to the ground, and lift my butt slightly to give my new partner a better angle."
            mc "I’m all yours…"
            hunk "With pleasure! I know what they said about treasure on beaches, but I wasn’t expecting to find gold today!"
            mc "You know, I love how forward you are. Willing to fuck a girl you’ve just met."
            "He pulls his cock out of his trunks, and mmm it looks big… I can’t help but bite my lip as he glides it back and forth against my pussy lips."
            hunk "How could I refuse such a gorgeous girl? I think many-a-guy would struggle with such an offer."
            $ condomon = 0
            if condoms > 0 and pregnancyshowing == 0:
                menu:
                    "Use a condom? Condoms: [condoms]. [fertilityrate]."
                    "Yeah." if True:
                        $ condomon = 1
                        $ condoms -= 1
                    "Fuck the rules! (Without protection!)" if True:
                        $ condomon = 0
            "Positioning his cock at the entrance to my pussy, he gently pushes forward in this tight position. But my pussy is so wet and ready that I readily accept him."
            play sound2 foreplay1
            play ambience sex
            play sound cum
            show beach1 v3 with d
            call virgin from _call_virgin_4
            hunk "Daammn… Your pussy is so nice and tight, your lips really grip around my cock."
            mc "Mmphh, and your cock fills me up so much, haahh! What a stud, I knew you were hiding something amazing under those trunks."
            "I’m so hot and horny at the risk of being seen. Just like he walked past, anyone else could too. Anyone could see me getting fucked, and that might not even realize it! Or maybe, they will, and that’s equally as hot."
            "Thrusting at a gentle pace as my big spoon, the hunk wraps his hands around to tease and knead my breasts."
            mc "Aahh, ohhh, this is so hot! Mmphh, your cock feels so good right now, and I mean really fucking good! Mmphh…"
            hunk "Oh yeah? Well, how about this?"
            "Taking one of his large hands from my breasts and positioning it between my legs, he begins to attentively rub my clit. My clit is so sensitive right now, that it quickly sends a strident wave of euphoria through my entire body."
            mc "Mmphh, yessshh… Haaahhh. Go harder, fuck me harder! Haahh, aahhh!"
            hunk "Ohh, you like it hard and fast, hmm?"
            mc "Mmm, yeaaahhh!"
            "Holding my hips tightly with his non-clit rubbing hand, he begins to pummel my pussy with vigour."
            mc "Aaahh! I love it! Aaahh, aaaahhh!"
            "While practically fucking me like a pornstar, a couple of people walk past in the distance. Oh gods, they could see me, and it’s making my mind absolutely numb with pleasure at the thought."
            hunk "I can’t hold on much longer, are you close?"
            mc "M-Me? Ahhaa, I’ve come lots of times already! Mmphh, aah-aand I’m close again! Cum with me, inside!"
            play sound cum
            show beach1 v4 with cum
            play sound cum
            show beach1 v4 with cum
            "Almost like I turned on a switch in his head, I can feel him unload deep inside of me. Fucking at such a speed that it froths and bubbles at our wet point of connection."
            play sound cum
            show beach1 v4 with cum
            play sound cum
            show beach1 v4 with cum
            stop ambience fadeout 2.0
            stop sound2 fadeout 5.0
            mc "Mmphhh, mmmm! That’s it! *Pant, pant*"
            "I orgasm too, a strong one this time. My thighs shiver and my mind briefly goes fuzzy as another wave of euphoria washes over me."
            play sound cum
            show beach1 5 with d
            "The hunk pulls out his thick cock, causing a lot of semen to leak out."
            mc "Haah, aaahhh… You really fucked me good… Those guys that walked past totally saw us, haha…"
            hunk "We certainly gave them a good show."
            scene bg black with d
            "…"
            if condomon == 0:
                call pregnancyroll from _call_pregnancyroll_13
            $ vaginalsexes += 1
            $ sbsex = 1
        "Public Anal! (65 Sexual Desire, 40 Shame)" if qanalqueen == 1:
            if sd < 65 or shame > 40:
                "Fucking a stranger on a public beach? That's kinda weird."
                jump sunbathingm2
            jump sunbathinganal
        "Public Anal! (75 Sexual Desire, 50 Shame)" if qanalqueen == 0:
            if sd < 75 or shame > 50:
                "Fucking a stranger on a public beach? That's kinda weird."
                jump sunbathingm2
            label sunbathinganal:
                pass
            "Am I really going to have anal sex with a stranger out in the open?"
            "Hell yes I am."
            show beach1 1b with d
            mc "Mmphh, you know, I’m a special kind of degenerate… What I’m about to ask you might scare off someone that wasn’t as sexy and strong looking as you."
            hunk "Aren’t you cheeky? Just come out and say it, then."
            show beach1 1 with d
            mc "Hehe, I want you to fuck my ass, right here, in the open."
            hunk "Cheeky, and daring too! Your ass? I bet it’s nice and tight."
            hunk "I’ll spoon you from behind you, so if anyone walks past from the front, it won’t one obvious that we’re fucking."
            mc "Mmm, good thinking, sexy. They’ll just think I’m sunbathing nude, hehe."
            play sound equip
            scene beach1b
            if tan == 1:
                show beachtan
            if pregnancyshowing == 1:
                show beach1e pregnant
                if tan == 1:
                    show beachtanp
            if hair == 1:
                show beachh black
            elif hair == 2:
                show beachh blonde
            show beach1 1
            if nude == 1:
                pass
            elif True:
                "I drop my bikini to the ground, and spread my butt slightly to give my new partner a view of my pucker."
            mc "I’m all yours…"
            hunk "I’ll plunder your booty with pleasure."
            mc "You know, I love how forward you are. Willing to fuck a girl you’ve just met in the ass."
            "He pulls his cock out of his trunks, and mmm it looks big… I can’t help but bite my lip as he glides it back and forth against my pussy lips, collecting some juices for lubrication before he moves up to my pucker."
            hunk "How could I refuse such a gorgeous girl? I think many-a-guy would struggle with such an offer."
            play sound2 foreplay1
            play ambience sex
            play sound cum
            show beach1 a3 with d
            "Positioning his cock at my anus, he gently pushes forward. Initially he’s met with some resistance, but as I relax, I slowly accept him deeper."
            hunk "Daammn… Your ass is so nice and tight, it’s really gripping around my cock."
            mc "Mmphh, and your cock fills me up so much, haahh! What a stud, I knew you were hiding something amazing under those trunks."
            "I’m so hot and horny at the risk of being seen. Just like he walked past, anyone else could too. Anyone could see me getting fucked, and that might not even realize it! Or maybe, they will, and that’s equally as hot."
            "Thrusting at a gentle pace as my big spoon, the hunk wraps his hands around to tease and knead my breasts."
            mc "Aahh, ohhh, this is so hot! Mmphh, your cock feels so good right now, and I mean really fucking good! Mmphh…"
            hunk "Oh yeah? Well, how about this?"
            "Taking one of his large hands from my breasts and positioning it between my legs, he begins to attentively rub my clit. My clit is so sensitive right now, that it quickly sends a strident wave of euphoria through my entire body."
            mc "Mmphh, yessshh… Haaahhh. Go harder, fuck me harder! Haahh, aahhh!"
            hunk "Ohh, you like it hard and fast, hmm?"
            mc "Mmm, yeaaahhh!"
            "Holding my hips tightly with his non-clit rubbing hand, he begins to pummel my ass with vigour."
            mc "Aaahh! I love it! Aaahh, aaaahhh!"
            "While practically fucking me like a pornstar, a couple of people walk past in the distance. Oh gods, they could see me, and it’s making my mind absolutely numb with pleasure at the thought."
            hunk "I can’t hold on much longer, are you close?"
            mc "M-Me? Ahhaa, I’ve come lots of times already! Mmphh, aah-aand I’m close again! Cum with me, inside!"
            play sound cum
            show beach1 a4 with cum
            play sound cum
            show beach1 a4 with cum
            "Almost like I turned on a switch in his head, I can feel him unload deep inside of me. Fucking at such a speed that it froths and bubbles at our wet point of connection."
            play sound cum
            show beach1 a4 with cum
            play sound cum
            show beach1 a4 with cum
            stop ambience fadeout 2.0
            stop sound2 fadeout 2.0
            mc "Mmphhh, mmmm! That’s it! *Pant, pant*"
            "I orgasm too, a strong one this time. My thighs shiver and my mind briefly goes fuzzy as another wave of euphoria washes over me."
            play sound cum
            show beach1 5 with d
            "The hunk pulls out his thick cock, causing a lot of semen to leak out."
            mc "Haah, aaahhh… You really fucked me good… Those guys that walked past totally saw us, haha…"
            hunk "We certainly gave them a good show."
            scene bg black with d
            "..."
            $ analsexes += 1
            $ sbsex = 1


    scene bg black with d
    play sound equip
    call sunbathingart from _call_sunbathingart_4
    if nude == 0:
        "Finishing up, I redress."
    elif True:
        "We finish up, and I wash off the cum."
    "And we end up chatting for almost an hour before we parted ways. It was a lot of fun!"
    scene bg black with d
    "Almost hard to believe I fucked him out in the open like that… Hehe."
    play sound success
    $ publicdisplays += 1
    $ sdgain = 1
    $ shameloss = 1
    $ status += 1
    call sdgain from _call_sdgain_130
    call shameloss from _call_shameloss_92
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    jump postworktrans

label sunbathingart:
    scene beach1b
    if tan == 1:
        show beachtan
    if hair == 1:
        show beachh black
    elif hair == 2:
        show beachh blonde
    show beach1 1
    if nude == 1:
        if pregnancyshowing == 1:
            show beach1e pregnant
            if tan == 1:
                show beachtanp
    elif True:
        if pregnancyshowing == 1:
            show beach1e underwearp
            if tan == 1:
                show beachtanunderwearp
        elif True:
            show beach1e underwear
    return
label beachbar:
    play music rest
    scene bg beachbar with d
    "A little closer to the main beach is a quaint bar that serves booze all day."
    "I can think of a few ways that can be fun!"
    if nude == 1:
        call clothes from _call_clothes_4
    elif True:
        call clothesbeach from _call_clothesbeach_2
    show mce happy
    with d
    if nude == 1:
        "Baring all, and getting a lot of looks. I sit myself at one of the bar stools, feeling a little hot and wet down there."
    elif True:
        "In my sexy bikini, I sit myself at one of the bar stools."
    menu:
        "Money: $[money] Sexual Desire: [sd], Shame: [shame]."
        "Order an alcoholic drink (-$10, +5 Sexual Desire, -5 Shame)" if pregnancyshowing == 0:
            $ money -= 10
            $ drunk += 1
            $ sd += 5
            $ shame -= 5
            if qlightweight == 1:
                $ sd += 5
                $ shame -= 5
                "As a lightweight, you feel twice the effects from the alcohol."
            "Ahh, it’s so sweet and refreshing on a hot day. And surprisingly alcoholic! I definitely feel a cosy buzz."
        "Order a soft drink (-$2)" if True:
            $ money -= 2
            "A sweet, refreshing drink to keep me cool on a day like this. Perfect!"
        "Order nothing" if True:
            "I could always use my feminine charm to encourage a boy to buy me a drink!"
    "It’s surprisingly quiet at the bar, but that’s pleasant in its own way. It means I get served drinks quickly, and I can relax."
    if nude == 1:
        "And as a girl, completely nude, at a beach bar, it doesn’t take long for some six-packed hunk in swimming trunks to sit beside me and start a conversation."
    elif True:
        "And as the only girl, in a bikini, at a beach bar, it doesn’t take long for some six-packed hunk in swimming trunks to sit beside me and start a conversation."
    show student3:
        xpos 1200
    with d
    if nude == 1:
        hunk "Woah, I didn't realize this was a nude beach. This seat taken?"
    elif True:
        hunk "Heya, this seat taken?"
    menu bbarm1:
        "Sexual Desire: [sd], Shame: [shame]."
        "Start flirty (10 Sexual Desire)" if True:
            if sd < 10:
                "I'm a little too shy to do that."
                jump bbarm1
            show mce horny with d
            $ genericvariable = 1
            mc "I’m not sure, but just in case, maybe you should sit on my lap."
            hunk "Hahah, can I sit here if I buy you a drink, then?"
        "Act 'normal'" if True:
            show mce happy2 with d
            $ genericvariable = 0
            mc "Not at all! I’d be quite happy for you to sit next to me, I mean, uh, sit there, that is."
            "Stumbling over my words, my nervousness around the beach hunk is obvious."
            hunk "Hahah, would a drink help calm those nerves of yours?"
    menu:
        "Accept a drink (+5 Sexual Desire, -5 Shame)" if pregnancyshowing == 0:
            $ drunk += 1
            $ sd += 5
            $ shame -= 5
            if qlightweight == 1:
                $ sd += 5
                $ shame -= 5
                "As a lightweight, you feel twice the effects from the alcohol."
            show mce laughing with d
            mc "Oohh, thank you. I really appreciate that!"
            hunk "Anything for such a lovely lady."
        "Politely decline" if True:
            show mce happy with d
            hunk "Ahh, no worries. I’ll be ordering something for sure, though."
            mc "Don’t let me stop you."
    show mce horny with d
    "I can’t help but bite my lip slightly as he leans forward to collect his own drink. The way his muscles move and flex is mesmerising."
    menu bbarm3:
        "Just chat" if True:
            if personality == 2 and sd > 60:
                "(Always Horny) I wanna do something lewd!"
                jump bbarm3
            "I chat with the beach hunk for a while, finishing our drinks before he eventually heads out, thanking me for the conversation."
            "It was pleasant from start to end, and put a bit of pep in my step for the rest of the day."
            scene bg beach with d
            "Not to mention… He was hot as hell, and interested in me! I almost feel giddy."
            $ sdgain = 1
            call sdgain from _call_sdgain_131
            "(+[fsd] Sexual Desire!)"
            jump postworktrans
        "Pursue something sexual (50 Sexual Desire)" if True:
            pass

    mc "Mmm, so… You’re pretty hot, if you don’t escape, I might have to do something about it."
    hunk "Oh, yeah? Tell me more."
    mc "Well… Are you staying near here?"
    hunk "I am, but… I’m on vacation with some family. I just came here while I had thirty minutes for a break."
    show mce neutral with d
    mc "Ohh, so we probably can’t do anything…"
    hunk "Hey, what’s a vacation without something exciting and memorable."
    "He points towards the corner of the bar, a slightly more secluded area where we wouldn’t be ‘entirely’ visible if you weren’t paying attention."
    show mce horny with d
    mc "*Gasp* Are you implying what I think you are?"
    hunk "Ahaha, wouldn’t be my first time trying something so risky. It’s more fun."
    "I gulp and take a second to seriously contemplate his decision. I’d love to sleep with him, but at risk of getting caught… that’s something else entirely."
    menu bbarm4:
        "Sexual Desire: [sd], Shame: [shame]."
        "Public Vaginal (65 Sexual Desire, <60 Shame)" if True:
            if sd < 65 or shame > 60:
                "N-No way!"
                jump bbarm4
            play music action
            mc "Okay, let’s do it quickly while it’s still quiet!"
            hunk "Now we’re talkin’!"
            scene standingsexb
            if tan == 1:
                show standingsexbtan
                if pregnancyshowing == 1:
                    show standingsexbtanp
            if hair == 1:
                show standingsexh black
            if hair == 2:
                show standingsexh blonde
            if nude == 0:
                show standingsexswimsuit
            if pregnancyshowing == 1:
                show standingsexe pregnant
                if tan == 1:
                    show standingsexe pregnanttan
            show standingsex 1
            with d
            "Tucked away in the corner of the bar, but still at an angle I could be seen if someone wanted to look this way. I lean over the counter, and present my ass to the sexy stranger."
            play sound equip
            hide standingsexswimsuit with d
            if nude == 0:
                "I wiggle my butt enthusiastically back and forth as he peels my bikini bottoms off, and pulls the string on the bra. The wetness on my pussy is so evident I can even feel it."
            hunk "Daamn, girl! You’re soaked down here, just how horny are you?"
            mc "Haahh, I’m always horny…"
            hunk "Living that college lifestyle to the fullest I see!"
            mc "I-I guess!"
            $ condomon = 0
            if condoms > 0 and pregnancyshowing == 0:
                menu:
                    "Use a condom? Condoms: [condoms]. [fertilityrate]."
                    "Yeah." if True:
                        $ condomon = 1
                        $ condoms -= 1
                    "Fuck the rules! (Without protection!)" if True:
                        $ condomon = 0
            "He shuffles closer and starts to rub my pussy, spreading my puffy lips and teasing my clit. All the motions that’ll help me readily take his cock. Although frankly I think I’m already ready."
            "Fortunately, he doesn’t waste much time as I feel the tip of his thick cock being guided towards my pussy, pushing deeper with no teasing."
            play sound cum
            show standingsex v2 with d
            "Slowly gliding deeper, I can’t help but moan as my soaking wet insides are completely and perfectly filled."
            call virgin from _call_virgin_5
            mc "Mmphhh, haaahhh… So good…"
            play ambience sex
            play sound2 foreplay1
            "Without a chance to savour the feeling, he starts thrusting back and forth. His cock smoothly glides from almost all the way out, to sinking deeply back in. The peak of each thrust drives me wild with pleasure, my fingers tightly gripping the bar as I try to keep quiet."
            hunk "How does it feel? Getting fucked out here, anyone could walk past and see."
            show standingsex v3 with d
            mc "Aahhh, *pant* it’s so hot… I feel like I could lose my mind…"
            hunk "Damn, they really were right about these college sluts."
            "Being called a slut almost ignites my loins in pure lust. The pleasure builds exponentially, and he only thrusts faster at that."
            show standingsex v2 with d
            mc "Ahh, oh my gosh! So deep! Mmpphh, y-you’re gonna make me… Hahh…"
            "A few moans slip out, accompanied by all the lewd wet sounds. I find myself climaxing earlier than usual, my pussy contracting and clenching around my partner."
            show standingsex v3 with d
            mc "Mmphh, cum for me! I want you to fill me up! Ahh, haaahh!"
            play sound cum
            show standingsex v4 with cum
            play sound cum
            show standingsex v4 with cum
            "It didn’t take long for his throbbing cock to soon explode deep inside of me too. My pussy tightly gripped around his shaft, wringing it out for every drop of cum I can as we kept up the pace throughout our orgasms."
            play sound cum
            show standingsex v4 with cum
            play sound cum
            show standingsex v4 with cum
            mc "Oohh, I can feel it… It’s so hot, and there’s so much! Aaahhh…"
            "He keeps thrusting his hips, and I roll mine back into him. It’s ecstasy all the way until my orgasm finally subsides and he slows down."
            play sound cum
            stop ambience fadeout 3.0
            stop sound2 fadeout 5.0
            show standingsex v5 with cum
            "He’s quick to pull out of my pussy, a load of cum dripping out as he does."
            "And within about ninety seconds flat, we managed to fuck behind the bar in complete secrecy."
            hunk "Ho, hoo… Not baaad, not bad at all…"
            "Spreading and playing with my pussy, the hunk chuckles to himself as he slips his swimming trunks back over his junk."
            if nude == 0:
                "I soon follow, slipping my bikini up, and trapping some of the semen under it."
            scene bg beachbar with d
            if nude == 1:
                call clothes from _call_clothes_5
            elif True:
                call clothesbeach from _call_clothesbeach_3
            show mce happy
            show student3:
                xpos 1200
            with d
            hunk "I best get off, my family is gonna be wondering what the hell I’ve been up to. I’ll remember you in therapy, sexy girl!"
            show mce laughing with d
            mc "Yeahh, I’ll remember you in therapy too!"
            hide student3 with d
            show mce horny with d
            "God… When did I become such a slut?"
            "At least no one saw, right?"
            "Riiight…?"
            play sound success
            $ sdgain = 1
            call sdgain from _call_sdgain_132
            $ shameloss = 1
            call shameloss from _call_shameloss_93
            call pregnancyroll from _call_pregnancyroll_14
            $ vaginalsexes += 1
            $ publicdisplays += 1
            $ status += 1
            $ bbsex = 1
            "(+[fsd] Sexual Desire, -[fshame] Shame!)"
            jump postworktrans
        "Public Anal (65 Sexual Desire, <60 Shame)" if qanalqueen == 1:
            if sd < 65 or shame > 60:
                "N-No way!"
                jump bbarm4
            jump bbaranal
        "Public Anal (75 Sexual Desire, <50 Shame)" if qanalqueen == 0:
            if sd < 75 or shame > 50:
                "N-No way!"
                jump bbarm4
            label bbaranal:
                pass
            play music action
            mc "If you want to make it really memorable, why not use my ass? Now that’d be a story to tell when you’re older."
            hunk "Ahaha, it sure would be. You ready for anal?"
            mc "Heh, always."
            scene standingsexb
            if tan == 1:
                show standingsexbtan
                if pregnancyshowing == 1:
                    show standingsexbtanp
            if hair == 1:
                show standingsexh black
            if hair == 2:
                show standingsexh blonde
            if nude == 0:
                show standingsexswimsuit
            if pregnancyshowing == 1:
                show standingsexe pregnant
                if tan == 1:
                    show standingsexe pregnanttan
            show standingsex 1
            with d
            "Tucked away in the corner of the bar, but still at an angle I could be seen if someone wanted to look this way. I lean over the counter, and present my ass to the sexy stranger."
            play sound equip
            hide standingsexswimsuit with d
            if nude == 0:
                "I wiggle my butt enthusiastically back and forth as her peels my bikini bottoms off, and pulls the string on the bra. The wetness on my pussy is so evident I can even feel it."
            hunk "Daamn, girl! You’re soaked down here, just how horny are you?"
            mc "Haahh, I’m always horny…"
            hunk "Of course, you’re more of a butt slut, aren’t you?"
            mc "When I want to be!"
            "He shuffles closer and starts to rub my pucker, spreading my ass cheeks slightly and dripping some of his spit to use as lubrication. All the motions that’ll help me readily take his cock. Although frankly I think I’m already ready."
            "Fortunately, he doesn’t waste much time as I feel the tip of his thick cock being guided towards my ass, pushing deeper with no teasing."
            play sound cum
            show standingsex a2 with d
            "Slowly gliding deeper, I can’t help but moan as my ass is completely and perfectly filled."
            mc "Mmphhh, haaahhh… So good…"
            play ambience sex
            play sound2 foreplay1
            "Without a chance to savour the feeling, he starts thrusting back and forth. Thanks to the saliva, his cock smoothly glides from almost all the way out, to sinking deeply back in. The peak of each thrust drives me wild with pleasure, my fingers tightly gripping the bar as I try to keep quiet."
            hunk "How does it feel? Getting fucked out here, anyone could walk past and see."
            show standingsex a3 with d
            mc "Aahhh, *pant* it’s kinda painful, but in a good way, it feels so amazing… I feel like I could lose my mind…"
            hunk "Damn, they really were right about these college sluts."
            "Being called a slut almost ignites my loins in pure lust. The pleasure builds exponentially, and he only thrusts faster at that."
            show standingsex a2 with d
            mc "Ahh, oh my gosh! So deep! Mmpphh, y-you’re gonna make me… Hahh…"
            "A few moans slip out, accompanied by all the lewd wet sounds. I find myself climaxing earlier than usual, my pussy contracting, and my ass clenching around my partner."
            show standingsex a3 with d
            mc "Mmphh, cum for me! I want you to fill me up! Ahh, haaahh!"
            play sound cum
            show standingsex a4 with cum
            play sound cum
            show standingsex a4 with cum
            "It didn’t take long for his throbbing cock to soon explode deep inside of me too. My pucker grips like a ring around his shaft, wringing it out for every drop of cum I can as we kept up the pace throughout our orgasms."
            play sound cum
            show standingsex a4 with cum
            play sound cum
            show standingsex a4 with cum
            mc "Oohh, I can feel it… It’s so hot, and there’s so much! Aaahhh…"
            stop ambience fadeout 3.0
            stop sound2 fadeout 5.0
            "He keeps thrusting his hips, and I roll mine back into him. It’s ecstasy all the way until my orgasm finally subsides and he slows down."
            play sound cum
            show standingsex a5 with cum
            "He’s quick to pull out of my ass, a load of cum dripping out as he does."
            "And within about ninety seconds flat, we managed to fuck behind the bar in complete secrecy."
            hunk "Ho, hoo… Not baaad, not bad at all…"
            "Spreading and playing with my ass, the hunk chuckles to himself as he redresses."
            if nude == 0:
                "I soon follow, slipping my bikini up, and trapping some of the semen under it."
            scene bg beachbar with d
            if nude == 1:
                call clothes from _call_clothes_17
            elif True:
                call clothesbeach from _call_clothesbeach_4
            show mce happy
            show student3:
                xpos 1200
            with d
            hunk "I best get off, my family is gonna be wondering what the hell I’ve been up to. I’ll remember you in therapy, sexy girl!"
            show mce laughing with d
            mc "Yeahh, I’ll remember you in therapy too!"
            hide student3
            show mce horny
            with d
            "God… When did I become such a slut?"
            show mce neutral with d
            "At least no one saw, right?"
            "Riiight…?"
            play sound success
            $ sdgain = 1
            call sdgain from _call_sdgain_133
            $ shameloss = 1
            call shameloss from _call_shameloss_94
            $ analsexes += 1
            $ publicdisplays += 1
            $ status += 1
            $ bbsex = 1
            "(+[fsd] Sexual Desire, -[fshame] Shame!)"
            jump postworktrans
        "Apologize for being a wimp" if True:
            if personality == 2 and sd > 85:
                "(Always Horny) I gotta try it!"
                jump bbarm4
            show mce sad with d
            mc "Phew… Sorry, I don’t quite have the temperament to do something so lewd!"
            hunk "Ahaha, especially with a stranger. I don’t blame ya."
            show mce happy with d
            "I chat with the beach hunk for a while, finishing our drinks before he eventually heads out, thanking me for the conversation."
            "It was pleasant from start to end, and put a bit of pep in my step for the rest of the day."
            scene bg beach with d
            "Not to mention… He was hot as hell, and interested in me! I almost feel giddy."
            play sound success
            $ sdgain = 1
            call sdgain from _call_sdgain_134
            "(+[fsd] Sexual Desire!)"
            jump postworktrans
label susuroute:
    if susuroute1 == 0:
        jump susuroute1
    elif susuroute2 == 0:
        jump susuroute2
    elif susuroute3 == 0:
        jump susuroute3
    elif True:
        jump susuroute4

label susuroute4:
    scene bg house2
    if nude == 1:
        call clothes from _call_clothes_18
    elif True:
        call clothesbeach from _call_clothesbeach_5
    show mce happy
    show susub:
        xpos 1200
    show susuo swimsuit:
        xpos 1200
    show susue happy:
        xpos 1200
    with d
    with d
    if nude == 1:
        susu "Well look at you! You're already ready for a good time."
    elif True:
        susu "Heyy, [mc]! It’s nice to see you. I don’t have anyone around this time, buuut… I think we should go and find someone."
    show mce horny with d
    mc "Easy, I’ve barely got my foot in the door and you’re already suggesting a threesome."
    susu "Hehe, I won’t be this young, flexible and horny all my life. Let’s go to the bar?"
    menu sur4m1:
        "Sexual Desire: [sd], Shame: [shame]"
        "Let’s relax together" if True:
            jump susulesbianmenu
        "Let’s go to the bar (Sexual Desire 75, Shame <50)" if True:
            if sd < 75 or shame > 50:
                "We're going to the bar specifically to pick someone up for a threesome. I know I've done it before, but I'm too nervous to go and actually ask someone!"
                jump sur4m1
            pass
    show mce laughing with d
    mc "Alright, let’s go find a hottie and get you fucked."
    susu "Yaaay! Hahaha."
    scene bg beachbar with d
    "It wasn’t hard for two attractive girls to find a good-looking guy willing to come with us."
    $ susuroute4 = 1
    scene bg house2
    if nude == 1:
        call clothes from _call_clothes_50
    elif True:
        call clothesbeach from _call_clothesbeach_6
    show mce happy
    show susub:
        xpos 1200
    show susuo swimsuit:
        xpos 1200
    show susue happy:
        xpos 1200
    with d
    show student1:
        xpos 50
    with d
    hunk "So… How are we going to do this? Are you going to get on top of her?"
    susu "How about I get on top? I'm smaller!"
    mc "Oohh, you're making me feel all hot and gooey. Let's do it!"
    play sound equip
    scene bg black with d
    "And pushing me down she does, as one by one she removes my clothes."
    "With her clothes soon coming off too, it isn't long until...!"
    play ambience oral1 fadein 2.0
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
    susu "Mmpphh, [mc]... I love being between your legs…"
    "I try to reply, but I just find [susu]'s pussy pressed against my face with a lustful energy. This not only silences me, but also prompts me to stick my tongue out and begin to focus on her swollen clit."
    "[susu], however, takes her time. She begins by teasingly kissing my thighs and gently grazing her fingers around my labia. Her delicate movements leave me absolutely throbbing with desire."
    "And what’s when our third fighter joins the fray as the man we picked up from the bar presses his erection against [susu]’s tight pussy."
    play sound cum
    show yuri69 1 with cum
    "With a satisfying schlick, he pushes in deeper as I flick my tongue across the point at which his cock connects with her pussy."
    play sound2 foreplay2 fadein 1.0
    play ambience sex fadein 2.0
    "AS he begins to thrust, I feel the warm press of [susu]’s long tongue against my aching clit, swiping back and forth, sending shivers of pure ecstasy through my nerves."
    susu "Mmm, ahhh... So thiiick, I don’t think I can handle you both! Hehe..."
    mc "Mmphh... *Lick* Quite a popular girl, aren’t you?"
    susu "Oohh, is that some jealousy? Here, let me sate that lust."
    "She speeds up, and I try to match her pace. Before we know it, we're both panting, and struggling to hold back moans."
    "Holding onto her hips, the hunk begins to piston rapidly in and out of [susu]’s pussy. It’s so messy that droplets of her wetness drip onto my face."
    susu "Aaahh! Ahh, I-I'm gonna come any second! K-Keep going!"
    mc "Mmphh, ahhh, m-me too!"
    "Determined, our tongues both focus our clits, swiping and twirling around to induce as much pleasure as possible from our lover."
    "The hunk’s hands grip tightly as he pushes himself hard, his body slapping repeatedly against [susu]’s butts as he prepares to unload."
    "The pleasure rises exponentially until we both hit our absolute limit."
    susu "Ohh god, oohhh, I-I'm gonna-"
    play sound cum
    show yuri69 2 with cum
    "Even as cum splatters and drips all over my face, I can't feel anything else except the electrifying pleasure of [susu]'s tongue rubbing my clit. It radiates all over my body as I'm brought to a powerful orgasm."
    play sound cum
    show yuri69 2 with cum
    "We both squirm with delight as euphoria washes over our bodies, and we desperately try to continue licking throughout."
    "Soon after, the euphoria melts away and is replaced with a calm feeling of peace and relief as I'm brought back to reality."
    play sound cum
    show yuri69 3 with cum
    "The man pulls out, dripping a little extra semen onto my face as I get the opportunity to admire [susu]’s gooey pussy."
    mc "Mmphh, stay still… I can’t help myself."
    stop sound2 fadeout 3.0
    "I playfully flick my tongue around [susu]’s cum-covered vulva one last time."
    stop ambience fadeout 1.0
    play sound equip
    scene bg house2
    call clothesnude from _call_clothesnude_6
    show mce happy
    show susub:
        xpos 1200
    show susue happy:
        xpos 1200
    with d
    with d
    susu "Haaahhh, wow... A part of me can't believe I just did that! And, I think we’re about to do it again, right?"
    mc "Yupo! My turn!"
    scene bg black with d

    $ sdgain = 2
    $ shameloss = 1
    call sdgain from _call_sdgain_135
    call shameloss from _call_shameloss_95
    $ vaginalsexes += 1
    $ lesbian += 1
    $ status += 2
    $ groupsexes += 1
    play sound success
    "(+[fsd] Sexual Desire, -[fshame] Shame)"
    jump postworktrans
label susuroute3:
    scene bg house2
    if nude == 1:
        call clothes from _call_clothes_51
    elif True:
        call clothesbeach from _call_clothesbeach_7
    show mce happy
    show susub:
        xpos 1200
    show susuo swimsuit:
        xpos 1200
    show susue happy:
        xpos 1200
    with d
    susu "Heyy, [mc]! Come in, we have a guest!"
    mc "Huh? Who is this?"
    show student4:
        xpos 50
    if nude == 1:
        hunk "Woah! A naked chick! Jackpot."
    elif True:
        hunk "Hey there!"
    susu "This is Chad, some guy from the beach bar I picked up."
    show mce neutral with d
    "Hmm... She really wasn't kidding about bringing guys over here, was she?"
    "[susu] is very bisexual, that much is clear."
    show mce happy with d
    mc "Hello, Chad."
    hunk "Hey, sexy!"
    show mce horny with d
    mc "I’m not interrupting anything, am I?"
    show susue horny with d
    susu "Well, not yet, but we were gonna make out a bit… I bet you want in though, don’tcha?"
    show mce happy2 with d
    "Hmm… I could probably cuck Chad if I wanted, or maybe I could join in on whatever they had planned…"
    menu sur3m1:
        "Sexual Desire: [sd], Shame: [shame]"
        "Threesome (Sexual Desire 65, Shame <65)" if True:
            if sd < 65 or shame > 65:
                "I really don't want to do that."
                jump sur3m1
            susu "Both of us? At the same time?"
            show mce horny with d
            mc "Yeah, how about it?"
            susu "Hehe, you're outrageous, [mc]... Okay, let's do it!"
            scene bg black with d
            "Both completely nude, [susu] and I take control of the situation to tease and toy with the boy."
            play music action
            scene ffmthreesomeb
            if tan == 1:
                show ffmthreesomebtan
            if hair == 1:
                show ffmthreesomeh black
            if hair == 2:
                show ffmthreesomeh blonde
            show ffmthreesome 1
            with d
            susu "Ohh, you're dripping wet, [mc]! So naughty!"
            mc "Ahhh, I think I'm ready for your big cock! Fuck me hard!"
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
            show ffmthreesome 2 with cum
            "Without messing around, he brings the tip of his cock to my pussy and slowly slides inside. It's so thick that mere penetration causes me to shiver and moan loudly."
            call virgin from _call_virgin_6
            play ambience sex fadein 3.0
            play sound2 foreplay2 fadein 3.0
            "With his hands on my hips, he begins vigorously fucking me. As his cock throbs, my pussy clenches around him tighter."
            "Having fun with one of my girlfriends makes this even more fun! [susu] wastes no time teasing all my weak spots. Moving from kissing me, to kneading my breasts, and even rubbing my clit."
            mc "Aahhh, yesss! Mmmmhh..."
            susu "Ooohhh, you're really filling her up! I can see her lips tightly gripping around your shaft."
            "The thrusts start to come faster, and in my enthusiasm, I try to match the thrusts by bouncing my butt against him. This results in hard, deep thrusts that pleasure every inch of my insides."
            "At this speed I'm really starting to get pushed over the edge. My muscles tense up, and my pussy tightens as my orgasm rises."
            mc "Aaahhh, f-fuuuckk! I-I'm gonna come!"
            susu "Oohh, yesss... Cum inside her, fill her pussy up!"
            "He starts to fuck my pussy as fast as he can, easily pushing me to a climax as he barrels towards his."
            mc "Y-Yes! I'm coming! Ahhh, aahhh."
            play sound cum
            show ffmthreesome 3 with cum
            play sound cum
            show ffmthreesome 3 with cum
            "Almost immediately as I moan, I feel a load shooting deep inside my pussy. The thick, hot cum seeps throughout me as we continue to fuck each other intensely."
            play sound cum
            show ffmthreesome 3 with cum
            play sound cum
            show ffmthreesome 3 with cum
            "After a few more loads of cum, the euphoria dissipates and we come to a stop."
            mc "*Pant, pant* That was so good, haaahh..."
            show ffmthreesome 4 with d
            stop ambience fadeout 1.0
            stop sound2 fadeout 1.0
            "Pulling out, cum freely drips from my pussy."
            susu "Ooohhh, so lewd, so naughty!"
            susu "My turn next, right? Hehe."
            scene bg black with d
            play sound success
            call pregnancyroll from _call_pregnancyroll_15
            $ sdgain = 2
            $ shameloss = 1
            call sdgain from _call_sdgain_136
            call shameloss from _call_shameloss_96
            $ status += 2
            $ vaginalsexes += 1
            $ groupsexes += 1
            $ susuroute3 = 1
            "(+[fsd] Sexual Desire, -[fshame] Shame)"
        "Wanna watch us make out, Chad?" if True:
            hunk "Awhh, hell yeah!"
            susu "Oohh, I like that idea… Come here you!"
            "Successfully occupying [susu] all to myself…"
            play sound equip
            scene bg house2
            show yomomakeout1
            with d
            play sound foreplay1
            "Our hands are quick to wrap around each other as she pulls me down into a kiss, one of her legs lifting up around mine and wrapping around."
            "Lips smack and tongues twirl as we roll around on the sofa in loving fashion."
            "The third wheel watches from a sofa, as he takes his cock out of his trunks and begins to masturbate at the sight. I don’t blame him, we’re hot as hell!"
            "She takes my hand and redirects it close to her thighs, where I affectionately brush my hands back and forth, although the true desire of [susu] is clear as her legs spread a little wider."
            show yomomakeout2 with d
            "I bring my fingers to her clit, and rub it in a focused manner. The high amount of pleasure contained within [susu] is immediately clear as her body shivers and spasms."
            play sound cum
            show yomomakeout1 with cum
            "I continue rubbing until the cute frog girl climaxes."
            "And it seems our third rubber has gotten himself off too, as he cums alone in the corner."
            hide yomomakeout2 with d
            "Eventually, our lips part and we return to our original positons."
            play sound success
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_137
            call shameloss from _call_shameloss_97
            $ kisses += 1
            $ groped += 1
            "(+[fsd] Sexual Desire, -[fshame] Shame)"
    scene bg house2
    if nude == 1:
        call clothes from _call_clothes_52
    elif True:
        call clothesnude from _call_clothesnude_7
    show mce happy
    show susub:
        xpos 1200
    show susue happy:
        xpos 1200
    show student4:
        xpos 50
    with d
    mc "Mmphh... I really enjoyed that."
    hunk "Yeah, that was super-hot!"
    susu "Hehe. I guess that’s that, huh?"
    mc "How about we go get some sun?"
    susu "Sure thing!"
    scene bg beach with d
    "We chill at the beach for a few hours before going our separate ways."
    jump postworktrans
label susuroute2:
    scene bg beachhut
    if nude == 1:
        call clothes from _call_clothes_53
    elif True:
        call clothesbeach from _call_clothesbeach_8
    show mce happy
    mc "Heyy Suuu! I better not catch you with your panties off!"
    show susub:
        xpos 1200
    show susuo swimsuit:
        xpos 1200
    show susue happy:
        xpos 1200
    with d
    if nude == 1:
        susu "Ahaha, as if you can talk! You're baring all!"
        susu "Maybe you could help me build up enough confidence to do that too?"
    elif True:
        susu "Ahaha, that is not the thing I want to become known for!"
        mc "What would you rather be known for?"
        susu "Mmmm, the girl that has her panties removed by you?"
    show susue horny
    show mce laughing
    with d
    "She winks and encourages me to follow her into her room."
    scene bg black with d
    scene bg house2
    if nude == 1:
        call clothes from _call_clothes_54
    elif True:
        call clothesbeach from _call_clothesbeach_9
    show mce happy
    show susub:
        xpos 1200
    show susuo swimsuit:
        xpos 1200
    show susue happy:
        xpos 1200
    with d
    susu "Are you horny? We could really turn up the heat."
    mc "Are you? You always seem horny."
    susu "Ahh, you know what they say about animal powers, we are indeed a little hornier than the average person."
    mc "Well, I suppose we could..."
    label susulesbianmenu:
        pass
    menu ssr2m1:
        "Sixty-Nine (45 Sexual Desire)" if True:
            if sd < 45:
                "I can't ask that... There's no way she'd agree to it, right?"
                jump ssr2m1
            $ susuroute2 = 1
            mc "Do you wanna uhhhmm, kiss somewhere else? Hehe... I know I would."
            susu "Ohh, I do, I really do! How about I get ontop? I'm smaller!"
            mc "Oohh, you're making me feel all hot and gooey. Let's do it!"
            play sound equip
            scene bg black with d
            "And pushing me down she does, as one by one she removes my clothes."
            "With her clothes soon coming off too, it isn't long until...!"
            play ambience oral1 fadein 2.0
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
            susu "Mmpphh, [mc]... I think I like you a lot."
            "I try to reply, but I just find [susu]'s pussy pressed against my face with a lustful energy. This not only silences me, but also prompts me to stick my tongue out and begin to focus on her swollen clit."
            "[susu], however, takes her time. She begins by teasingly kissing my thighs and gently grazing her fingers around my labia. Her delicate movements leaves me absolutely throbbing with desire."
            "That's when I feel the warm press of her long tongue against my aching clit, swiping back and forth, sending shivers of pure ecstasy through my nerves."
            "The tongue is a lot cooler and longer than anything I've felt before, and the unusual feeling only adds to the overall experience."
            susu "Mmm, ahhh... I imagine I'll become quite popular with the ladies when they realize how good I am with my tongue, hehe..."
            mc "Mmphh... *Lick* The only popularity you need with that is me."
            susu "Oohh, is that some jealousy? Here, let me sate that lust."
            "She speeds up, and I try to match her pace. Before we know it, we're both panting, and struggling to hold back moans."
            susu "Aaahh! You're great with your tongue too! Ahh, I-I'm gonna come any second! K-Keep going!"
            mc "Mmphh, ahhh, m-me too!"
            "Determined, our tongues both focus on our clits, swiping and twirling around to induce as much pleasure as possible from our lover."
            "The pleasure rises exponentially until we both hit our absolute limit."
            susu "Ohh god, oohhh, I-I'm gonna-"
            play sound cum
            show yuri69orgasm with cum
            "I can't feel anything else except the electrifying pleasure of [susu]'s tongue rubbing my clit. It radiates all over my body as I'm brought to a powerful orgasm."
            play sound cum
            show yuri69orgasm with cum
            "We both squirm with delight as euphoria washes over our bodies, and we desperately try to continue licking throughout."
            "Soon after, the euphoria melts away and is replaced with a calm feeling of peace and relief as I'm brought back to reality."
            stop ambience fadeout 1.0
            play sound equip
            scene bg house2
            call clothesnude from _call_clothesnude_8
            show mce happy
            show susub:
                xpos 1200
            show susue happy:
                xpos 1200
            with d
            susu "Haaahhh, wow... A part of me can't believe I just did that! I've never done anything quite so intimate with another girl before."
            mc "Did you enjoy it?"
            "I ask as I snuggle a little closer, my hands wrapping around her waist."
            susu "Yeahh, I really did! I never imagined we'd upgrade our friendship to one with benefits, but how can I complain after something that amazing?"
            susu "Let's get a guy in here next time! I wanna suck his cock fresh after it's fucked you."
            show mce laughing with d
            mc "*Giggles* You're even lewder than I am!"
            scene bg black with d
            $ sdgain = 1
            $ lesbian += 1
            call sdgain from _call_sdgain_89
            play sound success
            "(+[fsd] Sexual Desire)"
        "Make-out with [susu]" if True:
            mc "Ahh, come here you minx!"
            play sound equip
            scene bg house2
            show yomomakeout1
            with d
            play sound2 foreplay1
            "Our hands are quick to wrap around each other as she pulls me down into a kiss, one of her legs lifting up around mine and wrapping around."
            "Lips smack and tongues twirl as we roll around on the sofa in loving fashion."
            "She takes my hand and redirects it close to her thighs, where I affectionately brush my hands back and forth, although the true desire of [susu] is clear as her legs spread a little wider."
            menu ssr2m2:
                "Rub her pussy" if True:
                    show yomomakeout2
                    with d
                    "I bring my fingers to her clit, and rub it in a focused manner. The high amount of pleasure contained within [susu] is immediately clear as her body shivers and spasms."
                    "I continue rubbing until the cute frog girl climaxes."
                "That's enough" if True:
                    "I make my boundaries clear, but continue to kiss [susu]."
            stop sound2
            scene bg house2
            call clothesbeach from _call_clothesbeach_10
            show mce happy
            show susub:
                xpos 1200
            show susuo swimsuit:
                xpos 1200
            show susue happy:
                xpos 1200
            with d
            "Eventually, our lips part and we return to our original positons."
            mc "Mmphh... I really enjoyed that."
            susu "Yeahhh, me too... I wouldn't mind playing around with you if that's something you'd be open with."
            mc "Like, an open thing?"
            susu "Mhm, you wash my back, and I'll wash yours!"
            $ sdgain = 1
            $ kisses += 1
            call sdgain from _call_sdgain_54
            play sound success
            "(+[fsd] Sexual Desire)"
        "Go out to the beach" if True:
            susu "That's okay too! I wouldn't want to make you feel pressured into anything."
            mc "Ahh don't worry about it. Having someone as cute as you flirt with me is always an ego-boost."
    scene bg black with d
    show bg beachhut
    if nude == 1:
        call clothes from _call_clothes_55
    elif True:
        call clothesbeach from _call_clothesbeach_11
    show mce happy
    show susub:
        xpos 1200
    show susuo swimsuit:
        xpos 1200
    show susue happy:
        xpos 1200
    with d
    "We spend some time swimming, getting a tan, and having a few drinks together!"
    play sound success
    "(+1 [susu] Affection!)"
    $ susuroute1intro = 1
    jump postworktrans
label susuroute1:
    if susuroute1intro == 0:
        "Hmm... Where is [susu]? I think she actually has a bedroom somewhere in this hut. It's impressively sized."
        scene bg house2
        if nude == 1:
            call clothes from _call_clothes_56
        elif True:
            call clothesbeach from _call_clothesbeach_12
        show mce happy
        with d
        mc "[susu]! [susu]?"
        show susub:
            xpos 1200
        show susue neutral:
            xpos 1200
        with d
        show mce sad with d
        mc "Eek, I'm so sorry!"
        play sound equip
        show susuo swimsuit:
            xpos 1200
        with d
        "[susu] moves quickly to cover herself up, and she bashfully giggles once she's successfully. I accidentally walked in her masturbating! Woops."
        show susue happy with d
        susu "My baaad! I've always got my panties around my ankles in here, hahaha. It's usually always empty, so..."
        if nude == 1:
            susu "And you're naked anyway, so... Wait, why are you naked?"
            mc "Ehhh, I'm a free spirit, i guess? Hehe."
        elif True:
            mc "O-Oh, I really should have knocked."
        show susue horny with d
        susu "I don't mind if it's you."
        susu "Although, I suppose... If you're here, do you want toooo... aaahh, please join in!"
        play music action
        show mce horny with d
        "A hot blush encompasses my face as [susu] moves to uncover herself."
    elif True:
        scene bg house2
        if nude == 1:
            call clothes from _call_clothes_57
        elif True:
            call clothesbeach from _call_clothesbeach_13
        show mce happy
        mc "Heyy, [susu]!"
        show mce horny with d
        mc "Huh?"
        show susub:
            xpos 1200
        show susuo swimsuit:
            xpos 1200
        show susue happy:
            xpos 1200
        with d
        susu "Huh?! Heyy, how do we keep catching each other like this!"
        "She giggles as her bikini is around her ankles, her hand between her thighs barely covering her pussy."
        susu "I haven't even finished yet! Did you want to join in that badly?"
    menu ssr1m1:
        "Make-out with [susu] (15 Sexual Desire)" if True:
            if sd < 15:
                "I-I'm too nervous!"
                jump ssr1m1
            $ susuroute1 = 1
            mc "Mmm, what a shame that you couldn't finish. Maybe I can help you with that."
            play sound equip
            scene bg house2
            show yomomakeout1
            with d
            play sound2 foreplay1
            "Our hands are quick to wrap around each other as she pulls me down into a kiss, one of her legs lifting up around mine and wrapping around."
            "Lips smack and tongues twirl as we roll around on the sofa in loving fashion."
            "She takes my hand and redirects it close to her thighs, where I affectionately brush my hands back and forth, although the true desire of [susu] is clear as her legs spread a little wider."
            menu ssr1m2:
                "Rub her pussy (25 Sexual Desire)" if True:
                    if sd < 25:
                        "I'm not quite ready to do something like that."
                        jump ssr1m2
                    show yomomakeout2
                    with d
                    "I bring my fingers to her clit, and rub it in a focused manner. The high amount of pleasure contained within [susu] is immediately clear as her body shivers and spasms."
                    "I continue rubbing until the cute frog girl climaxes."
                "That's enough" if True:
                    "I make my boundaries clear, but continue to kiss [susu]."
            stop sound2
            scene bg house2
            if nude == 1:
                call clothes from _call_clothes_58
            elif True:
                call clothesnude from _call_clothesnude_9
            show mce happy
            show susub:
                xpos 1200
            show susue happy:
                xpos 1200
            with d
            "Eventually, our lips part and we return to our original positons."
            mc "Mmphh... I really enjoyed that."
            susu "Yeahhh, me too... I wouldn't mind playing around with you if that's something you'd be open with."
            mc "Like, an open thing?"
            susu "Mhm, you wash my back, and I'll wash yours!"
            $ sdgain = 1
            $ kisses += 1
            call sdgain from _call_sdgain_90
            play sound success
            "(+[fsd] Sexual Desire)"
        "Sorry, too shy!" if True:
            susu "Haahh, that's fine! Probably not the best situation to ask, I'm just a little horny right now, hehe."
    scene bg black with d
    "A few minutes later, after we've both cooled down from the unexpected event!"
    show bg beachhut
    if nude == 1:
        call clothes from _call_clothes_59
    elif True:
        call clothesbeach from _call_clothesbeach_14
    show mce happy
    show susub:
        xpos 1200
    show susuo swimsuit:
        xpos 1200
    show susue happy:
        xpos 1200
    with d
    "We spend some time swimming, getting a tan, and having a few drinks together!"
    play sound success
    "(+1 [susu] Affection!)"
    $ susuroute1intro = 1
    $ susuaffection += 1

jump postworktrans
init:
    $ beachvisited = 0
    $ susuaffection = 0
    $ susuroute1 = 0
    $ susuroute1intro = 0
    $ susuroute2 = 0
    $ susuroute3 = 0
    $ susuroute4 = 0
    $ sbmakeout = 0
    $ sbsex = 0
    $ bbsex = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
