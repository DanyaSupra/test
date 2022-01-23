label tutor:
    $ yomomet = 1
    scene bg house1 with d
    call clothes from _call_clothes_27
    show mce happy
    if nude == 1 or lewdoutfit == 1:
        show mce horny
    with d
    if tutorintro == 0:
        $ tutorintro = 1
        "One of my classmates mentioned they run a tutoring class, and since Hero Academy is so prestigious, students from my college are sought after as tutors."
        "She said she'd be willing to hire us to help tutor students from other universities. And I bet this'd look great on my resume."
        "Ah, there she is now."
        show yomob:
            xpos 1200
        show yomoo hero:
            xpos 1200
        show yomoe happy:
            xpos 1200
        with d
        unknown "Greetings! Welcome to my house."
        "Ahhh, t-this is her house? But it's soooooo biiiiiig!"
        "Although that's not the only thing I'm impressed with right now..."
        python:
            yomo = renpy.input("Name the Smart Girl. Leave blank for the default name 'Yomo'.")
            yomo = yomo.strip()
            if not yomo:
                yomo = "Yomo"
        show yomoe laughing with d
        yomo "Haha, apologies. I'm still in my hero uniform."
        if nude == 1 or lewdoutfit == 1:
            yomo "Although, it seems I'm not the only one with lewd apparel today."
        show mce horny
        "So revealing... How naughty."
        "Oh god, her thighs are to die for."
        show mce happy
        show yomoe happy:
            xpos 1200
        with d
        "[yomo] would make such a great sugar mommy, haha..."
        "That's a joke... Right? ... Right?"
        yomo "Here for the tutoring, then? I'll have to give you a quick crash course on how to best do so."
        yomo "In fact, as the current top in the class, I'm more than happy to tutor you too."
        mc "Ooohh, with someone as smart as you teaching me, I wouldn't have any issue getting through university at all!"
        show yomoe laughing with d
        yomo "Heh, goodness, I'm not that smart, I was just fortunate to have my own exceptional tutor when I was younger."
        yomo "Which is why I'm so eager to help others succeed like myself."
        mc "That's really amazing!"
        show yomoe happy with d
        yomo "Ah, but first, let me teach you some basics on how to tutor the clients that come here..."
        $ rand = 1
        jump yomotutor
    elif True:
        pass
    menu:
        "What should I do right now?"
        "Get tutored by [yomo]" if True:
            $ rand = renpy.random.randint(1,2)
            jump yomotutor
        "Tutor a student" if yomotutor1 == 1:
            jump studenttutor
        "Back" if True:
            jump worldmap
jump worldmap

label yomotutor:
    play music girls
    if yomotutor1 == 0:
        jump yomotutor1
    elif yomotutor2 == 0:
        jump yomotutor2
    elif yomotutor3 == 0:
        jump yomotutor3
    elif yomotutor4 == 0:
        jump yomotutor4
    elif yomotutor5 == 0:
        jump yomotutor5

