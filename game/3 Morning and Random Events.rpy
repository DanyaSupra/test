label morning:
    stop ambience
    scene bg black with d
    call dream from _call_dream
    play music daytime fadein 3.0
    show bg bedroomday with dissolve
    call morningeffects from _call_morningeffects
    if endingsunlocked == 0 and days > 31:
        show mce happy with d
        $ endingsunlocked = 1
        "It's officially been a month since I started college!"
        "With so many possible paths ahead of me, just what kind of person will I become?"
        play sound success
        "(Endings unlocked!)"
        "(Endings allow you to view one of many possible futures [mc] could pursue in her life based on your decisions so far.)"
        "(These are only glimpses, though, after viewing an ending, you will return back to the bedroom.)"
    if collegetutorial == 0:
        $ collegetutorial = 1
        "(Every morning you will be expected to go to college. There are consequences if you don't, and benefits if you do.)"
        "(You can visit the college by going 'outside', and selecting the 'College' location.)"
    if event == 6 or event == 7:
        jump weekend
    label bedroommorning:
        scene bg bedroomday
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
        call clothes from _call_clothes_19
        show mce happy:
            xpos 850
        with d
        show bedroom screen border
        $ dsd = int(sd)
        $ dshame = int(shame)+1
        call screen bedroom
        with d



