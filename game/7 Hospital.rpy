label hospital:
    if pregnancies > 1:
        pass
    elif pregnant == 0 or pregnancyterm < 10:
        "Unlock this location by becoming pregnant."
        jump postworldmap
    scene bg hospital
    call clothes from _call_clothes_60
    show mce happy
    with d
    "Hmm... The hospital. What am I here for?"
    menu:
        "Pregnancy Options" if pregnancyshowing == 1:
            "Ahh, I'll have to book an appointment. But what kind of appointment do I want?"
            menu hpom1:
                "Days Pregnant: [pregnancyterm]. Money: $[money]"
                "Abortion ($500, <90 Days Only)" if True:
                    if pregnancyterm > 90:
                        "It's too late for that."
                        jump hpom1
                    if money < 500:
                        "Hmph, that's expensive. But I guess it was my fault for not being careful."
                        jump hpom1
                    menu:
                        "Are you sure?"
                        "Yes" if True:
                            pass
                        "No" if True:
                            jump hpom1
                    scene bg black with d
                    pause 1.0
                    play sound success2
                    "(-$500)"
                    $ pregnancy = 0
                    $ pregnancyshowing = 0
                    $ pregnancyterm = 0
                    $ pregnant = 0
                    $ pregnancyintro = 0
                    $ money -= 500
                    scene bg hospital
                    call clothes from _call_clothes_61
                    show mce neutral
                    with d
                    "*Sigh* Well, with that sorted, I best be careful in the future."
                    jump postworktrans
                "Induce Birth (Unknown Cost)" if True:
                    if inductionintro == 0:
                        $ inductionintro = 1
                        play music studio
                        "In a society where everyone is born with powers, it is indeed possible to induce an early birth through powers."
                        "This is often done to protect the mother, as there are rare cases in which a child can access their powers early."
                        "Such as one case where a child was born invisible. That must have been a headache."
                        "This however, is not a cheap procedure... But as someone in Hero Academy, I do receive discounted treatments. So..."
                        scene bg black with d
                        "I setup an appointment, and I'm soon brought into a room with someone to discuss my options and get a health check-up."
                        scene bg hospital2
                        call clothes from _call_clothes_62
                        show mce happy
                        show stranger1:
                            xpos 50
                        with d
                        if nude == 1:
                            unknown "Why are you naked? You know what, nevermind."
                        unknown "I'm with the department of SPR; Super Power Research, you've probably seen our buildings."
                        show mce neutral with d
                        mc "Ahh, yes... You're not the doctor?"
                        unknown "Trust me, you can't afford that doctor. But if you have a genuine interest in birth induction, we can do it for free on the condition that you give your baby up for adoption to us."
                        show mce sad with d
                        mc "W-What? That's an insane proposition..."
                        unknown "Is it not an ideal propositon for a student like yourself? Wouldn't you like the opportunity to continue to live your life normally?"
                        show mce angry with d
                        mc "So, you've just been waiting around for some dumb student to come ask for a birth induction, to take advantage of them."
                        unknown "It's simply an offer. The treatment is $1,000, otherwise."
                        if money > 1000:
                            "Hmph, this bastard assumed I was just some poor student, when actually, I can actually afford that treatment."
                    elif True:
                        scene bg hospital2
                        call clothes from _call_clothes_63
                        show mce happy
                        show stranger1:
                            xpos 50
                        with d
                        unknown "Are you here to take the offer?"
                    menu hpom2:
                        "Money: $[money], Shame: [shame]"
                        "Accept the Offer (Free, <50 Shame)" if True:
                            if shame > 50:
                                "I can't do that! I'd be giving up my child to these weirdos!"
                                jump hpom2
                            mc "So... Just like that?"
                            unknown "You don't have to worry about anything at all. You'll be put to sleep and when you wake up everything will be sorted."
                            mc "I see... That's reassuring, I think..."
                            scene bg black with d
                            pause 1.0
                            play sound success2
                            "(You're no longer pregnant)"
                            $ pregnancy = 0
                            $ pregnancyshowing = 0
                            $ prenancyterm = 0
                            $ pregnant = 0
                            $ pregnancyintro = 0
                            scene bg hospital
                            call clothes from _call_clothes_64
                            show mce neutral
                            with d
                            jump postbirth
                        "Pay for Treatment (-$1,000)" if True:
                            if money < 1000:
                                "Yeaaahh, I can't afford that."
                                jump hpom2
                            scene bg black with d
                            pause 1.0
                            play sound success2
                            "(-$1000)"
                            $ pregnancy = 0
                            $ pregnancyshowing = 0
                            $ pregnancyterm = 0
                            $ pregnant = 0
                            $ pregnancyintro = 0
                            $ money -= 1000
                            scene bg hospital2
                            call clothes from _call_clothes_65
                            show mce neutral
                            with d
                            "That wasn't so bad, they just put me to sleep and everything was done when I woke up. My beautiful baby is just having a health checkup."
                            "But... What should I do with them?"
                            menu:
                                "Let your parents temporarily take care of them." if True:
                                    "Sorry Mom, sorry Dad!"
                                    "They're actually driving here anyway, I let them know what I was doing, and they'll be here in half an hour."
                                    $ children += 1
                                "Place them in an orphanage." if True:
                                    "I know it's adoption anyway, but at least it's not that slimy corporation."
                            label postbirth:
                                pass
                            $ births += 1
                            "*Sigh* What a stressful series of events."
                            if children == 1:
                                "I can't believe I have a child now... Life just got a lot more complicated."
                            if children > 1:
                                "I can't believe I have [children] children now... Life just got a lot more complicated."
                            scene bg black with d
                            "I spend the rest of the day with family, ultimately ending up back in my room alone with all things said and done."
                            if persistent.hospitalscare == False:
                                $ persistent.hospitalscare = True
                                show bg bedroomnight
                                call clothes from _call_clothes_66
                                show mce neutral:
                                    linear 10 xpos 750
                                with d
                                mc "I just feel... so... weird..."
                                show looking:
                                    alpha 0
                                    linear 4 alpha 0.5
                                mc "Like... I really fucked up."
                                mc "I never want to go through this again."
                            elif True:
                                show bg bedroomnight
                                call clothes from _call_clothes_67
                                show mce happy
                                with d
                                "I'm strong, I'll get through this. I always do!"
                            jump morning
                        "Back" if True:
                            jump hpom1
                "Back" if True:
                    jump worldmap2
        "Nothing" if True:
            scene bg street
            jump postworldmap

