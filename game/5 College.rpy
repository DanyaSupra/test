label college:
    if droppedout == 1:
        scene bg college
        if morning == 0:
            scene bg collegenight
        with d
        "I'm uhh, I'm not a student anymore..."
        "But, I could always take my supervisors... 'offer'..."
        menu svom:
            "Take Supervisor's offer. (50 Sexual Desire, <50 Shame)" if True:
                if sd < 50 or shame > 50:
                    "There's absolutely no way I could do that."
                    jump svom
                jump dropoutoffer
            "Leave" if True:
                jump worldmap
    if morning == 0 or event > 5:
        scene bg collegenight
        if event > 5:
            show bg college
        with d
        "College is currently closed, but the main office is still open."
        if tuition == 0:
            "I have no reason to go there, though."
            jump worldmap2
        menu:
            "Visit the Office (Pay Tuition)" if tuition > 0:
                scene bg office with d
                call clothesformal from _call_clothesformal_19
                show mce happy2
                with d
                label tuitionpaymenu:
                    call tuitionreward from _call_tuitionreward
                if tuition == 0:
                    jump worldmap2
                menu tmm:
                    "Your Money: $[money], Your Tuition: $[tuition]. Reward after every $10,000 paid."
                    "Pay $10,000" if tuition >= 10000:
                        if money < 10000:
                            "I don't have that kind of money!"
                            jump tmm
                        $ money -= 10000
                        $ tuition -= 10000
                        play sound success
                        pause 0.1
                        jump tuitionpaymenu
                    "Pay $1,000" if tuition >= 1000:
                        if money < 1000:
                            "I don't have that kind of money!"
                            jump tmm
                        $ money -= 1000
                        $ tuition -= 1000
                        play sound success
                        pause 0.1
                        jump tuitionpaymenu
                    "Pay $100" if True:
                        if money < 100:
                            "I don't have that kind of money!"
                            jump tmm
                        $ money -= 100
                        $ tuition -= 100
                        play sound success
                        pause 0.1
                        jump tuitionpaymenu
                    "Back" if True:
                        pass
            "Back" if True:
                pass
        jump worldmap2
    if clothes > 1 and ccm == 0 or clothes < 1 and ccm == 0:
        if clothes == 12:
            pass
        elif True:
            "I need to wear some formal clothes to college, should I change?"
            menu:
                "Yeah, wear formal clothes. (You'll change back afterwards)" if True:
                    $ ccm = 1
                "Back" if True:
                    jump worldmap
    $ potencollegemissed -= 1
    scene bg class with d
    if clothes == 12:
        call clothes from _call_clothes_101
    elif True:
        call clothesformal from _call_clothesformal_20
    show mce happy
    with d
    if event == 5:
        jump event
    "I attend my lectures and the day eventually wraps up."
    scene bg black with dissolve
    show bg college with dissolve
    pause 0.5
    $ rand = renpy.random.randint(1,100)
    jump event