label yomotutor5:
    show yomob:
        xpos 1200
    if rand == 1:
        show yomoo hero:
            xpos 1200
    elif True:
        show yomoo uniform:
            xpos 1200
    show yomoe happy:
        xpos 1200
    with d
    if yomoroutecomplete == 0:
        $ yomoroutecomplete = 1
        yomo "Hey, [mc], you've certainly been coming here to study a lot!"
        mc "That, among other things, hehe."
        yomo "Quite right! I've never gone so far 'sexually' with a single person before."
        show mce laughing with d
        mc "Really? That's a surprise."
        yomo "Haha, yeah... I was wondering if maybe you wanted to make it more of a serious thing? I don't mind having a friend with benefits, but I think you and I could maybe become something more."
        show mce horny with d
        "Ohh, she's asking me out! I wasn't expecting that!"
        if boyfriend == 1:
            show mce neutral with d
            "Aarrgghh, doesn't she know I already have a boyfriend, though? Is this a trick question? Is she onto me cheating?"
        show mce happy with d
        menu:
            "Date [yomo]" if True:
                $ yomogf = 1
                mc "Oh, [yomo], I'd love to date you."
                yomo "Ahh, how excellent!"
                play sound success
                "(You are now dating [yomo]!)"
                if boyfriend == 1:
                    "This couldn't possibly cause problems, r-right?"
            "Tell her you have a boyfriend" if boyfriend == 1:
                mc "Aaahh, s-sorry, [yomo], I'm already dating someone."
                show yomoe neutral with d
                yomo "You are?! Ohh! That's a surprise... I assume it must be an open arrangement, but I understand that means you're unable to 'date' me in the traditional sense."
            "Let her down gently" if True:
                mc "Sorry, [yomo], I'm not really in a situation where I can commit to something more serious."
                show yomoe neutral with d
                yomo "Awwhh, I understand though. Thanks for being such a great friend regardless."
        if yomogf == 1:
            show mce horny with d
            mc "I guess, we're uhm... Together! What do we do now?"
            show yomoe laughing with d
            yomo "Haha, I have somewhere nice in mind to take you."
            mc "Oh?"
            scene bg black with d
            "Yomo takes me to an expensive restaurant as our first official date, the food is absolutely delicious."
            "She definitely has sugar mommy potential. Ohh, uhm... I mean... She'd make a great wife."
            "Afterwards, we return home, and go over what we learnt in our last class."
            jump postyomodate
        elif True:
            mc "Sorry that we can't be together, but I'm still open to continuing as we are."
            show yomoe happy with d
            yomo "I wouldn't mind that at all, haha. Shall we go over what was in our last class?"
    "Yomo and I spend some time together studying, gossiping, and watching some television."
    label postyomodate:
        scene bg house1
        call clothes from _call_clothes_105
        show mce happy
        show yomob:
            xpos 1200
        if rand == 1:
            show yomoo hero:
                xpos 1200
        elif True:
            show yomoo uniform:
                xpos 1200
        show yomoe happy:
            xpos 1200
        with d
    play sound success
    $ smartsgain = 1
    call smartsgain from _call_smartsgain_14
    "(+[fsmarts] Smarts)"
    menu:
        "Sixty-Nine" if True:
            jump yomosixtynine
        "Fingering" if True:
            jump yomofingering
        "Make Out" if True:
            jump yomomakingout
        "Go Home" if True:
            mc "I best get off, see you later, [yomo]."
            yomo "Byee, [mc]!"
            jump postworktrans