label event:
    stop music fadeout 1.0
    play music rest
    $ morning = 0
    label extraevents:
        if crushmet == 0:
            jump crushintro
        if event == 5:
            jump eventtest
        if shame < 70 and studiounlocked == 0:
            label studiounlock:
                pass
            $ studiounlocked = 1
            scene bg street2
            call clothesformal from _call_clothesformal
            show mce happy
            with d
            $ maledormsunlocked = 1
            "While walking around the streets... Ohh, what's this?"
            "A poster, 'Looking for models, pays well $$$.'"
            show mce laughing with d
            "Oohhh, pays well!"
            "I don't mind showing myself off if it pays!"
            "I should visit this 'Studio' when I have the chance."
            play sound success
            "(Studio unlocked!)"
            $ shameloss = 1
            call shameloss from _call_shameloss_68
            "(-[fshame] Shame)"
            if morning == 1:
                jump postworldmap
            jump prebedroom
        if sd > 30 and stripclubunlocked == 0:
            label stripclubunlock:
                pass
            $ stripclubunlocked = 1
            scene bg street2
            call clothesformal from _call_clothesformal_1
            show mce happy
            with d
            "This building I walk past every time I go shopping... I knew it, it's a strip club!"
            "I can't believe I'm saying this, but it sounds like fun!"
            "I wouldn't mind checking it out..."
            play sound success
            $ sdgain = 1
            call sdgain from _call_sdgain_61
            "(+[fsd] Sexual Desire)"
            menu:
                "Visit Strip Club" if True:
                    jump stripclub2
                "Pass" if True:
                    "Ahh, maybe not... But, I'll keep it in the back of my mind."
                    if morning == 1:
                        jump postworldmap
                    jump prebedroom
        if massageparlourunlocked == 0 and sd > 20:
            label massageunlock:
                pass
            scene bg street2
            call clothesformal from _call_clothesformal_2
            show mce horny
            with d
            $ massageparlourunlocked = 1
            "I've been putting this off for a while, but there's this massage parlour shop really close to the female dorms."
            "I wonder if I should work there?"
            "What kind of massage parlour is it, anyway?"
            "Only one way to find out!"
            play sound success
            "(Massage Parlour unlocked!)"
            menu:
                "Visit Massage Parlour" if True:
                    jump massage
                "Pass" if True:
                    "Ahh, maybe not... But, I'll keep it in the back of my mind."
                    if morning == 1:
                        jump postworldmap
                    jump prebedroom
        if sd > 50 and shame < 50 and boyfriend == 0 and maledormsunlocked == 0:
            label maledormsunlock:
                pass
            scene bg maledorms
            call clothesformal from _call_clothesformal_3
            show mce horny
            with d
            $ maledormsunlocked = 1
            "Walking past the boys dorms, I see a fellow student sitting at a bench on his own, eating some lunch."
            "Hmm... I just had the radical idea to offer this guy a blowjob in exchange for $40..."
            "I mean... it wouldn't be that hard, would it? It might even be fun."
            play sound success
            "(Male Dorm Prostitution unlocked!)"
            $ sdgain = 1
            $ shameloss = 1
            call sdgain from _call_sdgain_102
            call shameloss from _call_shameloss_69
            "(+[fsd] Sexual Desire, -[fshame] Shame!)"
            $ moneygain = 40
            call moneycalculate from _call_moneycalculate
            menu:
                "Sexual Desire: [sd], Shame: [shame]"
                "Offer a Blowjob for $[fmoney]" if True:
                    "Hehe, this should be easy... All these students have loans and more money than sense."
                    jump maledormblowjob
                "Pass" if True:
                    "Ahh, maybe not... But, I'll keep it in the back of my mind as a money making scheme."
                    if morning == 1:
                        jump postworldmap
                    jump prebedroom
        if lewdoutfit == 1 and parkunlocked == 0 or nude == 1 and parkunlocked == 0 or sd > 100 and parkunlocked == 0:
            jump parkintro
        if dungeonunlocked == 0 and sd > 50:
            label dungeonunlock:
                pass
            play music girls
            scene bg street2 with d
            "While out and about today, I run into a student that's in some of my classes."
            call clothesformal from _call_clothesformal_4
            show mce happy
            show mikab:
                xpos 1200
            show mikao casual:
                xpos 1200
            show mikae happy:
                xpos 1200
            with d
            unknown "Hey, [mc]! How’s it hanging?"
            "Ah, it’s the slightly punk girl from my class, I wonder what she wants with me?"
            python:
                mika = renpy.input("Name the Punk (and Dominatrix) Girl. Leave blank for the default name 'Miku'.")
                mika = mika.strip()
                if not mika:
                    mika = "Miku"
            mc "I’m doing good, thanks, [mika]. Did you need something?"
            mika "I’ve been noticing you out in the corner of my eye, and I thiiink you and I might have shared interest."
            show mce laughing with d
            mc "Oh? Let’s hear it!"
            "I wonder what it could be? A genre of music? One of my hobbies?"
            show mikae horny with d
            mika "Yeah, you’ve gotten quite a reputation. I was wondering if you were interested in joining a secret bdsm club? We’re always looking for enthusiastic girls."
            show mce neutral with d
            "… Eh? BDSM… club?"
            "And what’s this about a reputation?! Oh no!"
            show mce sad with d
            mc "Ahahah, uhhhmm, uhh… I don’t know…"
            show mikae laughing with d
            mika "Pfft, who are you kidding? Give it a shot, you’ll love it."
            show mikae happy with d
            mika "It’s called the dungeon, it’s fun, friendly and open."
            show mce neutral with d
            "Hm… Maybe it’ll be a healthy way to use up my libido, but it’s not like I’ll get paid for anything I do there."
            show mce happy with d
            mc "Okay, I might swing by if I have some spare time."
            show mikae horny with d
            mika "Sexcellent! That’s all I can ask for!"
            mika "Here, take my number. Give me a text if you’re ever outside."
            show mce laughing with d
            mc "Thank you!"
            hide mikae
            hide mikab
            hide mikao
            show mce happy
            with d
            "A ‘secret’ BDSM club… I get it! What’s that going to look like realistically? I bet it’ll be 1-2 girls and a ton of guys. No wonder [mika] is going out of her way to invite potential female members."
            "Maybe this won’t be so bad after all."
            $ shameloss = 1
            $ dungeonunlocked = 1
            call shameloss from _call_shameloss_70
            play sound success
            "(Dungeon Unlocked!)"
            "(-1 Shame!)"
            if morning == 1:
                jump postworldmap
            jump prebedroom
        if herosuit == 0 and shame < 90 and event <= 5:
            $ herosuit = 1
            play ambience ambienceday
            play music dungeon
            scene bg maledorms with d
            "During college, we finally have one of our very first practical classes."
            "These are action-filled classes, where we put everything, we learnt in classes to the test."
            "And, this is the first time we get to use our custom-made hero costumes! These handy things are fully fitted with gadgets and support items to truly bring out our potential."
            "There’s… only one problem…"
            call clotheshero from _call_clotheshero
            show mce horny
            show crushb:
                xpos 1200
            show crushe horny:
                xpos 1200
            with d
            crush "Wow, [mc], you look, uhm… a-amazing!"
            mc "Ahaha… It’s really skin-tight! It’s a little embarrassing."
            "Oh gosh, I feel totally naked in front of [crush] right now!"
            hide crushb
            hide crushe
            with d
            "Did the designer give this costume a built-in camel toe?! What the heck!"
            "How do my boobs look? Does my butt look okay? Am I too sexualized? Argh, stop it, [mc], that’s not important now."
            show mce angry with d
            "I crack my knuckles as I prepare to join my class in some activities."
            "However, the people I’m working with don’t know my strengths and weaknesses very well, so we spend the first part of the lesson introducing ourselves."
            show mce happy with d
            "My super power is gravity manipulation. When I touch an object, I can control how light or heavy it is. But there’s a limitation to how much I change. The greater the weight I change, the greater the burden put upon myself."
            "I also have the ability to spontaneously ‘unlock’ my power, returning everything to its regular weight spontaneously."
            show mce laughing with d
            "The power is a little obtuse at times, but it’s an incredibly flexible and powerful."
            show mce neutral with d
            "Oh, and I can make myself float! Flying alone makes my power top tier, buuuut, it makes me want to vomit almost immediately. I need to work on that."
            show mce happy with d
            "As far as aptitude goes, I’m not exactly top of the class. While I’ve always kept up an above average athleticism due to my desire to become a hero, my abilities are niche, and I’m somewhat of a glass cannon."
            "In our athletics and skill tests, I got exactly 10th out of 20, but that’s mostly due to the fact my power to manipulate gravity has a few niche abilities that completely trivialized tests that the rest of the class struggled with."
            "Such as weightlifting, grip strength, long jump, ball throwing… Of course, I scored highest in all of these. But I was slightly below average in everything else."
            "My main strength is the ability to completely neutralize the majority of villains with a mere touch. Without any gravity, foes will be unable to generate any acceleration or force."
            show mce laughing with d
            "But my super power is also incredible at saving people in disaster rescue missions too."
            "I just know I can become a top hero. If I can work as hard as possible to become fit, fast and strong, I’ll be unstoppable with my power."
            show mce happy2 with d
            "So, I guess I can live with wearing a sexy, skin tight uniform… Hey, it might even be fun."
            show mce happy
            show crushb:
                xpos 1200
            show crushe horny:
                xpos 1200
            with d
            mc "Hey, uhmm… So, we’re in the same team!"
            crush "Yeah! I’m looking forward to working with you. You'll have to give me a few minutes to get changed into my new hero suit."
            mc "Before you do! I have a personal question just to quickly ask."
            show crushe laughing with d
            crush "Y-Yes, [mc]?"
            show mce horny with d
            mc "How does my butt look in this? Probably pretty good, right?"
            play sound success
            $ shameloss = 1
            call shameloss from _call_shameloss_121
            "(-[fshame] Shame)"
            jump prebedroom
        if clubunlocked == 0 and sd > 30 and susumet == 1:
            jump wednesdaybasicevent
        jump randomevents
    label randomevents:
        if event == 1:
            if crushmet == 0:
                label crushintro:
                    pass
                $ crushmet += 1
                scene bg class
                with d
                call clothesformal from _call_clothesformal_5
                show mce happy
                with d
                "In class..."
                "Ahh, it’s that boy! I can't believe he's in my classes too!"
                show crushb:
                    xpos 1200
                show crushe happy:
                    xpos 1200
                with d
                "His name is..."
                python:
                    crush = renpy.input("Name your Crush. Leave blank for the default name 'Crush'.")
                    crush = crush.strip()
                    if not crush:
                        crush = "Crush"
                "He helped me during the practical test, saving me from that rampaging robot."
                "He's {i}my hero{/i}!"
                show crushe laughing with d
                "Gosh, he's so handsome up close. Dare I say, I think I have a crush."
                scene bg class with d
                "He I and spend the entire day sitting together in class, chatting, and learning about each other."
                "I feel like I’ve made my first friend already!"
                "Maybe... Something more later?"
                play sound success
                $ ca += 1
                $ sdgain = 1
                call sdgain from _call_sdgain_2
                "(+1 Crush Affection, +[fsd] Sexual Desire)"
                scene bg college with d
                "As the day wraps up, we say goodbye and I return to the female dorms."

            elif crushmet == 1:
                scene bg college
                if clothes == 12:
                    call clothes from _call_clothes_93
                elif True:
                    call clothesformal from _call_clothesformal_6
                show mce happy
                show crushb:
                    xpos 1200
                show crushe happy:
                    xpos 1200
                with d
                "Later, [crush] asks me if I want to spend some time together."
                label crushmenu1:
                    if qpregnant == 0:
                        if bloated == 1:
                            show mce neutral with d
                            "[crush] notices my large belly, and asks if I'm pregnant."
                            "I explain to him that I just put on a lot of weight over the weekend... How embarrassing!"
                            "There's no way I can tell him that this is cum."
                            pass
                        elif pregnancyshowing == 1 and crushunsafesex == 1 and cpc1 == 0:
                            show mce neutral with d
                            $ cpc1 = 1
                            "[crush] notices I'm pregnant, and since we've had unsafe sex before, he assumes it's his."
                            "I mean... It might be..."
                            "Either way, he seems to be taking it rather well, all things considered. He's so sweet."
                            jump postday
                        elif pregnancyshowing == 1 and crushunsafesex == 0 and cpc1 == 0 and boyfriend == 1:
                            show mce sad with d
                            $ cpc1 = 1
                            "[crush] wonders why I'm pregnant..."
                            "It's an awkward conversation..."
                            "And it results in him breaking up with me..."
                            "Or at least, he says he's 'taking a break', yeah right..."
                            $ crush = "Friend"
                            jump postday
                        elif pregnancyshowing == 1 and crushunsafesex == 0 and cpc1 == 0:
                            show mce sad with d
                            $ cpc1 = 1
                            "[crush] wonders why I'm pregnant..."
                            "It's an awkward conversation..."
                            "And it results in the two of us not hanging out today."
                            jump postday
                    menu:
                        "Sexual Desire: [sd], Affection for [crush]: [ca]"
                        "Play Games." if True:
                            show bg bedroomday
                            if clothes == 12:
                                call clothes from _call_clothes_94
                            elif True:
                                call clothesformal from _call_clothesformal_7
                            show mce laughing
                            show crushb:
                                xpos 1200
                            show crushe laughing:
                                xpos 1200
                            with d
                            "We spend a few hours playing Smash together until I return home to eat dinner."
                            "You felt a little closer to your [crush] after spending some time with him."
                            $ ca += 1
                            play sound success
                            "(+1 [crush] Affection)"
                        "Study" if True:
                            show bg bedroomday
                            if clothes == 12:
                                call clothes from _call_clothes_78
                            elif True:
                                call clothesformal from _call_clothesformal_34
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
                            show bg bedroomday
                            if clothes == 12:
                                call clothes from _call_clothes_95
                            elif True:
                                call clothesformal from _call_clothesformal_8
                            show mce horny
                            show crushb:
                                xpos 1200
                            show crushe horny:
                                xpos 1200
                            with d
                            $ sdgain = 1
                            call sdgain from _call_sdgain_3
                            $ ca += 1
                            "I spend a few hours acting interested and flirty with my crush. He seems to reciprocate!"
                            "You felt a little closer to your crush after spending some time with him."
                            play sound success
                            "(+[fsd] Sexual Desire, +1 [crush] Affection)"
                        "Seduce (15 Sexual Desire, 2 [crush] Affection)" if True:
                            if sd < 15 or ca < 2:
                                "I'm not quite ready for that, and I don't think he'd be either."
                                jump crushmenu1
                            scene bg bedroomday
                            if clothes == 12:
                                call clothes from _call_clothes_96
                            elif True:
                                call clothesformal from _call_clothesformal_9
                            show mce laughing
                            show crushb:
                                xpos 1200
                            show crushe happy:
                                xpos 1200
                            with d
                            "What are we going to do on the bed, [crush]?"
                            menu csm1:
                                "Sexual Desire: [sd], [crush] Affection: [ca]"
                                "Make-Out Session (15 Sexual Desire, 2 [crush] Affection)" if True:
                                    if sd < 15 or ca < 2:
                                        "I'm not quite ready for that, and I don't think he'd be either."
                                        jump csm1
                                    scene bg bed with d
                                    "My crush and I spend about an hour making out and some conversation inbetween."
                                    "At times, I can feel his erection against my hips."
                                    "And when he rubs my body, sometimes he'd get extra frisky as he teasingly grazes around my waist and hips."
                                    "It turns me on so much."
                                    play sound success
                                    $ sdgain = 1
                                    call sdgain from _call_sdgain_4
                                    $ ca += 1
                                    "(+[fsd] Sexual Desire, +1 Crush Affection)"
                                    jump prebedroom
                                "Blowjob (25 Sexual Desire, 3 [crush] Affection)" if True:
                                    if sd < 25 or ca < 3:
                                        "I'm not quite ready for that, and I don't think he'd be either."
                                        jump csm1
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
                                    "[crush] lays back and I soon have his erection in my hands. Curiously, I wrap my lips around the tip and swirl my toungue around the glans."
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
                                    call sdgain from _call_sdgain_5
                                    $ blowjobs += 1
                                    $ ca += 2
                                    "(+[fsd] Sexual Desire, +2 Crush Affection)"
                                    "We spend the rest of about an hour chatting before he returns to the male dorms."
                                    jump prebedroom
                                "Vaginal Sex (40 Sexual Desire, 4 [crush] Affection)" if True:
                                    if sd < 40 or ca < 4:
                                        "I'm not quite ready for that, and I don't think he'd be either."
                                        jump csm1
                                    $ condomon = 0
                                    $ crushsex = 1
                                    if pregnancyshowing == 0:
                                        $ condomon = 1
                                        "Wear a condom?"
                                        menu crushsexmenu:
                                            "Your Crush has some condoms, so don't worry about your own stash!"
                                            "Yup!" if True:
                                                $ condomon = 1
                                            "Nah." if True:
                                                if boyfriend == 1:
                                                    $ condomon = 0
                                                    $ crushunsafesex = 1
                                                elif True:
                                                    "Your [crush] refuses. Maybe if the circumstances were right he'd change his mind."
                                                    jump crushsexmenu
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
                                        "[crush] puts on a condom and I coo in anticipation as he taps the tip of his cock against my wet pussy."
                                    elif True:
                                        "[crush] kneels behind me and I coo in anticipation as he taps the tip of his cock against my wet pussy."
                                    "On my knees, I thrust my butt against him and beckon for him to take me."
                                    "As he pushes the tip inside me, he pushes forward and slides deeper into my soaking wet insides."
                                    play ambience sex
                                    play sound cum
                                    show doggystylesex 2
                                    with d
                                    if virgin == 0:
                                        "And just like that, [crush] takes my virginity!"
                                    mc "Ahhh, your cock feels so good..."
                                    "He begins thrusting back and forth, slowly sliding his cock almost all the way out before sinking back in."
                                    "These deep thrusts drive me wild as they grind against sensitive erogenous zones deep inside of me."
                                    mc "Haaahh, mmmmpphhh... Right there, keep going!"
                                    "Making me feel even better, he starts to thrust faster while reaching down to rub my clit."
                                    "The pleasure overwhelmed me, turning my mind blank as my body trembled towards a potent orgasm."
                                    mc "Ahhh, it's so good! I-I'm gonna, aahhh... Ahhhh!"
                                    "I tightly grip the bedsheets as I climax, my pussy tightening around [crush]'s throbbing cock."
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
                                        "His tight cock explodes a hot load deep into my pussy as he ravishes me."
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
                                        call pregnancyroll from _call_pregnancyroll
                                    scene bg black with d
                                    stop ambience
                                    "[crush] and I spend the rest of our time snuggling and having some post-sex discussion."
                                    if virgin == 0:
                                        "For my first time, that wasn't bad at all! I really liked being able to share such a special moment with [crush]."
                                        $ virgin = 1
                                    play sound success
                                    $ status += 1
                                    $ sdgain = 1
                                    call sdgain from _call_sdgain_6
                                    $ ca += 2
                                    $ vaginalsexes += 1
                                    "(+[fsd] Sexual Desire, +2 Crush Affection)"
                                    jump prebedroom
                                "Anal Sex (40 Sexual Desire, 4 [crush] Affection)" if qanalqueen == 1:
                                    if sd < 40 or ca < 4:
                                        "I'm not quite ready for that, and I don't think he'd be either."
                                        jump csm1
                                    "(Anal Queen) Your high desire for anal has convinced your crush to partake!"
                                    jump crushanalsex
                                "Anal Sex (50 Sexual Desire, 5 [crush] Affection)" if qanalqueen == 0:
                                    if sd < 50 or ca < 5:
                                        "I'm not quite ready for that, and I don't think he'd be either."
                                        jump csm1
                                    label crushanalsex:
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
                                    "I coo in anticipation as [crush] taps the tip of his cock against my wet pussy. He slides it up and down, collecting a generous amount of my wetness before he presses the tip against my butt."
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
                                    "I bite my lip and grip the bedsheets as I come, my ass squeezing around [crush]'s throbbing cock needily."
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
                                    "[crush] and I spend the rest of our time snuggling and having some post-sex discussion."
                                    play sound success
                                    $ status += 1
                                    $ sdgain = 1
                                    call sdgain from _call_sdgain_7
                                    $ ca += 2
                                    $ analsexes += 1
                                    "(+[fsd] Sexual Desire, +2 Crush Affection)"
                                    jump prebedroom
                                "Nothing?" if True:
                                    "I chicken out, and we just decide to chat instead. It's still a cheerful conversation. I'm glad he's so understanding."
                                    jump prebedroom
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
                            $ boyfriend = 1
                            scene bg black with d
                            "We use the opportunity to go somewhere nice together, we have lunch at a nearby restaurant before returning to our dorms."
                            jump prebedroom
                        "Break up with him (Permanent)" if boyfriend == 1:
                            scene bg black with d
                            $ boyfriend = 0
                            "Although I feel bad, I feel like this would be for the best..."
                            "The breakup is a little difficult, but we both take it quite well in the moment before returning to our respective dorms for a little cry."
                            $ crush = "Friend"
                            "We'll still be friends though, of course!"
                            jump prebedroom
                        "Politely decline" if True:
                            pass
        elif event == 2 and sd > 7:
            if rand >= 30:
                label tuesdaybasicevent:
                scene bg street
                call clothesformal from _call_clothesformal_10
                show mce happy
                with d
                if days > 50:
                    "Ah, it's those guys again. Might as well see what they're up to."
                    "The one with spiky hair calls me 'beautiful', as par for the course."
                    show mce happy with d
                elif days > 25:
                    "On the way home, the students I pass every Tuesday flirt with me again."
                    show mce neutral with d
                elif True:
                    "On the way home, I get catcalled by a couple of students."
                    show mce angry
                    with d
                show student1:
                    xpos 0
                show student2:
                    xpos 1200
                with d
                if sd > 15 and personality == 2:
                    "(Always Horny) I really want to do something with them..."
                menu event2menu:
                    "Sexual Desire: [sd], Shame: [shame]"
                    "Call them jerks and be on your way." if days <= 50:
                        if sd > 15 and personality == 2:
                            "(Always Horny) I'm too horny to just leave..."
                            jump event2menu
                        "They call me ungrateful, but I just roll my eyes and ignore them."
                    "Say goodbye" if days > 50:
                        "I chat for five minutes before saying goodbye to the guys. They've essentially become my friends at this point."
                    "Respond flirtaciously. (15 Sexual Desire)" if True:
                        if sd < 15:
                            "Yeahh... I don't think so."
                            jump event2menu
                        show mce happy
                        with d
                        "I give the boys a wink and thank them for indirect 'compliment'."
                        hide student1
                        hide student2
                        with d
                        "I don't know if I entirely mean it or not, but injecting some positivity into the atmosphere seems to have left both them and I feeling better."
                        "Kinda wish they didn't catcall at all, though."
                        "Oh well, I can use behaviour like that to my advantage, hehe..."
                        play sound success
                        $ shameloss = 1
                        call shameloss from _call_shameloss_56
                        "(-[fshame] Shame)"
                    "Flash them everything. (50 Sexual Desire, <90 Shame)" if True:
                        if sd < 50 or shame > 90:
                            "Not in a million years!"
                            jump event2menu
                        $ eventflash = 1
                        show mce happy
                        "Oh? They think I'm hot? Well, this is one way to give us all an ego boost."
                        show mce horny
                        mc "Hey boys, if you think I'm so sexy, how about you rate this?"
                        play sound equip
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
                        stua "Woah-hoh! Smoking hot! 10/10 for sure!"
                        stub "Daaaammn... 10/10 from me too! Can we touch?"
                        mc "Haha, maybe another time, boys."
                        play sound equip
                        scene bg street
                        call clothesformal from _call_clothesformal_11
                        show mce happy
                        show student1:
                            xpos 0
                        show student2:
                            xpos 1200
                        with d
                        "Starry eyes, the students stare at me in disbelief as I quickly redress and walk off."
                        hide student1
                        hide student2
                        with d
                        "What a rush of adrenaline! The thrill has my heart beating furiously."
                        "I'm definitely going to need to masturbate when I get back home."
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
                        play sound success
                        "(+[fsd] Sexual Desire, -[fshame] Shame)"
                        play sound cum
                        show masturbation 1a with cum
                        play sound cum
                        show masturbation 1a with cum
                        pause 1.0
                        $ publicdisplays += 1
                        $ sdgain = 1
                        call sdgain from _call_sdgain_8
                        $ shameloss = 1
                        call shameloss from _call_shameloss_57
                        jump prebedroom
                    "Invite them to your place. (150 Sexual Desire, <75 Shame)" if True:
                        if sd < 150 or shame > 75:
                            "Not today, not any day..."
                            jump event2menu
                        if event2threesome == 0:
                            $ event2threesome = 1
                            show mce happy with d
                            mc "Gosh, you guys are always here on Tuesday, aren't you? What gives?"
                            stua "We finish up swimming club at this time. So we always come here to buy an ice cream together."
                            stub "Yup! Hey, maybe you should join us since you always seem to show up."
                            mc "Pfft, no need to invite me, I'm just walking home, it's not like I'd ever invit-"
                            show mce neutral with d
                            "For as long as I've been going to university, these two boys have been no less insistent on flirting with me every time I pass."
                            "I bet they're desperate to fuck me, haha."
                            show mce horny with d
                            mc "Heyy, do you guys flirt with every girl that passes you?"
                            stub "I can't speak for my friend, but I don't..."
                            stua "Heyy, I'm not some deranged guy that harasses every women I pass."
                            mc "Just me, then?"
                            stua "Wha? No way! I just... I think you're really beautiful and have trouble expressing it, I guess."
                            stub "You are consistently the hottest girl that passes by."
                            "That settles it... I'll have them both at once."
                            mc "Hm... Maybe I should invite you to my place then. It's only fair after your invitation."
                            "Two at once? I can definitely handle them; they both seem quite inexperienced after all, hehe. It's just how I like them."
                            scene bg bedroomday
                            call clothesformal from _call_clothesformal_12
                            show mce horny
                            with d
                            show student1:
                                xpos 0
                            show student2:
                                xpos 1200
                            with d
                            stub "I've never been to the female dorms before, it's pretty strange."
                            stua "Nice dorm! You got any games or something?"
                            mc "Games? We don't need any games..."
                            stua "Eh? What are we gonna do then?"
                        elif True:
                            stua "Again? Sure!"
                            scene bg black with d
                            scene bg bedroomday
                            call clothesformal from _call_clothesformal_13
                            show mce horny
                            show student1:
                                xpos 0
                            show student2:
                                xpos 1200
                            with d
                        play music action
                        play sound equip
                        call clothespanties from _call_clothespanties
                        with d
                        "I drop several articles of clothing to the floor, one by one to the absolute awe of the onlookers."
                        mc "Your persistence paid off, boys."
                        mc "I'm going to give you what we all want."
                        stua "Woaaahhh... This is like some kinda dream! Such a hot girl undressing like that."
                        play sound equip
                        call clothesnude from _call_clothesnude
                        with d
                        stub "D-Damn... You're extremely sexy."
                        "My loins are burning with desire, especially at the compliments. I can be such a sucker for compliments..."
                        mc "You're not nervous, are you?"
                        show student2:
                            linear 1.0 xpos 1000
                        play sound fondle
                        "I take the second student's hand and place it on my breast, encouraging him to touch and caress me."
                        show student1:
                            linear 1.0 xpos 200
                        play sound fondle
                        "The other student takes the hint and begins to feel me up from behind too."
                        "I feel both immensely aroused and in control right now. What an exceptional feeling."
                        stua "God damn, girl. I can't believe you're doing this."
                        mc "A horny girl like me has to get her fill, hehe."
                        stub "Uhhmm, how exactly are you going to get your fill?"
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
                        "The first boy lays down beneath me, and I get ontop of him in a pseudo-reverse cowgirl position as he positions his cock against my ass. With lubrication, his cock manages to slip inside just easily enough to not be uncomfortable."
                        "The second boy takes a more direct position infront of me and the bed, and fortunately it puts him at the perfect height to easily slide his cock into my pussy."
                        if virgin == 0:
                            $ virgin = 1
                            call virgin from _call_virgin
                            "Wow, what a crazy way to lose it! I'm so glad I saved my first time for such a wild, memorable experience."
                        play ambience sex fadein 3.0
                        "They both clumsily roll their hips back and forth, fucking me slowly as I adjust to the girth."
                        "And damn, I really need to adjust to the girth! It's intense, but it's delightful. It's like I'm experiencing the best of both worlds."
                        "The intense feeling of being filled this much is exceptional, and as I slowly get used to it, the boys find their footing and begin thrusting in tandem with each other."
                        "The guy on the bottom is especially eager, as the lubrication allows him to sink deeply and pound my tight ass however he likes."
                        "Meanwhile my pussy only gets wetter allowing the second student to fuck me freely."
                        "The pleasure builds tremendously, spiralling me closer to an orgasm, faster than I could have ever imagined."
                        "I feel overwhelmed with a sense of languor, my mind blanking as pleasure feelings my mind and body."
                        "The two guys use me almost like a toy as they experiment and push themselves."
                        "The position for them is just awkward enough to not let them go all-out and cum, meaning I have to endure their pounding for far longer than a normal session."
                        "There's nothing but the deep feeling of being totally filled up, combined with the outrageous pleasure and constant orgasmic rises causing me to lose count."
                        "My mind simply switches off and I just begin to 'feel' everything in such an attuned way."
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
                        "Another few blasts of cum are enough to make me come again, as the guys fuck until they go sensitive."
                        play sound cum
                        show fmmthreesome 4 with d
                        "They both pull out, creating a messy mixture of cum and my juices."

                        if condomon == 1:
                            "Thanks to the condom, I don't need to worry about getting pregnant."
                        elif True:
                            call pregnancyroll from _call_pregnancyroll_1
                        "We all take a moment to cooldown and catch our breath..."
                        scene bg bedroomday
                        call clothesnude from _call_clothesnude_1
                        show mce happy
                        show student1:
                            xpos 0
                        show student2:
                            xpos 1200
                        with d
                        "Then, well... they don't exactly stick around for snuggles."
                        hide student1
                        hide student2
                        with d
                        "I don't know if it's more or less awkward that they 'thanked' me for the threesome, but they do indeed thank me and take their leave."
                        "This gives me an opportunity to nap and recuperate."
                        play sound success
                        $ sdgain = 2
                        call sdgain from _call_sdgain_9
                        $ status += 2
                        $ shameloss = 2
                        call shameloss from _call_shameloss_58
                        $ analsexes += 1
                        $ vaginalsexes += 1
                        $ groupsexes += 1
                        "(+[fsd] Sexual Desire, -[fshame] Shame)"
                        if qsecretlydepraved == 1:
                            "The enjoyment of a depraved act causes you to gain an additional [fsd] sexual desire!"
                            call sdgain from _call_sdgain_78
                        scene bg black with d
                        jump prebedroom
        elif event == 3 and sd > 5:
            if susumet == 1 and rand >= 30 or susumet == 1 and clubunlocked == 0:
                label wednesdaybasicevent:
                    scene bg college
                    if clothes == 12:
                        call clothes from _call_clothes_97
                    elif True:
                        call clothesformal from _call_clothesformal_14
                    show mce laughing
                    show susub:
                        xpos 1200
                    show susuo uniform:
                        xpos 1200
                    show susue happy:
                        xpos 1200
                    with d
                    "Your friend [susu] invites you to go out drinking with them. This’ll take all night and cost some money."
                    play sound success
                    if clubunlocked == 0:
                        $ clubunlocked = 1
                        "(Club Unlocked!)"
                    menu event3menu:
                        "Politely decline" if True:
                            pass
                        "Go out clubbing (-10$)" if True:
                            if money < 10:
                                "Unfortunately, I don't have enough money."
                                jump event3menu
                            $ money -= 10
                            jump clubbing
        elif event == 4 and sd > 30:
            if rand >= 30:
                label thursdaybasicevent:
                scene bg bus with d
                show student1:
                    xpos 950
                call clothesformal from _call_clothesformal_15
                show mce neutral
                with d
                "While taking a crowded bus, you can feel a hand groping at your skirt."
                if sd > 45 and personality == 2:
                    "(Always Horny) Oh god, I'm getting so wet..."
                menu event4menu:
                    "Sexual Desire: [sd]"
                    "Move away" if True:
                        if sd > 50 and personality == 2:
                            "(Always Horny) I need him to touch me..."
                            jump event4menu
                        "I make my discomfort clear, and successfully move away."
                    "Press your butt back. (45 Sexual Desire)" if True:
                        if sd < 45:
                            "Not a chance! I'd sooner kick him in the balls."
                            jump event4menu
                        play music action
                        scene chikanbus
                        if tan == 1:
                            show chikanbtan
                        if hair == 1:
                            show chikanh black
                        if hair == 2:
                            show chikanh blonde
                        show chikan 1
                        with d
                        "No harm in having a little fun, right? Hehe..."
                        "Not to mention the fact I'm not even wearing panties under my hose right now..."
                        play sound fondle
                        show chikan 2
                        with d
                        $ groped += 1
                        "Oooohhh... To be felt up like this in such a crowded environment, it's really starting to turn me on."
                        "And I've taken the control away from him too, how exciting."
                        menu event4menu2:
                            "Sexual Desire: [sd]"
                            "That's enough fun for now." if True:
                                if sd > 70 and personality == 2:
                                    "(Always Horny) I want more, I neeeed more.."
                                    jump event4menu2
                                show chikan 1
                                with d
                                "I pull away from the man and he understandably stops. He's probably just happy with what he got."
                                "Phew... I'm really aroused right now."
                                play sound success
                                $ sdgain = 1
                                call sdgain from _call_sdgain_10
                                "(+[fsd] Sexual Desire)"
                                scene bg black with d
                            "Keep going! (60 Sexual Desire)" if True:
                                if sd < 60:
                                    "I'm in a bus, I really shouldn't..."
                                    jump event4menu2
                                "My loins are starting to burn up, and my pussy is getting wet."
                                "Almost operating more off instinct than mind, I begin to subtly grind my butt against the buldge in the man's pants."
                                "And then..."
                                play sound rip
                                show chikan 3 with d
                                "Riiip! The cheeky bastard creates an opening, exposing my glistening, wet pussy to the cool air."
                                "Oohhh, fuuuck... This is turning me on a lot."
                                "As the stranger behind me occasionally rubs my pussy, my body shivers in response to the building pleasure..."
                                "Ohhh! He's... he's taking out his cock..."
                                "His fully erect cock... W-Without a condom!"
                                "If I don't stop now, then..."
                                menu event4menu3:
                                    "Sexual Desire: [sd]"
                                    "Stop, stop!" if True:
                                        if sd > 90 and personality == 2:
                                            "(Always Horny) I can't stop now!"
                                            jump event4menu3
                                        show chikan 3b with d
                                        "I cough and excuse myself by moving forward. Causing the man to quickly lift his pants up so no one would notice he was exposing himself."
                                        "Damn... My tights are totally shot up. I'll have to buy some more."
                                        "A part of me can't wait to shop while feeling so wet and exposed, though."
                                        play sound success
                                        $ sdgain = 1
                                        call sdgain from _call_sdgain_79
                                        $ money -= 5
                                        "(-$5, +[fsd] Sexual Desire)"
                                        scene bg black with d
                                    "I can't stop! (80 Sexual Desire)" if True:
                                        if sd < 80:
                                            "I'm not going to let myself get fucked in a bus!"
                                            jump event4menu3
                                        $ event4complete = 1
                                        "There's nothing I can do, I'm frozen with arousal."
                                        "Despite being in a crowded bus, despite the fact anyone could look over and see me getting fucked..."
                                        "I need it so bad, I've never needed anything this bad before."
                                        "Against the window of the bus, just inconspicuous enough to have no one notice, he takes his cock and slides the tip up and down my labia."
                                        play sound cum
                                        show chikan 4 with d
                                        "Then, he positions it against my lips, and pushes inside."
                                        if virgin == 0:
                                            $ virgin = 1
                                            "Ahhh, I can't believe I just lost my virginity to a stranger on the bus..."
                                        play ambience sex fadein 3.0
                                        "I'm so wet that it easily slides in with a lewd schlick. I arch my back slightly to give it a better angle and sigh in relief as I'm filled up."
                                        "As subtly as possible, my lover slowly moves their hips. It's a gentle fuck that savours every inch of the act, but in the daring circumstances it's euphoric."
                                        "Not only that, but since we're standing and my legs are together, my pussy is even tighter around his throbbing shaft."
                                        "The result was ecstasy, beyond amazing, even when moving slowly."
                                        "Ahh, I'm going to come already! My insides started to constrict around my partner's tight cock in rhythmical waves, squeezing and sucking for more."
                                        "Fucking faster and harder, I could feel the pressure building as his shaft throbbed and it was evident that he wouldn't be able to hold back much longer."
                                        play sound cum
                                        show chikan 5 with cum
                                        play sound cum
                                        show chikan 5 with cum
                                        "Then cum exploded from his tip as he relentlessly and carelessly pounded my pussy."
                                        play sound cum
                                        show chikan 5 with cum
                                        play sound cum
                                        show chikan 5 with cum
                                        "I think I came again, but the orgasms overlapped so much I could barely tell; all whilst my insides were pumped with semen."
                                        "My orgasm eventually faded. I hadn't even realized but I was moving my hips too."
                                        stop ambience fadeout 1.0
                                        play sound cum
                                        show chikan 6 with d
                                        "Pulling out, the stranger quickly covers himself up before taking out his wallet..."
                                        stranger "Sorry about the tights."
                                        "He hands me some money and turns away, leaving me to fix my disheveled appearance."
                                        "I look around me and it seems a miracle that no one noticed, especially near the end... Although maybe it was a situation where anyone that noticed pretended not to."
                                        $ condomon = 0
                                        call pregnancyroll from _call_pregnancyroll_2
                                        stop music fadeout 3.0
                                        "I look down and notice that my pussy is dripping cum onto the floor."
                                        scene bg bus with d
                                        call clothesformal from _call_clothesformal_16
                                        show mce neutral
                                        with d
                                        "Eek!"
                                        "As to not cause any more of a mess than I already have, I vow to get off the bus as quickly as I can."
                                        "Taking the next stop, I walk to the shops to buy some new tights."
                                        scene bg black with d
                                        "*Sigh* I can't believe I did that! I need to try to keep my libido under better control."
                                        play sound success
                                        $ sdgain = 2
                                        call sdgain from _call_sdgain_80
                                        $ moneygain = 20
                                        call moneygain from _call_moneygain_51
                                        $ status += 1
                                        $ vaginalsexes += 1
                                        $ publicdisplays += 1
                                        "(+$[fmoney], +[fsd] Sexual Desire)"
                                        if qsecretlydepraved == 1:
                                            call sdgain from _call_sdgain_81
                                            "(For doing a depraved act, you gain another [fsd] sexual desire!)"
                                        scene bg black
        elif event == 5:
            label eventtest:
                pass
            scene bg class
            if clothes == 12:
                call clothes from _call_clothes_98
            elif True:
                call clothesformal from _call_clothesformal_17
            show mce happy
            with d
            show mce neutral with d
            "Uh oh! It's test day today..."
            if testintroduced == 0:
                $ testintroduced = 1
                "(Every Friday you will have a test. If you can pass that test, you'll receieve a bonus, and advance to the next test!)"
            "Test Difficulty = [testdemand], Smarts = [smarts]"
            "Result..."
            if smarts - testdemand >= 0:
                play sound success
                show mce happy2 with d
                "Pass!"
                $ moneygain = testdemand * 3
                $ testdemand += 5
                call moneygain from _call_moneygain_64
                "For your exceptional academic prowess, you have been awarded a grant of $[fmoney]!"
            elif True:
                play sound success2
                show mce sad with d
                $ testfailed += 1
                "Failure!"
            if lonelyfans12 == 1 or chatfaproute2 == 1 or studioroute2intro == 1 or parksex == 1:
                if event5intro == 0:
                    $ event5intro = 1
                    show student6:
                        xpos 1200
                    "Just as I’m about to leave class, a student stops me. He's in a few of my classes, but I've never spoken to him before, he's definitely a little below my standards."
                    mc "Ah, can I help you?"
                    "He squints at me for a moment before taking his phone out."
                    student "I knew it… You are this girl…"
                    if parksex == 1:
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
                        "*Gulp* Fucking someone in public really was asking for trouble. To think this brat took a picture too."
                    elif studioroute2intro == 1:
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
                        "What the?! Oh great, that damn director practically doxed me when he named the videos 'NeoHero City Student' in the title."
                    elif chatfaproute2 == 1:
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
                        "Ohh shiiiit, someone in my class found out about my ChatFap stream?!"
                    elif lonelyfans12 == 1:
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
                        "Eek! My LonelyFans! I didn’t think someone would ever recognize me!"
                    scene bg class
                    if clothes == 12:
                        call clothes from _call_clothes_99
                    elif True:
                        call clothesformal from _call_clothesformal_18
                    show mce neutral
                    show student6:
                        xpos 1200
                    with d
                    mc "Ahh, you must have made a mistake. That’s really not me."
                    student "Oh really? So it should be fine if I show this to everyone in the class."
                    mc "You definitely shouldn’t do that, no."
                    student "Hmm… I’m not sure.... I’ve got a bulge in my pants that might help me make up my mind on what I should do."
                    if shame < 0:
                        "Feeling completely shameless, I shrug."
                        mc "Are you trying to blackmail me for sex, or something?"
                        mc "People in this class already know I’m a bit of a slut, were you late to the party or something?"
                    if boyfriend == 1:
                        "Naturally, I want to avoid my boyfriend finding out. So, it’d probably be best to give this guy a little something to shut him up."
                    elif True:
                        "Hm... Getting angry is exactly what this guy wants, and he wasn’t lying, this guy is already erect and ready to go in his pants."
                    student "What do you say? As a hypothetical fan of this ‘other person’, maybe you could help me forget."
                    "There were 1,000 better ways to approach me, and even get something out of me. But this guy had to try and blackmail me. How boring."
                    "I really don’t like the idea of everyone in my class knowing about my more ‘taboo’ sexual pursuits. A few of my female friends are one thing, but I’ve intentionally been avoiding letting the boys in my class find these things out."
                    if boyfriend == 1:
                        "Especially my boyfriend."
                elif blackmailsex == 1:
                    show mce neutral with d
                    "After the last class of college, I end up packing up my bags as the room clears up"
                    "As with every Friday, I pack up a little slower, allowing time for the class to clear out."
                    "Leaving the room with just me, and the guy I fucked after he tried to blackmail me."
                    if clothes == 12:
                        "This time, however, I approach myself."
                    elif True:
                        scene bg class with d
                        play sound equip
                        "This time, however, I make a quick change and approach myself."
                    call clothesuniform from _call_clothesuniform
                    show mce horny
                    show student6:
                        xpos 1200
                    with d
                    mc "Alright, toy boy. Tell me more about how you’ve been looking up my pictures online."
                    if chatfaproute1 == 1:
                        student "Not just pictures, I caught one of our live streams. Jacked off to it a few times, it was hot as well."
                        mc "Heh, let me guess, if I don’t let you feel the real thing, you’d share that stream with your friends."
                    elif True:
                        mc "Heh, let me guess, if I don’t let you feel the real thing, you’d share what you saw with your friends."
                    student "I never said that."
                    show student6:
                        linear 0.5 xpos 1000
                    "I pull him closer, my hand grazing against his crotch."
                    mc "I wouldn’t want you to do that, so let’s call this insurance to make sure you behave…"
                    "He quivers in my grip as I decide what I’m going to do next."
                elif event5intro == 1:
                    "After the last class of college, I end up packing up my bags as the room clears up"
                    show student6:
                        xpos 1200
                    with d
                    "Just it’s me and the last student left, I turn around and… Oh god, it’s this guy again."
                    student "Hey, [mc]... I saw some more of your stuff online, it’s damn sexy."
                    mc "Tch, you’re here to blackmail me again?"
                    student "What? Nooo… But you know, usually me and the lads share the good stuff. I wouldn’t usually make exceptions, but I think I’d keep it between us if we were closer, though."
                    mc "Eh?! What do you think I am? Some toy you can call upon when you’re horny?"
                    student "Hey, you said it, not me."

                menu e5bmm:
                    "Sexual Desire: [sd], Shame: [shame]"
                    "Kick him in the balls" if True:
                        if personality == 2 and sd > 45 and shame < 65:
                            "(Always Horny) Hey, if all I need to do to shut him up is let off some steam, I can't complain."
                            jump e5bmm
                        show mce horny with d
                        mc "Alright, come closer."
                        show mce angry
                        show student6:
                            linear 0.5 xpos 1000
                        pause 0.5
                        play sound spank
                        show student6:
                            linear 0.5 ypos 1000
                        "And as the jackass does, I give him a solid falcon-knee straight into the balls."
                        mc "Don't fuck with me."
                        "This winds him so much, he can’t even muster a reply before I storm off."
                        play sound success
                        "(+100 Style Points, Smoking Sexy Style)"
                        if blackmailsex == 0:
                            "It’s obvious that jerk wouldn’t go through with it, since it’d put him in as much trouble as me."
                        elif True:
                            "Ehh, I know I've already fucked him... But I have to remind this loser of his place."
                    "Kiss (<90 Shame)" if blackmailsex == 0:
                        if shame > 90:
                            "Not a chance, this guy is a pig."
                            jump e5bmm
                        mc "Hmph… Maybe a kiss on the cheek?"
                        student "How about a kiss below the waist?"
                        mc "Lips, or no deal."
                        student "Fine."
                        show student6:
                            linear 0.5 xpos 900
                        "I awkwardly approach and meet his lips."
                        play sound fondle
                        show buttgropeo formal:
                            xalign 0.5 yalign 0.5
                        if pregnancyshowing == 1:
                            show buttgropeo formalp:
                                xalign 0.5 yalign 0.5
                        show buttgrope grope:
                            xalign 0.5 yalign 0.5
                        with d
                        "As I do, he pulls me closer, disgustingly forcing his tongue down my mouth while his grubby hands squeeze my ass through my pleated skirt."
                        play sound equip
                        hide buttgropeo
                        hide buttgrope
                        show student6:
                            linear 0.5 xpos 1200
                        with d
                        "It’s gross. I’m quick to pull away, and use my hand to wipe the drool from my mouth."
                        mc "What the hell was that?!"
                        student "It was worth it, that’s what! Now I have something real to imagine when I jack off to your stuff, hehehe."
                        mc "Don’t think just because there’s content like that of me on the internet, that it’s automatically consent, you pig."
                        student "I’ll happily oink away after today."
                        hide student6 with d
                        "With rotten glee, he skips away. I suppose I can only be satisfied that he won’t share what he found. The last thing I want is for my recent pursuits to stain my reputation."
                        "It’s strange, though… When he grabbed me like that, it turned me on a little. I hate what he did, and I hate that it turned me on. But despite everything, that situation appealed to me for some reason…"
                        "A part of me hates what I do for money, and wants to be revealed for it. Yet another part of me wants to be sexually fulfilled."
                        "Why couldn’t that guy have just approached me differently? He could have been so much kinder, shown me the images and taken a genuine interest in me."
                        "I could see myself forming a lewd relationship naturally with him that way, instead of whatever the fuck that was."
                        $ kisses += 1
                        $ groped += 1
                        play sound success
                        $ sdgain = 1
                        $ shameless = 1
                        "(+[fsd] Sexual Desire, -[fshame] Shame)"
                    "Blowjob (40 Sexual Desire, <70 Shame)" if True:
                        if sd < 40 or shame > 70:
                            "Forget that. This guy doesn’t deserve anything for his callous approach."
                            jump e5bmm
                        mc "Alright… You can use my mouth."
                        "With classes over, we should have the entire room to ourselves, but I’d still rather get this done as quickly as possible."
                        play music action
                        play sound equip
                        scene bg class
                        call clothesunderwear from _call_clothesunderwear_3
                        show mce neutral
                        with d
                        "I start by removing my clothes to the awe of the student. He can barely believe his eyes as I unbutton my shirt, revealing my lingerie underneath."
                        "I’m not even trying to be sexy, as I unhook my bra and reveal my modest bosom, but that doesn’t stop him from enjoying the sight."
                        "As he ogles my body, he’s quick to unzip his pants and take out his already erect shaft."
                        mc "Heh, that’s all?"
                        student "Yeah well, I’m sure a slut like you has seen 100s."
                        mc "Tch. Lie down before I change my mind."
                        play sound equip
                        scene bg class
                        call clothesnude from _call_clothesnude_64
                        show mce angry
                        with d
                        "I slip my panties off and toss them in the crumpled pile of my clothes before I stand with my feet on either side of his face."
                        mc "This’ll shut you up."
                        scene bg class with d
                        "I wouldn't be satisfied giving this jerk all the power of the interaction, so I sit my tush on his face before leaning over towards is cock."
                        "While this does catch him off guard, he’s hardly in a position to complain with my pussy in his face."
                        mc "Alright… Let’s hurry this up before we get caught."
                        show classroombjb
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
                        play sound2 oral1 fadein 3.0
                        student "Mmhhmphh…"
                        "Wrapping my lips around the tip of his cock, I feel it swell up more with excitement. The tip particularly throbs each time I brush my tongue against its tip."
                        "To my surprise, it grows even larger, leaving me at least a little impressed."
                        "Despite my work on his shaft, however, this jerk doesn’t even return the favour."
                        mc "What gives? Stick that tongue out, you should be worshipping my pussy in your situation."
                        "Grinding my hips against his face, I get a little high on the unusual power dynamic, especially as I finally coax his tongue out."
                        "His tongue work is awful, though. Instead of focusing on my clit, he just trails his tongue around randomly like a wet slug."
                        "Looks like I won’t be getting off, but it’s better than nothing. And taking control of the situation has made the blowjob a little easier to get into."
                        "I keep focusing on his tip, my aim is to make him cum as fast as possible to get rid of him. My tongue swirls around the tip constantly, and my hand jerks the shaft at an accelerating pace."
                        show classroombj 2 with d
                        "I’m actually kinda enjoying this. It’s thrilling to do something this naughty in a classroom, and even more so with a student that has seen my content online."
                        "If only he wasn't such a dick about it, I think, as I intentionally grind my pussy against his face a little harder."
                        "My pussy is getting sensitive and drippy wet, and I can’t help but hold back a few moans as his tongue does ‘accidentally’ hit my swollen clit."
                        mc "Mmphh… *Lick, lick* Aahhh…"
                        "Damn it… Why am I enjoying this so much? I’m being blackmailed into sucking this guy’s cock, I should hate this. However, the knowledge that this person found lewd content of me online, is turning me on like crazy."
                        "In a sense, this guy has definitely jacked off to me, and I’ve already masturbated to the thought of that in itself."
                        "He’s like a living example of the consequences of my actions, and that is turning me on like nothing else ever could. The culmination of all my sexual taboos coming back to haunt me."
                        "F-Fuck… My mind is growing hazy with pleasure, my pussy dripping as I hastily grind on his face. I can feel his hot breath against my pussy as he desperately tries to lick."
                        "Meanwhile on my end, my tongue flicks rapidly against his tip, I feel him tighten and throb. My hand moves as fast as I can to try and make him cum."
                        play sound cum
                        show classroombj 3 with cum
                        "My technique easily pushes him over the edge, and within moments my mouth is filled up with ropes of hot jism that splash the back of my throat."
                        play sound cum
                        show classroombj 3 with cum
                        "Not particularly desiring to make much of a mess, I do my best to swallow each drop, but the quantity of cum is surprisingly excessive, and it bubbles and spills from my lips."
                        mc "Haahh, f-fuck, mmphh… *Slurp*"
                        stop sound2
                        "What a mess… If someone were to walk in now…"
                        play sound equip
                        scene bg class
                        call clothesunderwear from _call_clothesunderwear_4
                        show mce neutral
                        with d
                        "Despite not getting off, I’m quick to rise and redress. Slipping my panties up against my damp pussy and hooking my bra back up."
                        show student6 with d:
                            xpos 1200
                        student "Well, I gu-"
                        mc "Not another word from you."
                        play sound equip
                        scene bg class
                        call clothesformal from _call_clothesformal_33
                        show mce neutral
                        show student6:
                            xpos 1200
                        with d
                        "Pantyhose back on, skirt around the waist… buttoning up my blouse, then my blazer."
                        student "Oh, you still have some cum, just…"
                        scene bg black with d
                        "I push past him, ignoring him as I walk to the girl’s bathroom to clean myself up properly."
                        scene bg toiletstall with d
                        "God… My clit is so tingly right now…"
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
                        "More out of necessity than anything, I end up finishing myself off in the toilets, imagining myself riding a fan’s thick cock."
                        "A part of me really hopes more people recognize me in person."
                        $ blackmailbj = 1
                        $ masturbations += 1
                        $ blowjobs += 1
                        play sound success
                        $ sdgain = 1
                        $ shameless = 1
                        "(+[fsd] Sexual Desire, -[fshame] Shame)"
                    "Vaginal Sex (70 Sexual Desire, <40 Shame)" if True:
                        if sd < 70 or shame > 40:
                            "Honestly, my reputation isn’t worth giving up that much."
                            jump e5bmm
                        if virgin == 0:
                            "I can’t believe this twerp is going to take my virginity."
                            "It’s probably worth it though, I’d be so embarrassed I’d have to leave the college if my classmates knew what I’ve been up to."
                            $ virgin = 1
                        play music action
                        show mce angry with d
                        mc "Hmph, wanna try again?"
                        student "Try what again?"
                        show mce neutral with d
                        mc "Hopeless... You really have no charisma at all, do you? Do you really think anyone is going to want to fuck you if you approach them like that?"
                        student "Uhh, what?"
                        mc "Repeat after me. ‘Hey, [mc], I saw your stuff online, and I’m a really big fan."
                        student "... I saw your stuff online, and I’m a really big fan?"
                        show mce happy with d
                        mc "‘And I was hoping that maybe we could get closer’.’"
                        student "I’m not looking to get closer; I’m looking to get my dick wet."
                        show mce angry with d
                        mc "You’re such a moron. You’re in the perfect situation to pick me up, you’re in my class, I’ve known you for a while now."
                        mc "You know I’m the kind of person that puts erotic material of myself out there, so I’m probably down to fuck."
                        student "Ah-... Right… I was hoping that maybe we could get closer…"
                        show mce horny with d
                        mc "Closer, we won’t get. But… I will fuck you."
                        student "Maybe you could wear, uhm..."
                        show mce neutral with d
                        "I raise an eyebrow as he takes out a girl's uniform. I don't even want to ask why he has that, but I roll my eyes and take it."
                        play sound equip
                        scene bg class
                        show student6:
                            xpos 1200
                        with d
                        "Redressing in the new uniform, I sit back on one of the desks."
                        play music action
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
                        "Leaning back, I spread my legs."
                        "My pussy is actually already pretty hot and wet. Getting recognized in public was an unexpected, immense turn on."
                        student "Really? You’ll fuck me?"
                        mc "Look, I’m a dumb slut that spreads my pussy for tons of people online. I masturbate to the comments I get."
                        mc "If it wasn’t obvious, I not only get off on showing myself off, but I get off of being admired and complimented too."
                        student "You are very beautiful… I have jacked off to your pictures a few times before I built the courage to confront you."
                        show classroomsex 1b with d
                        mc "See? That’s all you had to say. My pussy is all hot and tingly just at the thought of you enjoying my content and recognizing me."
                        mc "Now take that cock out, and ram me with it."
                        student "J-Jeez, I really underestimated you."
                        show classroomsex 1 with d
                        mc "Didn’t you? You better not disappoint now, after all, in this position it’s all up to you."
                        "Heh, this started with him blackmailing me, but the power dynamic has shifted so much that it’s almost like I’m blackmailing him."
                        "It makes sense though, his twisted approach to propositioning me is probably due to bad social skills, or difficulties talking with women."
                        "He unzips his pants and jacks himself into an easy erection as he admires my spread legs, especially loving the cute panties I’m wearing. He can barely keep his eyes off them."
                        mc "Go on then, take my panties off, if you insist."
                        play sound equip
                        show classroomsexo uniform2 with d
                        "Instinctively he licks his lips, and as I temporarily bring my legs together, he takes the opportunity to slip my panties straight off."
                        show classroomsex 1b with d
                        mc "Mmphh, don’t stop complimenting me, boy toy."
                        student "I don’t need to ask, I’m in awe of your amazing pussy. I can’t believe I’m about to fuck something I’ve already jacked off to several times."
                        mc "Be sure to savour every inch, then."
                        $ condomon = 0
                        if condoms > 0 and pregnancyshowing == 0:
                            menu:
                                "Use a condom? Condoms: [condoms]. [fertilityrate]."
                                "Yeah." if True:
                                    $ condomon = 1
                                    $ condoms -= 1
                                "Fuck the rules! (Without protection!)" if True:
                                    $ condomon = 0
                        "He nods as he taps the tip of his cock against my pussy, prodding it deeper as he does genuinely savour each push."
                        play sound cum
                        show classroomsex 2 with d
                        play sound2 foreplay1 fadein 3.0
                        "Each time he moves a little deeper, at first only half of his tip is inside, and then his full tip. My vaginal entrance doesn’t hold back as it tightens and teases everything it touches."
                        "His groaning is music to my ears; I can’t help but bite my lip as his enjoyment rubs off onto me."
                        "He pushes all the way in, causing me to coo and shiver a little."
                        mc "Not bad… Your cock fills me nicely. But don’t hold back, someone could come into the class any second."
                        play ambience sex fadein 2.0
                        "While tightly holding onto my thighs, he certainly fucks me fast, causing my entire body to rock back and forth on the desk."
                        mc "Mmphh, mmmm… That’s it, just like that, aahhh haahhh…"
                        "I can’t help but let a few moans slip out, even if we are technically in a public place. My pussy is just so sensitive because fucking a fan like this is such a turn on for me."
                        "Doesn’t take long for my hips to rock back against each of his thrusts, leaving us both rutting hard like rabbits."
                        "The wet sounds created by my pussy at our point of contact are absolutely obscene, creating an erotic symphony as it mixes with my moans."
                        "It feels good, but there’s something missing… Ah, I have an idea. I guide his right hand to my pussy, and place his right thumb on my clitoris. He diligently keeps it in place, and the constant movement of our rutting results in tremendously pleasurable friction and movement against my clit."
                        "This is.. almost too pleasurable. The erotic situation combined with the immensely stimulating movements in my pussy and on my clit easily bring me to repeated orgasms."
                        "I never would have expected one of my best fucks to happen in my classroom, let alone with someone that discovered my darkest secrets."
                        "But that makes it all the more exhilarating."
                        "This is who I am now. I’m not even doing this for money. I’m a slut, and I love this."
                        "The resignation and swirling thoughts are almost enough to make me come alone."
                        "I barely notice his cock swell up and prepare to unload inside me. Although it was inevitable with my pussy endlessly sucking and squeezing every inch of his shaft."
                        play sound cum
                        show classroomsex 3 with cum
                        play sound cum
                        show classroomsex 3 with cum
                        "Within an instant, I feel several thick loads seep deep into my pussy, painting my walls white with its excess as it seeps and bubbles out."
                        play sound cum
                        show classroomsex 3 with cum
                        play sound cum
                        show classroomsex 3 with cum
                        stop ambience fadeout 3.0
                        "Euphoria drowns me as I come for perhaps the third time, his thumb still flicking my clit even as he pumps me full of cum."
                        stop sound2 fadeout 3.0
                        "Neither of us stop rutting until the very end of our orgasms, only when sensitivity and fatigue set in do we finally come to a stop. Both left panting, and sweaty."
                        play sound cum
                        show classroomsex 4 with d
                        "He pulls out a trial of various sexual juices briefly connecting us before it drips down onto the desk."
                        if condomon == 1:
                            "Thanks to the condom, I don't need to worry about getting pregnant."
                        elif True:
                            call pregnancyroll from _call_pregnancyroll_25
                        student "Thanks… I won’t say anything for now…"
                        mc "*Pant* F-For now? You little rat, keeping one foot in the door in the hopes I’ll fuck you again."
                        if blackmailsex == 0:
                            student "Well, I am a really big fan, and I did say I wanted to ‘get closer to you’."
                            mc "Using my words against me, huh? I swear, I’ll fuck you so good I’ll ruin the rest of your sex life, because you’ll never find anyone else that’ll ever satisfy you."
                            mc "I’ll have you come crawling back to my pictures, just for you to wank to the memory of this amazing pussy."
                            student "R-Right… Thanks, see you next week…"
                            "With his ‘cool’ attitude wiped away, he cleans up and escapes. Hmph… Maybe I went a little too far."
                            scene bg class
                            call clothesuniform from _call_clothesuniform_1
                            show mce neutral
                            with d
                            "It was pretty fulfilling to take control like that, even if he was blackmailing me."
                            "Did I really fuck him because I was blackmailed? Or was I just happy to have an excuse?"
                            show mce horny with d
                            "Hmph… I don’t even know anymore. But I felt like a bad bitch turning that around on him. I should toy with him some more if I ever get the chance."
                        play sound success
                        $ blackmailsex = 1
                        $ vaginalsexes += 1
                        $ status += 1
                        $ sdgain = 1
                        $ shameloss = 1
                        call sdgain from _call_sdgain_145
                        call shameloss from _call_shameloss_122
                        play sound success
                        "(+[fsd] Sexual Desire, -[fshame] Shame.)"
                        if blackmailsex == 0:
                            show mce happy2 with d
                            "... Heyy, uhh... Do I just get to keep this uniform? Cool."
                            play sound success
                            "('Lewder Formal' outfit unlocked.)"
                    "Just Leave" if True:
                        if personality == 2 and sd > 45 and shame < 65:
                            "(Always Horny) Hey, if all I need to do to shut him up is let off some steam, I can't complain."
                            jump e5bmm
                        mc "Yeaaahh… No. Bye."
                        "I push past him, ignoring him as I slip into the hall."
                        "He doesn’t follow me, but I bet the asshole is already formulating a better plan to try and coerce me into something sexual."
                jump prebedroom
        elif event == 6 and sd > 12:
            scene bg onsen with d
            "A little later..."
            call clothesnude from _call_clothesnude_65
            show mce laughing
            with d
            "Aahhh… So nice and warm…"
            "The college has an on-site onsen, and it’s really quiet on weekends. So, it’s become a perfect, sneaky spot for me to relax at."
            "The only problem is when I show up and I’m not alone. It doesn’t happen very often, but…"
            "It’s usually not a mixed gender onsen, but on weekends only a single bath is open because there are less staff around, so that leaves all the men and women in the same place."
            show mce neutral with d
            "Just my luck, there’s a perv staring at my butt while I’m trying to relax. Ah, I get it, this guy must only be here to gawk at the girls."
            if sd < 10:
                "The way he keeps looking over at me is pretty creepy. I wish he was at least a little more subtle."
            elif sd < 30:
                "I surprisingly don’t mind him staring. It’s an onsen, we’re supposed to be nude, so… It certainly relaxes me a little."
            elif sd < 60:
                show mce horny with d
                "It’s pretty hot having someone admire my body. I wasn’t expecting to get aroused here."
            elif True:
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
                show onsensex 1
                with d
                "I lay down and adjust my butt slightly to give him a better view, while my pussy blooms with some arousal and wetness, my clit peeking through its hood. I wonder if I can coax a boner out of him if I tease him enough… Nah, probably not, right?"
            "Wait... Is it just me or his dick growing a bit? Don’t tell me he’s going to get a boner in a public onsen because of me. I can’t help but giggle under my breath."
            "There’s no one around, I wonder if I could, maybe..."
            menu foem:
                "Sexual Desire: [sd], Shame: [shame]."
                "Tease From Afar (12 Sexual Desire, <92 Shame)" if True:
                    if sd < 12 or shame > 92:
                        "Why would I tease this perv? I should move out of sight."
                        jump foem
                    "Well… No harm in a bit of excitement. I’m already completely naked and compromised, so let's tease this perv a little."
                    play sound equip
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
                    "He keeps trying to look at my butt huh? I wonder if this view would be better for him."
                    show onsensex 1 with d
                    "Laying on my side, I angle my butt in such a way that would give just a slight glimpse of my glistening pussy."
                    "It’s so inconspicuous it could barely be called teasing or lewd, because he’d only see it if he looked."
                    show onsensex 1b with d
                    "With a poker face, I look back, and see his cock swelling up."
                    "With his face flushed red, he covers himself and shuffles away, not wanting to risk getting caught with a boner."
                    show onsensex 1 with d
                    "That was pretty exhilarating. I managed to make him leave in such a subtle way, giving me the entire onsen to myself."
                    "My sexuality might have more power than I think"
                    $ sdgain = 1
                    $ shameloss = 1
                    call sdgain from _call_sdgain_171
                    call shameloss from _call_shameloss_123
                    play sound success
                    "(+[fsd] Sexual Desire, -[fshame] Shame.)"
                "Doubleteam Handjob (25 Sexual Desire, <75 Shame, Meet [susu])" if susumet == 1:
                    if sd < 25 or shame > 75:
                        "A handjob? what am I thinking?"
                        jump foem
                    scene bg onsen
                    call clothesnude from _call_clothesnude_66
                    show mce laughing
                    with d
                    play music action
                    "Alriiight… This guy got hard staring at my ass. Least I can do is help him out with it, right?"
                    "I stand up, my two perky nipples standing proud and erect from a slight tinge of arousal as I start walking towards the perv."
                    show mce neutral with d
                    "Shit! Someone else is coming, I can see their shadow through the paper wall between the onsen and the changing rooms."
                    "Abort, abort! I change course and pretend I was walking somewhere else instead, as obviously not the case to both me and the perv who already took notice."
                    show susub:
                        xpos 1200
                    show susue happy:
                        xpos 1200
                    with d
                    susu "Ohhh, hey, [mc]. You’re here too? Gosh, I loooove the onsen, it’s perfect for my froggy side."
                    "Pheewww… it’s just [susu]."
                    show mce happy2 with d
                    mc "Heyy, yeah, I love coming here on the weekends, it’s always so quiet."
                    "[susu] nods, before we both turn to the only other person in the entire onsen, the semi-erect man."
                    "We make some awkward eye contact for a moment, before [susu] turns back to me."
                    show susue neutral with d
                    susu "S-Sorry, I didn’t realize I was interrupting something!"
                    show mce neutral with d
                    mc "H-Hey, you have the wrong ide-..."
                    show mce horny with d
                    mc "..."
                    mc "Wanna tag team him?"
                    show susue laughing with d
                    susu "Join in? Gladly, I love going at it in hot, wet conditions, hehehe."
                    perv "*Gulp* A-Are you guys talking about me?"
                    show mce laughing with d
                    mc "Dick out, show us what you’ve got, big boy!"
                    show susue horny with d
                    susu "Yeah, yeah!"
                    perv "But what if someone comes in?"
                    susu "Well, you better hurry and cum on our faces, then, hmm? We’re relying on you!"
                    show onsenbjb
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
                    "Having the sexually assertive [susu] here helps bolster my confidence, so I follow her lead and kneel down in the water, in front of the guy sitting on the edge of the pool."
                    "I reach out, wrap my fingers around his surprisingly large cock, and slowly glide my fingers back and forth until it’s fully erect."
                    mc "Mmm… Not bad at all. What do you think, [susu]?"
                    susu "Really delish. If we weren’t in the onsen, I wouldn’t mind taking a ride on that beast."
                    mc "Phew, you’re such a slutty frog! Hahaha."
                    "I teasingly nudge [susu], and she playfully returns the gesture."
                    play ambience sex fadein 2.0
                    "I jack his cock off at a moderate pace, really enjoying the way it twitches and throbs in my hand."
                    "On our end, [susu] teasingly plays with my breasts, and then hers, squeezing them to give the guy some good material to cum to."
                    susu "You like what you see? Do you like my boobies or [mc]’s the most?"
                    perv "U-Uhmm, I like them big and soft! But, uh… small are nice too."
                    "Susu pouts and squeezes hers a bit."
                    susu "Heyy, they’re not that small, are they?"
                    mc "Hehe, you shouldn’t ask questions if you won’t like the answer. *Wink*"
                    susu "Alright, that’s it!"
                    play sound2 foreplay1 fadein 1.0
                    "Susu giggles as one of her hands slips below us and finds itself between my legs, rubbing at my clit."
                    "The erotic sight makes our guest harden even more."
                    mc "Mmpphhh, enjoying the show? The moment someone comes in, this ends immediately, so don’t hold back for our sake, big boy."
                    susu "Yeah, I want you to cum all over my boobs to make up for what you said!"
                    perv "Haahh… Speed up a little, and green haired girl, squeeze your boobs together."
                    susu "Ohh, so you do like them? Hehe, you got it boss!"
                    mc "Guess I’ll rub my own pussy, you like that too, don’t you?"
                    perv "Yeahh, *pant*, I’m getting really close."
                    mc "Mmphh, cum all over us!"
                    "I speed my hand up as fast as I can, while sticking my tongue out and wiggling it back and forth eagerly."
                    play sound cum
                    show onsenbj 2 with cum
                    play sound cum
                    show onsenbj 2 with cum
                    "His cock swells up a few times, hardening even more, before a sudden monsoon of cum befalls both [susu] and I."
                    play sound cum
                    show onsenbj 2 with cum
                    play sound cum
                    show onsenbj 2 with cum
                    stop ambience
                    stop sound2 fadeout 3.0
                    "As if this guy was bottled up for a while, repeatedly hot, thick loads drench us."
                    "Our hair, faces, mouths and breasts don’t go untouched by his rapid spray."
                    mc "Mmphh, perfect… Haahhh... "
                    susu "Oohhh, yummy cum! Thank you, sexy."
                    perv "Thank me? No, thank you two! I can barely believe you aren’t succubi for how seductive and sexy you just were."
                    mc "Oh, [susu]..."
                    stop music fadeout 1.0
                    play ambience ambienceday
                    scene bg onsen
                    call clothesnude from _call_clothesnude_67
                    show mce happy
                    show susub:
                        xpos 1200
                    show susue happy:
                        xpos 1200
                    with d
                    "I nudge her, pointing towards the paper doors separating us from the changing rooms. Looks like someone else is coming in."
                    "She nods and we quietly move away without another word, briefly diving under the water to clean our hair and faces from cum."
                    "This naturally disappointed the perv, as we go from that erotic situation to completely ignoring him. But [susu] gives him one last wink as a reminder that ‘yes you didn’t imagine it, that REALLY did just happen’."
                    "[susu] and I enjoy the rest of our onsen time gossiping before we walk back to the female dorms together."
                    $ onsenhj = 1
                    $ groupsexes += 1
                    $ sdgain = 1
                    $ shameloss = 1
                    call sdgain from _call_sdgain_172
                    call shameloss from _call_shameloss_124
                    play sound success
                    "(+[fsd] Sexual Desire, -[fshame] Shame.)"
                "Vaginal Sex (75 Sexual Desire, <30 Shame)" if True:
                    if sd < 75 or shame > 30:
                        "Oh no, there no way I can have sex with this guy. I don’t even know them, and this is a public place."
                        jump foem
                    $ hole = "pussy"
                    label onsensex:
                        pass
                    play music action
                    "Well, I’m pretty horny too… If this guy likes staring at me so much, let’s see if he has the balls to go all the way and satisfy me."
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
                    "I lay down and wiggle my butt back and forth in blatant view of the staring pervert, and this really gets his attention, and his erection."
                    mc "Tsk, tsk… Staring at girls in the onsen? You know that’s frowned upon."
                    perv "S-Sorry! You were just so sexy, and…"
                    mc "Look at that boner, phew… You best put that away before someone sees it."
                    perv "R-Right, I guess I’ll just leave…"
                    show onsensex 1 with d
                    mc "Hmm, I have a better idea… Why don’t you come over here and hide it in my [hole]?"
                    perv "Hide it in you? But then it’ll look like we’re having sex."
                    mc ".. Yeah… That’s the point… *Facepalm*."
                    show onsensex 1b with d
                    mc "Just get over here and fuck me, you pervert, I know you want to."
                    play sound fondle
                    "I enthusiastically wiggle my butt a little more, blatantly showing off my ass and pussy as the muppet I’m trying to seduce makes his way over."
                    perv "Are you sure? I’m not dreaming? This extremely hot girl just wants to fuck?"
                    show onsensex 1 with d
                    mc "Well now you’ve called me hot, I’m definitely gonna fuck ya. You have to do all the work though; I still want this to be a relaxing onsen trip."
                    perv "Okay, I can do that! Wow, your [hole] is beautiful… Uhm, I guess I’ll just…"
                    show onsensex 1b with d
                    mc "I don’t need a running commentary, just fuck me good, alright?"
                    if hole == "pussy":
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
                    "I take a deep breath and relax in the hot water as the pervert kneels down beside my butt and prepares to penetrate me."
                    "My body quivers slightly as I feel the tip of his cock brush against me, a slight drip of precum mixing with my own drippy juices."
                    "He messily glides the tip of his dick back and forth against my lips, collecting a fair amount of juices before pressing its head against the entrance to my [hole]."
                    play sound2 foreplay2 fadein 3.0
                    play sound cum
                    if hole == "pussy":
                        show onsensex v2 with d
                    elif True:
                        show onsensex a2 with d
                    "As he attempts to push deeper inside, I relax my body and he easily sinks in with a schlick."
                    if hole == "pussy" and virgin == 0:
                        call virgin from _call_virgin_14
                    if hole == "pussy":
                        "The wet walls of my pussy tighten and squeeze as he sinks all the way."
                    elif True:
                        "The tight pucker of my anus squeezes around his shaft like an iron ring as he pushes deeper"
                    "I bite my lip and stifle a cute moan as I feel myself getting filled up, while feigning some sort of ignorance to the entire thing. It really does feel amazing."
                    play ambience sex fadein 5.0
                    "The perv is enjoying it a little too much as he begins humping me like a dog, his hands tightly holding and squeezing everything he can get a hold on."
                    "Needless to say, I just continue to relax and soak in the hot water, treating the rutting as if it was an extreme happy ending at a massage parlour."
                    "Even so, I find it hard to hold back my moans as he speeds up. Even I can only pretend to be bored and ignore the situation for so long when he’s fucking my [hole] so well."
                    mc "Mmmphh, god damn… You’re certainly not holding back."
                    perv "Someone could walk in here any second, and I wanna fill you up! I have no time to waste!"
                    mc "Ahaha, that’s the attitude. Cum then, you fucking pervert."
                    "After that provocation he grits his teeth and fucks me even harder. His fingers digging into my thigh for support as he rocks my world."
                    mc "Mmphh, aahhh, there you go… Ahhhahh… *Pant, pant*. Fill me up..."
                    "Almost as if I ordered it, I can feel his cock swell up and prepare to unload. I’m pretty close to a light orgasm too, my mind growing slightly hazy as a surge of pleasure swells up from deep within."
                    play sound cum
                    if hole == "pussy":
                        show onsensex v3 with cum
                    elif True:
                        show onsensex a3 with cum
                    play sound cum
                    if hole == "pussy":
                        show onsensex v3 with cum
                    elif True:
                        show onsensex a3 with cum
                    "My [hole] tightens around my partner’s cock as I climax, pushing him over the edge and causing him to unload deep inside."
                    play sound cum
                    if hole == "pussy":
                        show onsensex v3 with cum
                    elif True:
                        show onsensex a3 with cum
                    play sound cum
                    if hole == "pussy":
                        show onsensex v3 with cum
                    elif True:
                        show onsensex a3 with cum
                    stop ambience fadeout 3.0
                    stop sound2 fadeout 3.0
                    "Cum drips and bubbles from our point of contact, getting messy and mixed up as he continues to fuck throughout the brief bliss."
                    if condomon == 1 and hole == "pussy":
                        "Thanks to the condom, I don't need to worry about getting pregnant."
                    elif hole == "pussy":
                        call pregnancyroll from _call_pregnancyroll_26
                    play sound cum
                    show onsensex 4 with d
                    "He is quick to finish up and pull out, admiring my well-fucked [hole] as the pleasure of my own orgasm finally settles."
                    scene bg onsen with d
                    call clothesnude from _call_clothesnude_68
                    show mce horny
                    with d
                    "We can’t indulge in this moment much longer however, as we both spot someone else about to enter the onsen. Causing me to quickly sit down to hide the cum dripping from me."
                    "The perv drifts away, pretending as if he had never interacted with me."
                    "And when the other person arrives, it’s like nothing happened at all."
                    "The only subtle give away would be the smug looks of satisfaction plastered on both of our faces."
                    "I could get used to being manhandled like that, hehe. It’s not bad getting the guy to do all the work."
                    if hole == "pussy":
                        $ vaginalsexes += 1
                    elif True:
                        $ analsexes += 1
                    $ status += 1
                    $ onsensex = 1
                    $ sdgain = 1
                    $ shameloss = 1
                    call sdgain from _call_sdgain_173
                    call shameloss from _call_shameloss_125
                    play sound success
                    "(+[fsd] Sexual Desire, -[fshame] Shame.)"
                "Anal Sex (85 Sexual Desire, <20 Shame)" if qanalqueen == 0:
                    if sd < 85 or shame > 20:
                        "Oh no, there no way I can have sex with this guy. I don’t even know them, and this is a public place."
                        jump foem
                    $ hole = "ass"
                    jump onsensex
                "Anal Sex (75 Sexual Desire, <30 Shame)" if qanalqueen == 1:
                    if sd < 75 or shame > 30:
                        "Oh no, there no way I can have sex with this guy. I don’t even know them, and this is a public place."
                        jump foem
                    $ hole = "ass"
                    jump onsensex
                "Move away" if True:
                    if personality == 2 and sd > 25 and shame < 75:
                        "(Always Horny) I'm horny, he's horny, I've got nothing to lose."
                        jump foem
                    "Nah, what am I thinking? Let's move somewhere where he can’t see me."
        elif event == 7 and sd > 40 and mrslime == 0:
            scene bg shops with d
            call clothescasual from _call_clothescasual_8
            show mce happy
            if tentacleintro == 0:
                "Just as I’m walking around town after doing a bit of casual Sunday shopping, I find myself running a bit late."
                "However, I spot a convenient alleyway, looks like it could be an efficient shortcut back to my place. It’s pretty dark, and creepy, but… I’m a pro hero in training, so I’m not exactly worried."
            elif tentacleintro == 1:
                "Just as I’m walking around town after doing a bit of casual Sunday shopping, I find myself running a bit late."
                "However, I spot a recognizable alleyway. It’s the one with the strange tentacle thing… Hmm…"
            menu:
                "Take the alleyway shortcut." if True:
                    scene bg alleyway
                    if tentacleintro == 0:
                        call clothescasual from _call_clothescasual_9
                        show mce neutral
                        "Let’s go. I power walk through the alleyway."
                        "Everything seems to be going fine until the oddest thing happens in my peripheral vision."
                        "It’s no human, it’s no animal. It’s some kind of strange amorphous goo dripping down the sides of one of the buildings."
                        play music dungeon
                        play sound whip
                        show tentaclesstandingsexb
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
                        "It's so quick, it catches me in the middle of my double-take, various tentacle-esque appendages launch in my direction, beginning to wrap around me, tugging and pulling at my clothes."
                        play sound2 foreplay1 fadein 3.0
                        mc "W-What on earth is this stuff?! Is this the result of someone’s power?"
                        "As the tentacles graze and rub against my exposed skin, they leave some strange, tingly residue. Whatever it is, it’s a fairly fast acting aphrodisiac, because my body has already started to become physically aroused, my nipples growing stiff and my pussy blooming."
                        "Regardless of whatever it is, it’s progressively getting a tighter grip on me, and if I don’t make a move now, it’s going to pull my shirt up, and my shorts down."
                        $ tentacleintro = 1
                    elif tentacleintro == 1:
                        play music dungeon
                        "I walk through the alley, keeping my eyes peeled for that strange blob again."
                        "The aphrodisiac left such a mark on me, that I don’t entirely know if I’m keeping an eye out to avoid it, or indulge in it again."
                        show mrslime:
                            xpos 50
                        with d
                        "On que, the tentacle creature appears before me, forgoing stealth to almost politely inform me of its presence before its tentacles protrude outwards and towards me."
                        show tentaclesstandingsexb
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
                            xpos 50
                        with hpunch
                        "As the tentacles graze and rub against my exposed skin, they leave some strange, tingly residue. Whatever it is, it’s a fairly fast acting aphrodisiac, because my body has already started to become physically aroused, my nipples growing stiff and my pussy blooming."
                        play sound2 foreplay1 fadein 3.0
                        if sd > 50:
                            "This feels amazing… I suppose I should decide whether to stay or not."
                        elif True:
                            "Mmphh, as good as it feels… I can’t let this pervy thing have its way with me. Sorry, lil’ blob."
                    menu e7m:
                        "Sexual Desire: [sd], Shame: [shame]."
                        "Double Penetration Tentacles (100 Sexual Desire, <20 Shame, Complete Standing Tentacles)" if True:
                            if sd < 100 or shame > 20 or standingtentacles == 0:
                                jump e7m
                            "I can’t resist… I think this time, I’ll just become one with the tentacles."
                            scene bg alleyway with d
                            play sound equip
                            "The tentacles struggle to undress me on their own, but this time I help them out. Once it looks like the alley is completely clear, I strip down every item of clothing until I’m left just with my panties."
                            show tentaclesdpsexb
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
                            "And then I sit my butt on the cold concrete floor, somewhere clean. The cold won’t matter once I’m being filled up by that gooey delight."
                            label doubletentaclessex:
                                pass
                            "I tease the tentacles by taking my thong off slower than everything else, holding it between my toes as it gently slithers closer."
                            "It’s quick to wrap me up, holding my foot and effectively locking my panties in place. Then my other thigh, and there’s even one affectionately swishing me on my head. I don’t know what this thing is, but it’s surprisingly cute."
                            "And as the tentacles wriggle around me, I start to feel the aphrodisiac again. My nipples tighten, and my breathing grows shallow. Two particularly thick tentacles approach my bottom and all I can really do is bite my lip with anticipation."
                            mc "Yeahh… You know what I want, don’t you? Take me in both holes if you’d like."
                            "I imagine that the natural lubrication of these tentacles is going to make anal sex with it feel extremely pleasing."
                            "Slithering closer and with purpose, the two tentacle tips poke and prod around my vagina and pucker, lubing me up nicely."
                            play sound cum
                            show tentaclesdpsex 2 with d
                            play ambience sex fadein 3.0
                            "And then with a satisfying schlick, they both push deeper, and deeper, and deeper!"
                            if mrslime == 0:
                                mc "Mmphhh, you fill me so damn well… I might just have to take you home."
                            elif True:
                                mc "Mmphhh, you fill me so damn well… I'm so glad I brought you home."
                            "The tentacles respond to my admiration with excited squirms inside of me, directly pleasing me even more. In only a few moments, that tantalising aphrodisiac takes effect from within and my entire body is burning with passion and desire."
                            "After the previous time, I was worried I might have built up a resistance to it, but it seems to be just as powerful as ever."
                            mc "Aahhh, mmphhh… *Pant, pant*... I don’t think any guy could make me feel this good, haahhh…"
                            play sound cum
                            show tentaclesdpsexmilking 1
                            show tentaclesdpsex 2b
                            with d
                            "While I’m distracted with pleasure, two particularly uniquely tipped tentacles manage to sneakily latch onto my stiff nipples."
                            if mrslime == 0:
                                mc "Hmm…? Aahhh! What are these? Mmphh…"
                            elif True:
                                mc "Mmphh, these again? Go for it!"
                            "They immediately begin sucking intensely, adding yet another mind-blowing pleasure to this already overwhelming event."
                            if pregnancyshowing == 1:
                                play sound cum
                                show tentaclesdpsex 2
                                show tentaclesdpsexmilking 2
                                with cum
                                "Almost immediately and efficiently, milk squirts and spurts out. Easily sucked up by the vacuum-like tentacle appendages."
                                mc "Aaahh, are you hungry, Mr. Slime? Have as much as you want, hehe."
                            elif True:
                                mc "Aahh, unfortunately for you, Mr. Slime, there’s no milk in there."
                                "Almost disappointed, the two suckers cease, and something a little concerning happens. A strange, sharp, pointy tooth-like needle appears from the centre of both appendages, and it pierces both my nipples!"
                                "What is it injecting me with?! It was too quick for me to react fast enough."
                                "As the needle disappears, the strangest thing happens… A faint, white dribble appears on top of my nipple."
                                play sound cum
                                show tentaclesdpsex 2
                                show tentaclesdpsexmilking 2
                                with cum
                                "At first, I just disregarded it as some of the strange residue it injected, but as the tentacle cups begin to suck again, there’s a sudden torrent of white!"
                                mc "Aaahhh, w-what the?! M-MILK!?"
                            "I throw my head back and moan as it squeezes and sucks my nipples, milk dribbling everywhere as the tentacle excitedly speeds up, pounding both of my holes one after the other in a pattern."
                            "Harder and faster, my entire body is thoroughly used, and every combination of pleasure easily brings me endless orgasms."
                            "And as before, it doesn’t take long for the tentacles to swell up, undulating as they prepare to coat me in excessive amounts of cum."
                            play sound cum
                            show tentaclesdpsex 3 with cum
                            play sound cum
                            show tentaclesdpsex 3 with cum
                            "The tip of each tentacle sprays cum in every corner and crevice they can."
                            play sound cum
                            show tentaclesdpsex 3 with cum
                            play sound cum
                            hide tentaclesdpsex 3
                            show tentaclesdpsexbp
                            if tan == 1:
                                show tentaclesdpsexbtanp
                            show tentaclesdpsex 3
                            with cum
                            "Whilst my ass and pussy are knotted and both filled to bursting with an intense amount of cum, over, and over inflating my belly slightly with the cum."
                            play sound cum
                            show tentaclesdpsex 3 with cum
                            play sound cum
                            show tentaclesdpsex 3 with cum
                            mc "Aaahh, fuck yeah! Fill me up! Aaahh, aaahhhhh!"
                            stop ambience fadeout 3.0
                            stop sound2 fadeout 3.0
                            "I’m left in a state of utter bliss for a full thirty seconds before my orgasm fades. Although my pussy and ass are still left tied up by the tentacles for just a little longer."
                            "It still feels incredible, but I notice that the aphrodisiac has worn off again, leaving me feeling satisfied rather than needing more."
                            show tentaclesdpsex 3b with d
                            if mrslime == 0:
                                mc "Mmphh… You really cum a lot, don’t you? I don’t have all day, you know, and someone could walk by and see us!"
                            elif True:
                                mc "Mmphh… You really cum a lot, don’t you? I don’t have all day, you know!"
                            play sound cum
                            hide tentaclesdpsexmilking
                            show tentaclesdpsex 4
                            show tentaclesdpsexmilk
                            with d
                            "The slime seems to apologetically shrink away as it pulls out, a hefty waterfall of cum pooling from my pussy and ass to the ground."
                            "I don’t waste any time getting up, redressing and cleaning myself off."
                            $ bloated = 1
                            $ pregnancyshowing = 1
                            if mrslime == 0:
                                play sound hypnosis
                                scene bg alleyway
                                call clothescasual from _call_clothescasual_10
                                show mce neutral
                                show mrslime:
                                    xpos 50
                                show pinkhair
                                show pinkeyes
                                with hypno
                                mc "Mmphh… So bloated, it’s unreal…"
                                show mce horny with d
                                mc "Just why do you need to cum so much anyway? I was worried I’d get pregnant at first, but nothing happened at all. I suppose it’s a price I’ll have to pay for such an amazing fuck."
                                "The slime blob claps two tentacles together as it watches me. It understands me surprisingly well, maybe even better than before? I’m not really sure what exactly this thing is, but I’m certainly curious."
                                hide pinkeyes
                                show mce laughing
                                with d
                                mc "Do you live anywhere in particular, Mr. Slime? Maybe you should come live with me."
                                show mce neutral
                                show pinkeyes
                                with d
                                "Huh, what am I even saying? I said it without really thinking, as if it wasn’t a genuine thought, but more an impulse."
                                "While I can certainly see the benefits of having this thing, I don’t even know where I’d put it, how I’d feed it, or really… anything…"
                                "Yet, I feel strangely compelled. To such a degree that when the slime lifts up two tentacles like gooey hands, I reach out and pick it up."
                                play sound equip
                                hide mrslime
                                show mce happy with d
                                mc "Alright, I’ve decided. You’re coming to live with me, Mr. Slime!"
                                scene bg street2 with d
                                "I hide the strange amorphous blob in one of my shopping bags as I walk out of the alley."
                                call clothescasual from _call_clothescasual_11
                                show mce happy
                                show pinkeyes
                                with d
                                "Self-consciously I touch my hair, just to ensure there’s no cum in there. Fortunately, it’s completely clean, dry and normal. Strange, I swear I could have felt wet a second ago. I’m just being paranoid."
                                show mce neutral with d
                                "Out of pure curiosity, I check the buildings adjacent to the alleyway. Maybe this thing came from one of them?"
                                show mce horny with d
                                "‘NeoHero City Power Research and Development Labs’. Is this thing the result of some kind of experiment? What, were they trying to make the best sex toy ever? Heh, well, he’s mine now."
                                scene bg black with d
                                $ mrslime = 1
                                $ vaginalsexes += 1
                                $ analsexes += 1
                                $ status += 1
                                $ sdgain = 1
                                $ shameloss = 1
                                call sdgain from _call_sdgain_174
                                call shameloss from _call_shameloss_126
                                play sound success
                                "(+[fsd] Sexual Desire, -[fshame] Shame.)"
                                if qsecretlydepraved == 1:
                                    call sdgain from _call_sdgain_175
                                    "(Secretly Depraved) And since you enjoyed the depraved act! (+1 Sexual Desire!)"
                                scene bg bedroomnight
                                call clothescasual from _call_clothescasual_12
                                show mce happy
                                show pinkeyes
                                with d
                                mc "Welcome to my room, Mr. Slime! I think I’ll keep calling you that, it sounds a bit better than ‘amorphous tentacle thing’."
                                play sound equip
                                show mrslime:
                                    xpos 50
                                with d
                                "I drop the slime down and it happily wanders around."
                                play sound fondle
                                show mrslime:
                                    linear 10.0 xpos 1200
                                "... Hmm… How do I even take care of this thing…? A part of me doesn’t even know why I felt so compelled to bring it here, but oh well."
                                "When it isn’t cumming buckets on me, it’s surprisingly not messy, so that’s a relief."
                                show mce neutral with d
                                "In my peripheral vision, I catch a glimpse of myself in the mirror for a moment, and something looks off."
                                "Did I see that right? I have pink eyes?"
                                scene bg door with d
                                call clothescasual from _call_clothescasual_13
                                show mce neutral
                                with d
                                "I check again, closer… Hm… No? Just normal eyes."
                                "Ah, I must be tired. Having sex with Mr. Slime really takes a lot out of me."
                                scene bg bedroomnight
                                play sound equip
                                call clothesnude from _call_clothesnude_69
                                show mce happy2
                                with d
                                "Let’s have a nap, hopefully my belly will be a bit smaller by then too."
                                scene bg bed
                                show mrslime:
                                    xpos 50
                                with d
                                "I curl up in bed, and Mr. Slime joins me. It’s no different than having a blobby cat, I think."
                                play sound success
                                "(You can now play with Mr. Slime in your bedroom at any time.)"
                                if mrslime == 1:
                                    jump postworktrans
                            elif True:
                                scene bg black with d
                                $ mrslime = 1
                                $ vaginalsexes += 1
                                $ analsexes += 1
                                $ status += 1
                                $ sdgain = 1
                                $ shameloss = 1
                                call sdgain from _call_sdgain_176
                                call shameloss from _call_shameloss_127
                                play sound success
                                "(+[fsd] Sexual Desire, -[fshame] Shame.)"
                                if qsecretlydepraved == 1:
                                    call sdgain from _call_sdgain_177
                                    "(Secretly Depraved) And since you enjoyed the depraved act! (+1 Sexual Desire!)"
                                if mrslime == 1:
                                    jump postworktrans
                        "Standing Tentacles. (50 Sexual Desire, <50 Shame)" if True:
                            if sd < 50 or shame > 50:
                                jump e7m
                            "It certainly doesn’t seem harmful… What it’s trying to do could potentially be very pleasurable, and the aphrodisiac coating its tentacles is slowly winning me over."
                            "Who knows how long it’ll take for me to be mad, drunk with pleasure if the effect is already this strong."
                            "I look ahead of me, and then behind me. The coast is clear."
                            mc "Okay, you slimy things, what exactly are you planning to do to poor, innocent me?"
                            label standingtentaclessex:
                                pass
                            play sound equip
                            hide tentaclesstandingsexbedroomclip
                            show tentaclesstandingsex 2
                            hide tentaclesstandingsex1p
                            hide tentaclesstandingsex1clip
                            with d
                            "As if it understood me, the tentacles wriggle with more excitement, getting under my tank top, lifting my top and fondling my breast. Down below, the crafty tentacle manages to peel away my shorts and panties."
                            if mrslime == 0:
                                "Is it really trying to penetrate me? Oh god, if the aphrodisiac feels so good just against my skin, what’s it going to feel like inside?"
                                "Looks like I’m about to find out, as the tip of a warm, slimy tentacle teases the moist lips of my pussy. Why exactly does this thing want to copulate with me, and why is it so good at it?"
                            elif True:
                                "Mmphh, he teases and prods around my pussy, slathering it in aphrodisiac that feels so good against my skin."
                            mc "Mmphhh… You’re quite a loving partner, aren’t you? Go on, then, if you insist, my pussy is all yours."
                            "The tentacles playfully writhe around again, while the tentacle pushes deeper inside, finally penetrating me and sending several waves of pleasure throughout my body, resonating from our point of contact."
                            play sound cum
                            show tentaclesstandingsex 3
                            with d
                            if virgin == 0:
                                "Does this technically take my virginity…? Hmm…"
                                menu:
                                    "Yeah!" if True:
                                        $ virgin = 1
                                        "At least I can claim to be one of the only people in the world to lose their virginity this way."
                                    "Nah!" if True:
                                        pass
                            play ambience sex fadein 3.0
                            "The thick tentacle inside me goes deep, and pleasures me masterfully with a combination of motions. Thrusting, rotating, and applying pressure deep inside all serve to create ecstasy."
                            "And as it pleases every inch of my pussy, practically causing my eyes to roll back in pleasure, it also coats my insides with its strange erotic, purple residue. Everywhere it touches aches and throbs with need."
                            "I’ve really gone and let this tentacle monster beguile me, I can only hope it lets me go whenever it’s finished whatever it’s trying to do."
                            "My knees grow weak and my thighs quiver as the tentacle gives me a good thrashing. The one around my breast curiously pokes and prods around my nipple, teasing that too."
                            mc "Aahh, haahhh… S-So good, I c-can’t believe it!"
                            "That aphrodisiac really is going to my head, clouding any doubts or thoughts I could have about the situation with pure lustful desire."
                            "My body nearly buckles under the pressure, but the hold of the tentacles keeps me upright as it continues to pound me, bringing me closer and closer to a mind-blowing, full-body orgasm."
                            mc "Hohh! You’re going to make me come really hard!"
                            "It speeds up, surpassing the speed you’d expect any man to achieve, as it rushes both me and itself towards a climax."
                            "My pussy contracts and clenches rhythmically as I orgasm, moans freely slipping from my mouth as I radiate excess pleasure through sound and body language."
                            "And only a few moments into my powerful orgasm, I can feel a peculiar swelling and undulating deep inside of me. Ah, it’s about to-"
                            play sound cum
                            show tentaclesstandingsex 4 with cum
                            play sound cum
                            show tentaclesstandingsex 4 with cum
                            "Cum! Cum everywhere! Thick, hot and… tasty! Mmm!"
                            play sound cum
                            show tentaclesstandingsex 4 with cum
                            play sound cum
                            show tentaclesstandingsex 4 with cum
                            "The tip of each tentacle freely unloads several shots of its unique tentacle cum. Several shots would be an understatement for the one inside me however, as it just keeps pumping, and keeps pumping!"
                            play sound cum
                            show tentaclesstandingsex 4 with cum
                            play sound cum
                            show tentaclesstandingsex 4 with cum
                            "Oh, ohhh, when is it going to stop? I feel so full, my pussy and womb not filled completely by this cum and it shows no signs of stopping."
                            play sound cum
                            show tentaclesstandingsex 4 with cum
                            play sound cum
                            show tentaclesstandingsex 4 with cum
                            stop ambience fadeout 3.0
                            stop sound2 fadeout 3.0
                            "The thick, bulbous tentacle remains stuck inside me for a while as it fills me, I couldn’t even slip it out if I wanted to because it swelled up thicker inside my pussy than out."
                            if pregnancyshowing == 0:
                                hide tentaclesstandingsex 4
                                show tentaclesstandingsexbp
                                if tan == 1:
                                    show tentaclesstandingsexbtanp
                                show tentaclesstandingsex 4
                            with d
                            play sound cum
                            play sound cum
                            show tentaclesstandingsex 4 with cum
                            "My euphoric orgasm long fades before it finally comes to a stop, leaving me thoroughly fatigued and panting."
                            play sound cum
                            show tentaclesstandingsex 5 with d
                            "It slips itself out with a schlick, and returns to the amorphous mound of purple goo that it originated from."
                            if mrslime == 0:
                                mc "Haaahhh, sheesh… I wasn’t expecting that at all. My belly is so swollen!"
                                if pregnancyshowing == 0:
                                    mc "Eek, it’s so big that I literally look pregnant! I better not actually {i}be{/i} pregnant, you damn slime-thing!"
                                    "The purple blob shyly shrinks away after I tell it off, causing me to feel a teeny bit guilty, since it did make me feel really good."
                                    "I hope this belly clears up a bit later…"
                                elif True:
                                    "I’m already pregnant, but I swear I feel even more bloated than usual."
                                "Ahh, I can actually feel my bloated belly already settling down and shrinking a little, that’s a relief."
                                "It looks like I'll have a big belly until morning."
                                "Oh, and I noticed that the aphrodisiac liquid’s effect that drove me so crazy at the start seems to have been completely neutralized."
                                "That’s good, I think… I still feel like there’s just something a little off."
                                "I’m probably imagining it. Heck I wonder if I imagined this entire scenario by the time I get back home."
                                play sound equip
                                show tentaclesstandingsex 6
                                show tentaclesstandingsex1p
                                with d
                                mc "Thank you, Mr. Tentacle. Uhmm… If you ever see me again, don’t be shy."
                                "It reaches a tentacle out affectionately, and like a dolt I shake it like a hand."
                                mc "Bye bye!"
                                $ bloated = 1
                                if pregnancyshowing == 0:
                                    $ pregnancyshowing = 1
                                scene bg alleyway
                                call clothescasual from _call_clothescasual_14
                                show mce neutral
                                show pinkeyes
                                with d
                                "Cleaning myself up to the best of my ability, which is admittedly not great. I was covered in a seriously high volume of cum. I hurriedly return home, with the slight discomforting knowledge that {i}something{/i} feels off."
                            elif True:
                                mc "Hehe, what a mess... Thank you, Mr. Slime."
                                $ bloated = 1
                                $ pregnancyshowing = 1
                            $ standingtentacles = 1
                            $ vaginalsexes += 1
                            $ status += 1
                            $ sdgain = 1
                            $ shameloss = 1
                            call sdgain from _call_sdgain_178
                            call shameloss from _call_shameloss_128
                            play sound success
                            "(+[fsd] Sexual Desire, -[fshame] Shame.)"
                            if mrslime == 1:
                                jump postworktrans
                        "Make an escape." if True:
                            if personality == 2 and sd > 55 and shame < 45:
                                "(Always Horny) Ahh, I really can't stop, I need to be fucked!"
                                jump e7m
                            "Looks like it’s more focused on molesting me than holding me down, so once it loosens its grip to try and get my clothes off, I can make a quick getaway."
                            stop sound2 fadeout 3.0
                            play sound equip
                            scene bg alleyway with d
                            call clothescasual from _call_clothescasual_15
                            show mce neutral
                            "And... Success, my plan goes off without a hitch, and I’m quick to escape the slow drippy tentacle-thing."
                            show bg street2 with d
                            "What a truly strange encounter. No one would believe me if I told them."
                            scene bg black with d
                            "The strange aphrodisiac residue of the tentacle still lingers around every area they had touched, causing a hot throbbing desire within me for a few hours afterwards…"
                            "Just what the heck is this stuff?"
                            $ sdgain = 1
                            call sdgain from _call_sdgain_179
                            play sound success
                            "(+[fsd] Sexual Desire, -[fshame] Shame.)"
                            if mrslime == 1:
                                jump postworktrans
                "Go the long way." if True:
                    "No shame in being a wimp. The shortcut only saves a couple of minutes anyway."

init:
    $ eventflash = 0
    $ event2threesome = 0
    $ event4complete = 0


label postday:
    if qintrovert == 1:
        $ alonemult = 1.1
    scene bg bedroomnight with d
    "At 4:00pm, I prepare and eat dinner."
    jump prebedroom
label weekend:
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
    call clothes from _call_clothes_20
    show mce happy2:
        xpos 850
    with d
    "It's the weekend!"
    "After a well deserved sleep-in, I decide what to spend my free time doing."
    $ potencollegemissed -= 1
    $ weekend = 1
    if weekendtut == 0:
        $ weekendtut = 1
        "(On the weekend, college will be closed.)"
    $ dsd = int(sd)
    $ dshame = int(shame)+1
    call screen bedroom with d
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