label tuitionreward:
    if tuition <= 62000 and tuitionreward1 == 0:
        "There's the first chunk! That felt good. Although... There's still so much more to go!"
        "Time to get serious!"
        play sound success
        "You unlocked a new perk! 'Serious Grafter!'"
        "5%% Bonus to all money from now on."
        $ qseriouslyfocused = 1
        $ seriouslyfocused = 1.05
        $ tuitionreward1 = 1
    if tuition <= 52000 and tuitionreward2 == 0:
        "My heart is absolutely pumping right now! I can't believe I've paid off another 10,000!"
        "If I keep going like this... Yes, I can do this!"
        play sound success
        "You've unlocked a new perk! 'Unwavering Will'!"
        "-1 Shame now, and -5%% bonus to all shame loss from now on."
        $ shame -= 1
        $ qunwavering = 1
        $ unwavering = 1.05
        $ tuitionreward2 = 1
    if tuition <= 42000 and tuitionreward3 == 0:
        "Finally down to the big 42k! That's almost halfway. Let's keep going!"
        "I feel a lot less stressed with this large number being chipped away."
        play sound success
        "You've unlocked a new perk! 'Stress Free'!"
        "+1 Smarts now, and +5%% bonus to all smarts gains from now on."
        $ smarts += 1
        $ qstressfree = 1
        $ stressfree = 1.05
        $ tuitionreward3 = 1
    if tuition <= 32000 and tuitionreward4 == 0:
        "Yes! We're finally halfway done! Yes, yes, yes!"
        "Almost cheering in the office, I have to settle down a little before I embarrass myself!"
        play sound success
        "Your 'Seriously Focused', 'Unwavering Will', and 'Stress Free' perks have been upgraded!"
        "You now gain an additional 5%% bonus to all money, smart and shame stat changes."
        $ seriouslyfocused = 1.1
        $ unwavering = 1.1
        $ stressfree = 1.1
        $ tuitionreward4 = 1
    if tuition <= 22000 and tuitionreward5 == 0:
        "This is it! We're in the end-game now. What's 22,000 when I've already paid off 50,000?"
        "My god, has it really been 50k already? Wow..."
        play sound success
        "For recognition of your excellent progress at the university, you've been sent a care package of gifts."
        "Receieved 25 Condoms, 5 Study Books, 10 Aphrodisiacs, a large box of chocolates, a teddy bear and a fancy pen."
        $ condoms += 25
        $ smarts += 10
        $ aphrodisiac += 5
        $ tuitionreward5 = 1
        "(+10 Smarts from the Study Books!)"
    if tuition <= 12000 and tuitionreward6 == 0:
        "Not long now. Just a little more..."
        play sound success
        "You've unlocked a new perk! 'Determination!'"
        "Your unbreakable determination leaves people to regard you highly. +10%% to all follower gains from now on."
        $ qdetermination = 1
        $ determination = 1.10
        $ tuitionreward6 = 1
        "(The next reward will come when you've fully paid your tuition.)"
    if tuition == 0 and tuitionreward7 == 0:
        "Finally! I've done it!"
        "In [days] days I've managed to finally pay off my tuition..."
        "I let out a long sigh of relief and the office staff have a small cheer in recognition of my efforts."
        "The only thing left now is to enjoy college to the best of my ability!"
        play sound success
        "You've unlocked a new perk! 'Living Life to the Full!'"
        "+50%% Sexual Desire and Shame stat changes from now on!"
        $ qllthf = 1
        $ llthf = 1.5
        $ tuitionreward7 = 1
        "Time to finally leave the office and treat myself to something special."
    return