label yomotutor4:
    show yomob:
        xpos 1200
    if rand == 1:
        show yomoo hero:
            xpos 1200
    elif True:
        show yomoo uniform:
            xpos 1200
    show yomoe happy:
        xpos 1200
    with d
    menu ymsm5:
        "Smarts: [smarts]"
        "Impress [yomo] with your smarts (20 Smarts)" if True:
            if smarts < 20:
                "The form of this option is beyond my intelligence!"
                jump ymsm5
            pass
        "Be a pleb" if True:
            yomo "Shall we get to studying, then?"
            mc "Yes! Thank you, [yomo]."
            scene bg black with d
            "Some studying later..."
            scene bg house1
            call clothes from _call_clothes_29
            show mce happy
            show yomob:
                xpos 1200
            if rand == 1:
                show yomoo hero:
                    xpos 1200
            elif True:
                show yomoo uniform:
                    xpos 1200
            show yomoe happy:
                xpos 1200
            with d
            yomo "You're so good, [mc]... If you improve a little more, I might just give you a reward!!"
            mc "O-Oh my! [yomo]..."
            $ smartsgain = 1
            call smartsgain from _call_smartsgain_8
            play sound success
            "(+[fsmarts] Smarts)"
            scene bg black with d
            "About an hour later, we wrap things up and I return home."
            jump postworktrans
    show yomoe horny with d
    yomo "Hey cutie! You're already top of the class with me, so let's have some fun? I was thinking we could try something new."
    "Ohh, I'm already looking forward to it."
    menu ys4m1:
        "Sexual Desire: [sd], Shame: [shame]"
        "Sixty-Nine (45 Sexual Desire)" if True:
            if sd < 45:
                "I can't ask that... There's no way she'd agree to it, right?"
                jump ys4m1
            $ yomotutor4 = 1
            label yomosixtynine:
                pass
            mc "Do you wanna uhhhmm, kiss somewhere else? Hehe... I know I would."
            yomo "Ohh, both at the same time? You sly devil, I knew you had it in you."
            yomo "Truth is, I'm not that confident, so I struggle to initiate."
            mc "Ahh, I can be quite confident sometimes, or maybe just 'stubborn' as my dad would say."
            yomo "*Giggles* You really will make a great support hero, you're just the catalyst I need to encourage me to push you down, and begin."
            mc "Oh? Oh!"
            play sound equip
            scene bg black with d
            if nude == 1:
                "And she does indeed push me down, as one by one she removes my clothes."
            elif True:
                "And she does indeed push me down!"
            "With her clothes soon coming off too, it isn't long until...!"
            play sound2 oral1 fadein 2.0
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
            yomo "Ahh, your skin is so soft..."
            "I try to reply, but I just find [yomo]'s pussy pressed against my face with a lustful energy. This both silences me, but also prompts me to stick my tongue out and begin to focus on her swollen clit."
            "My lover takes her time however, teasing me as she kisses my thighs and gently grazes her finger tips against my pussy. Her expert touch leaves me absolutely aching with desire."
            yomo "Mmm, ahhh... You're so warm, and already so wet too, hehe..."
            "That's when I feel the warm press of her tongue against my throbbing clit, swiping back and forth, sending shivers of pure ecstasy through my nerves."
            "Also bringing a finger to my pussy, poking and teasing me, I squirm under her movements."
            "She speeds up, and I try to match her pace. Before we know it, we're both panting, and struggling to hold back moans."
            yomo "Oohhh, you're so good with your tongue! If you keep going like that, you're going to make me come..."
            mc "Mmphh, mmaahhh, m-me too!"
            "Determined, our tongues both focus our respective clits, swiping and twirling around to induce as much pleasure as possible from our lover."
            "We don't go harder, nor faster, but the pleasure rises regardless; eventually to a boiling point. My toes curl, and my body tenses up slightly as I reach the precipice of my orgasm."
            yomo "Ohh god, oohhh, I-I'm gonna-"
            play sound cum
            show yuri69orgasm with cum
            "I can't feel anything else except the electrifying pleasure of [yomo]'s tongue rubbing my clit. It radiates all over my body as I'm brought to a powerful orgasm."
            play sound cum
            show yuri69orgasm with cum
            "We both squirm with delight as euphoria washes over our bodies, and we desperately try to continue licking throughout."
            "Soon after, the euphoria melts away and is replaced with a calm feeling of peace and relief as I'm brought back to reality."
            stop ambience fadeout 2.0
            stop sound2 fadeout 2.0
            play sound equip
            scene bg house1
            call clothesnude from _call_clothesnude_30
            show mce happy
            show yomob:
                xpos 1200
            show yomoo nude:
                xpos 1200
            show yomoe happy:
                xpos 1200
            with d
            yomo "Haaahhh, quite the maestro with your tongue, aren't you?"
            mc "Really? You were excellent too! It must have been a harder angle, but you still made me come hard."
            yomo "Mmm, I couldn't help myself, you're just so tasty. How about some more tea?"
            mc "Okay!"
            scene bg black with d
            $ sdgain = 1
            $ status += 1
            $ lesbian += 1
            call sdgain from _call_sdgain_97
            play sound success
            "(+[fsd] Sexual Desire)"
            "(+1 [yomo] Affection!)"
        "Fingering" if True:
            jump yomofingering
        "Make Out" if True:
            jump yomomakingout
        "Study" if True:
            if sd > 15 and personality == 2:
                "(Always Horny) How can I refuse that?"
                jump ys4m1
            show yomoe happy with d
            yomo "Mmm, okay! Let's get back to studying, then!"
            "Taking the small loss with grace, she happily returns to studying with me."
    $ smartsgain = 1
    call smartsgain from _call_smartsgain_6
    play sound success
    "(+[fsmarts] Smarts)"
    scene bg black with d
    "About an hour later, we wrap things up and I return home."
    jump postworktrans