label naturalbirth:
    scene bg hospital2
    call clothesnude from _call_clothesnude_10
    show mce neutral
    with d
    "Ohh god, why was that so painful?! I thought we had the technology to make it bearable!"
    show mce happy with d
    "At least, I have my beautiful baby now..."
    "But... What should I do with them?"
    menu:
        "Let your parents temporarily take care of them." if True:
            "Sorry Mom, sorry Dad!"
            "They're actually driving here anyway, I let them know I was giving birth, and they'll be here in half an hour."
            $ children += 1
        "Place them in an orphanage." if True:
            "Sorry, little one... I'm just in no position to give you the care you need right now."
    scene bg black with d
    show bg hospital
    call clothesnude from _call_clothesnude_11
    show mce neutral
    with d
    $ births += 1
    "*Sigh* What a stressful series of events."
    if children == 1:
        "I can't believe I have a child now... Life just got a lot more complicated."
    if children > 1:
        "I can't believe I have a [children] children now... Life just got a lot more complicated."
    scene bg black with d
    "I spend the rest of the day with family, ultimately ending up back in my room alone with all things said and done."
    $ pregnancy = 0
    $ pregnancyshowing = 0
    $ pregnancyterm = 0
    $ pregnant = 0
    $ pregnancyintro = 0
    if births == 1:
        show bg bedroomnight
        call clothes from _call_clothes_68
        show mce neutral:
            linear 10 xpos 750
        with d
        mc "I just feel... so... weird..."
        mc "Like... I really fucked up."
        show looking:
            alpha 0
            linear 5 alpha 0.5
        mc "I never want to go through this again."
    elif True:
        show bg bedroomnight
        call clothes from _call_clothes_69
        show mce happy
        with d
        "I'm strong, I'll get through this. I always do!"
    jump morning

init:
    $ inductionintro = 0
    $ children = 0
    $ births = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