label potencollegemissed:
    if droppedout == 1:
        return
    if potencollegemissed == 3:
        $ potencollegemissed += 1
        "You've missed three days of college! You're starting to notice gaps in your knowledge compared to your classmates."
        play sound success2
        "(-1 Smarts)"
        $ smarts -= 1
    elif potencollegemissed == 8:
        $ potencollegemissed += 1
        "You've missed seven days of college! You're starting to struggle following class."
        if testfailed == 0:
            "Fortunately, you've yet to fail a test. Hang in there!"
        play sound success2
        "(-2 Smarts)"
        $ smarts -= 2
    elif potencollegemissed == 16:
        $ potencollegemissed += 1
        "You've missed fifteen days of college! You've defintely missed some important things!"
        if testfailed == 0:
            "Fortunately, you've yet to fail a test. Hang in there!"
        play sound success2
        "(-3 Smarts)"
        $ smarts -= 3
    elif potencollegemissed == 32:
        $ potencollegemissed += 1
        stop music fadeout 3.0
        "You get a phone call from your college... Your supervisor wants to meet you immediately regarding your attendance."
        show mce sad with d
        mc "Uh oh..."
        play sound equip
        call clothesformal from _call_clothesformal_21
        with d
        "You put on some formal clothes and leave to the college."
        scene bg class with d
        call clothesformal from _call_clothesformal_22
        show mce sad
        with d
        show supervisor:
            xpos 1200
        with dissolve
        supervisor "Look, if you're not going to take college seriously, you shouldn't have come at all."
        supervisor "This isn't some walk in the park that you can leisurely take time off whenever you see fit."
        if testfailed >= 2:
            supervisor "And frankly with the way your test scores are going, you're not likely to even finish the year."
        mc "B-But, I'm going through a lot right now!"
        supervisor "Everyone is going through a lot right now, [mc], and I don't expect anymore from you than I do from anyone else."
        supervisor "If you can't keep up, and have nothing else to offer; frankly, I see no reason to keep you in my classes if you're going to behave like this."
        "N-Nothing else to offer? What does he mean by that? Is paying not enough?"
        if personality == 2:
            "(Always Horny) Hmm.. I have an idea on how I could convince him, though..."
        menu cdom1:
            "Bribe him with a blowjob (30 Sexual Desire, <70 Shame)" if True:
                if sd < 30 or shame > 70:
                    "I just couldn't..."
                    jump cdom1
                mc "Surely there's something I could do for you? I'm young, dumb and impressionable."
                supervisor "For me? What are you suggesting?"
                scene bg class
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
                mc "Are you not interested in my body even a little bit? I'm definitely interested in you, and I'd be so sad if I couldn't see you."
                "*Gulp* I don't know what came over me, but as if this very moment was life threatening, I was willing to do almost anything to save myself."
                supervisor "If you're that desperate, then... You don't need to..."
                "Hah, I made him flustered!"
                supervisor "Very well, clothes off and on your knees."
                play sound equip
                scene bg class
                call clothesnude from _call_clothesnude_2
                show mce neutral
                with d
                "Eek! He's not flustered at all! Did he plan this?"
                scene bg class
                with d
                play music action fadein 3.0
                "Shamefully, I kneel down before my supervisor as he takes out his half-erection."
                scene bg class2
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
                "Taking his cock in my hand, I guide it to my mouth and wordlessly begin to twirl my tongue around his tip."
                "There's absolutely no way I'm letting this idiot make me leave college. Not only is this essential for my career, but I've invested far too much money into it..."
                "This is a small sacrifice for my future. I'll barely remember this when I'm successful in a few years."
                "I begin by bringing my mouth level to its tip and accepting it into my mouth, swirling my tongue around the edge of the glans for a high pleasure start."
                "Meanwhile my hands begin to naturally caress the cock, my left jacking it off while my right delicately massages the balls."
                "My plan is to finish him as fast as possible. So I'm attacking as many nerve endings as possible."
                mc "Mmphh, mmm... *Lick, slurp*"
                "Occasionally flicking my tongue across the sensitive tip of the erection, I focus on where he reacts the most favourably."
                "When his cock throbs in response to my movements, I know I'm doing something right."
                "My thighs brush together, and I shiver with desire. Am I really getting aroused by this? There is something hot about it..."
                "I can't help but get more passionate, my handjob speeds up as the desire to have my mouth filled up with hot cum grows."
                "I purse my lips around the glans and guide it back and forth in a fucking motion, sucking and licking with each movement."
                "These motions are most similar to vaginal sex, this should make him cum in no time. And the tense throbbing in his cock confirms my thoughts."
                "Using the last of my stamina I go all out to bring my supervisor to climax. I fuck his cock with my mouth deeply, while jacking him off intensely."
                play sound cum
                show blowjob3 2 with cum
                play sound cum
                show blowjob3 2 with cum
                "Finally! That took longer than I wanted, but now his cock unloads several hot jets of cum straight into the back of my mouth."
                play sound cum
                show blowjob3 2 with cum
                play sound cum
                show blowjob3 2 with cum
                "Load after load, I struggle to swallow it all. Some of it seeps outwards, dripping on my chin and face."
                stop ambience
                scene bg class with d
                "I finish up the job, and he withdraws his rapidly shrinking cock and pulls his pants back up"
                $ blowjobs += 1
                $ sdgain = 1
                $ shameloss = 1
                call sdgain from _call_sdgain_1
                call shameloss from _call_shameloss
                play sound success
                "(+[fsd] Sexual Desire, -[fshame] Shame.)"
                if qsecretlydepraved == 1:
                    "(Secretly Depraved) Your secret enjoyment of the depraved action causes you to gain an additional [fsd] sexual desire!"
                    call sdgain from _call_sdgain_11
                scene bg class with d
                call clothesformal from _call_clothesformal_23
                show mce sad
                with d
                show supervisor:
                    xpos 1200
                with dissolve
            "Beg him for one more chance." if True:
                if personality == 2 and sd > 30 and shame < 70:
                    "(Always Horny) I want to do something that'll definitely convince him!"
                    jump cdom1
                pass
            "Agree and leave college" if True:
                jump collegedropout
        supervisor "One more chance? Right. I'll be keeping a close eye on you. If this pattern of behaviour continues, I don't know if I'll be able to give you a second chance."
        show mce happy with d
        mc "Understood, Sir. I'll try my best."
        if morning == 0:
            scene bg bedroomday
        elif True:
            scene bg bedroomnight
        show mc:
            xpos 850
        show mcpiercings blank:
            xpos 850
        show mccatears blank:
            xpos 850
        show mch:
            xpos 850
        show mco:
            xpos 850
        call clothespjs from _call_clothespjs
        show mce sad:
            xpos 850
        with d
        "Phew... I can't believe I was nearly kicked out... That would have meant everything I've done so far was for nothing."
        "I genuinely feel terrified."
        return
    elif potencollegemissed == 45:
        $ potencollegemissed += 1
        stop music fadeout 3.0
        "I get phone call from college... My supervisor wants to meet you immediately!"
        show mce sad with d
        mc "Oh fuck..."
        play sound equip
        call clothesformal from _call_clothesformal_24
        with d
        "I put on some formal clothes and leave to the college."
        scene bg class with d
        call clothesformal from _call_clothesformal_25
        show mce sad
        with d
        show supervisor:
            xpos 1200
        with dissolve
        supervisor "I warned you, [mc]."
        supervisor "I'm afraid that unless you can convince me within the next sixty seconds to let you stay, you're going to have to leave the college."
        mc "Sixty seconds? But, uhh, I don't..."
        supervisor "Maybe I could be convinced if you and I were to get closer, then I'd have a reason to keep you around."
        if sd > 50 and shame < 50 or personality == 2 or qsecretlydepraved == 1:
            "Mmphh... He's blackmailing me, and I'm kinda into it..."
        elif True:
            "You rotten piece of..."
        menu dom2:
            "Bribe him with sex... (30 Sexual Desire, <70 Shame)" if True:
                if sd < 30 or shame > 70:
                    "I just can't..."
                    jump dom2
                label bhws:
                    pass
                $ supervisorsex = 1
                play music action fadein 3.0
                "With little fight, I begin to remove my clothes."
                play sound equip
                call clothesnude from _call_clothesnude_3
                with d
                mc "Right... How do you want it?"
                supervisor "Sit on that desk."
                scene bg class2
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
                play music action
                "Following his instructions, I get into position and expose my pussy to him."
                menu:
                    "Ask for vaginal" if True:
                        $ vora = "pussy"
                    "Ask for anal" if True:
                        $ vora = "ass"
                "With the last bit of control I can muster, I ask him to fuck my [vora], and thankfully he agrees."
                $ condomon = 0
                if vora == "pussy" and pregnancyshowing == 0 and condoms > 0:
                    menu:
                        "Use a condom?"
                        "Yeah" if True:
                            $ condomon = 1
                            $ condoms -= 1
                        "Nope" if True:
                            $ condomon = 0
                "The faster I get this over with, the better, so I at least try to act enthusiastic."
                "And hopefully this'll just be a one time thing."
                "On my butt, I spread my legs out and wiggle my butt. My lustful pussy is on full display, sheening slightly from its wetness."
                "Getting into position before me, he presses his tip against my [vora] and begins to slowly slide deeper inside."
                play sound cum
                if vora == "ass":
                    show sittingsex a2 with d
                    "With no lubrication other than a tiny bit of spit, it's painful at first, but I imagine to persevere as I adjust to his girth."
                elif True:
                    show sittingsex v2 with d
                    if virgin == 0:
                        "And just like that, I lose my virginity through blackmail. I won't give him the satisfaction by telling him that, though."
                        $ virgin = 1
                mc "Mmphh, your cock is huge! Don't hold back though..."
                play ambience sex fadein 3.0
                "Starting with a gentle pace, he slides in and out of my [vora] with long, deep thrusts."
                "It's a little irritating how pleasureful the deep thrusts are, as they constantly grind against sensitive erogenous zones causing me to get hot and bothered."
                "Almost cockily, he starts to rub my clit, as if I'm supposed to enjoy this and I'm not just someone he's using."
                "That being said, it is starting to become extremely pleasureful, especially now he's fucking faster."
                "Ahh, god! I can't believe it... My supervisor is fucking me and I'm about to come!"
                mc "Ahhh, it feels so good! Keep going, haahhh, aaahhh!"
                "He keeps rubbing my clit, and pounding my [vora]. Harder, faster! Before I know it, my mind goes white as I'm overwhelmed with an orgasm."
                "And as my [vora] rhythmically clenches around my partner's throbbing cock."
                play sound cum
                show sittingsex a3
                if vora == "pussy":
                    show sittingsex v3
                with cum
                play sound cum
                show sittingsex a3
                if vora == "pussy":
                    show sittingsex v3
                with cum
                "His throbbing cock completely unloads several thick ropes of cum directly into my pussy, and he doesn't miss a beat as he fucks me throughout."
                play sound cum
                show sittingsex a3
                if vora == "pussy":
                    show sittingsex v3
                with cum
                play sound cum
                show sittingsex a3
                if vora == "pussy":
                    show sittingsex v3
                with cum
                "Despite the situation, I've become so into it that I'm lustfully grinding my hips back into him, just to scrape together as much pleasure as I can from our orgasms."
                play sound cum
                show sittingsex 4 with d
                stop ambience fadeout 3.0
                "Ahhh... As he pulls out, several droplets of hot cum seep out my well-fucked [vora] and drip down my cool skin."
                if condomon == 0 and vora == "pussy":
                    call pregnancyroll from _call_pregnancyroll_8
                mc "Haaahhh... Well... I suppose that wasn't too bad..."
                scene bg class with d
                call clothesnude from _call_clothesnude_4
                show mce sad
                with d
                show supervisor:
                    xpos 1200
                with dissolve
                supervisor "You can forget what I was saying before about being kicked out."
                show mce neutral with d
                mc "Thank you! I really enjoyed spending time with you here today, so I hope to see you again lots and lots!"
                supervisor "I'll bet."
                "Grr, this guy!"
                "Oh well... The sex was actually pretty good..."
                if vora == "pussy":
                    $ vaginalsexes += 1
                elif True:
                    $ analsexes += 1
                $ sdgain = 1
                $ shameloss = 1
                $ status += 1
                call sdgain from _call_sdgain_12
                call shameloss from _call_shameloss_1
                play music rest
                "The conversation stops there, and I return home."
                if morning == 0:
                    scene bg bedroomday
                elif True:
                    scene bg bedroomnight
                call clothespjs from _call_clothespjs_1
                show mce sad
                with d
                "Phew... I must admit, I'm relieved that he changed his mind."
                "A part of me feels 'used', like he blackmailed me into sex..."
                show mce happy with d
                "But if you really think about it, there's a good argument for me using my sexuality to manipulate him into letting me stay."
                "Especially since I've been using my sexuality a lot lately to get what I want, how is this any different?"
                "Heh, and I'm safe now. No need to worry about getting kicked out. I know some people would feel bad in my situation, but I feel amazing!"
                play sound success
                "(+[fsd] Sexual Desire, +[fshame] Shame.)"
                if qsecretlydepraved == 1:
                    "(Secretly Depraved) Due to enjoying the depraved act, you gain an additional [fsd] Sexual Desire!"
                    call sdgain from _call_sdgain_14
                return
            "Give up and drop out." if True:
                jump collegedropout