label yomotutor3:
    show yomob:
        xpos 1200
    if rand == 1:
        show yomoo hero:
            xpos 1200
    elif True:
        show yomoo uniform:
            xpos 1200
    show yomoe happy:
        xpos 1200
    with d
    yomo "Heyy, how's it going?"
    "Greeting me with a hug, we catch up a little."
    menu ymsm4:
        "Smarts: [smarts]"
        "Impress [yomo] with your smarts (15 Smarts)" if True:
            if smarts < 15:
                "The form of this option is beyond my intelligence!"
                jump ymsm4
            pass
        "Be a pleb" if True:
            yomo "Shall we get to studying, then?"
            mc "Yes! Thank you, [yomo]."
            scene bg black with d
            "Some studying later..."
            scene bg house1
            call clothes from _call_clothes_30
            show mce happy
            show yomob:
                xpos 1200
            if rand == 1:
                show yomoo hero:
                    xpos 1200
            elif True:
                show yomoo uniform:
                    xpos 1200
            show yomoe happy:
                xpos 1200
            with d
            yomo "Excellent, you're showing great progress!"
            yomo "Hehe, I might even need to up my own studying to make sure you don't overtake me."
            $ smartsgain = 1
            call smartsgain from _call_smartsgain_10
            play sound success
            "(+[fsmarts] Smarts)"
            scene bg black with d
            "About an hour later, we wrap things up and I return home."
            jump postworktrans
    show yomoe horny with d
    yomo "Youuu, uhh, here for tutoring? Or would you rather just get to the good stuff?"
    "Ooohh? Has our relationship really progressed to such an extent where we don't even bother with the studying anymore?"
    "My heart throbs slightly, the 'good' stuff sounds rather nice around now."
    menu ys3m1:
        "Sexual Desire: [sd], Shame: [shame]"
        "Fingering (30 Sexual Desire)" if True:
            if sd < 30:
                "I-I'm not ready for that!"
                jump ys3m1
            $ yomotutor3 = 1
            label yomofingering:
                pass
            play sound equip
            scene bg house1
            "Exhibiting a greater confidence than before, [yomo] crawls over me, pinning me down and initating a kiss."
            yomo "I'm going to make you mine..."
            scene bg black with d
            "At some point, we'd stumbled into [yomo]'s bedroom. We were completely naked, passionately kissing, hands roaming everywhere and anywhere they could."
            "And then..."
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
            play sound2 foreplay1 fadein 3.0
            mc "Aaahhh, oh gosh! That feels so good!"
            yomo "Ohhh, you're so wet! Are you feeling all bottled up?"
            mc "Maah, maybe!"
            "[yomo] teases as she grinds her fingers against several spots, gauging my reaction with each before returning to the most pleasureful areas."
            mc "Mmphhh, fuuuuck! Aahhh, haaahhh!"
            "I lean back and let her completely take me."
            play ambience sex fadein 3.0
            show yomofingering 2
            with d
            "Wet and noisy, her fingers begin to thoroughly fuck me, her hand slapping back and forth against my ass causing it to shake."
            "My thighs quiver as I enter a new realm of pleasure. [yomo]'s finger work is fantastic and is quickly bringing me close to an orgasm."
            mc "Ohhhh, Y-[yomo]! I-I'm getting close!"
            yomo "Gooood girl, come for me, then."
            show yomofingering 3
            with d
            mc "Yess, yesss! I-I'm coming!"
            play sound cum
            show yomofingering 3 with cum
            "My entire body shivers as pleasure overwhelms me. each and every movement in my pussy fills me up with so much pleasure I feel absolutely euphoric."
            play sound cum
            show yomofingering 3 with cum
            "It managed to be such a strong orgasm that I squirted slightly!"
            stop ambience fadeout 2.0
            stop sound2 fadeout 2.0
            yomo "Mmmhh, such a good girl, [mc]..."
            mc "Mmmhh, y-yeah..."
            $ groped += 1
            $ masturbations += 1
            $ sdgain = 1
            $ lesbian += 1
            call sdgain from _call_sdgain_98
            play sound success
            "(+[fsd] Sexual Desire)"
            "(+1 [yomo] Affection!)"
        "Make Out" if True:
            jump yomomakingout
        "Study" if True:
            if sd > 15 and personality == 2:
                "(Always Horny) How can I refuse that?"
                jump ys3m1
            show yomoe happy with d
            yomo "Mmm, okay! Let's get back to studying, then!"
            "Taking the small loss with grace, she happily returns to studying with me."
    $ smartsgain = 1
    call smartsgain from _call_smartsgain_7
    play sound success
    "(+[fsmarts] Smarts)"
    scene bg black with d
    "About an hour later, we wrap things up and I return home."
    jump postworktrans
label yomotutor2:
    show yomob:
        xpos 1200
    if rand == 1:
        show yomoo hero:
            xpos 1200
    elif True:
        show yomoo uniform:
            xpos 1200
    show yomoe happy:
        xpos 1200
    with d
    if yomotutor2intro == 0:
        $ yomotutor2intro = 1
        if nude == 1 or lewdoutfit == 1:
            yomo "Ohh myy, you want me while dressed like that?"
        elif True:
            yomo "You called?"
        mc "Yeah! Can we study again?"
        if nude == 1 or lewdoutfit == 1:
            yomo "I think I'll get distracted, but I can try my best."
        yomo "Hehe, I usually charge students that want to study with me."
        show mce neutral with d
        mc "C-Charge? But we're-"
        yomo "Shhh... There are other ways you could pay me."
        show mce horny with d
        mc "Oo-ohh?"
        yomo "Let's see how you feel after our study session, hmm?"
        menu ymsm2:
            "Smarts: [smarts]"
            "Impress [yomo] with your smarts (10 Smarts)" if True:
                if smarts < 10:
                    "Unfortunately, I'm not smart enough to keep up with her!"
                    jump ymsm2
                scene bg black with d
                "Some herbal tea and studying later..."
                scene bg house1
                call clothes from _call_clothes_46
                show mce happy
                show yomob:
                    xpos 1200
                if rand == 1:
                    show yomoo hero:
                        xpos 1200
                elif True:
                    show yomoo uniform:
                        xpos 1200
                show yomoe happy:
                    xpos 1200
                with d
                yomo "Haahh, it's so hot..."
                show mce horny with d
                mc "Ohh? Y-[yomo], you appear to be unbuttoning your shirt."
                show yomoe horny with d
                yomo "Ahh? Is there something wrong with being open around my girlies?"
                mc "Heh, it's just... Quite sexually charged, you know?"
                yomo "Mmm, it is? Is that what you think?"
                "She confidently leans back on the sofa, her eyes half-lidded. Chest pushed out, thighs and panties on display as her shirt lifts slightly."
                mc "Maybe..."
                yomo "Wanna make out?"
                jump ys1m2
            "Be a pleb" if True:
                yomo "Not bad at all!"
                yomo "Still some ways off beating the tests, but you're so close!"
                $ smartsgain = 1
                call smartsgain from _call_smartsgain_11
                play sound success
                "(+[fsmarts] Smarts)"
                scene bg black with d
                "About an hour later, we wrap things up and I return home."
                jump postworktrans
    elif True:
        yomo "Time to study what we've been learning lately?"
        mc "That, and maybe something more..."
        if nude == 1 or lewdoutfit == 1:
            yomo "With you dressed like that, don't think I won't pounce when I get a chance!"
        elif True:
            yomo "Hehe, let's do something at the end so we can look forward to it."
        menu ymsm3:
            "Smarts: [smarts]"
            "Impress [yomo] with your smarts (10 Smarts)" if True:
                if smarts < 10:
                    "Unfortunately, I'm not smart enough to keep up with her!"
                    jump ymsm3
                scene bg black with d
                "Some herbal tea and studying later..."
                scene bg house1
                call clothes from _call_clothes_47
                show mce happy
                show yomob:
                    xpos 1200
                if rand == 1:
                    show yomoo hero:
                        xpos 1200
                elif True:
                    show yomoo uniform:
                        xpos 1200
                show yomoe happy:
                    xpos 1200
                with d
                yomo "I think it's just about time to wrap up studying, anything else you wanted to 'discuss' with me?"
                jump ys1m2
            "Be a pleb" if True:
                yomo "Not bad at all!"
                yomo "Still some ways off beating the tests, but you're so close!"
                $ smartsgain = 1
                call smartsgain from _call_smartsgain_12
                play sound success
                "(+[fsmarts] Smarts)"
                scene bg black with d
                "About an hour later, we wrap things up and I return home."
                jump postworktrans
    menu ys1m2:
        "Sexual Desire: [sd], Shame: [shame]"
        "Make Out (15 Sexual Desire)" if True:
            if sd < 15:
                "I-I'm too nervous!"
                jump ys1m2
            $ yomotutor2 = 1
            mc "Sure!"
            label yomomakingout:
                pass
            yomo "Heh, come here you..."
            play sound equip
            scene bg house1
            show yomomakeout1
            with d
            play sound2 foreplay1
            "Our hands are quick to wrap around each other as she pulls me down into a kiss, one of her legs lifting up around mine and wrapping around."
            "Lips smack and tongues twirl as we roll around on the sofa in loving fashion."
            "Ah! One of her hands is encroaching particularly close to my crotch."
            menu ys1m3:
                "Let her rub your crotch (25 Sexual Desire)" if True:
                    if sd < 25:
                        "I'm not quite ready to do something like that."
                        jump ys1m3
                    show yomomakeout2
                    with d
                    "I spread my legs slightly, completely welcoming the advance which she readily pursues as she rubs me."
                    "We continue like this for a while, entwined together in loving passion."
                    $ masturbations += 1
                "That's enough" if True:
                    "I make my boundaries clear, but continue to kiss [yomo]."
            stop ambience fadeout 2.0
            stop sound2 fadeout 2.0
            scene bg house1
            call clothes from _call_clothes_31
            show mce happy
            show yomob:
                xpos 1200
            if rand == 1:
                show yomoo hero:
                    xpos 1200
            elif True:
                show yomoo uniform:
                    xpos 1200
            show yomoe happy:
                xpos 1200
            with d
            "Eventually, our lips part and we return to our original positons."
            mc "Haahh, t-that was nice..."
            yomo "Mmmphh, you're quite the sweet treat."
            yomo "I wouldn't mind doing things like that with you... 'often'."
            mc "O-Ohhh, is that so? Hehe..."
            $ sdgain = 1
            $ kisses += 1
            call sdgain from _call_sdgain_99
            play sound success
            "(+[fsd] Sexual Desire)"
            "(+1 [yomo] Affection!)"
        "Pass" if True:
            if sd > 15 and personality == 2:
                "(Always Horny) How can I refuse that?"
                jump ys1m2
            show yomoe happy with d
            yomo "Mmm, okay! Let's get back to studying, then!"
            "Taking the small loss with grace, she happily returns to studying with me."
    $ smartsgain = 1
    call smartsgain from _call_smartsgain_13
    play sound success
    "(+[fsmarts] Smarts)"
    scene bg black with d
    "About an hour later, we wrap things up and I return home."
    jump postworktrans