return

label collegedropout:
    $ droppedout = 1
    supervisor "Understood. You'll be able to remain in your accomodation for however long you paid for it, but you'll no longer be allowed to attend classes."
    mc "Yes, sir... Apologies for the trouble."
    supervisor "If you're ever 'interested' in coming back, come and see me again, alright?"
    show mce angry with d
    mc "What's that supposed to mean?"
    supervisor "Well, I think you're attractive, and I can think of some reasons you should stick around."
    mc "Aaahh, uhh..."
    "I roll my eyes and just leave."
    if morning == 0:
        scene bg bedroomday
    elif True:
        scene bg bedroomnight
    show mc:
        xpos 850
    show mcpiercings blank:
        xpos 850
    show mccatears blank:
        xpos 850
    show mch:
        xpos 850
    show mco:
        xpos 850
    call clothespjs from _call_clothespjs_2
    show mce neutral:
        xpos 850
    with d
    play sound success
    "(You've dropped out of college! Yikes!)"
    return
label dropoutoffer:
    scene bg class with d
    call clothesformal from _call_clothesformal_26
    show mce sad
    with d
    show supervisor:
        xpos 1200
    with dissolve
    supervisor "I see you're back. Any particular reason? Good ones only."
    mc "I uhh, I really want to join college again... What do I have to do?"
    supervisor "You don't have to do anything. But since you're not a student at the moment, how about you and I get to know each other a little more intimately? That might help clear my mind on a few things."
    "This guy really is scum... But I suppose I did come here precisely knowing this'd happen. I'm even a little wet at the thought, I guess that's just the kind of person I am."
    menu:
        "Accept" if True:
            $ droppedout = 0
            call bhws from _call_bhws
            jump bedroom
        "Refuse?" if True:
            "I shake my head."
            mc "Sorry, I changed my mind."
            supervisor "I'll be here..."
            jump worldmap


init:
    $ tuition = 72000
    $ qllthf = 0
    $ llthf = 1
    $ qdetermination = 0
    $ determination = 1
    $ qstressfree = 0
    $ stressfree = 1
    $ qseriouslyfocused = 0
    $ seriouslyfocused = 1
    $ qunwavering = 0
    $ unwavering = 1
    $ tuitionreward1 = 0
    $ tuitionreward2 = 0
    $ tuitionreward3 = 0
    $ tuitionreward4 = 0
    $ tuitionreward5 = 0
    $ tuitionreward6 = 0
    $ tuitionreward7 = 0
    $ supervisorsex = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