label yomotutor1:
    scene bg black with d
    "Some herbal tea and a few minutes later."
    scene bg house1 with d
    call clothes from _call_clothes_32
    show mce happy
    if nude == 1 or lewdoutfit == 1:
        show mce horny
    show yomob:
        xpos 1200
    show yomoo hero:
        xpos 1200
    show yomoe happy:
        xpos 1200
    with d
    if nude == 1 or lewdoutfit == 1:
        yomo "Hmm, your clothing choice is a little naughty, but that's okay, sometimes I tutor in my hero outfit too. It's quite liberating."
    elif True:
        yomo "You don't mind if I stay in my hero outfit, do you? It's very comfy."
    mc "Not at all! I think you look great, in that... Hahhh..."
    yomo "Hehe, oh dear, I'm not distracting you, am I?"
    show mce horny with d
    mc "Maybe a little, that is a lot of skin you're showing..."
    yomo "Ahh? Do you swing that way too, [mc]?"
    menu:
        "Yup!" if True:
            yomo "Me too! How exciting!"
        "K-Kinda?" if True:
            yomo "Ahh, a bicurious girl. I really can teach you a few things."
        "I don't think so" if True:
            yomo "Well, you know what they say about noodles..."
            mc "H-Huh?"
    "[yomo] gives me a quick guide on how to tutor students, and she's remarkably flirtacious to me throughout."
    "Gosh... She's amazing, she even smells good."
    $ sdgain = 1
    $ smartsgain = 1
    call sdgain from _call_sdgain_100
    call smartsgain from _call_smartsgain_9
    play sound success
    "(+[fsd] Sexual Desire, +[fsmarts] Smarts!)"
    menu ymsm0:
        "Smarts: [smarts]"
        "Impress [yomo] with your smarts (5 Smarts)" if True:
            if smarts < 5:
                "The form of this option is beyond my intelligence!"
                jump ymsm0
            scene bg black with d
            "Some studying later..."
            scene bg house1 with d
            call clothes from _call_clothes_48
            show mce happy
            show yomob:
                xpos 1200
            if rand == 1:
                show yomoo hero:
                    xpos 1200
            elif True:
                show yomoo uniform:
                    xpos 1200
            show yomoe happy:
                xpos 1200
            with d
            yomo "What an excellent student you are."
            mc "Thank you, and you're an excellent teacher. You explain everything so clearly, I'll have to remember those tricks you taught me."
            yomo "I must be off for now, but do come back if you'd like to become proper study buddies, after all, we're going through the same material, and two heads working together can better consolidate that."
            mc "Y-Yeah! Study buddies, hehe."
            play sound success
            "(+1 [yomo] Affection!)"
            scene bg street with d
            call clothes from _call_clothes_33
            show mce horny
            with d
            "I leave the estate in a daze."
            "Why am I so horny? Hahhh."
            play sound success
            "(You can now tutor students at [yomo]'s estate, and also receive tutoring from her.)"
            $ yomotutor1 = 1
        "Be a pleb" if True:
            scene bg black with d
            "Some studying later..."
            scene bg house1 with d
            call clothes from _call_clothes_49
            show mce happy
            show yomob:
                xpos 1200
            if rand == 1:
                show yomoo hero:
                    xpos 1200
            elif True:
                show yomoo uniform:
                    xpos 1200
            show yomoe happy:
                xpos 1200
            with d
            yomo "Not bad, not bad..."
            yomo "Although you still have a ways to go. I say let's practice on helping you pass next Friday's test first!"
            mc "Okay, thank you!"
    jump postworktrans

label studenttutor:
    show bg house1 with d
    "One of the students arrives, and I spend a few hours tutoring them through their studies."
    show student1:
        xpos 1200
        ypos 100
    with d
    if nude == 1 or lewdoutfit == 1 or sd > 50:
        show mce horny with d
        if nude == 1 or lewdoutfit == 1:
            "However, my overwhelmingly lewd prescence is clearly distracting them."
        elif True:
            "But I can't help but get slightly horny, maybe I could..."
        menu tutorlewdmenu:
            "Sexual Desire: [sd], Shame: [shame]"
            "Give him a blowjob. (50 Sexual Desire, <75 Shame)" if True:
                if sd < 50 or shame > 75:
                    "Heh, it's one thing to dress like this, but that's another thing entirely..."
                    jump tutorlewdmenu
                $ tutorbj = 1
                show mce horny with d
                play music action
                "Yep, I'm gonna do it."
                "I want him now."
                "Whispering into his ear, I manage to convince him"
                mc "Heyy, I can make you feel really good..."
                stu "W-What about studying?"
                mc "You've worked so hard, I think you deserve a little break, and a reward... What do you say?"
                stu "Uuhhmmm..."
                scene bg house1 with d
                "I coo as I get on my knees infront of my partner. I'm eager, and the vulgar situation is making my heart race."
                stu "O-Okay!"
                "I unbuckle his belt and take out his delicious cock, it's everything I'd imagined it'd be and more."
                hide student3
                play ambience oral1 fadein 3.0
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
                play ambience blowjob
                "Wasting no time, I begin to stroke his cock and wrap my tongue around its tip."
                mc "Mmphhh... I love your cock..."
                "I allow its taste, smell and feel to overwhelm my senses as I fully indulge in the blowjob with a lustful pride."
                "In my horny stupor, the hand I'm not jacking him off with finds itself between my legs and rubbing my wet pussy."
                "The pleasure I feel from just unfocused rubbing is electrifying, showing just how aroused I am right now."
                mc "Haaah... *Slurp, lick*"
                "My partner strokes my hair as I take his cock deeper while swirling my tongue around his sensitive glans."
                "I can't help but stifle several moans into his cock as I increase my effort. The vibrations seem to make him feel even better, hehe."
                "With the combined sensations of my tongue, mouth and hand, I should be able to get him off quickly, and I'm eager to guzzle on his hot cum."
                "It doesn't take long for his throbbing cock to swell up, signalling an orgasm."
                "I fuck his cock with my mouth, almost deepthroating him on occasion; whilst creating the most lecherous, sloppy wet noises possible."
                play sound cum
                show povblowjob 2 with cum
                play sound cum
                show povblowjob 2 with cum
                "The orgasm came quick and strong, taking me by surprise. Immediately, several loads of thick cum coated the back at my throat."
                play sound cum
                show povblowjob 2 with cum
                play sound cum
                show povblowjob 2 with cum
                stop ambience fadeout 3.0
                "I struggle to swallow the tremendous amount of cum, causing a lot to spill out from my mouth. For one load I pull back, causing several loads to get on my face; I love it."
                "I swallow each drop that I can. The pure erotic stimulation is enough to make me come as I finally rub myself off."
                scene bg house1 with d
                show student1:
                    xpos 1200
                    ypos 100
                with d
                "Pulling his deflating cock away, he hoists it back into his pants and does his belt back up as I sheepishly peer at him from below with a face covered in cum."
                stu "Uhmm... Let me get you a tissue!"
                scene bg black with d
                scene bg house1
                call clothesnude from _call_clothesnude_31
                show mce horny
                show student1:
                    xpos 1200
                    ypos 100
                with d
                "I finish the rest of the session in the nude, to my client's delight."
                $ blowjobs += 1
                $ sdgain = 1
                $ shameloss = 1
                call sdgain from _call_sdgain_74
                call shameloss from _call_shameloss_52
                play sound success
                "(+[fsd] Sexual Desire, -[fshame] Shame!)"
            "Focus on the studies." if True:
                if personality == 2 and sd > 50 and shame < 75:
                    "(Always Horny) I can't focus like this... The only way to move on from here is to deal with the issue at hand, hehe."
                    jump tutorlewdmenu
                pass
    $ moneygain = smarts + 5
    $ smartsgain = 1
    if moneygain > 40:
        $ moneygain = 40
    call moneygain from _call_moneygain_49
    call smartsgain from _call_smartsgain_4
    play sound success
    "For the quality of work, I receive $[fmoney]!"
    "And, I feel a bit smarter! (+[fsmarts] Smarts)"
    $ smarts += 1
    if moneygain < 10:
        "It's not much right now, but if I focus on my studies I could earn more."
    jump postworktrans

init:
    $ tutorintro = 0
    $ yomotutor1 = 0
    $ yomotutor2 = 0
    $ yomotutor2intro = 0
    $ yomotutor3 = 0
    $ yomotutor4 = 0
    $ yomotutor5 = 0
    $ tutorbj = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
